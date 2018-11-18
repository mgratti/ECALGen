CONDITIONS="102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1" #
# 100X_upgrade2018_realistic_v7 for                      for Run-2 std  (low thresholds for PFrechits)
# 100X_upgrade2018_realistic_Fromv10ExtZeroMaterial_v1   for Run-2 std  ("" and zero material) 
# 102X_upgrade2018_realistic_v15                         for Run-2 new std (high PFrechits, which must be changed by hand), noise and laser corrections from data
#  
# 102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1  for Run-3 (ext material does *NOT* need to be specified here)
# 102X_upgrade2018_realistic_EcalAging_mid2022_315fb_v1  "" 
# 102X_upgrade2018_realistic_EcalAging_mid2023_400fb_v1  ""
GEOMETRY="DB:Extended" # ExtendedZeroMaterial -> no tracker, Extended -> stdandard
ERA="Run2_2018" # are you sure this is the case also for Run 3 ? 
PU="NoPileUp" # this is also the default 
NEVENTS=50000
FRAGMENT="DoubleElectron" # DoublePhoton DoubleElectron

# step 1: gen + sim
echo 'Going to run step 1'

cmsDriver.py ${FRAGMENT}.py --conditions $CONDITIONS --geometry $GEOMETRY --beamspot Realistic25ns13TeVEarly2017Collision  --era $ERA --pileup $PU --step GEN,SIM --datatier GEN-SIM --eventcontent FEVTDEBUG --fileout file:EGM-RunIISpring18_GEN_SIM.root -n $NEVENTS --no_exec

cmsRun ${FRAGMENT}_py_GEN_SIM.py &> log_${CONDITIONS}_${GEOMETRY}_${ERA}_${PU}_${FRAGMENT}_GEN_SIM

# step 2: digi
echo 'Going to run step 2'
cmsDriver.py step2  --conditions $CONDITIONS --geometry $GEOMETRY  --beamspot Realistic25ns13TeVEarly2017Collision --era $ERA --pileup $PU --step DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2018 --datatier GEN-SIM-DIGI-RAW  --eventcontent FEVTDEBUGHLT --filein file:EGM-RunIISpring18_GEN_SIM.root  --fileout file:EGM-RunIISpring18_GEN_SIM_DIGI.root -n $NEVENTS  &> log_${CONDITIONS}_${GEOMETRY}_${ERA}_${PU}_${FRAGMENT}_DIGI
