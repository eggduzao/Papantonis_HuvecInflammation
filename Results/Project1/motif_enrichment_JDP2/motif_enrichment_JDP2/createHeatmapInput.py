# Creates heatmap entry based on motif statistics output

# Import
import os
import sys
from glob import glob

# Reading data
headerList = ["FACTOR"]
resDict = dict()
for inFileName in glob("/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/result/*/*/*/randtest_statistics.txt"):

  if("random" in inFileName):
    ll = inFileName.split("/")
    ss = ll[-3].split("_")
    if("NFKBwith" in inFileName): labelName = "_".join(ss[1:-2])+"_with_vs_random"
    else: labelName = "_".join(ss[1:-2])+"_wo_vs_random"
  else: labelName = "_".join(inFileName.split("/")[-3].split("_")[1:])
  headerList.append(labelName)

  inFile = open(inFileName,"r")
  inFile.readline()
  for line in inFile:
    ll = line.strip().split("\t")
    factor = ll[0]
    pvalue = ll[2]
    try: resDict[factor].append(pvalue)
    except Exception: resDict[factor] = [pvalue]

  inFile.close()

# Writing data
outFileName = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/heatmap/motif_enrichment_table.txt"
outFile = open(outFileName,"w")
outFile.write("\t".join(headerList)+"\n")
for k in sorted(resDict.keys()): outFile.write("\t".join([k]+resDict[k])+"\n")
outFile.close()


