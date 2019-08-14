library(gplots)
library(RColorBrewer)
library(Heatplus)

hmcol <- colorRampPalette(c("green", "black", "red"))(1000)
#hmcol <- colorRampPalette(brewer.pal(9, "Reds"))(1000)
pvalue=0.01

# footprints

postscript('/home/egg/hpcwork/izkf/projects/huvec_inflammation/heatmap/Results/footprints/rand_corr_diff.eps',width=5.0,height=10.0,horizontal=FALSE,paper='special')
par(cex.axis=1.0, cex.main=0.8)

d=as.matrix(read.table('/home/egg/hpcwork/izkf/projects/huvec_inflammation/heatmap/Input/footprints/rand_corr.txt'))
colnames(d)=gsub('\\.', ' ', colnames(d))

d=d[rowSums(d>pvalue)<dim(d)[2],]
d=d[rowSums(d)>0,]

minV = min(d[d>0])
d = apply(d, 1:2, function(x) -log10(x+minV))

selectVecWith = c(3,4,5,6,7)
dWith = d[,selectVecWith]
colnames(dWith)=c("cluster1","cluster2","cluster3","cluster4","cluster5")
selectVecWO = c(9,10,11,12,13)
dWO = d[,selectVecWO]
colnames(dWO)=c("cluster1","cluster2","cluster3","cluster4","cluster5")

newD = dWith - dWO

heatmap.2(newD,col=hmcol,main='TF Enrichment / footprints',margins=c(5,5),cexCol=0.8,cexRow=0.3,trace='none', sepwidth=c(2,2),sepcolor='black',Rowv=TRUE, Colv=FALSE,density.info = "none",lhei = c(1.2, 8))

dev.off()
system("epstopdf /home/egg/hpcwork/izkf/projects/huvec_inflammation/heatmap/Results/footprints/rand_corr_diff.eps")


