
import os

genomeFile = "/hpcwork/izkf/projects/TfbsPrediction/Data/HG19/hg19.fa"

inputF = "./HMGB1_allpeaks_hg19.bed"
outputF = "./HMGB1_allpeaks_hg19_random500.bed"
outputFS = "./HMGB1_allpeaks_hg19_random500.fa"
tempF = "./temp.bed"

os.system("sort -R "+inputF+" > "+tempF)
os.system("head -n 500 "+tempF+" > "+outputF)
os.system("fastaFromBed -fi "+genomeFile+" -bed "+outputF+" -fo "+outputFS)
os.system("rm "+tempF)


