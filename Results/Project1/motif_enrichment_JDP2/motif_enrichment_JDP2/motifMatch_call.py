
# Import
import os

# Parameters
organism="--organism hg18"
fpr="--fpr 0.0001"
precision="--precision 10000"
pseudocounts="--pseudocounts 0.1"
bigbed="--bigbed"

###################################################################################################
# RANDOM BACKGROUND
###################################################################################################

# Parameters
myL = "MM_RAND2"
rand_proportion="--rand-proportion 0.0001"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/result/"
inputMatrix="/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/exp_mat/MM_all.txt"

# Execution
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 100:00 -M 12000 -S 100 -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+bigbed+" "+inputMatrix
os.system(clusterCommand)
# -P izkf

