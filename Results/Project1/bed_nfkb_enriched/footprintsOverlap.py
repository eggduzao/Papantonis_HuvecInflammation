
# Import
import os
import sys
import glob

# Input
inLoc = "/hpcwork/izkf/projects/huvec_inflammation/bed_nfkb_enriched/original/"
outLoc = "/hpcwork/izkf/projects/huvec_inflammation/bed_nfkb_enriched/footprints/"
footprintFileName = "/hpcwork/izkf/projects/huvec_inflammation/bed_footprints/hg18/HD_H3K4me1_ModelHuvec_10.bed"
inFileList = glob.glob(inLoc+"*.bed")

# Execution
for inFileName in inFileList:
    inName = inFileName.split("/")[-1].split(".")[0]
    inFileNameSorted = outLoc+inName+"_sort.bed"
    outputFileName = outLoc+inName+".bed"
    os.system("sort -k1,1 -k2,2n "+inFileName+" > "+inFileNameSorted)
    os.system("intersectBed -wa -a "+footprintFileName+" -b "+inFileNameSorted+" -f 1 > "+outputFileName)
    os.system("rm "+inFileNameSorted)


