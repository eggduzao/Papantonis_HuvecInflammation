python createHeatmap.py . */
head -n 1 rand_pvalue.txt > head.txt
grep -i -f ../../expression/tf_sel.txt rand_corr.txt > rand_corr_sela.txt
cat head.txt rand_corr_sela.txt > rand_corr_sel.txt
