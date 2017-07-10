
# Import
import os
import sys

inList = ["/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment/results/HMGB1/ME_HMGB1_footprints_peaks/HMGB1_footprints_peaks/randtest_statistics.txt", "/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment/results/HMGB2/ME_HMGB2_footprints_peaks/HMGB2_footprints_peaks/randtest_statistics.txt"]
geneFileName = "/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/expression/young_90perc_mapped.txt"

geneList = []
geneFile = open(geneFileName,"r")
for line in geneFile:
  geneList.append(line.strip().upper())
geneFile.close()

for inFileName in inList:

  outFileName = inFileName[:-4]+"_filtered.txt"
  outFile = open(outFileName,"w")

  inFile = open(inFileName,"r")
  inFile.readline()

  for line in inFile:

    ll = line.strip().split("\t")
    
    if(ll[0][:2] == "MA"):
      tfList = [e.upper() for e in ll[0].split(".")]
    else:
      tfList = [e.upper() for e in ll[0].split("_")]

    flag = False
    for tf in tfList:
      if(tf in geneList):
        flag = True
        break
 
    if(flag): outFile.write(line) 

  inFile.close()
  outFile.close()



