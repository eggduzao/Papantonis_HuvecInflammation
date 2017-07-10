
# Import
import os
import sys

inList = ["/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment_top_peaks/results/HMGB1_hg19_top500_fp_withpeak/ME_HMGB1_hg19_top500_fp_withpeak/randtest_statistics.txt", "/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment_top_peaks/results/HMGB2_hg19_top500_Broad_fp_withpeak/ME_HMGB2_hg19_top500_Broad_fp_withpeak/randtest_statistics.txt", "/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment_top_peaks/results/HMGB2_hg19_top500_Narrow_fp_withpeak/ME_HMGB2_hg19_top500_Narrow_fp_withpeak/randtest_statistics.txt"]
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



