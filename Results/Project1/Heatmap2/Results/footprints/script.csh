grep -h -i -f ../../../geneexp/genes_all_tfcheckpoint_high_noexact.txt  cluster*.txt > motifs_fold_high.txt
grep -h -i -f ../../../geneexp/genes_all_tfcheckpoint_noexact.txt  cluster*.txt > motifs_fold.txt
grep -v -f motifs_fold.txt  motifs_fold_high.txt > motif_high.txt
