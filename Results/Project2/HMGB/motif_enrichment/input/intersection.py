
# Import
import os
import sys

# Input
inputFileName = "/home/egg/Projects/HuvecInflammation/Results/HMGB/motif_enrichment/footprints/Huvec_footprints.bed"
peakFileName = "/home/egg/Projects/HuvecInflammation/Results/HMGB/motif_enrichment/peaks/HMGB2_allpeaks_hg19.bed"
outPeak = "/home/egg/Projects/HuvecInflammation/Results/HMGB/motif_enrichment/input/HMGB2_footprints_peaks_hg19.bed"
outNotPeak = "/home/egg/Projects/HuvecInflammation/Results/HMGB/motif_enrichment/input/HMGB2_footprints_no_peaks_hg19.bed"

# Sort all
it1 = "it1.bed"
pt1 = "pt1.bed"
os.system("sort -k1,1 -k2,2n "+inputFileName+" > "+it1)
os.system("sort -k1,1 -k2,2n "+peakFileName+" > "+pt1)

# Input in Peak
os.system("intersectBed -a "+it1+" -b "+pt1+" -wa -u > "+outPeak)
os.system("intersectBed -a "+it1+" -b "+pt1+" -wa -v > "+outNotPeak)

toRemove = [it1,pt1]
for e in toRemove: os.system("rm "+e)


