
# Import
import os

# Parameters
organism="--organism hg19"
promoter_length="--promoter-length 1000"
maximum_association_length="--maximum-association-length 50000"
multiple_test_alpha="--multiple-test-alpha 0.05"
processes="--processes 1"
print_thresh="--print-thresh 1.0"
bigbed="--bigbed"

###################################################################################################
# PEAKS
###################################################################################################

peakList = ["HMGB1", "HMGB2"]

for peakName in peakList:

  # Parameters
  inputMatrix="/home/egg/Projects/HuvecInflammation/Results/HMGB/motif_enrichment/matrix/ME_"+peakName+"_footprints_peaks.txt"
  matchLoc="/home/egg/Projects/HuvecInflammation/Results/HMGB/motif_enrichment/results/"+peakName+"/"
  output_location="--output-location /home/egg/Projects/HuvecInflammation/Results/HMGB/motif_enrichment/results/"+peakName+"/"

  # Execution
  clusterCommand = "rgt-motifanalysis --enrichment "
  clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
  clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
  os.system(clusterCommand)


