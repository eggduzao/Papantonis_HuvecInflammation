
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

peakList = ["p10", "p28"]

for peakName in peakList:

  # Parameters
  inputMatrix="/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB2_IMR90/motif_enrichment/matrix/motif_enrichment_HMGB2_"+peakName+".txt"
  matchLoc="/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB2_IMR90/motif_enrichment/results/HMGB2_"+peakName+"/"
  output_location="--output-location /Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB2_IMR90/motif_enrichment/results/HMGB2_"+peakName+"/"

  # Execution
  clusterCommand = "rgt-motifanalysis --enrichment "
  clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
  clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
  os.system(clusterCommand)


