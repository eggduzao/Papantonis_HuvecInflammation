
# Import
import os
import sys

# Input
inLoc = "/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB1_HUVEC/motif_enrichment/raw_peaks/"
inFileList = ["HMGB1_HUVEC peaks_final"]
outLoc = "./"

for inName in inFileList:

  inFileName = inLoc+inName+".csv"
  outFileName = outLoc+inName+".bed"
  inFile = open(inFileName,"r")
  outFile = open(outFileName,"w")
  inFile.readline()
  for line in inFile:
    ll = line.strip().split(",")
    outFile.write("\t".join(["chr"+ll[0]]+ll[1:3])+"\n")
  inFile.close()
  outFile.close()


