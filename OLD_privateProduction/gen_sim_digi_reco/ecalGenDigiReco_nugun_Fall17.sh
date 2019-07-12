CONDITIONS="94X_mc2017_realistic_v10" #
# 94X_mc2017_realistic_v10                               ALLEGEDLY for Fall17 campaign
GEOMETRY="DB:Extended" # ExtendedZeroMaterial -> no tracker, Extended -> stdandard
ERA="Run2_2017" # # Run2_2018, Run2_2017  are you sure this is the case also for Run 3 ? 
#PU="NoPileUp" # this is also the default 
PU="dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW" # this is pile up input which is different from pileup
NEVENTS=15000 ## 15000

# step 1: gen + sim
echo 'Going to run step 1'

cmsDriver.py SingleNuE10_cfi.py  --conditions $CONDITIONS -n $NEVENTS --geometry $GEOMETRY  --beamspot Realistic25ns13TeVEarly2017Collision --era $ERA  --step GEN,SIM --datatier GEN-SIM --eventcontent FEVTDEBUG --fileout file:SingleNuE10_GEN_SIM.root  --nThreads 8  &> log_${CONDITIONS}_${GEOMETRY}_${ERA}_SingleNu_GEN_SIM


# step 2: digi
echo 'Going to run step 2'

cmsDriver.py step2 --conditions $CONDITIONS --geometry $GEOMETRY --beamspot Realistic25ns13TeVEarly2017Collision --era $ERA --pileup_input "${PU}"  --mc --datamix PreMix  --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --datatier GEN-SIM-RAW  --eventcontent PREMIXRAW --filein file:SingleNuE10_GEN_SIM.root  --fileout file:SingleNuE10_GEN_SIM_DIGI.root -n $NEVENTS  --nThreads 8   &> log_${CONDITIONS}_${GEOMETRY}_${ERA}_SingleNu_DIGI


# step 3: reco
echo 'Going to run step 3'

cmsDriver.py step3  --conditions $CONDITIONS -n $NEVENTS  --geometry $GEOMETRY  --era $ERA -s RAW2DIGI,L1Reco,RECO,RECOSIM --datatier GEN-SIM-RECO --eventcontent RECOSIM  --filein file:SingleNuE10_GEN_SIM_DIGI.root --fileout file:SingleNuE10_GEN_SIM_DIGI_RECO.root --nThreads 8  &> log_${CONDITIONS}_${GEOMETRY}_${ERA}_SingleNu_RECO



# the name of the step is just a stupid convention !

#cmsDriver.py SingleNuE10_cfi.py --fileout file:SingleNu_GEN_SIM.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step GEN,SIM --nThreads 8 --geometry DB:Extended --era Run2_2017  --customise Configuration/DataProcessing/Utils.addMonitoring  -n 200
#
#
#cmsDriver.py step1 --filein file:SingleNu_GEN_SIM.root --fileout file:SingleNu_GEN_SIM_step1.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v10 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads 8 --datamix PreMix --era Run2_2017  --customise Configuration/DataProcessing/Utils.addMonitoring -n 200
#
#
##cmsDriver.py step2 --filein file:SingleNu_step1.root --fileout file:SingleNu_stepAOD.root --mc --eventcontent AODSIM,ALCARECO runUnscheduled --datatier AODSIM,ALCARECO --conditions 94X_mc2017_realistic_v10 --step RAW2DIGI,RECO,EI,ALCA:EcalUncalZElectron --nThreads 8 --era Run2_2017 --python_filename EGM-RunIIFall17DRPremix-00012_2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 703 






