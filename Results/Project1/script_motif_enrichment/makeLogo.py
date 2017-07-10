
# Import
import sys
from Bio import Motif

# Reading input
resolution = int(sys.argv[1])
outExt = sys.argv[2]
inputFileName = sys.argv[3]
outputLocation = sys.argv[4]
if(outputLocation[-1] != "/"): outputLocation+="/"

# File handling
inputFile = open(inputFileName,"r")
outName = inputFileName.split("/")[-1].split(".")[0]

# Creating weblogo
pwm = Motif.read(inputFile,"jaspar-pfm")
pwm.weblogo(outputLocation+outName+"."+outExt, res=resolution, format=outExt)

# Termination
inputFile.close()

