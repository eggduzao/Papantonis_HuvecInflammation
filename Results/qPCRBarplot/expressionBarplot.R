
##########################################
### Initialization
##########################################

# Import
library(ggplot2)
library(reshape2)

# Barplot Parameters
graphWidth = 5
graphHeight = 6
deviceName = "pdf"
deviceDPI = 300

##########################################
### Heatmap Functions
##########################################

# Barplot
createBarplot <- function(data, outputFile){

  # Barplot
  bar = ggplot(data, aes(Region, value)) 
  bar = bar + geom_bar(aes(fill = variable), width = 0.6, position = position_dodge(width=0.6), stat="identity")
  bar = bar + scale_fill_manual(values = c("Target1" = "black", "Target2" = "darkgrey", "Target3" = "grey"))
  bar = bar + coord_flip()
  bar = bar + theme_bw()

  # Saving graph
  ggsave(outputFile, plot=bar, device = deviceName, dpi = deviceDPI, width = graphWidth, height = graphHeight)

}

##########################################
### Execution
##########################################

# Reading gene symbols
df <- data.frame(Region = c("Control","p1","e1","e2","e3","e4","e5"), Target3 = c(0.98,0.37,0.56,0.59,0.64,0.74,0.85), Target2 = c(0.96,0.42,0.55,0.57,0.67,0.79,0.83), Target1 = c(0.99,0.40,0.51,0.62,0.69,0.74,0.88))
df$Region <- factor(rev(df$Region), levels = unique(rev(df$Region)))
df$Target3 <- factor(rev(df$Target3), levels = unique(rev(df$Target3)))
df$Target2 <- factor(rev(df$Target2), levels = unique(rev(df$Target2)))
df$Target1 <- factor(rev(df$Target1), levels = unique(rev(df$Target1)))
dataMelt <- melt(df, id.vars='Region')

# Barplot
outputFileNamePlot = "./qpcr.pdf"
createBarplot(dataMelt, outputFileNamePlot)


