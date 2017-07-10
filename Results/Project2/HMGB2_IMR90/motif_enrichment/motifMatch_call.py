
# Import
import os

# Parameters
organism="--organism hg19"
fpr="--fpr 0.0001"
precision="--precision 10000"
pseudocounts="--pseudocounts 0.1"
#bigbed="--bigbed"

###################################################################################################
# FOOTPRINTS
###################################################################################################

# Parameters
rand_proportion="--rand-proportion 0.0001"
output_location="--output-location /Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB2_IMR90/motif_enrichment/results/"
inputMatrix="/Users/egg/Projects/Papantonis_HuvecInflammation/Results/HMGB2_IMR90/motif_enrichment/matrix/motif_match.txt"

# Execution
clusterCommand = "rgt-motifanalysis --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+inputMatrix
os.system(clusterCommand)


