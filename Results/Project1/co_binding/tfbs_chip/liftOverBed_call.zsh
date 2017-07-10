#!/bin/zsh

# Input
liftFileName="/hpcwork/izkf/projects/TfbsPrediction/Data/HG19/hg19ToHg18.over.chain"
csFile18="/hpcwork/izkf/projects/TfbsPrediction/Data/HG18/hg18.chrom.sizes.filtered.increased.10e6.ForBw"
ilp="/home/egg/Projects/HuvecInflammation/Results/co_binding/tfbs_chip/peakseq_hg19/"
ils="/home/egg/Projects/HuvecInflammation/Results/co_binding/tfbs_chip/spp_hg19/"
olp="/home/egg/Projects/HuvecInflammation/Results/co_binding/tfbs_chip/peakseq_hg18/"
ols="/home/egg/Projects/HuvecInflammation/Results/co_binding/tfbs_chip/spp_hg18/"
inFileList=( 
  $ilp"peakSeq.optimal.wgEncodeBroadHistoneHuvecCtcfStdAlnRep0_vs_wgEncodeBroadHistoneHuvecControlStdAlnRep0"
  $ilp"peakSeq.optimal.wgEncodeOpenChromChipHuvecCtcfAlnRep0_vs_wgEncodeOpenChromChipHuvecInputAlnRep1"
  $ilp"peakSeq.optimal.wgEncodeSydhTfbsHuvecCfosUcdAlnRep0_vs_wgEncodeSydhTfbsHuvecInputUcdAlnRep1"
  $ilp"peakSeq.optimal.wgEncodeSydhTfbsHuvecCjunStdAlnRep0_vs_wgEncodeSydhTfbsHuvecInputStdAlnRep0"
  $ilp"peakSeq.optimal.wgEncodeSydhTfbsHuvecGata2UcdAlnRep0_vs_wgEncodeSydhTfbsHuvecInputUcdAlnRep1"
  $ilp"peakSeq.optimal.wgEncodeSydhTfbsHuvecMaxStdAlnRep0_vs_wgEncodeSydhTfbsHuvecInputStdAlnRep0"
  $ilp"peakSeq.optimal.wgEncodeUwTfbsHuvecCtcfStdAlnRep0_vs_wgEncodeUwTfbsHuvecInputStdAlnRep1"
  $ils"spp.optimal.wgEncodeBroadHistoneHuvecCtcfStdAlnRep0_VS_wgEncodeBroadHistoneHuvecControlStdAlnRep0"
  $ils"spp.optimal.wgEncodeOpenChromChipHuvecCtcfAlnRep0_VS_wgEncodeOpenChromChipHuvecInputAln"
  $ils"spp.optimal.wgEncodeSydhTfbsHuvecCfosUcdAlnRep0_VS_wgEncodeSydhTfbsHuvecInputUcdAlnRep1"
  $ils"spp.optimal.wgEncodeSydhTfbsHuvecCjunStdAlnRep0_VS_wgEncodeSydhTfbsHuvecInputStdAlnRep0"
  $ils"spp.optimal.wgEncodeSydhTfbsHuvecGata2UcdAlnRep0_VS_wgEncodeSydhTfbsHuvecInputUcdAlnRep1"
  $ils"spp.optimal.wgEncodeSydhTfbsHuvecMaxStdAlnRep0_VS_wgEncodeSydhTfbsHuvecInputStdAlnRep0"
  $ils"spp.optimal.wgEncodeUwTfbsHuvecCtcfStdAlnRep0_VS_wgEncodeUwTfbsHuvecInputStdAlnRep1"
)
outFileList=( 
  $olp"broad_huvec_ctcf"
  $olp"duke_huvec_ctcf"
  $olp"sydh_huvec_fos"
  $olp"sydh_huvec_jun"
  $olp"sydh_huvec_gata2"
  $olp"sydh_huvec_max"
  $olp"uw_huvec_ctcf"
  $ols"broad_huvec_ctcf"
  $ols"duke_huvec_ctcf"
  $ols"sydh_huvec_fos"
  $ols"sydh_huvec_jun"
  $ols"sydh_huvec_gata2"
  $ols"sydh_huvec_max"
  $ols"uw_huvec_ctcf"
)

# Iterating on input
for i in {1..$#inFileList}
do

  # Files
  inFileBed=$inFileList[$i]".bed"
  inFileBb=$inFileList[$i]".bb"
  outFileBed=$outFileList[$i]".bed"
  outUnliftBed=$outFileList[$i]"_unlifted.bed"

  # Execution
  bigBedToBed $inFileBb $inFileBed
  python extPeak.py 100 $inFileBed $inFileBed".ext"
  grep -v -E "chrY|chrM|random|hap" $inFileBed".ext" | cut -f 1,2,3,4,5 > $inFileBed".filt"
  liftOver $inFileBed".filt" $liftFileName $outFileBed".unsorted" $outUnliftBed".unsorted"
  grep -v -E "chrY|chrM|random|hap" $outFileBed".unsorted" | cut -f 1,2,3,4,5 > $outFileBed".filt"
  grep -v -E "chrY|chrM|random|hap" $outUnliftBed".unsorted" | cut -f 1,2,3,4,5 > $outUnliftBed".filt"
  sort -k1,1 -k2,2n $outFileBed".filt" > $outFileBed
  sort -k1,1 -k2,2n $outUnliftBed".filt" > $outUnliftBed
  rm $inFileBed $inFileBed".ext" $inFileBed".filt" $outFileBed".unsorted" $outUnliftBed".unsorted" $outFileBed".filt" $outUnliftBed".filt"

done


