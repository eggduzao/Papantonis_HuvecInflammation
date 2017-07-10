
# Import
import os
import sys
import glob

# Input
outputLocation = "/home/egg/hpcwork/izkf/projects/huvec_inflammation/dnase_profile/Input/"
inputFileList = glob.glob("/home/egg/hpcwork/izkf/projects/huvec_inflammation/motif_enrichment/Results_10/footprints/*/mpbs.bb")
factorList = ["MA0105.3.NFKB1", "MA0101.1.REL", "MA0107.1.RELA"]

# Iterating on input files
for inputFileName in inputFileList:

    # Fetching file names
    inName = inputFileName.split("/")[-2].split(".")[0]
    bedFileName = inputFileName[:-2]+".bed"

    # Converting to bed
    os.system("bigBedToBed "+inputFileName+" "+bedFileName)

    # Iterating on factorList
    for factor in factorList:
        factorName = factor.split(".")[2]
        outputFileName = outputLocation+inName+"_"+factorName+".bed"
        os.system("grep "+factor+" "+bedFileName+" > "+outputFileName)

    # Removing files
    os.system("rm "+bedFileName)


