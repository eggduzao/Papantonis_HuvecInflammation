cut -f 2 ../fimo_with/fimo.txt  | sort | uniq | wc
cut -f 2 ../fimo_with/fimo.txt  |  wc
wc ../with.bed

cut -f 2 ../fimo_wo/fimo.txt  | sort | uniq | wc
cut -f 9 ../fimo_wo/fimo.txt  > binding.txt
cut -f 2 ../fimo_wo/fimo.txt  |  wc
wc ../wo.bed

cut -f 2 ../fimo_wo/fimo.txt  | sort | uniq > wo_hit.txt
cut -d ":" -f 1 wo_hit.txt > chr.txt
cut -d ":" -f 2 wo_hit.txt > pos.txt
cut -d "-" -f 1 pos.txt  > pos1.txt
cut -d "-" -f 2 pos.txt  > pos2.txt
paste chr.txt pos1.txt pos2.txt > wo_hit.bed
subtractBed -a ../wo.bed -b wo_hit.bed > wo_no_nfkb.bed

