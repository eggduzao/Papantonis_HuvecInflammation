
# Import
import os
import sys

# Input
footprintFileName = "/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB1_HUVEC/motif_enrichment/footprints/Huvec_footprints.bed"
peakLoc = "/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB1_HUVEC/motif_enrichment/peaks/"
peakList = ["HMGB1_HUVEC_peaks_final"]
outLoc = "./"

def fileLen(fname):
  i = 0
  with open(fname) as f:
    for i, l in enumerate(f): pass
  return i + 1

# Interating on peaks
for peakName in peakList:

  # Input
  peakFileName = peakLoc+peakName+".bed"
  outPeak = outLoc+peakName+"_peaks.bed"
  outNotPeak = outLoc+peakName+"_no_peaks.bed"

  # Sort all
  it1 = "it1.bed"
  pt1 = "pt1.bed"
  os.system("sort -k1,1 -k2,2n "+footprintFileName+" > "+it1)
  os.system("sort -k1,1 -k2,2n "+peakFileName+" > "+pt1)

  # Input in Peak
  onpt1 = "onpt1.bed"
  os.system("intersectBed -a "+it1+" -b "+pt1+" -wa -u > "+outPeak)
  os.system("intersectBed -a "+it1+" -b "+pt1+" -wa -v > "+onpt1)

  # Veryfying the number of lines
  numberLines = int(fileLen(outPeak) * 10)

  # Selecting random lines
  os.system("gshuf -n "+str(numberLines)+" "+onpt1+" > "+outNotPeak)

  toRemove = [it1,pt1,onpt1]
  for e in toRemove: os.system("rm "+e)


