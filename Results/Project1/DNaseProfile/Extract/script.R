
#################################################
# Parameters
#################################################

# Import
library(plotrix)

# Data Parameters
inputLocation = '/home/egg/hpcwork/izkf/projects/huvec_inflammation/dnase_profile/Results/'
outLoc = '/home/egg/hpcwork/izkf/projects/huvec_inflammation/dnase_profile/Extract/'

# Plot Parameters
cols=rainbow(1)
styVec=c(1)
pointStyVec=c(21)
mar.default <- c(5,5,4,2)

#################################################
# Individual Plots
#################################################

if(FALSE){

# Input File Parameters
dataFileNameList = c( 'DNaseBO_NFKB1', 'DNaseBO_REL', 'DNaseBO_RELA', 'DNase_NFKB1', 'DNase_REL', 'DNase_RELA' )
maxYList = c(18.0,22.0,23.0,2.5,3.0,3.0)
halfWindowList = c(300,300,300,150,150,150)
outputLocation = paste(outLoc,'Individual/',sep='')

# Input File Loop
for (d in (1:length(dataFileNameList))){

  # Column Parameters / Reading Input Data
  maxY = maxYList[d]
  halfWindow = halfWindowList[d]
  dataFileName = paste(inputLocation,dataFileNameList[d],'_1000_norm_line.txt',sep='')
  fullData = read.table(dataFileName,header=TRUE)

  # Column Loop
  for (c in (2:ncol(fullData))){

    # Parameters
    outLoc = paste(outputLocation,dataFileNameList[d],'/',sep='')
    outputFileName = paste(outLoc,colnames(fullData)[c],'.eps',sep='')
    system(paste('mkdir -p',outLoc,sep=' '))

    # Initializing Graph
    postscript(outputFileName,width=7.0,height=7.0,horizontal=FALSE,paper='special')
    par(mar=mar.default)

    # Selecting Columns
    selData = fullData[,c(1,c)]

    # Selecting Rows
    midPoint = ceiling(nrow(selData)/2)
    selectList = c((midPoint-halfWindow):(midPoint+halfWindow))
    selData = selData[selectList,]

    # Plot
    plot(selData[,1],selData[,2],type='n',ylab='Average DNase Intensity',xlab='Distance to TF (bp)',
         main=paste(dataFileNameList[d],colnames(fullData)[c],sep=' / '),
         ylim=c(0,maxY),cex.lab=1.0,cex.axis=1.0,cex.main=1.0,cex.sub=1.0)
    #myLegend(-0.035,0.59,c(''),lty=legendStyVec,col=legendCol,lwd=2.0,title='',cex=1.3,ncol=2,seg.len=segLen)
    for (i in (2:ncol(selData))){
      lines(selData[,1],selData[,i],col=cols[i-1],lty=styVec[i-1],lwd=0.8)
    }

    # Termination
    dev.off()
    system(paste('epstopdf',outputFileName,sep=' '))

  }
}

}
#################################################
# Cluster
#################################################

# Plot Parameters
cols=rainbow(5)
styVec=c(1,1,1,1,1)
pointStyVec=c(21,21,21,21,21)

# Input File Parameters
dataFileNameList = c( 'DNaseBO_NFKB1', 'DNaseBO_REL', 'DNaseBO_RELA', 'DNase_NFKB1', 'DNase_REL', 'DNase_RELA' )
maxYList = c(18.0,22.0,23.0,2.5,3.0,3.0)
halfWindowList = c(300,300,300,100,100,100)
outputLocation = paste(outLoc,'Cluster/',sep='')

# Input File Loop
for (d in (1:length(dataFileNameList))){

  # Column Parameters / Reading Input Data
  maxY = maxYList[d]
  halfWindow = halfWindowList[d]
  selMatrix = matrix( c(c(2,3,4,5,6), c(7,8,9,10,11)), nrow=5, ncol=2, byrow = FALSE)
  outName = c("with","without")
  dataFileName = paste(inputLocation,dataFileNameList[d],'_1000_norm_line.txt',sep='')
  fullData = read.table(dataFileName,header=TRUE)

  # Column Loop
  for (c in (1:ncol(selMatrix))){

    # Parameters
    outLoc = paste(outputLocation,dataFileNameList[d],'/',sep='')
    outputFileName = paste(outLoc,outName[c],'.eps',sep='')
    system(paste('mkdir -p',outLoc,sep=' '))

    # Initializing Graph
    postscript(outputFileName,width=7.0,height=7.0,horizontal=FALSE,paper='special')
    par(mar=mar.default)

    # Selecting Columns
    selVec = selMatrix[,c]
    selData = fullData[,c(1,selVec)]

    # Selecting Rows
    midPoint = ceiling(nrow(selData)/2)
    selectList = c((midPoint-halfWindow):(midPoint+halfWindow))
    selData = selData[selectList,]

    # Plot
    plot(selData[,1],selData[,2],type='n',ylab='Average DNase Intensity',xlab='Distance to TF (bp)',
         main=paste(dataFileNameList[d],outName[c],sep=' / '),
         ylim=c(0,maxY),cex.lab=1.0,cex.axis=1.0,cex.main=1.0,cex.sub=1.0)
    legend('topright',c('cluster 1','cluster 2','cluster 3','cluster 4','cluster 5'),
           lty=styVec,col=cols,lwd=2.0,cex=1.0,ncol=1)
    for (i in (2:ncol(selData))){
      lines(selData[,1],selData[,i],col=cols[i-1],lty=styVec[i-1],lwd=0.5)
    }
    abline(v=0.0,col='gray',lty='22')

    # Termination
    dev.off()
    system(paste('epstopdf',outputFileName,sep=' '))

  }
}


