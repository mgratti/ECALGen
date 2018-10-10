# Script to launch several MC productions - at reco level
# parameters will be:
#  - number of events
#  - parameters to change in the ECAL clustering

# python Evreco_submit.py

import sys
print(sys.version)
import os
import time
import math
import itertools

# NOTE: you MUST have created this directory before
# xrdfs t3dcachedb03.psi.ch mkdir /pnfs/psi.ch/cms/trivcat/store/user/mratti/EcalGen/TEST_PRODUCTION
productionDir = "EcalGen/PROD_SeedingGathering_v3"
params = {}
params["nevts"] =     [50000]
params["gathering"] = [10.0, 5.0, 1.0, 2.0, 0.5] # multiplier
params["seeding"] =   [10.0, 5.0, 1.0, 2.0, 0.5] # multiplier

# Default thresholds for the moment not used
thrs={}
thrs['EB']={}
thrs['EB']['seed']= 0.23 # 230 MeV
thrs['EB']['gather'] = 0.08 # 80 MeV

thrs['EEP']={}
thrs['EEP']['seed']=0.60 # 600 MeV
thrs['EEP']['gather']=0.30 # 300 MeV

thrs['EEM']=thrs['EEP']


##### Submission
parameters_set = list(itertools.product(params["nevts"],params["gathering"],params["seeding"] ))
for iset in parameters_set:
  inevts = iset[0]
  igathering = iset[1]
  iseeding = iset[2]

  command = "qsub ecalReco_template.sh {p} {n} {s} {g}".format(p=productionDir, n=inevts, s=iseeding, g=igathering)
  print "Going to submit ecalGen_template.sh for production={p} nevts={n} seeding={s} gathering={g}".format(p=productionDir, n=inevts, s=iseeding, g=igathering)
  os.system(command)
