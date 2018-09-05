NEVENTS=50000

# step 1: gen + sim
echo 'Going to run step 1'
cmsRun EGM-RunIISpring18_GEN_SIM_cfg.py -n $NEVENTS  &> log_GEN_SIM 

# step 2: digi
#echo 'Going to run step 2'
#cmsDriver.py step2  --conditions 100X_upgrade2018_realistic_Fromv10ExtZeroMaterial_v1 -n $NEVENTS --geometry DB:ExtendedZeroMaterial  --beamspot Realistic25ns13TeVEarly2017Collision --era Run2_2018 --step DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2018 --datatier GEN-SIM-DIGI-RAW  --eventcontent FEVTDEBUGHLT --filein file:EGM-RunIISpring18_GEN_SIM.root --python_filename EGM-RunIISpring18_DIGI_cfg.py --fileout file:EGM-RunIISpring18_GEN_SIM_DIGI.root &> log_DIGI
