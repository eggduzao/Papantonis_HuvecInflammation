library(gplots)
library(RColorBrewer)

d=read.table("motifs_fold_high.txt")
#hmcol <- colorRampPalette(brewer.pal(3,'RdBu'))(1000)
hmcol <- colorRampPalette(c('red', 'white', 'blue'))(n = 899)
pdf("Comp_enrich_high_fold.txt")
d1=d[abs(rowMeans(d[, 1:4] - d[, 6:9])) > 1,1:4]-d[abs(rowMeans(d[, 1:4] - d[, 6:9])) > 1,6:9]

heatmap.2(as.matrix(d1]),col=hmcol,main='TF Enrichment Comp',margins=c(7,8),cexCol=1,cexRow=0.7,trace='none', sepwidth=c(2,2),sepcolor='black',Rowv=TRUE, Colv=FALSE,density.info = 'none')
dev.off()

d=read.table("comb_pvalues.txt")
pdf("comp_final.pdf")
heatmap.2(as.matrix(d),col=hmcol,main='TF Enrich. Foot. (Exp)',margins=c(7,15),cexCol=1,cexRow=0.75,trace='none', sepwidth=c(2,2),sepcolor='black',Rowv=TRUE, Colv=FALSE,density.info = 'none')
dev.off()


