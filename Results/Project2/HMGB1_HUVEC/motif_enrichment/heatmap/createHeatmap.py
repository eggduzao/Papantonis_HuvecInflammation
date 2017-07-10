# Creates heatmap entry based on motif statistics output

# Import
import os
import sys

# Input
inList = ["/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB1_HUVEC/motif_enrichment/results/motif_enrichment_HMGB1/HMGB1_HUVEC_peaks_final_peaks/fulltest_statistics.txt"]
outFileName = "./matrix_pvalue.txt"

headerList = ["", "HMGB1", " "]
resDict = dict()

for inFileName in inList:

  inFile = open(inFileName,"r")
  inFile.readline()
  for line in inFile:
    ll = line.strip().split("\t")
    try: resDict[ll[0]].append(ll[1])
    except Exception: resDict[ll[0]] = [ll[1]]
  inFile.close()

outFile = open(outFileName,"w")
outFile.write("\t".join(headerList)+"\n")
for k in sorted(resDict.keys()):
  outFile.write("\t".join([k]+resDict[k]+resDict[k])+"\n")
outFile.close()


