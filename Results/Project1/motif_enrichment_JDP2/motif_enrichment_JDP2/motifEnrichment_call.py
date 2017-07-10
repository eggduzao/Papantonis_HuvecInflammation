
# Import
import os

# Parameters
organism="--organism hg18"
promoter_length="--promoter-length 1000"
maximum_association_length="--maximum-association-length 50000"
multiple_test_alpha="--multiple-test-alpha 0.05"
processes="--processes 1"
print_thresh="--print-thresh 1.0"
bigbed="--bigbed"

###################################################################################################
# JDP2_FOS_NFKB_vs_random
###################################################################################################

# Parameters
inputMatrix="/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/exp_mat/ME_JDP2_FOS_NFKB_vs_random.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/result/JDP2_FOS_NFKB_vs_random/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/result/JDP2_FOS_NFKB_vs_random/"
myL = "ME_JDP2_FOS_NFKB_vs_random"

# Execution
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 200:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)

###################################################################################################
# JDP2_FOS_NFKB_with_vs_wo
###################################################################################################

# Parameters
inputMatrix="/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/exp_mat/ME_JDP2_FOS_NFKB_with_vs_wo.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/result/JDP2_FOS_NFKB_with_vs_wo/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/result/JDP2_FOS_NFKB_with_vs_wo/"
myL = "ME_JDP2_FOS_NFKB_with_vs_wo"

# Execution
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 200:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)

###################################################################################################
# JDP2_NFKB_vs_random
###################################################################################################

# Parameters
inputMatrix="/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/exp_mat/ME_JDP2_NFKB_vs_random.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/result/JDP2_NFKB_vs_random/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/result/JDP2_NFKB_vs_random/"
myL = "ME_JDP2_NFKB_vs_random"

# Execution
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 200:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)

###################################################################################################
# JDP2_NFKB_with_vs_wo
###################################################################################################

# Parameters
inputMatrix="/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/exp_mat/ME_JDP2_NFKB_with_vs_wo.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/result/JDP2_NFKB_with_vs_wo/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/result/JDP2_NFKB_with_vs_wo/"
myL = "ME_JDP2_NFKB_with_vs_wo"

# Execution
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 200:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)

###################################################################################################
# JDP2_vs_random
###################################################################################################

# Parameters
inputMatrix="/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/exp_mat/ME_JDP2_vs_random.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/result/JDP2_vs_random/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_JDP2/result/JDP2_vs_random/"
myL = "ME_JDP2_vs_random"

# Execution
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 200:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)


