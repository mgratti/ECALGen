# driver extracted from request directly
#  https://cmsweb.cern.ch/couchdb/reqmgr_config_cache/3e93dd3aa3b8a7db74a211e5c4c407e4/configFile

cmsDriver.py step3 --conditions auto:phase1_2017_realistic -n 20000 --era Run2_2017 --eventcontent RECOSIM,MINIAODSIM,DQM --runUnscheduled -s RAW2DIGI,L1Reco,RECO,RECOSIM,EI,PAT,VALIDATION:@standardValidation+@miniAODValidation,DQM:@standardDQM+@ExtraHLT+@miniAODDQM --datatier GEN-SIM-RECO,MINIAODSIM,DQMIO --geometry DB:Extended --io RecoFull_2017.io --python RecoFull_2017.py --conditions=103X_mc2017_realistic_v2_AB_v01 --no_exec --filein file:${XRDGLO}//store/relval/CMSSW_10_4_0_pre2/RelValNuGun/GEN-SIM-DIGI-RAW/103X_mc2017_realistic_v2_AB_v01_HS-v1/20000/FB71DFBC-AE6E-5D43-9823-07CBAC93A47C.root --fileout file:RelValNuGun_103X_mc2017_realistic_v2_AB_v01_HS-v1.root --nThreads 8

echo "going to run step 3"

cmsRun RecoFull_2017.py 
