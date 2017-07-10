
# Import
import os
import sys

inList = ["/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB1_HUVEC/motif_enrichment/results/motif_enrichment_HMGB1/HMGB1_HUVEC_peaks_final_peaks/fulltest_statistics.txt"]
geneFileName = "/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB/expression/young_90perc_mapped.txt"

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
      tfList = [e.upper() for e in "//".join(tfList).split("//")]
    else:
      tfList = [e.upper() for e in ll[0].split("_")]
    if(ll[0] == "E2A-Homer.pwm"): tfList = ["E2A","TCF3","TCF-3"]

    flag = False
    for tf in tfList:
      if(tf in geneList):
        flag = True
        break
 
    if(flag): outFile.write(line) 

  inFile.close()
  outFile.close()


