
###################################################################################################
# INPUT
###################################################################################################

# Import
library(lattice)
library(reshape)
library(plotrix)

###################################################################################################
# FUNCTIONS
###################################################################################################

lineplot <- function(inName, dataFrame, outFileName){

  # Parameters
  minValue = 0 - (0.15 * max(dataFrame))
  maxValue = max(dataFrame)#1.5
  window = 500
  window_tick = 50
  yaxis_tick = 0.1
  my_lwd = 2.0
  my_lty = 1

  # Data frame
  nrows = nrow(dataFrame)
  ncols = ncol(dataFrame)

  # Cutting data frame
  dataFrame = dataFrame[((nrows/2)-(window/2)+1):((nrows/2)+(window/2)),]

  postscript(outFileName, width=8.0, height=5.0, horizontal=FALSE, paper='special')
  par(mar=c(5,4,1,1))
  
  plot(1:nrow(dataFrame), dataFrame[,1], type = "n", ylim=c(minValue,maxValue),
       xlab="Distance from motif center", ylab="Average profile", lwd=my_lwd, main=inName,
       lty=my_lty, axes = FALSE)

  lines(1:nrow(dataFrame), dataFrame[,1], col="red", lwd=my_lwd, lty=my_lty)
  lines(1:nrow(dataFrame), dataFrame[,2], col="green", lwd=my_lwd, lty=my_lty)

  axis(side = 1, at=seq(1,nrow(dataFrame)+1,window_tick), labels=seq(-(window/2),(window/2),window_tick))
  axis(side = 2, at=seq(0,maxValue,yaxis_tick))

  abline(h = 0, col = "gray60")
  abline(v = (window/2)+1, col = "gray60")

  abline(h = seq(0,maxValue,yaxis_tick), v = seq(1,nrow(dataFrame)+1,window_tick), col = "lightgray", lty = 3)

  dev.off()
  system(paste("epstopdf",outFileName,sep=" "))
  system(paste("rm",outFileName,sep=" "))

}

###################################################################################################
# EXECUTION
###################################################################################################

# Parameters
inLoc = "/work/eg474423/eg474423_Projects/trunk/TfbsPrediction/Results/ATAC/Profile/profile_table/"
outLoc = "/work/eg474423/eg474423_Projects/trunk/TfbsPrediction/Results/ATAC/Profile/profile_graphs/"

# Iterating on input folders
inFileNameList = Sys.glob(paste(inLoc,"*/",sep=""))
for(inFileName in inFileNameList){

  splVec = strsplit(inFileName,"/",fixed=TRUE)[[1]]
  inName = splVec[length(splVec)]

  inFileName = paste(inFileName,inName,"_twoside_1.txt",sep="")
  outFileName = paste(outLoc,inName,".eps",sep="")
  dataTable = read.table(inFileName, header=TRUE)

  lineplot(inName,dataTable,outFileName)

}

# Reading table
#bx = read.table(inFileName, header=TRUE)

# Making plot
#lineplot(bx,outFileName)

#strsplit(Sys.glob("./*.*")[1],"/",fixed=TRUE)[[1]][-1]

