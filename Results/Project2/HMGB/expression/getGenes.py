
# Import
import os
import sys
import numpy as np
from rgt.AnnotationSet import AnnotationSet

# Input
percentile = 90
expFileName = "HUVEC_OldvYoung_Expression.tab"
outputFileNameM = "young_90perc_mapped.txt"
outputFileNameU = "young_90perc_unmapped.txt"

# Fetching expression
expFile = open(expFileName,"r")
expFile.readline()
allExpVec = []
geneList = []
counter = 0
for line in expFile:
  ll = line.strip().split("\t")
  if(len(ll) < 15): continue
  gene = ll[0]
  meanExpYoung = (float(ll[11].replace(",",".")) + float(ll[13].replace(",",".")) + float(ll[15].replace(",","."))) / 3.0
  allExpVec.append(meanExpYoung)
  geneList.append([gene,meanExpYoung])
  counter += 1
expFile.close()

# Calculating percentile
allExpVec = np.array(allExpVec)
perc = np.percentile(allExpVec, percentile)

# Iterating in gene list to fetch only above percentile
resGeneList = []
for v in geneList:
  if(v[1] >= perc):
    resGeneList.append(v[0])
#resGeneList = sorted(resGeneList, key=lambda x:x[1], reverse=True)

# Fetching gene symbol
an = AnnotationSet("hg19", alias_source="hg19")
mapped_list, unmapped_list = an.get_official_symbol(resGeneList)

# Writing gene list
outputFile = open(outputFileNameM,"w")
for v in mapped_list: outputFile.write(v+"\n")
outputFile.close()
outputFile = open(outputFileNameU,"w")
for v in unmapped_list: outputFile.write(v+"\n")
outputFile.close()


