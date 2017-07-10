
# Import
import os
import sys

# Input
jdpFileName = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/raw/JDP2.rep1.fwd.HG18.peak30.fdr0.001.overpal.with.other.TFs.txt"
outLoc = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/input2/"
originalFpFileName = "/hpcwork/izkf/projects/HuvecInflammation/Results/Footprints/hg18/HD_H3K4me1_ModelHuvec_10.bed"
toRemove = []

# Sorting and merging footprints file
sortedFpFileName = outLoc+"sorted_FP.bed"; toRemove.append(sortedFpFileName)
mergedFpFileName = outLoc+"merged_FP.bed"; toRemove.append(mergedFpFileName)
os.system("cut -f 1,2,3 "+originalFpFileName+" | sort -k1,1 -k2,2n > "+sortedFpFileName)
os.system("mergeBed -i "+sortedFpFileName+" > "+mergedFpFileName)

#####################################################################
# 1. with the full peak list
#####################################################################

# Convert JDP file from Akis to bed standard format
outFileNameTemp1 = outLoc+"JDP_all_T1.bed"; toRemove.append(outFileNameTemp1)
jdpFullPeaksFileName = outLoc+"JDP_peaks.bed"
os.system("sed 1d "+jdpFileName+" > "+outFileNameTemp1)
os.system("cut -f 1,2,3 "+outFileNameTemp1+" | sort -k1,1 -k2,2n > "+jdpFullPeaksFileName)

# Intersect with footprints
jdpFootprintsFileName = outLoc+"JDP_FP.bed"
os.system("intersectBed -a "+mergedFpFileName+" -b "+jdpFullPeaksFileName+" -wa -u > "+jdpFootprintsFileName)

#####################################################################
# 2. only with peaks coinciding NfkB "with" or "without" motif peaks
#####################################################################

# Fetch JDP+NFKBwith and JDP+NFKBwo peaks
tempFileName1 = outLoc+"JDP+NFKB_T1.bed"; toRemove.append(tempFileName1)
tempFileName2 = outLoc+"JDP+NFKB_T2.bed"; toRemove.append(tempFileName2)
jdpNfkbWithFileName = outLoc+"JDP+NFKBwith_peaks.bed"
jdpNfkbWoFileName = outLoc+"JDP+NFKBwo_peaks.bed"
inFile = open(jdpFileName,"r")
outFileWith = open(tempFileName1,"w")
outFileWo = open(tempFileName2,"w")
inFile.readline()
for line in inFile:
  ll = line.strip().split("\t")
  if(ll[16] == "TRUE"): outFileWith.write("\t".join(ll[:3])+"\n")
  else: outFileWo.write("\t".join(ll[:3])+"\n")
inFile.close()
outFileWith.close()
outFileWo.close()
os.system("sort -k1,1 -k2,2n "+tempFileName1+" > "+jdpNfkbWithFileName)
os.system("sort -k1,1 -k2,2n "+tempFileName2+" > "+jdpNfkbWoFileName)

# Intersect with footprints
jdpNfkbwithFootprintsFileName = outLoc+"JDP+NFKBwith_FP.bed"
jdpNfkbwoFootprintsFileName = outLoc+"JDP+NFKBwo_FP.bed"
os.system("intersectBed -a "+mergedFpFileName+" -b "+jdpNfkbWithFileName+" -wa -u > "+jdpNfkbwithFootprintsFileName)
os.system("intersectBed -a "+mergedFpFileName+" -b "+jdpNfkbWoFileName+" -wa -u > "+jdpNfkbwoFootprintsFileName)

#####################################################################
# 3. with the peaks coinciding with both NFkB and FOS
#####################################################################

# Fetch JDP+FOS+NFKBwith and JDP+FOS+NFKBwo peaks
tempFileName1 = outLoc+"JDP+NFKB+FOS_T1.bed"; toRemove.append(tempFileName1)
tempFileName2 = outLoc+"JDP+NFKB+FOS_T2.bed"; toRemove.append(tempFileName2)
jdpFosNfkbWithFileName = outLoc+"JDP+FOS+NFKBwith_peaks.bed"
jdpFosNfkbWoFileName = outLoc+"JDP+FOS+NFKBwo_peaks.bed"
inFile = open(jdpFileName,"r")
outFileWith = open(tempFileName1,"w")
outFileWo = open(tempFileName2,"w")
inFile.readline()
for line in inFile:
  ll = line.strip().split("\t")
  if(ll[10] == "TRUE"):
    if(ll[16] == "TRUE"): outFileWith.write("\t".join(ll[:3])+"\n")
    else: outFileWo.write("\t".join(ll[:3])+"\n")
inFile.close()
outFileWith.close()
outFileWo.close()
os.system("sort -k1,1 -k2,2n "+tempFileName1+" > "+jdpFosNfkbWithFileName)
os.system("sort -k1,1 -k2,2n "+tempFileName2+" > "+jdpFosNfkbWoFileName)

# Intersect with footprints
jdpFosNfkbwithFootprintsFileName = outLoc+"JDP+FOS+NFKBwith_FP.bed"
jdpFosNfkbwoFootprintsFileName = outLoc+"JDP+FOS+NFKBwo_FP.bed"
os.system("intersectBed -a "+mergedFpFileName+" -b "+jdpFosNfkbWithFileName+" -wa -u > "+jdpFosNfkbwithFootprintsFileName)
os.system("intersectBed -a "+mergedFpFileName+" -b "+jdpFosNfkbWoFileName+" -wa -u > "+jdpFosNfkbwoFootprintsFileName)

# Termination
for e in toRemove: os.system("rm "+e)


