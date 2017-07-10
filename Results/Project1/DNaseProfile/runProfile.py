
# Import
import os
import sys
import glob

# Input
inputLocation = "/hpcwork/izkf/projects/huvec_inflammation/dnase_profile/Input/"
outLoc = "/hpcwork/izkf/projects/huvec_inflammation/dnase_profile/Results/"
wigFileNameList = [ "/hpcwork/izkf/projects/huvec_inflammation/wig_signal/hg18/DNase.bw",
                    "/hpcwork/izkf/projects/egg/Data/DNase/Huvec_HG18/DNaseBO.bw" ]
factorList = ["NFKB1", "REL", "RELA"]
inputBedList = ["with_clust1","with_clust2","with_clust3","with_clust4","with_clust5",
                "wo_clust1","wo_clust2","wo_clust3","wo_clust4","wo_clust5",
                "with","wo","all"]

# Iterating on wig files
for wigFileName in wigFileNameList:

  # Fetching wig name
  wigName = wigFileName.split("/")[-1].split(".")[0]

  # Iterating on TFs
  for factor in factorList:

    # Fetching input list
    bedFileList = [inputLocation+e+"_"+factor+".bed" for e in inputBedList]

    # Parameters
    invNeg = "n" 
    windowSize = "1000" 
    scaling = "10.0" 
    useLog = "n" 
    ext = "png" 
    labelList = ",".join([e.split("/")[-1].split(".")[0] for e in bedFileList])
    bedList = ",".join(bedFileList)
    wigLabel = wigName+"_"+factor
    wigFile = wigFileName
    outputLocation = outLoc

    # Execution
    clustComm = "bsub -J RPH -o RPH_out.txt -e RPH_err.txt -W 24:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" "
    clustComm += "./runProfile.zsh "
    clustComm += invNeg+" "
    clustComm += windowSize+" "
    clustComm += scaling+" "
    clustComm += useLog+" "
    clustComm += ext+" "
    clustComm += labelList+" "
    clustComm += bedList+" "
    clustComm += wigLabel+" "
    clustComm += wigFile+" "
    clustComm += outputLocation
    os.system(clustComm)


