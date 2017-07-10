
# Import
import os
import sys

inList = ["/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB2_IMR90/motif_enrichment/results/HMGB2_p10/motif_enrichment_HMGB2_p10/p10_peaks_final_peaks/fulltest_statistics.txt", "/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB2_IMR90/motif_enrichment/results/HMGB2_p28/motif_enrichment_HMGB2_p28/p28_peaks_final_peaks/fulltest_statistics.txt"]
geneFileNameList = ["/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB2_IMR90/motif_enrichment/expression/young_genes.txt", "/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB2_IMR90/motif_enrichment/expression/old_genes.txt"]

for i in range(0,len(inList)):

  inFileName = inList[i]
  geneFileName = geneFileNameList[i]
  outFileName = inFileName[:-4]+"_filtered.txt"
  outFile = open(outFileName,"w")

  geneList = []
  geneFile = open(geneFileName,"r")
  for line in geneFile:
    geneList.append(line.strip().upper())
  geneFile.close()

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


