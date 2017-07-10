#!/bin/zsh

sort -k1,1 -k2,2n HMGB1_hg19_top500.bed > sort.bed
mergeBed -i sort.bed > HMGB1_hg19_top500.bed
rm sort.bed

sort -k1,1 -k2,2n HMGB2_hg19_top500_Broad.bed > sort.bed
mergeBed -i sort.bed > HMGB2_hg19_top500_Broad.bed
rm sort.bed

sort -k1,1 -k2,2n HMGB2_hg19_top500_Narrow.bed > sort.bed
mergeBed -i sort.bed > HMGB2_hg19_top500_Narrow.bed
rm sort.bed


