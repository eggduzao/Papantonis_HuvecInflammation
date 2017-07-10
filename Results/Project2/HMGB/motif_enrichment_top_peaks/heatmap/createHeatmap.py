# Creates heatmap entry based on motif statistics output

# Import
import os
import sys

# Input
inLoc = "/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment_top_peaks/results/"
inList = ["HMGB1_hg19_top500_fp_withpeak/ME_HMGB1_hg19_top500_fp_withpeak/randtest_statistics_filtered.txt", "HMGB2_hg19_top500_Broad_fp_withpeak/ME_HMGB2_hg19_top500_Broad_fp_withpeak/randtest_statistics_filtered.txt", "HMGB2_hg19_top500_Narrow_fp_withpeak/ME_HMGB2_hg19_top500_Narrow_fp_withpeak/randtest_statistics_filtered.txt"]
outFileName = "./matrix_pvalue.txt"

headerList = ["", "HMGB1", "HMGB2_broad", "HMGB2_narrow"]
resDict = dict()

for inName in inList:

  inFileName = inLoc+inName
  inFile = open(inFileName,"r")
  #inFile.readline()
  for line in inFile:
    ll = line.strip().split("\t")
    try: resDict[ll[0]].append(ll[1])
    except Exception: resDict[ll[0]] = [ll[1]]
  inFile.close()

outFile = open(outFileName,"w")
outFile.write("\t".join(headerList)+"\n")
for k in sorted(resDict.keys()):
  outFile.write("\t".join([k]+resDict[k])+"\n")
outFile.close()


