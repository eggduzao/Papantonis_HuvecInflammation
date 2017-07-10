
# Import
import os
import sys

# Input
inLoc = "/hpcwork/izkf/projects/HuvecInflammation/Results/MotifEnrichment/"
outLoc = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_with_vs_wo/input/"

# Function to get values into dictionary
def getValues(inFileName, inDict):
  inFile = open(inFileName,"r")
  inFile.readline()
  for line in inFile:
    ll = line.strip().split("\t")
    inDict[ll[0]] = [ll[3],ll[4]]
  inFile.close()
  return 0

# Type Loop
typeList = ["footprints", "original"]
for t in typeList:

  # Clust Loop
  inList = ["", "_clust1", "_clust2", "_clust3", "_clust4", "_clust5"]
  for inName in inList:

    # Parameters
    inFileNameWith = inLoc+t+"/with"+inName+"/rand_1_statistics.txt"
    inFileNameWo = inLoc+t+"/wo"+inName+"/rand_1_statistics.txt"
    outFileName = outLoc+t+inName+".txt"

    # Execution
    inDictWith = dict()
    inDictWo = dict()
    getValues(inFileNameWith, inDictWith)
    getValues(inFileNameWo, inDictWo)

    # Writing results
    outFile = open(outFileName, "w")
    for k in sorted(inDictWith.keys()):
      outFile.write("\t".join([k]+inDictWith[k]+inDictWo[k])+"\n")
    outFile.close()


