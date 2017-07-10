
# Import
import os
import sys
import glob

# Input
inLoc = "/hpcwork/izkf/projects/huvec_inflammation/bed_nfkb_enriched/original/"
outLoc = "/hpcwork/izkf/projects/huvec_inflammation/bed_nfkb_enriched/"
footprintFileName = "/hpcwork/izkf/projects/huvec_inflammation/bed_footprints/hg18/HD_H3K4me1_ModelHuvec_10.bed"
inFileList = glob.glob(inLoc+"*.bed")

# Counts number of lines in a file
def getFileSize(fileName):
    inFile = open(fileName,"r")
    counter = 0
    for line in inFile: counter += 1
    inFile.close()
    return counter

# Output statistics file
outputStatsFileName = outLoc+"stats.txt"
outputStatsFile = open(outputStatsFileName,"w")

# Execution
for inFileName in inFileList:
    inName = inFileName.split("/")[-1].split(".")[0]
    inFileNameSorted = outLoc+inName+"_sort.bed"
    outputFileName = outLoc+inName+".bed"
    outputFileNameSorted = outLoc+inName+"_sort2.bed"
    os.system("sort -k1,1 -k2,2n "+inFileName+" > "+inFileNameSorted)
    os.system("intersectBed -wa -a "+inFileNameSorted+" -b "+footprintFileName+" > "+outputFileName)
    os.system("sort "+outputFileName+" | uniq > "+outputFileNameSorted)
    lineNb = getFileSize(outputFileNameSorted)
    totLineNb = getFileSize(inFileNameSorted)
    outputStatsFile.write("\t".join([inName,str(float(lineNb)*100/float(totLineNb))+"%"])+"\n")
    os.system("rm "+inFileNameSorted+" "+outputFileName+" "+outputFileNameSorted)

# Termination
outputStatsFile.close()


