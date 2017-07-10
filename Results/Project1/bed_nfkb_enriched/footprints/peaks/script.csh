fastaFromBed -bed wo.bed -fi ~/projects/genomes/hg18.fa -fo wo.fa
fastaFromBed -bed with.bed -fi ~/projects/genomes/hg18.fa -fo with.fa
head -n 1000  with.fa  > with_1000.fa
head -n 1000  wo.fa  > wo_1000.fa
#meme-chip -oc wo -db ~/app/meme_4.11.0/motif_databases/JASPAR/JASPAR_CORE_2016_vertebrates.meme wo_1000.fa &
meme-chip -oc with -meme-nmotifs 1 -db ~/app/meme_4.11.0/motif_databases/JASPAR/JASPAR_CORE_2016_vertebrates.meme with_1000.fa &

fimo --oc fimo_with with/meme_out/meme.xml with.fa 
fimo --thresh 0.001 --oc fimo_wo with/meme_out/meme.xml wo.fa


#cat with_1000.fa wo_1000.fa > both.fa
#meme-chip -oc both -db ~/app/meme_4.11.0/motif_databases/JASPAR/JASPAR_CORE_2016_vertebrates.meme both.fa -meme-maxw 15 &

