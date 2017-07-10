
# Import
import os
import sys

#/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment_top_peaks/top_peaks/HMGB1_hg19_top500.bed
#/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment_top_peaks/top_peaks/HMGB2_hg19_top500_Broad.bed
#/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment_top_peaks/top_peaks/HMGB2_hg19_top500_Narrow.bed

# Input
inputFileName = "/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment/footprints/Huvec_footprints.bed"
peakFileName = "/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment_top_peaks/top_peaks/HMGB2_hg19_top500_Narrow.bed"
outPeak = "/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment_top_peaks/input/HMGB2_hg19_top500_Narrow_fp_withpeak.bed"
outNotPeak = "/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment_top_peaks/input/HMGB2_hg19_top500_Narrow_fp_wopeak.bed"

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


