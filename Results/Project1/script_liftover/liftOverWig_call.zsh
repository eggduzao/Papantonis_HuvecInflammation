#!/bin/zsh

liftFileName="/hpcwork/izkf/projects/egg/Data/HG19/hg19ToHg18.over.chain.gz"
il="/hpcwork/izkf/projects/egg/TfbsPrediction/Results/Counts/Huvec/"
ol="/hpcwork/izkf/projects/huvec_inflammation/wig_signal/hg18/"

# Variation
inFileList=( "DNase" "H3K4me1" "H3K4me3" )

# Execution
for inFileName in $inFileList
do
    bsub -J $inFileName"_LOW" -o $inFileName"_LOW_out.txt" -e $inFileName"_LOW_err.txt" -W 100:00 -M 50000 -S 100 -R "select[hpcwork]" -P izkf ./liftOverWig_pipeline.zsh $il$inFileName".bw" $liftFileName $ol$inFileName".bw" $ol$inFileName"_unlifted.bed"
done


