
# Import
import os
import sys

# Parameters
pl = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/co_binding/tfbs_chip/"
cl = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/bed_nfkb_enriched/original/"
ol = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/co_binding/statistics/result/"

# Iterating on peak types
peakList = ["peakseq", "spp"]
for peakName in peakList:

  # Input files
  to_remove = []
  mpbsFileList = ["broad_huvec_ctcf","duke_huvec_ctcf","sydh_huvec_fos","sydh_huvec_gata2","sydh_huvec_jun","sydh_huvec_max","uw_huvec_ctcf"]
  clusterFileList = [ "all","with","with_clust1","with_clust2","with_clust3","with_clust4","with_clust5",
                      "wo","wo_clust1","wo_clust2","wo_clust3","wo_clust4","wo_clust5"]

  # Creating query input matrix
  queryMatrixFileName = "./"+peakName+"_query.txt"
  to_remove.append(queryMatrixFileName)
  inMatrixFile = open(queryMatrixFileName,"w")
  inMatrixFile.write("\t".join(["name","type","file"])+"\n")
  for e in mpbsFileList: inMatrixFile.write("\t".join([e,"regions",pl+peakName+"_hg18/"+e+".bed"])+"\n")
  inMatrixFile.close()

  # Creating reference input matrix
  refMatrixFileName = "./"+peakName+"_reference.txt"
  to_remove.append(refMatrixFileName)
  inMatrixFile = open(refMatrixFileName,"w")
  inMatrixFile.write("\t".join(["name","type","file"])+"\n")
  for e in clusterFileList: inMatrixFile.write("\t".join([e,"regions",cl+e+".bed"])+"\n")
  inMatrixFile.close()

  # Output directories
  intTestDir = ol+peakName+"_intersect/"
  jacTestDir = ol+peakName+"_jaccard/"

  # Execution
  os.system("rgt-viz intersect -r "+refMatrixFileName+" -q "+queryMatrixFileName+" "+intTestDir)
  os.system("rgt-viz jaccard -r "+refMatrixFileName+" -q "+queryMatrixFileName+" "+jacTestDir+" -rt 100")


