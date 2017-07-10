
# Import
import os
import sys

#################################################
# Input
#################################################

# Input Location
ilFoot = "/hpcwork/izkf/projects/huvec_inflammation/bed_nfkb_enriched/footprints/"
ilCoord = "/hpcwork/izkf/projects/huvec_inflammation/bed_nfkb_enriched/original/"
ilList = [ilFoot, ilCoord]

# Output Location
ol = "/hpcwork/izkf/projects/huvec_inflammation/motif_enrichment/Results_10/"

# Coordinates
coordList = [ "with_clust1", "with_clust2", "with_clust3", "with_clust4", "with_clust5", 
              "wo_clust1", "wo_clust2", "wo_clust3", "wo_clust4", "wo_clust5",
              "wo", "with", "all"]

#################################################
# Cluster Call
#################################################

# Input Location Loop
for inputLoc in ilList:

  inLocName = inputLoc.strip().split("/")[-2]

  # Coordinate Loop
  for coordName in coordList:

    ###########################################
    # Parameters
    ###########################################

    coord_file="-coord_file="+inputLoc+coordName+".bed"
    #motif_list="-motif_list="
    #gene_list="-gene_list="
    #assoc_coord_file="-assoc_coord_file="
    #mpbs_file="-mpbs_file="
    #mpbs_final_file="-mpbs_final_file="

    genome_list="-genome_list=/work/eg474423/reg-gen/data/hg18/genome.fa"
    association_file="-association_file=/work/eg474423/reg-gen/data/hg18/association_file.bed"
    chrom_sizes_file="-chrom_sizes_file=/work/eg474423/reg-gen/data/hg18/chrom.sizes"
    pwm_dataset="-pwm_dataset=/hpcwork/izkf/projects/huvec_inflammation/motif_enrichment/Input/PWM/"
    logo_location="-logo_location=../../../logo/"
    #random_coordinates="-random_coordinates="

    #organism="-organism="
    motif_match_fpr="-motif_match_fpr=0.0001"
    motif_match_precision="-motif_match_precision=10000"
    motif_match_pseudocounts="-motif_match_pseudocounts=0.0"
    multiple_test_alpha="-multiple_test_alpha=0.05"
    #promoter_length="-promoter_length=1000"
    #maximum_association_length="-maximum_association_length=50000"
    #cobinding="-cobinding="
    #cobinding_enriched_only="-cobinding_enriched_only="
    #enriched_pvalue="-enriched_pvalue="
    rand_proportion_size="-rand_proportion_size=10"
    all_coord_evidence="-all_coord_evidence=Y"

    outLoc = ol+inLocName+"/"+coordName+"/"
    os.system("mkdir -p "+outLoc)
    output_location="-output_location="+outLoc
    print_association="-print_association=Y"
    print_mpbs="-print_mpbs=Y"
    print_results_text="-print_results_text=Y"
    print_results_html="-print_results_html=Y"
    print_enriched_genes="-print_enriched_genes=N"
    print_rand_coordinates="-print_rand_coordinates=Y"
    print_graph_mmscore="-print_graph_mmscore=N"
    print_graph_heatmap="-print_graph_heatmap=N"

    ###########################################
    # Execution
    ###########################################

    myL = inLocName+"_"+coordName
    clusterCommand = "bsub "
    clusterCommand += "-J "+myL+"_HIE -o "+myL+"_HIE_out.txt -e "+myL+"_HIE_err.txt "
    clusterCommand += "-W 300:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifStatistics_pipeline.zsh "
    clusterCommand += coord_file+" "+genome_list+" "+association_file+" "+chrom_sizes_file+" "+pwm_dataset+" "+logo_location+" "
    clusterCommand += motif_match_fpr+" "+motif_match_precision+" "+motif_match_pseudocounts+" "+multiple_test_alpha+" "
    clusterCommand += rand_proportion_size+" "+all_coord_evidence+" "
    clusterCommand += output_location+" "+print_association+" "+print_mpbs+" "+print_results_text+" "+print_results_html+" "
    clusterCommand += print_enriched_genes+" "+print_rand_coordinates+" "+print_graph_mmscore+" "+print_graph_heatmap
    os.system(clusterCommand)


