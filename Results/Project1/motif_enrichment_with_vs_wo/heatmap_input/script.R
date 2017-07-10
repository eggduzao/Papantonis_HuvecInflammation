library(gplots)
library(RColorBrewer)

hmcol <- colorRampPalette(brewer.pal(20, "RdBu"),interpolate = "linear")(256)



d=read.table("footprints_corr_sel.txt",sep="\t",header=TRUE)
row.names(d)=d[,1]
d=d[,-1]

pvalue=0.0001
d_filter=d[rowSums(d[,c(1,7)]<pvalue)>0,c(1,7)]

d_filter[d_filter>pvalue]=1

d_filter=-log10(d_filter)

d_aux=cbind(d_filter[,1]-d_filter[,2],d_filter[,1]-d_filter[,2])
row.names(d_aux)=row.names(d_filter)

colnames(d_aux)=c("","")
heatmap.2(as.matrix(d_aux), Colv=FALSE, col=hmcol,margins = c(8,9),cexCol = 1.5,cexRow=0.6,trace="none", sepwidth=c(2, 2),sepcolor='black')
title('TF Enrichment')


pvalue=0.001
d_filter=d[rowSums(d[,c(1:6,7:12)]<pvalue)>0,c(1:6,7:12)]

d_filter[d_filter>pvalue]=1

d_filter=-log10(d_filter)

d_aux=d_filter[,1:6]-d_filter[,7:12]

pdf("heatmap_groups.pdf")
colnames(d_aux)=c("All","G1","G2","G3","G4","G5")
heatmap.2(as.matrix(d_aux), Colv=FALSE, col=hmcol,margins = c(10,10),cexCol = 1.5,cexRow=0.8,trace="none", sepwidth=c(2, 2),sepcolor='black')
title('TF Enrichment ')
dev.off()


