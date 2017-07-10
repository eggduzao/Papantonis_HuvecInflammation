table=read.table("plot_table.txt",row.names=NULL)

library(ggplot2)
library(reshape)

names=colnames(table)
names[4:83]=seq(-2000,2000,by=50)
colnames(table)=names
rownames(table)=paste0(table[,1],"_",table[,2],"_",table[,3])

table$names=paste0(table[,1],"_",table[,2],"_",table[,3])


dfm <- melt(table, variable_name = "position")

dfm$position=as.numeric(dfm$position)

#ggplot(dfm, aes(x=position, y=value, color=Canonical, group=Canonical)) + geom_line(alpha=0.8,size=0.5) +  scale_color_manual(values=c("red", "blue")) +  scale_fill_discrete(name = "Canonical Motif")  + #geom_area(aes(fill=Canonical),alpha=0.25,position="identity") +  facet_grid(Group_tag~row.names) + scale_fill_manual(values=c("red", "blue"))  + theme(axis.ticks.y = element_blank())



pdf("lineplots.pdf")


ggplot(dfm, aes(x=position, y=value, color=Canonical,
group=Canonical)) + geom_line(alpha=0.8) +
scale_color_manual(values=c("red", "blue")) +
scale_fill_discrete(name = "Canonical Motif") + theme_bw() +
geom_area(aes(fill=Canonical),alpha=0.25,position="identity") +
facet_grid(Group_tag~row.names) + scale_fill_manual(values=c("red",
"blue"))+

theme(strip.text.x = element_text(size = 12),axis.title.x =
element_text(size = 14),axis.title.y = element_text(size =
14),strip.text.y = element_text(size =
12))+scale_x_continuous(breaks=c(0,20,40,60,80), labels=c("","-1000",
"0","1000","")) + ylab("Read (RPKM)") + xlab("Position")

dev.off()

