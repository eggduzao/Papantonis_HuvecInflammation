
##########################################
### Initialization
##########################################

# Import
library(gplots)
library(RColorBrewer)

# Parameters
pvalue1 = 0.001
pvalue2 = 0.00001
wid1 = 6
hei1 = 10
wid2 = 8
hei2 = 10
wid3 = 8
hei3 = 10
mx1 = 10
my1 = 5
mx2 = 10
my2 = 5
mx3 = 10
my3 = 5
cexRow1 = 0.6
cexRow2 = 0.8
cexRow3 = 0.8
myDist = function(p1) dist(p1, method="euclidean")
myHclust = function(p2) hclust(p2, method="ward")
heatmapTitle = 'TF Enrichment\nin Footprints\n(-log10(X))'

fileName = "matrix_pvalue"

# Reading Raw Data
d=as.matrix(read.table(paste(fileName,".mtx",sep=""), sep="\t", header=T, row.names=1))

# Log-transformation pseudocount calculation
minV = min(d[d>0]) # Calculating the minimum value greater than 0.0

##########################################
### Heatmap Print Functions
##########################################

# Regular Heatmap
createHeatmap <- function(data,title,colorScheme,wid,hei,mx,my,rCex,outputFile){
  postscript(outputFile,width=wid,height=hei,horizontal=FALSE,paper='special')
  par(cex.axis=0.8, cex.main=0.8)
  heatmap.2(data, col=colorScheme, breaks = hmbreaks, main=title, margins=c(my,mx), cexCol=0.8, cexRow=rCex, trace='none',
            sepwidth=c(2,2), sepcolor='black', Rowv=TRUE, Colv=FALSE, density.info = 'none', lhei = c(0.55, 4), tracecol=NA,
            distfun=myDist, hclustfun=myHclust, keysize = 2.5 )
  dev.off()
  system(paste('epstopdf',outputFile,sep=' '))
  system(paste('rm',outputFile,sep=' '))
}

# Differential Heatmap
createHeatmapDiff <- function(data,title,colorScheme,colorBreaks,wid,hei,mx,my,rCex,outputFile){
  postscript(outputFile,width=wid,height=hei,horizontal=FALSE,paper='special')
  par(cex.axis=1.0, cex.main=0.8)
  heatmap.2(data, col=colorScheme, breaks=colorBreaks, main=title, margins=c(my,mx), cexCol=0.8, cexRow=rCex, trace='none', sepwidth=c(2,2), sepcolor='black', density.info = 'none', lhei = c(1.2, 6), dendrogram = "none", Rowv = FALSE, Colv = FALSE )
  dev.off()
  system(paste('epstopdf',outputFile,sep=' '))
  system(paste('rm',outputFile,sep=' '))
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
hmcol = colorRampPalette(brewer.pal(9, 'Reds'))(99)
hmbreaks = c(seq(0,10,length=100))

# Creating Heatmaps
outputFileName = paste(fileName,".eps",sep="")
createHeatmap(dFilt1_All,heatmapTitle,hmcol,wid1,hei1,mx1,my1,cexRow1,outputFileName)

# Write matrix to tab-separated txt
outputFileName = paste(fileName,"_out.txt",sep="")
write.table(dFilt1_All, file = outputFileName, sep='\t', append = FALSE)


