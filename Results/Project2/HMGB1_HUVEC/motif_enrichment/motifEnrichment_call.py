
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

# Parameters
inputMatrix="/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB1_HUVEC/motif_enrichment/matrix/motif_enrichment_HMGB1.txt"
matchLoc="/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB1_HUVEC/motif_enrichment/results/"
output_location="--output-location /Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB1_HUVEC/motif_enrichment/results/"

# Execution
clusterCommand = "rgt-motifanalysis --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)


