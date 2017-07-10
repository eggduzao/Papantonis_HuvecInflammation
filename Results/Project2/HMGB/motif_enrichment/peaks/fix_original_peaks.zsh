#!/bin/zsh

sort -k1,1 -k2,2n HMGB1_allpeaks_hg19.bed > sort.bed
mergeBed -i sort.bed > HMGB1_allpeaks_hg19.bed
rm sort.bed

sort -k1,1 -k2,2n HMGB2_allpeaks_hg19.bed > sort.bed
mergeBed -i sort.bed > HMGB2_allpeaks_hg19.bed
rm sort.bed

