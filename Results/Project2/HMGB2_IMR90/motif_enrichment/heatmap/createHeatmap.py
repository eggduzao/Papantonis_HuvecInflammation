# Creates heatmap entry based on motif statistics output

# Import
import os
import sys

resDict = dict()

inFileName = "/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB2_IMR90/motif_enrichment/results/HMGB2_p10/motif_enrichment_HMGB2_p10/p10_peaks_final_peaks/fulltest_statistics_filtered.txt"
inFile = open(inFileName,"r")
inFile.readline()
for line in inFile:
  ll = line.strip().split("\t")
  resDict[ll[0]] = [ll[1],"0.0"]
inFile.close()

inFileName = "/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB2_IMR90/motif_enrichment/results/HMGB2_p28/motif_enrichment_HMGB2_p28/p28_peaks_final_peaks/fulltest_statistics_filtered.txt"
inFile = open(inFileName,"r")
inFile.readline()
for line in inFile:
  ll = line.strip().split("\t")
  try: resDict[ll[0]][1] = ll[1]
  except Exception: resDict[ll[0]] = ["0.0",ll[1]]
inFile.close()

outFileName = "./matrix_pvalue_filtered.txt"
headerList = ["", "HMGB2.Young", "HMGB2.Old"]
outFile = open(outFileName,"w")
outFile.write("\t".join(headerList)+"\n")
for k in sorted(resDict.keys()):
  outFile.write("\t".join([k]+resDict[k])+"\n")
outFile.close()


