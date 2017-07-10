
import os
import sys

halfExt = 20
inFileName = "./IMR90_raw.bed"
outFileTemp = "./temp.bed"
outFileName = "./IMR90_footprints.bed"

inFile = open(inFileName,"r")
outFile = open(outFileTemp,"w")
for line in inFile:
  ll = line.strip().split("\t")
  mid = (int(ll[1]) + int(ll[2])) / 2
  p1 = str(mid-halfExt)
  p2 = str(mid+halfExt)
  outFile.write("\t".join([ll[0],p1,p2])+"\n")

inFile.close()
outFile.close()

os.system("sort -k1,1 -k2,2n "+outFileTemp+" > "+outFileName)
os.system("rm "+outFileTemp)


