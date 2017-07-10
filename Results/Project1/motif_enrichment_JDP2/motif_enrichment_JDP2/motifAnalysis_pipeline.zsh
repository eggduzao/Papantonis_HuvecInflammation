#!/bin/zsh

# Libraries
module load DEVELOP python/2.7.5 &> /dev/null
export PATH=$PATH:/home/eg474423/Installation/motifanalysis/bin
export PATH=$PATH:/hpcwork/izkf/bin
export PATH=$PATH:/hpcwork/izkf/opt/bin
export PATH=$PATH:/home/eg474423/perl/bin
export PATH=$PATH:/work/eg474423/eg474423_Projects/trunk/TfbsPrediction/Code/bin
export PYTHONPATH=$PYTHONPATH:/home/eg474423/Installation/motifanalysis/lib/python2.7/site-packages
export PYTHONPATH=$PYTHONPATH:/hpcwork/izkf/lib64/python2.7/site-packages
export PYTHONPATH=$PYTHONPATH:/hpcwork/izkf/lib/python2.7/site-packages

allParameters=($argv[1,$#argv])
rgt-motifanalysis $allParameters


