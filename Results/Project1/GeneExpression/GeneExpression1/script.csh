awk '$6>=1 {print $1,$6}' 0-30.analysis.merged.RNA.analyzed.basemean..with.pseudolog2foldchange.txt  | grep -P -v "NA|Inf" | sort  -k 2 -r -n > up_2_30.txt
awk '$6>=1 {print $1,$6}' 0-60.analysis.merged.RNA.analyzed.basemean..with.pseudolog2foldchange.txt  | grep -P -v "NA|Inf" | sort  -k 2 -r -n > up_2_60.txt
cut -d " " -f 1 up_2_30.txt > genes_2_30.txt
cut -d " " -f 1 up_2_60.txt > genes_2_60.txt
grep -w -f genes_2_30.txt genes_2_60.txt | wc
wc genes_2_30.txt
wc genes_2_60.txt
cat genes_* | sort | uniq > genes_all.txt

grep -i -f genes_all.txt --color=auto  /home/ivan/projects/dendriticcells/data/motifs/tfmapping.txt
