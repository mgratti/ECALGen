CONDITIONS="102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1" #
# 100X_upgrade2018_realistic_v7 for                      for Run-2 std  (low thresholds for PFrechits)
# 100X_upgrade2018_realistic_Fromv10ExtZeroMaterial_v1   for Run-2 std  ("" and zero material) 
#  
# 102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1  for Run-3 (ext material does *NOT* need to be specified here)
# 102X_upgrade2018_realistic_EcalAging_mid2022_315fb_v1  "" 
# 102X_upgrade2018_realistic_EcalAging_mid2023_400fb_v1  ""
GEOMETRY="DB:ExtendedZeroMaterial" # ExtendedZeroMaterial -> no tracker, Extended -> stdandard
ERA="Run2_2018" # are you sure this is the case also for Run 3 ? 
PU="NoPileUp" # this is also the default 
NEVENTS=50000

cmsDriver.py step3 --conditions ${CONDITIONS} -n ${NEVENTS} --geometry ${GEOMETRY} --beamspot Realistic25ns13TeVEarly2017Collision --era ${ERA} --pileup ${PU} -s RAW2DIGI,L1Reco,RECO,RECOSIM --datatier GEN-SIM-RECO --eventcontent RECOSIM --filein file:EGM-RunIISpring18_GEN_SIM_DIGI.root --fileout file:EGM-RunIISpring18_GEN_SIM_DIGI_RECO.root --no_exec

