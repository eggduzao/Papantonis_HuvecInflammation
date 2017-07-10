#!/bin/zsh

bedToBam -i /hpcwork/izkf/projects/TfbsPrediction/Results_DNase/MPBSAWG/Huvec_Evidence/fdr_4/CTCF.bed -g /hpcwork/izkf/projects/TfbsPrediction/Data/HG19/hg19.chrom.sizes.filtered > ./CTCF_MPBS.bam

samtools index ./CTCF_MPBS.bam


