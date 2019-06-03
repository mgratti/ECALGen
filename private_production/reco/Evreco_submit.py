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
import subprocess

anaName='SingleNuE10' # 'EGM', 'SingleNuE10'
lumi='450' # 180 450
inputDir = 'EcalGen/GEN_SIM_DIGI/SingleNu/Run3Cond/105X_upgrade2018_realistic_v3/'
productionDir = 'EcalGen/PROD_SeedingGathering_v41'
logsDir = 'PROD_SeedingGathering_v41'

conditions = '105X_upgrade2018_realistic_v3' # coherently with gen+sim+digi steps
era = 'Run2_2018' # coherently with gen+sim+digi steps

params = {}
params['nevts'] =     [15000] # for nu gun 15000, for Egamma 150000
params['gathering'] = [1.0] #2.0,3.0]#[10.0, 5.0, 1.0, 2.0, 0.5] # multiplier
params['seeding'] =   [3.1,4.0]#[10.0, 5.0, 1.0, 2.0, 0.5] # multiplier

# Default thresholds for the moment not used
#thrs={}
#thrs['EB']={}
#thrs['EB']['seed']= 0.23 # 230 MeV
#thrs['EB']['gather'] = 0.08 # 80 MeV

#thrs['EEP']={}
#thrs['EEP']['seed']=0.60 # 600 MeV
#thrs['EEP']['gather']=0.30 # 300 MeV

#thrs['EEM']=thrs['EEP']

##### Create output dir and logsdir
prefix='/pnfs/psi.ch/cms/trivcat/store/user/mratti/'
print 'Going to create output directory ', prefix + productionDir
command = 'xrdfs t3dcachedb03.psi.ch mkdir {p}'.format(p=prefix + productionDir)
if not os.path.isdir(prefix + productionDir):
  subprocess.check_output(command, shell=True)
#else: raise RuntimeError('productionDir already present please check')

command = 'mkdir -p {l}'.format(l=logsDir)
if not os.path.isdir(logsDir):
  subprocess.check_output(command, shell=True)
#else: raise RuntimeError('logsDir already present please check')

##### Submission
parameters_set = list(itertools.product(params['nevts'],params['gathering'],params['seeding'] ))
for iset in parameters_set:
  inevts = iset[0]
  igathering = iset[1]
  iseeding = iset[2]

  #command = 'qsub -o {l} -e {l} -pe smp 8 ecalReco_template.sh {p} {i} {n} {s} {g} {c} {e} {a} {lu}'.format(p=productionDir, i=inputDir, l=logsDir, n=inevts, s=iseeding, g=igathering, c=conditions, e=era, a=anaName, lu=lumi)
  command = 'qsub -o {l} -e {l} -l h_vmem=4g ecalReco_template.sh {p} {i} {n} {s} {g} {c} {e} {a} {lu}'.format(p=productionDir, i=inputDir, l=logsDir, n=inevts, s=iseeding, g=igathering, c=conditions, e=era, a=anaName, lu=lumi)
  print command
  print 'Going to submit ecalReco_template.sh for production={p} inDir={i} logsDir={l} nevts={n} seeding={s} gathering={g} conditions={c} era={e} anaName={a} lumi={lu}'.format(p=productionDir, i=inputDir, l=logsDir, n=inevts, s=iseeding, g=igathering, c=conditions, e=era, a=anaName, lu=lumi)
  os.system(command)
