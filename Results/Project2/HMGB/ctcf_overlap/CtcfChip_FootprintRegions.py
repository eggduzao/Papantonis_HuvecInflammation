
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
bamList = [bamLoc+"BroadInstitute/HUVEC_CTCF.bam", bamLoc+"UTA/HUVEC_CTCF.bam", bamLoc+"UW/HUVEC_CTCF.bam"]

bedLoc = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/motif_enrichment/input/"
bedList = [bedLoc+"HMGB1_footprints_peaks_hg19.bed,"+bedLoc+"HMGB1_footprints_no_peaks_hg19.bed",
           bedLoc+"HMGB2_footprints_peaks_hg19.bed,"+bedLoc+"HMGB2_footprints_no_peaks_hg19.bed",]

outLoc = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/HMGB/ctcf_overlap/table/"

for i in range(0,len(bamList)):

  bamName = bamList[i]

  for bedName in bedList:

    label = "_".join(bedName.split(",")[0].split("/")[-1].split("_")[:2]+[bamName.split("/")[-2],"chip"])+".txt"
    print label

    # Parameters
    totalWindow="10000"
    bedFileNameList = bedName
    bamFileName = bamName
    outFileName = outLoc+label
    signalExt = "200"
    signalExtBoth = "N"
 
    # Execution
    myL = "_".join(["PG"])
    clusterCommand = "bsub -J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
    clusterCommand += "-W 100:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./profile_table_pipeline.zsh "
    clusterCommand += totalWindow+" "+bedFileNameList+" "+bamFileName+" "+outFileName+" "+signalExt+" "+signalExtBoth
    os.system(clusterCommand)


