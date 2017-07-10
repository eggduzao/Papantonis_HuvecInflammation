
# Import
import os
import sys
import glob
from Bio import Motif

# Input
pwmLoc = "/home/egg/hpcwork/izkf/projects/huvec_inflammation/motif_enrichment/Input/PWM/"
logoLoc = "/home/egg/hpcwork/izkf/projects/huvec_inflammation/motif_enrichment/Input/logo/"
os.system("mkdir -p "+logoLoc)

# Execution
for inFileName in glob.glob(pwmLoc+"*.pwm"):
  inName = ".".join(inFileName.split("/")[-1].split(".")[:-1])
  inputFile = open(inFileName,"r")
  outputFileName = logoLoc+inName+".png"
  pwm = Motif.read(inputFile,"jaspar-pfm")
  pwm.weblogo(outputFileName, res=300)
  inputFile.close()


