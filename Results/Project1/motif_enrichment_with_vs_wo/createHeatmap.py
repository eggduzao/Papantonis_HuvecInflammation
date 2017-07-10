
# Import
import os
import sys

# Input
il = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_with_vs_wo/results/"
ol = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_with_vs_wo/heatmap_input/"

# Pvalue Loop
pListIndex = [1,2]
pList = ["pvalue","corr"]
for i in range(0,len(pList)):

  pIndex = pListIndex[i]
  pName = pList[i]

  # Type Loop
  typeList = ["footprints", "original"]
  for t in typeList:

    # Fetching pvalues
    inList = ["_with", "_clust1_with", "_clust2_with", "_clust3_with", "_clust4_with", "_clust5_with", 
              "_wo", "_clust1_wo", "_clust2_wo", "_clust3_wo", "_clust4_wo", "_clust5_wo"]
    outList = []
    for inName in inList:
      inFileName = il+t+inName+".txt"
      inFile = open(inFileName,"r")
      inFile.readline()
      outDict = dict()
      for line in inFile:
        ll = line.strip().split("\t")
        outDict[ll[0]] = ll[pIndex]
      inFile.close()
      outList.append(outDict)

    # Writing results
    header = ["TF", 
             "MERGED_WITH", "CLUSTER1_WITH", "CLUSTER2_WITH", "CLUSTER3_WITH", "CLUSTER4_WITH", "CLUSTER5_WITH", 
             "MERGED_WO", "CLUSTER1_WO", "CLUSTER2_WO", "CLUSTER3_WO", "CLUSTER4_WO", "CLUSTER5_WO" ]
    outFileName = ol+t+"_"+pName+".txt"
    outFile = open(outFileName,"w")
    outFile.write("\t".join(header)+"\n")
    for k in sorted(outList[0].keys()):
      printVec = [k]
      for j in range(0,len(outList)): printVec.append(outList[j][k])
      outFile.write("\t".join(printVec)+"\n")
    outFile.close()


