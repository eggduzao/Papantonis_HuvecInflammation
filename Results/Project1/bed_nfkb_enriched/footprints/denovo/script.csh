slopBed -b 10 -i ../with.bed  -g hg18.genome > with.bed
slopBed -b 10 -i ../wo.bed  -g hg18.genome > wo.bed
fastaFromBed -bed wo.bed -fi ~/projects/genomes/hg18.fa -fo wo.fa
fastaFromBed -bed with.bed -fi ~/projects/genomes/hg18.fa -fo with.fa
head -n 5000  with.fa  > with_1000.fa
head -n 5000  wo.fa  > wo_1000.fa
meme-chip -oc wo -db ~/app/meme_4.11.0/motif_databases/JASPAR/JASPAR_CORE_2016_vertebrates.meme wo_1000.fa &
meme-chip -oc with -db ~/app/meme_4.11.0/motif_databases/JASPAR/JASPAR_CORE_2016_vertebrates.meme with_1000.fa &

