library(gplots)
library(RColorBrewer)

hmcol <- colorRampPalette(brewer.pal(9, "Reds"))(256)
hmcol <- hmcol[length(hmcol):1]
colnames(d)=gsub("\\.", " ", colnames(d))

d=as.matrix(read.table("rand_corr_sel.txt"))
pvalue=0.05

pdf("gfp_enrich_irf8_pu1.pdf")
d[d>pvalue]=pvalue+0.01 # make all values to be between 0 and pvalue + 0.01
d=d[rowSums(d>pvalue)<dim(d)[2],] # keep only motifs with at least one entry < pvalue

#colnames(d)=c("IRF8-PU.1 Induc.","IRF8-PU.1 Rep.","IRF8+PU.1 Induc.","PU.1-IRF8 Induc.","IRF8+PU.1 Rep.","PU.1-IRF8  Rep.")
heatmap.2(d,col=hmcol,margins = c(8,9),cexCol = 0.8,cexRow=0.7,trace="none", sepwidth=c(2, 2),sepcolor='black')

title('TF Enrichment GFP+/GFP- Irf8 and PU.1 Peaks (0.05)')
dev.off()


