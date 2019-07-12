CONDITIONS="105X_upgrade2018_realistic_v3" #
# 100X_upgrade2018_realistic_v7 for                      for Run-2 std  (low thresholds for PFrechits)
# 100X_upgrade2018_realistic_Fromv10ExtZeroMaterial_v1   for Run-2 std  ("" and zero material) 
# 102X_upgrade2018_realistic_v15                         for Run-2 new std (high PFrechits, which must be changed by hand), noise and laser corrections from data
#  
# 102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1  for Run-3 (ext material does *NOT* need to be specified here)
# 102X_upgrade2018_realistic_EcalAging_mid2022_315fb_v1  "" 
# 102X_upgrade2018_realistic_EcalAging_mid2023_400fb_v1  ""
#
# 105X_upgrade2018_realistic_v3                          for Run-2 vs Run-3 studies from March 2019

GEOMETRY="DB:ExtendedZeroMaterial" # DB:ExtendedZeroMaterial -> no tracker, DB:Extended -> stdandard
ERA="Run2_2018" # currently an era for Run-3 not avaialble 
PU="NoPileUp" # this is also the default 
NEVENTS=500000
FRAGMENT="DoublePhoton" # DoublePhoton DoubleElectron

# step 1: gen + sim
echo 'Going to run step 1'

cmsDriver.py ${FRAGMENT}.py --conditions $CONDITIONS --geometry $GEOMETRY --beamspot Realistic25ns13TeVEarly2017Collision  --era $ERA --pileup $PU --step GEN,SIM --datatier GEN-SIM --eventcontent FEVTDEBUG --fileout file:${FRAGMENT}_GEN_SIM.root -n $NEVENTS  --python_filename step1_${FRAGMENT}.py --nThreads 8  --no_exec

#cmsRun ${FRAGMENT}_py_GEN_SIM.py &> log_${CONDITIONS}_${GEOMETRY}_${ERA}_${PU}_${FRAGMENT}_GEN_SIM

# step 2: digi
echo 'Going to run step 2'

cmsDriver.py step2  --conditions $CONDITIONS --geometry $GEOMETRY  --beamspot Realistic25ns13TeVEarly2017Collision --era $ERA --pileup $PU --step DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2018 --datatier GEN-SIM-DIGI-RAW  --eventcontent FEVTDEBUGHLT --filein file:${FRAGMENT}_GEN_SIM.root  --fileout file:${FRAGMENT}_GEN_SIM_DIGI.root -n $NEVENTS --python_filename step2_${FRAGMENT}.py --nThreads 8 --no_exec
