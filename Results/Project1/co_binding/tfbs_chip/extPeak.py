# Import
import os
import sys

# Input
ext = int(sys.argv[1])
inFile = open(sys.argv[2],"r")
outFile = open(sys.argv[3],"w")

# Execution
for line in inFile:
  ll = line.strip().split("\t")
  summit = int(ll[1])+int(ll[9])
  ll[1] = str(summit-ext)
  ll[2] = str(summit+ext)
  outFile.write("\t".join(ll)+"\n")

# Termination
inFile.close()
outFile.close()


