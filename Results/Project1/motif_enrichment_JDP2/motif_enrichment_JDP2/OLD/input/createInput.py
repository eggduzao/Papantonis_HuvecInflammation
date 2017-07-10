
# Import
import os
import sys

# Input
jdpFileName = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/raw/JDP2.rep1.fwd.HG18.peak30.fdr0.001.overpal.with.other.TFs.txt"
fpLoc = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/bed_nfkb_enriched/footprints/"
fpList = ["with","with_clust1","with_clust2","with_clust3","with_clust4","with_clust5",
          "wo","wo_clust1","wo_clust2","wo_clust3","wo_clust4","wo_clust5"]
outLoc = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/input/"
originalFpFileName = "/hpcwork/izkf/projects/HuvecInflammation/Results/Footprints/hg18/HD_H3K4me1_ModelHuvec_10.bed"

# 1. with the full peak list

# Convert JDP file from Akis to bed standard format
outFileNameTemp1 = outLoc+"JDP_all_T1.bed"
outFileNameTemp2 = outLoc+"JDP_all_T2.bed"
outFileName = outLoc+"JDP_peaks.bed"
os.system("sed 1d "+jdpFileName+" > "+outFileNameTemp1)
os.system("cut -f 1,2,3 "+outFileNameTemp1+" > "+outFileNameTemp2)
os.system("sort -k1,1 -k2,2n "+outFileNameTemp2+" > "+outFileName)
os.system("rm "+outFileNameTemp1+" "+outFileNameTemp2)

# Intersect JDP peaks with hg18 DNase-seq footprints
jdpFootprintsFileNameTemp1 = outLoc+"JDP_FP_T1.bed"
jdpFootprintsFileNameTemp2 = outLoc+"JDP_FP_T2.bed"
jdpFootprintsFileName = outLoc+"JDP_FP.bed"
os.system("sort -k1,1 -k2,2n "+originalFpFileName+" > "+jdpFootprintsFileNameTemp1)
os.system("intersectBed -a "+jdpFootprintsFileNameTemp1+" -b "+outFileName+" -wa -u > "+jdpFootprintsFileNameTemp2)
os.system("mergeBed -i "+jdpFootprintsFileNameTemp2+" > "+jdpFootprintsFileName)
os.system("rm "+jdpFootprintsFileNameTemp1+" "+jdpFootprintsFileNameTemp2)

# 2. only with peaks coinciding NfkB "with" or "without" motif peaks

# Intersect JDP peaks with footprints categorized as with/without NFKB motif
for fpName in fpList:
  fpFileName = fpLoc+fpName+".bed"
  intersectFileNameTemp1 = outLoc+"JDP+NFKB_"+fpName+"_T1.bed"
  intersectFileNameTemp2 = outLoc+"JDP+NFKB_"+fpName+"_T2.bed"
  intersectFileName = outLoc+"JDP+NFKB_"+fpName+"_FP.bed"
  os.system("sort -k1,1 -k2,2n "+fpFileName+" > "+intersectFileNameTemp2)
  os.system("intersectBed -a "+intersectFileNameTemp2+" -b "+outFileName+" -wa -u > "+intersectFileNameTemp1)
  os.system("mergeBed -i "+intersectFileNameTemp1+" > "+intersectFileName)
  os.system("rm "+intersectFileNameTemp1+" "+intersectFileNameTemp2)

# 3. with the peaks coinciding with both NFkB and FOS

# Fetch FOS+JDP peaks
tempFileName1 = outLoc+"JDP+FOS_T1.bed"
tempFileName2 = outLoc+"JDP+FOS_T2.bed"
inFile = open(jdpFileName,"r")
outFile = open(tempFileName1,"w")
inFile.readline()
for line in inFile:
  ll = line.strip().split("\t")
  if(ll[10] == "TRUE"): outFile.write("\t".join(ll[:3])+"\n")
inFile.close()
outFile.close()
os.system("sort -k1,1 -k2,2n "+tempFileName1+" > "+tempFileName2)

# Intersecting with NFKB+footprints
for fpName in ["with"]:
  fpFileName = fpLoc+fpName+".bed"
  intersectFileNameTemp1 = outLoc+"JDP+FOS+NFKB_"+fpName+"_T1.bed"
  intersectFileNameTemp2 = outLoc+"JDP+FOS+NFKB_"+fpName+"_T2.bed"
  intersectFileName = outLoc+"JDP+FOS+NFKB_"+fpName+"_FP.bed"
  os.system("sort -k1,1 -k2,2n "+fpFileName+" > "+intersectFileNameTemp2)
  os.system("intersectBed -a "+intersectFileNameTemp2+" -b "+tempFileName2+" -wa -u > "+intersectFileNameTemp1)
  os.system("mergeBed -i "+intersectFileNameTemp1+" > "+intersectFileName)
  os.system("rm "+intersectFileNameTemp1+" "+intersectFileNameTemp2)

os.system("rm "+tempFileName1+" "+tempFileName2)


