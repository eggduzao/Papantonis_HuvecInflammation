
# Import
import os
import sys
from fisher import pvalue
from rgt.motifanalysis.Statistics import multiple_test_correction
from rgt.motifanalysis.Util import Result
from rgt.GeneSet import GeneSet

# Input
il = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_with_vs_wo/input/"
ol = "/work/eg474423/eg474423_Projects/trunk/HuvecInflammation/Results/motif_enrichment_with_vs_wo/results/"
inList = [ "footprints", "footprints_clust1", "footprints_clust2", "footprints_clust3", "footprints_clust4",
           "footprints_clust5", "original", "original_clust1", "original_clust2", "original_clust3",
           "original_clust4", "original_clust5" ]
results_header_text = "\t".join(["FACTOR","P-VALUE","CORR.P-VALUE","A","B","C","D","FREQ","BACK.FREQ.","GENES"])

# Loop in inList
for inName in inList:

  # Tail Loop
  tailLabelList = ["with", "wo"]
  for tailLabel in tailLabelList:

    # Parameters
    inFileName = il+inName+".txt"
    outFileName = ol+inName+"_"+tailLabel+".txt"

    # Fetching input values
    motif_names = []
    curr_a_dict = dict(); curr_b_dict = dict(); curr_c_dict = dict(); curr_d_dict = dict()
    inFile = open(inFileName,"r")
    for line in inFile:
      ll = line.strip().split("\t")
      motif_names.append(ll[0])
      curr_a_dict[ll[0]] = float(ll[1])
      curr_b_dict[ll[0]] = float(ll[2])
      curr_c_dict[ll[0]] = float(ll[3])
      curr_d_dict[ll[0]] = float(ll[4])
    inFile.close()

    # Performing fisher test
    result_list = []
    for k in motif_names:
      r = Result()
      r.name = k; r.a = curr_a_dict[k]; r.b = curr_b_dict[k]; r.c = curr_c_dict[k]; r.d = curr_d_dict[k]
      r.percent = float(r.a)/float(r.a+r.b); r.back_percent = float(r.c)/float(r.c+r.d)
      gs = GeneSet("gs"); gs.genes.append("NA"); r.genes = gs
      try:
        p = pvalue(r.a,r.b,r.c,r.d)
        if(tailLabel == "with"): r.p_value = p.right_tail
        else: r.p_value = p.left_tail
      except Exception: r.p_value = 1.0
      result_list.append(r)
                
    # Performing multiple test correction
    multuple_corr_rej, multiple_corr_list = multiple_test_correction([e.p_value for e in result_list], 
                                                                    alpha=0.05, method='indep')
    for i in range(0,len(multiple_corr_list)): result_list[i].corr_p_value = multiple_corr_list[i]

    # Sorting result list
    result_list = sorted(result_list, key=lambda x: x.name)
    result_list = sorted(result_list, key=lambda x: x.percent, reverse=True)
    result_list = sorted(result_list, key=lambda x: x.p_value)
    result_list = sorted(result_list, key=lambda x: x.corr_p_value)

    # Preparing results for printing
    for r in result_list:
      #r.p_value = "%.4e" % r.p_value
      #r.corr_p_value = "%.4e" % r.corr_p_value
      r.percent = str(round(r.percent,4)*100)+"%"
      r.back_percent = str(round(r.back_percent,4)*100)+"%"

    # Printing statistics text
    output_file = open(outFileName,"w")
    output_file.write(results_header_text+"\n")
    for r in result_list: output_file.write(str(r)+"\n")
    output_file.close()


