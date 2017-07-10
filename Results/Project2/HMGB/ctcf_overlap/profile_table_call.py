
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

/hpcwork/izkf/projects/HuvecInflammation/Data/ctcf_chipseq/BroadInstitute/HUVEC_CTCF.bam
/hpcwork/izkf/projects/HuvecInflammation/Data/ctcf_chipseq/UTA/HUVEC_CTCF.bam
/hpcwork/izkf/projects/HuvecInflammation/Data/ctcf_chipseq/UW/HUVEC_CTCF.bamls

/home/egg/Projects/HuvecInflammation/Results/HMGB/motif_enrichment/peaks/HMGB1_allpeaks_hg19.bed
/home/egg/Projects/HuvecInflammation/Results/HMGB/motif_enrichment/peaks/HMGB2_allpeaks_hg19.bed



# Input
tfLoc = "/hpcwork/izkf/projects/TfbsPrediction/Results_DNase/MPBSAWG/K562_Evidence/fdr_4/"
tempLoc = "/work/eg474423/eg474423_Projects/trunk/TfbsPrediction/Results/ATAC/Profile/profile_regions/"
outLoc = "/work/eg474423/eg474423_Projects/trunk/TfbsPrediction/Results/ATAC/Profile/profile_table/"



      # Parameters
      totalWindow="500"
      bedFileNameList = ",".join([nFileName,yFileName])
      bamFileName = bamLoc+"K562/ATAC.bam"
      ol = outLoc+tfName+"/"
      outFileName = ol+tfName+"_"+ebn+"_"+ext+".txt"
      signalExt = ext
      signalExtBoth = eb
      os.system("mkdir -p "+ol)
 
      # Execution
      myL = "_".join(["PG",tfName])
      clusterCommand = "bsub -J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
      clusterCommand += "-W 100:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./profile_table_pipeline.zsh "
      clusterCommand += totalWindow+" "+bedFileNameList+" "+bamFileName+" "+outFileName+" "+signalExt+" "+signalExtBoth
      os.system(clusterCommand)


