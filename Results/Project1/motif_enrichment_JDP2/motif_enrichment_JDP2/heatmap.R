
##########################################
### Initialization
##########################################

# Import
library(gplots)
library(RColorBrewer)

# Parameters
pvalue1 = 0.001
pvalue2 = 0.00001
wid1 = 5
hei1 = 10
wid2 = 8
hei2 = 10
wid3 = 8
hei3 = 10
mx1 = 6
my1 = 7
mx2 = 10
my2 = 5
mx3 = 10
my3 = 5
cexRow1 = 0.4
cexRow2 = 0.8
cexRow3 = 0.8
myDist = function(p1) dist(p1, method="euclidean")
myHclust = function(p2) hclust(p2, method="ward")
heatmapTitle = 'TF Enrichment in Footprints\n(-log10(X))'
heatmapDiffTitle = 'TF Enrichment in Footprints\n(-log10(with)) - (-log10(without))'
inLoc = '/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/heatmap/'
outLoc = '/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/heatmap/'

# Reading Raw Data
d = as.matrix(read.table(paste(inLoc,'motif_enrichment_table.txt',sep=''), header=TRUE, row.names = 1))

# Log-transformation pseudocount calculation
minV = min(d[d>0]) # Calculating the minimum value greater than 0.0 

##########################################
### Heatmap Print Functions
##########################################

# Regular Heatmap
createHeatmap <- function(data,title,colorScheme,wid,hei,mx,my,rCex,outputFile){
  postscript(outputFile,width=wid,height=hei,horizontal=FALSE,paper='special')
  par(cex.axis=0.8, cex.main=0.8)
  heatmap.2(data, col=colorScheme, main=title, margins=c(my,mx), cexCol=0.4, cexRow=rCex, trace='none',
            sepwidth=c(2,2), sepcolor='black', Rowv=TRUE, Colv=FALSE, density.info = 'none', lhei = c(1.2, 8),
            distfun=myDist, hclustfun=myHclust, keysize = 2.0)
  dev.off()
  system(paste('epstopdf',outputFile,sep=' '))
}

##########################################
### All Conditions
##########################################

# Filter 1 = Keep only the lines in which there is at least one value < p-value1
dFilt1_All = d[apply(d,1,function(x) sum(x < pvalue1))>0,]

# All values X are now -log10(X+pseudocount), where pseudocount is the minimum value > 0.
dFilt1_All = apply(dFilt1_All, 1:2, function(x) -log10(x+minV))

# Filter 2 = Maximum p-value = 30
dFilt2_All = pmin(dFilt1_All,30)

# Parameters
hmcol <- colorRampPalette(brewer.pal(9, 'Reds'))(30)

# Creating Heatmaps
outputFileName = paste(outLoc,'all.eps',sep='')
createHeatmap(dFilt2_All,heatmapTitle,hmcol,wid1,hei1,mx1,my1,cexRow1,outputFileName)

##########################################
### Graphs with All Columns (All)
##########################################

# Filtering Data
# Filter 1 = Keep only the lines in which there is at least one value < p-value1
#dFilt1_All = d[apply(d,1,function(x) sum(x < pvalue1))>0,]
#colnames(dFilt1_All) = colnames(d)
# Filter 2.1 = Keep only the lines in which there is at least one value > p-value2
#dFilt2_All = dFilt1_All[apply(dFilt1_All,1,function(x) sum(x > pvalue2))>0,]
#colnames(dFilt2_All) = colnames(d)
# Filter 2.2 = Only the entries removed by filter 2.1
#dFilt3_All = dFilt1_All[apply(dFilt1_All,1,function(x) sum(x > pvalue2))<=0,]
#colnames(dFilt3_All) = colnames(d)

# Applying p-value Fix
# All values X are now -log10(X+pseudocount), where pseudocount is the minimum value > 0.
#dFilt1_All = apply(dFilt1_All, 1:2, function(x) -log10(x+minV)) # Converting values
#dFilt2_All = apply(dFilt2_All, 1:2, function(x) -log10(x+minV)) # Converting values
#dFilt3_All = apply(dFilt3_All, 1:2, function(x) -log10(x+minV)) # Converting values

# Parameters
#hmcol <- colorRampPalette(brewer.pal(9, 'Reds'))(1000)

# Creating Heatmaps
#outputFileName = paste(outLoc,'all.eps',sep='')
#createHeatmap(dFilt1_All,heatmapTitle,hmcol,wid1,hei1,mx1,my1,cexRow1,outputFileName)
#outputFileName = paste(outLoc,'all_CE.eps',sep='')
#createHeatmap(dFilt2_All,heatmapTitle,hmcol,wid2,hei2,mx2,my2,cexRow2,outputFileName)
#outputFileName = paste(outLoc,'all_NCE.eps',sep='')
#createHeatmap(dFilt3_All,heatmapTitle,hmcol,wid3,hei3,mx3,my3,cexRow3,outputFileName)

# Write matrix to tab-separated txt
#outputFileName = paste(outLoc,'all_CE.txt', sep='')
#write.table(dFilt2_All, file = outputFileName, sep='\t', append = FALSE)
#outputFileName = paste(outLoc,'all_NCE.txt', sep='')
#write.table(dFilt3_All, file = outputFileName, sep='\t', append = FALSE)


