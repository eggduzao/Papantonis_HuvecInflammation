
##########################################
### Initialization
##########################################

# Import
library(gplots)
library(RColorBrewer)

# Parameters
pvalue1 = 0.01
wid1 = 5
hei1 = 10
wid2 = 8
hei2 = 10
wid3 = 8
hei3 = 10
mx1 = 5
my1 = 5
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
inLoc = '/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_with_vs_wo/heatmap_input/'
outLoc = '/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_with_vs_wo/heatmap_results/'

inName = "footprints_corr"

# Reading Raw Data
d=as.matrix(read.table(paste(inLoc,inName,'.txt',sep=''),header = TRUE, row.names=1))
#colnames(d)=gsub('\\.', ' ', colnames(d))

# Log-transformation pseudocount calculation
minV = min(d[d>0]) # Calculating the minimum value greater than 0.0 

##########################################
### Heatmap Print Functions
##########################################

# Regular Heatmap
createHeatmap <- function(data,title,colorScheme,breaks,wid,hei,mx,my,rCex,outputFile){
  postscript(outputFile,width=wid,height=hei,horizontal=FALSE,paper='special')
  par(cex.axis=1.0, cex.main=0.8)
  heatmap.2(data, col=colorScheme, breaks=breaks, main=title, margins=c(my,mx), cexCol=0.8, cexRow=rCex, trace='none',
            sepwidth=c(2,2), sepcolor='black', Rowv=TRUE, Colv=FALSE, density.info = 'none', lhei = c(1.2, 8),
            distfun=myDist, hclustfun=myHclust, keysize = 2.5 )
  dev.off()
  system(paste('epstopdf',outputFile,sep=' '))
}

##########################################
### Graphs with All Columns (All)
##########################################

# Filtering Data
# Filter 1 = Keep only the lines in which there is at least one value < p-value1
dFilt1_All = d[apply(d,1,function(x) sum(x < pvalue1))>0,]
colnames(dFilt1_All) = colnames(d)

# Applying p-value Fix
# All values X are now -log10(X+pseudocount), where pseudocount is the minimum value > 0.
dFilt1_All = apply(dFilt1_All, 1:2, function(x) -log10(x+minV)) # Converting values

# Parameters
colors = c(seq(0,3,length=100),seq(3,6,length=100))
hmcol <- colorRampPalette(c("white", "blue"))(n = 199)
#hmcol <- colorRampPalette(brewer.pal(9, 'Reds'))(1000)

# Creating Heatmaps
outputFileName = paste(outLoc,inName,'.eps',sep='')
createHeatmap(dFilt1_All,heatmapTitle,hmcol,colors,wid1,hei1,mx1,my1,cexRow1,outputFileName)

# Write matrix to tab-separated txt
outputFileName = paste(outLoc,inName,'.txt', sep='')
write.table(dFilt1_All, file = outputFileName, sep='\t', append = FALSE)


