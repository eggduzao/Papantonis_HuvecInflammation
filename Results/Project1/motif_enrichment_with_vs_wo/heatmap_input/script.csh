cat ../../GeneExpression/GeneExpression2/genes_all_tfcheckpoint_high.txt ../../GeneExpression/GeneExpression2/genes_all_tfcheckpoint.txt | sort | uniq > tfs_sel.txt
grep -h -i -f tfs_sel.txt  footprints_corr.txt > footprints_corr_sel.txt

