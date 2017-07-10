
# Import
import os

###################################################################################################
# HS background
###################################################################################################

# Parameters
organism="--organism hg18"
fpr="--fpr 0.0001"
precision="--precision 10000"
pseudocounts="--pseudocounts 0.1"
rand_proportion="--rand-proportion 0.001"
bigbed="--bigbed"

# Execution PeakSeq
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/co_binding/tfbs_motifmatch/result/peakseq/"
inputMatrix="/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/co_binding/tfbs_motifmatch/exp_mat/peakseq.txt"
myL = "MM_HU_PS"
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 48:00 -M 24000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+bigbed+" "+inputMatrix
os.system(clusterCommand)

# Execution Spp
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/co_binding/tfbs_motifmatch/result/spp/"
inputMatrix="/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/co_binding/tfbs_motifmatch/exp_mat/spp.txt"
myL = "MM_HU_SP"
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 48:00 -M 24000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+bigbed+" "+inputMatrix
os.system(clusterCommand)


