#!/bin/zsh

liftFileName="/hpcwork/izkf/projects/egg/Data/HG19/hg19ToHg18.over.chain.gz"
csFile19="/hpcwork/izkf/projects/egg/Data/HG19/hg19.chrom.sizes"
csFile18="/hpcwork/izkf/projects/egg/Data/HG18/hg18.chrom.sizes"
il="/hpcwork/izkf/projects/huvec_inflammation/bed_footprints/hg19/"
ol="/hpcwork/izkf/projects/huvec_inflammation/bed_footprints/hg18/"

# Variation
inFileList=( "HD_H3K4me1_ModelHuvec_5" "HD_H3K4me3_ModelHuvec_5" "HD_H3K4me1_ModelHuvec_10" "HD_H3K4me3_ModelHuvec_10" )

# Execution
for inFileName in $inFileList
do
    bedToBigBed $il$inFileName".bed" $csFile19 $il$inFileName".bb"
    liftOver $il$inFileName".bed" $liftFileName $ol$inFileName".bed" $ol$inFileName"_unlifted.bed"
    sort -k1,1 -k2,2n $ol$inFileName".bed" > $ol$inFileName"_sort.bed"
    bedToBigBed $ol$inFileName"_sort.bed" $csFile18 $ol$inFileName".bb"
    rm $ol$inFileName"_sort.bed"
done


