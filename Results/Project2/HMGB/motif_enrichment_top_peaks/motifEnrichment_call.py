
# Import
import os

# Parameters
organism="--organism hg19"
promoter_length="--promoter-length 1000"
maximum_association_length="--maximum-association-length 50000"
multiple_test_alpha="--multiple-test-alpha 0.05"
processes="--processes 1"
print_thresh="--print-thresh 1.0"

###################################################################################################
# PEAKS
###################################################################################################

peakList = ["HMGB1_hg19_top500_fp_withpeak", "HMGB2_hg19_top500_Broad_fp_withpeak", "HMGB2_hg19_top500_Narrow_fp_withpeak"]

for peakName in peakList:

  # Parameters
  inputMatrix="/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment_top_peaks/matrix/ME_"+peakName+".txt"
  matchLoc="/home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment_top_peaks/results/"+peakName+"/"
  output_location="--output-location /home/egg/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment_top_peaks/results/"+peakName+"/"

  # Execution
  clusterCommand = "rgt-motifanalysis --enrichment "
  clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
  clusterCommand += processes+" "+output_location+" "+print_thresh+" "+inputMatrix+" "+matchLoc
  os.system(clusterCommand)


