
import os
import sys
from fisher import pvalue

def filelen(fname):
  i = 0
  with open(fname) as f:
    for i, l in enumerate(f):
      pass
  return i + 1

def withwithout(f1, f2, of, l1, l2):
  
  f1sort = "./f1s.bed"
  f2sort = "./f2s.bed"
  os.system("sort -k1,1 -k2,2n "+f1+" > "+f1sort)
  os.system("sort -k1,1 -k2,2n "+f2+" > "+f2sort)

  f1wf2 = "./f1wf2.bed"; f2wf1 = "./f2wf1.bed"; f1wof2 = "./f1wof2.bed"; f2wof1 = "./f2wof1.bed"
  toRemove = [f1sort,f2sort,f1wf2,f2wf1,f1wof2,f2wof1]
  
  os.system("intersectBed -a "+f1sort+" -b "+f2sort+" -wa -u > "+f1wf2)
  os.system("intersectBed -a "+f1sort+" -b "+f2sort+" -wa -v > "+f1wof2)
  os.system("intersectBed -a "+f2sort+" -b "+f1sort+" -wa -u > "+f2wf1)
  os.system("intersectBed -a "+f2sort+" -b "+f1sort+" -wa -v > "+f2wof1)

  f1wf2n = filelen(f1wf2)
  f2wf1n = filelen(f2wf1)
  f1wof2n = filelen(f1wof2)
  f2wof1n = filelen(f2wof1)

  p = pvalue(f1wf2n,f1wof2n,f2wf1n,f2wof1n)
  p_value = p.right_tail

  of.write(l1+" WITH "+l2+":\t"+str(f1wf2n)+"\n")
  of.write(l1+" WITHOUT "+l2+":\t"+str(f1wof2n)+"\n")
  of.write(l2+" WITH "+l1+":\t"+str(f2wf1n)+"\n")
  of.write(l2+" WITHOUT "+l1+":\t"+str(f2wof1n)+"\n")
  of.write("Fisher p-value = "+str(p_value)+"\n")
  of.write("---------------------------------------------\n\n")

  for e in toRemove: os.system("rm "+e)
  return "0"

# Input
ctcfPeaks = "/hpcwork/izkf/projects/HuvecInflammation/Data/ctcf_chipseq/BroadInstitute/HUVEC_CTCF_Peaks.bed"
ctcfMpbsHmgb1 = "../../motif_enrichment/results/HMGB1/Match/HMGB1_footprints_peaks_mpbs_ctcf.bed"
ctcfMpbsHmgb2 = "../../motif_enrichment/results/HMGB2/Match/HMGB2_footprints_peaks_mpbs_ctcf.bed"
hmgb1 = "../../motif_enrichment/peaks/HMGB1_allpeaks_hg19.bed"
hmgb2 = "../../motif_enrichment/peaks/HMGB2_allpeaks_hg19.bed"
outFile = open("overlap.txt","w")

####

# HMGB1 / CTCF PEAKS
withwithout(hmgb1, ctcfPeaks, outFile, "HMGB1 Peaks", "CTCF ChIP-seq Peaks")

# HMGB2 / CTCF PEAKS
withwithout(hmgb2, ctcfPeaks, outFile, "HMGB2 Peaks (narrow)", "CTCF ChIP-seq Peaks")

####

# HMGB1 / CTCF MPBS
withwithout(hmgb1, ctcfMpbsHmgb1, outFile, "HMGB1 Peaks", "CTCF MPBSs")

# HMGB2 / CTCF MPBS
withwithout(hmgb2, ctcfMpbsHmgb2, outFile, "HMGB2 Peaks (narrow)", "CTCF MPBSs")


outFile.close()

