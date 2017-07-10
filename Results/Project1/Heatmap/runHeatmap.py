
###################################################################################################
# Import
###################################################################################################

import os
import sys
import glob

###################################################################################################
# Input
###################################################################################################

# Input
inLoc = "/home/egg/hpcwork/izkf/projects/huvec_inflammation/motif_enrichment/Results_10/"
#inList = ["footprints", "original"]
inList = ["footprints"]

# File/Folder
createHeatmapPy = "/home/egg/hpcwork/izkf/projects/huvec_inflammation/heatmap/createHeatmap.py"
inFolder = "/home/egg/hpcwork/izkf/projects/huvec_inflammation/heatmap/Input/"
resFolder = "/home/egg/hpcwork/izkf/projects/huvec_inflammation/heatmap/Results/"

# Parameters
pValue = "0.01"
factorsToRemove = []

###################################################################################################
# Creating Input
###################################################################################################

# Iterating on input list
for inName in inList:
 
    # Creating output folder
    outputLocation = inFolder+inName+"/"
    os.system("mkdir -p "+outputLocation)

    # Executing python script to create input
    createComm = "python "+createHeatmapPy+" "
    createComm += outputLocation+" "+inLoc+inName+"/*/"
    os.system(createComm)

    # Removing factors
    if(factorsToRemove):
        for inFileName in glob.glob(outputLocation+"*.txt"):
            tempFileName = inFileName+"TEMP"
            tempFile = open(tempFileName,"w")
            inFile = open(inFileName,"r")
            for line in inFile:
                ll = line.strip().split("\t")
                if(ll[0] not in factorsToRemove): tempFile.write(line)
            os.system("rm "+inFileName)
            os.system("mv "+tempFileName+" "+inFileName)

###################################################################################################
# Creating Heatmap
###################################################################################################

"""
# Creating output .R file
outputFileName = resFolder+"script.R"
outputFile = open(outputFileName,"w")

# Initialize .R file
outputFile.write("library(gplots)\n")
outputFile.write("library(RColorBrewer)\n")
outputFile.write("pvalue="+pValue+"\n\n")

# Iterating on input list
for inName in inList:

    # Fetching txtList
    txtList = ["rand_corr"]

    # Iterating on txtList
    for txtFileName in txtList:

        # Parameters
        inTxtFileName = inFolder+inName+"/"+txtFileName+".txt"
        outputEpsNameAll = resFolder+inName+"/"+txtFileName+"_all.eps"
        outputEpsNameCluster = resFolder+inName+"/"+txtFileName+"_cluster.eps"
        outputEpsNameDiff = resFolder+inName+"/"+txtFileName+"_diff.eps"

        # Writing R - Init
        outputFile.write("##########################################\n")
        outputFile.write("### "+inName+"\n")
        outputFile.write("##########################################\n\n")
        outputFile.write("d=as.matrix(read.table('"+inTxtFileName+"'))\n")
        outputFile.write("colnames(d)=gsub('\\\\.', ' ', colnames(d))\n")
        outputFile.write("d=d[rowSums(d>pvalue)<dim(d)[2],]\n")
        outputFile.write("d=d[rowSums(d)>0,]\n")
        outputFile.write("minV = min(d[d>0])\n")
        outputFile.write("d = apply(d, 1:2, function(x) -log10(x+minV))\n\n")

        # Writing R - All
        outputFile.write("# All\n")
        outputFile.write("postscript('"+outputEpsNameAll+"',width=5.0,height=10.0,horizontal=FALSE,paper='special')\n")
        outputFile.write("par(cex.axis=1.0, cex.main=0.8)\n")
        outputFile.write("hmcol <- colorRampPalette(brewer.pal(9, 'Reds'))(1000)\n")
        outputFile.write("heatmap.2(d,col=hmcol,main='TF Enrichment / "+inName+"',margins=c(5,5),cexCol=0.8,cexRow=0.3,trace='none', sepwidth=c(2,2),sepcolor='black',Rowv=TRUE, Colv=FALSE,density.info = 'none',lhei = c(1.2, 8))\n")
        outputFile.write("dev.off()\n")
        outputFile.write("system('epstopdf "+outputEpsNameAll+"')\n\n")

        # Writing R - Cluster
        outputFile.write("# Cluster\n")
        outputFile.write("selectVecCluster = c(3,4,5,6,7,9,10,11,12,13)\n")
        outputFile.write("dCluster = d[,selectVecCluster]\n")
        outputFile.write("colnames(dCluster) = colnames(d)[selectVecCluster]\n\n")
        outputFile.write("postscript('"+outputEpsNameCluster+"',width=5.0,height=10.0,horizontal=FALSE,paper='special')\n")
        outputFile.write("par(cex.axis=1.0, cex.main=0.8)\n")
        outputFile.write("hmcol <- colorRampPalette(brewer.pal(9, 'Reds'))(1000)\n")
        outputFile.write("heatmap.2(dCluster,col=hmcol,main='TF Enrichment / "+inName+"',margins=c(5,5),cexCol=0.8,cexRow=0.3,trace='none', sepwidth=c(2,2),sepcolor='black',Rowv=TRUE, Colv=FALSE,density.info = 'none',lhei = c(1.2, 8))\n")
        outputFile.write("dev.off()\n")
        outputFile.write("system('epstopdf "+outputEpsNameCluster+"')\n\n")

        # Writing R - Diff
        outputFile.write("# Diff\n")
        outputFile.write("selectVecWith = c(3,4,5)\n")
        outputFile.write("dWith = d[,selectVecWith]\n")
        outputFile.write("colnames(dWith)=c('cluster1','cluster2','cluster3')\n")
        outputFile.write("selectVecWO = c(9,10,11)\n")
        outputFile.write("dWO = d[,selectVecWO]\n")
        outputFile.write("colnames(dWO)=c('cluster1','cluster2','cluster3')\n")
        outputFile.write("newD = dWith - dWO\n\n")
        outputFile.write("postscript('"+outputEpsNameDiff+"',width=5.0,height=10.0,horizontal=FALSE,paper='special')\n")
        outputFile.write("par(cex.axis=1.0, cex.main=0.8)\n")
        outputFile.write("colorBreaks = c(seq(-10,-2,length=300),seq(-2,2,length=300),seq(2,10,length=300))\n")
        outputFile.write("hmcol <- colorRampPalette(c('red', 'black', 'green'))(n = 899)\n")
        outputFile.write("heatmap.2(newD,col=hmcol,breaks=colorBreaks,main='TF Enrichment / "+inName+"',margins=c(5,5),cexCol=0.8,cexRow=0.3,trace='none', sepwidth=c(2,2),sepcolor='black',Rowv=TRUE, Colv=FALSE,density.info = 'none',lhei = c(1.2, 8))\n")
        outputFile.write("dev.off()\n")
        outputFile.write("system('epstopdf "+outputEpsNameDiff+"')\n\n")

# Termination
outputFile.close()
os.system("R CMD BATCH "+outputFileName+" "+outputFileName+"out")
#os.system("rm "+outputFileName+"out")
"""


