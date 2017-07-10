
# Import
import os
import sys
from glob import glob

# File length function
def file_len(fname):
  i = 0
  with open(fname) as f:
    for i, l in enumerate(f): pass
  return i + 1

# Input
bamLoc = "/hpcwork/izkf/projects/HuvecInflammation/Data/ctcf_chipseq/"
bamList = ["BroadInstitute/HUVEC_CTCF.bam", "UTA/HUVEC_CTCF.bam", "UW/HUVEC_CTCF.bam"]

randLoc = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/ctcf_overlap/random_peaks/"
randList = ["BroadInstitute_HUVEC_CTCF.bed", "UTA_HUVEC_CTCF.bed", "UW_HUVEC_CTCF.bed"]

peakLoc = "/hpcwork/izkf/projects/HuvecInflammation/Data/ctcf_chipseq/"
peakList = ["BroadInstitute/HUVEC_CTCF_Peaks.bed", "UTA/HUVEC_CTCF_Peaks.bed", "UW/HUVEC_CTCF_Peaks.bed"]

bedLoc = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment/peaks/"
bedList = ["HMGB1_allpeaks_hg19.bed", "HMGB2_allpeaks_hg19.bed"]

outLoc = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/ctcf_overlap/table/"

for i in range(0,len(bamList)):

  bamName = bamList[i]
  randName = randList[i]
  peakName = peakList[i]

  for bedName in bedList:

    bamLabel = "CTCF_"+bamName.split("/")[0]
    bedLabel = bedName.split("_")[0]

    # Parameters
    totalWindow="10000"
    bedFileNameList = ",".join([randLoc+randName,bedLoc+bedName,peakLoc+peakName])
    bamFileName = bamLoc+bamName
    outFileName = outLoc+bedLabel+"_"+bamLabel+".txt"
    signalExt = "200"
    signalExtBoth = "N"
 
    # Execution
    myL = "_".join(["PG"])
    clusterCommand = "bsub -J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
    clusterCommand += "-W 100:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./profile_table_pipeline.zsh "
    clusterCommand += totalWindow+" "+bedFileNameList+" "+bamFileName+" "+outFileName+" "+signalExt+" "+signalExtBoth
    os.system(clusterCommand)


