### Run time for Double Photon / Double electron in Run 2 / Run 3 conditions

#### Gen+Sim+Digi step
Gen + Sim + Digi steps produced in local in the /input dir

1) create a new dir in ```gen_sim_digi``` with a sensible name
2) copy there ```ecalGenDigi.sh``` and edit it to set what are the parameters you need for the production
3) ```source ecalGenDigi.sh```
4) once the job is finished copy output files to the tier3 area with appropriate naming convention

Outputs:
```
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run2Cond --> Run2 conditions, 50K evts, 100X_upgrade2018_realistic_Fromv10ExtZeroMaterial_v1
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2022_315fb_v1 
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2023_400fb_v1
$PNFS/EcalGen/GEN_SIM_DIGI/doubleElectron/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1 
$PNFS/EcalGen/GEN_SIM_DIGI/doubleElectron/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2022_315fb_v1
$PNFS/EcalGen/GEN_SIM_DIGI/doubleElectron/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2023_400fb_v1
$PNFS/EcalGen/GEN_SIM_DIGI/doubleElectron/Run2Cond/100X_upgrade2018_realistic_v7
$PNFS/EcalGen/GEN_SIM_DIGI/doubleElectron/Run2Cond/102X_upgrade2018_realistic_v15 <== to be added
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run2Cond/102X_upgrade2018_realistic_v15 <== to be added
```
#### Reco step
Reco step with different seeding and gathering thresholds submitted to batch

0) should you have to change the reco step, edit ```step3_template.py```
1) edit ```Evreco_submit.py``` edit input , output logs directories, and global tag consistently with previous steps
2) you're ready to submit to batch ```python Evreco_submit.py```

Outputs:

50K
```
$PNFS/EcalGen/PROD_SeedingGathering_v3/  --> Run2 conditions, 50K evts, w/o tracker, 100X_upgrade2018_realistic_Fromv10ExtZeroMaterial_v1
$PNFS/EcalGen/PROD_SeedingGathering_v4/  --> Run3 conditions, 50K evts, w/o tracker, 102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1
$PNFS/EcalGen/PROD_SeedingGathering_v5/  --> Run3 conditions, 50K evts, w/o tracker, 102X_upgrade2018_realistic_EcalAging_mid2022_315fb_v1
$PNFS/EcalGen/PROD_SeedingGathering_v6/  --> Run3 conditions, 50K evts, w/o tracker, 102X_upgrade2018_realistic_EcalAging_mid2023_400fb_v1
$PNFS/EcalGen/PROD_SeedingGathering_v7/  --> Run3 conditions, 50K evts, w   tracker, 102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1
$PNFS/EcalGen/PROD_SeedingGathering_v8/  --> Run3 conditions, 50K evts, w   tracker, 102X_upgrade2018_realistic_EcalAging_mid2022_315fb_v1
$PNFS/EcalGen/PROD_SeedingGathering_v9/  --> Run3 conditions, 50K evts, w   tracker, 102X_upgrade2018_realistic_EcalAging_mid2023_400fb_v1
$PNFS/EcalGen/PROD_SeedingGathering_v10/ --> Run2 conditions, 50K evts, w   tracker, 100X_upgrade2018_realistic_v7
```

#### Gen+Sim+Digi+Reco steps all at once for neutrino gun
Gen + Sim + Digi + Reco steps all at once in local

1) create a new dir in ```gen_sim_digi_reco``` with a sensibe name
2) copy there ```ecalGenDigi.sh`` and edit it to set what are the parameters you need for the production
3) ```source ecalGenDigi.sh```
4) once the job is finished copy output files to the tier3 area with appropriate naming convention

Outputs:
```
$PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run2Cond/100X_upgrade2018_realistic_v7/SingleNuE10_GEN_SIM_DIGI_RECO.root
$PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1/SingleNuE10_GEN_SIM_DIGI_RECO.root
$PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2022_315fb_v1/SingleNuE10_GEN_SIM_DIGI_RECO.root
$PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2023_400fb_v1/SingleNuE10_GEN_SIM_DIGI_RECO.root
$PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run2Cond/102X_upgrade2018_realistic_v15/SingleNuE10_GEN_SIM_DIGI_RECO.root
```

