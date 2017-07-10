# This script standardize scores from bed files from [0,1000]
import os
import sys
inFileName = sys.argv[1]
outFileName = sys.argv[2]
inFile = open(inFileName,"r")
minS = 99999999; maxS = -99999999
for line in inFile:
  ll = line.strip().split("\t")
  score = float(ll[4])
  if(score<minS): minS = score
  if(score>maxS): maxS = score
inFile.close()
inFile = open(inFileName,"r")
outFile = open(outFileName,"w")
for line in inFile:
  ll = line.strip().split("\t")
  outFile.write("\t".join(ll[:4]+[str(int(1000*(float(ll[4])-minS)/(maxS-minS)))])+"\n")
inFile.close()
outFile.close()
