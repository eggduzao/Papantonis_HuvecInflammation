
# Import
import os
import sys

# Input
pl = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/co_binding/tfbs_chip/"
ml = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/co_binding/tfbs_motifmatch/result/"
ol = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/co_binding/tfbs_chip+motif/"
peakList = ["peakseq","spp"]
inFileList = ["broad_huvec_ctcf","duke_huvec_ctcf","sydh_huvec_fos","sydh_huvec_gata2","sydh_huvec_jun","sydh_huvec_max","uw_huvec_ctcf"]

# Iterating on peaks
for peakName in peakList:

  # Iterating on input files
  for inName in inFileList:

    # Parameters
    motifName = inName.split("_")[-1].upper()
    peakFileName = pl+peakName+"_hg18/"+inName+".bed"
    motifFileName = ml+peakName+"/Match/"+inName+"_mpbs.bb"
    outFileNamePM = ol+peakName+"/"+inName+"_PM.bed"
    outFileNameMP = ol+peakName+"/"+inName+"_MP.bed"
    outFileNameP = ol+peakName+"/"+inName+"_P.bed"
    outFileNameM = ol+peakName+"/"+inName+"_M.bed"

    # Temp files
    t1 = "t1.bed"
    t2 = "t2.bed"
    t3 = "t3.bed"
    t4 = "t4.bed"
    to_remove = [t1,t2,t3,t4]

    # Convert to bed
    os.system("bigBedToBed "+motifFileName+" "+t1)

    # Fetch motifs
    os.system("grep -i "+motifName+" "+t1+" > "+t2)

    # Sort motif file
    os.system("sort -k1,1 -k2,2n "+t2+" > "+t3)

    # Sort peak file
    os.system("sort -k1,1 -k2,2n "+peakFileName+" > "+t4)

    # Execution
    os.system("intersectBed -u -wa -a "+t4+" -b "+t3+" > "+outFileNamePM)
    os.system("intersectBed -u -wa -a "+t3+" -b "+t4+" > "+outFileNameMP)
    os.system("intersectBed -v -wa -a "+t4+" -b "+t3+" > "+outFileNameP)
    os.system("intersectBed -v -wa -a "+t3+" -b "+t4+" > "+outFileNameM)

    # Termination
    for e in to_remove: os.system("rm "+e)


