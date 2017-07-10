#!/bin/zsh

fastaFromBed -fi /hpcwork/izkf/projects/TfbsPrediction/Data/HG19/hg19.fa -bed ./HMGB1_hg19_top500.bed -fo ./HMGB1_hg19_top500.fa

fastaFromBed -fi /hpcwork/izkf/projects/TfbsPrediction/Data/HG19/hg19.fa -bed ./HMGB2_hg19_top500_Broad.bed -fo ./HMGB2_hg19_top500_Broad.fa

fastaFromBed -fi /hpcwork/izkf/projects/TfbsPrediction/Data/HG19/hg19.fa -bed ./HMGB2_hg19_top500_Narrow.bed -fo ./HMGB2_hg19_top500_Narrow.fa


