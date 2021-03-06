### Run time for Double Photon / Double electron in Run 2 / Run 3 conditions

#### Gen+Sim+Digi step
Gen + Sim + Digi steps produced in local

1) create a new dir in ```gen_sim_digi``` with a sensible name
2) copy there ```ecalGenDigi.sh``` and edit it to set what are the parameters you need for the production
3) ```source ecalGenDigi.sh```
4) once the job is finished copy output files to the tier3 area with appropriate naming convention

Outputs:
```
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run2Cond --> 100X_upgrade2018_realistic_Fromv10ExtZeroMaterial_v1 # To be discarded: noise too high
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2022_315fb_v1 
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2023_400fb_v1
$PNFS/EcalGen/GEN_SIM_DIGI/doubleElectron/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1 
$PNFS/EcalGen/GEN_SIM_DIGI/doubleElectron/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2022_315fb_v1
$PNFS/EcalGen/GEN_SIM_DIGI/doubleElectron/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2023_400fb_v1
$PNFS/EcalGen/GEN_SIM_DIGI/doubleElectron/Run2Cond/100X_upgrade2018_realistic_v7 # To be discarded: noise too high
$PNFS/EcalGen/GEN_SIM_DIGI/doubleElectron/Run2Cond/102X_upgrade2018_realistic_v15
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run2Cond/102X_upgrade2018_realistic_v15
```
#### Gen+Sim+Digi step (after March 2019)
Gen + Sim + Digi steps produced in patch, from 1 to 100 GeV, 500 K in total

1) create a new dir in ```gen_sim_digi``` with a sensible name
2) copy there ```ecalGenDigi.sh``` and edit it to set what are the parameters you need for the production
3) ```source ecalGenDigi.sh```
4) manually edit the tags that you need in all *.py files
5) then you can ```cmsRun``` everything !

Outputs:
```
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run2Cond/105X_upgrade2018_realistic_v3/
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run3Cond/105X_upgrade2018_realistic_v3/

$PNFS/EcalGen/GEN_SIM_DIGI/doubleElectron/Run3Cond/105X_upgrade2018_realistic_v3/
$PNFS/EcalGen/GEN_SIM_DIGI/doubleElectron/Run2Cond/105X_upgrade2018_realistic_v3/

```

#### Reco step
Reco step with different seeding and gathering thresholds submitted to batch

0) should you have to change the reco step, edit ```step3_template.py```
1) edit ```Evreco_submit.py``` edit input , output logs directories, and global tag consistently with previous steps
2) you're ready to submit to batch ```python Evreco_submit.py```

Outputs:

50K
```
$PNFS/EcalGen/PROD_SeedingGathering_v3/  --> Run2 conditions, 50K evts, w/o tracker, 100X_upgrade2018_realistic_Fromv10ExtZeroMaterial_v1 # To be discarded: noise too high
$PNFS/EcalGen/PROD_SeedingGathering_v4/  --> Run3 conditions, 50K evts, w/o tracker, 102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1
$PNFS/EcalGen/PROD_SeedingGathering_v5/  --> Run3 conditions, 50K evts, w/o tracker, 102X_upgrade2018_realistic_EcalAging_mid2022_315fb_v1
$PNFS/EcalGen/PROD_SeedingGathering_v6/  --> Run3 conditions, 50K evts, w/o tracker, 102X_upgrade2018_realistic_EcalAging_mid2023_400fb_v1
$PNFS/EcalGen/PROD_SeedingGathering_v7/  --> Run3 conditions, 50K evts, w   tracker, 102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1
$PNFS/EcalGen/PROD_SeedingGathering_v8/  --> Run3 conditions, 50K evts, w   tracker, 102X_upgrade2018_realistic_EcalAging_mid2022_315fb_v1
$PNFS/EcalGen/PROD_SeedingGathering_v9/  --> Run3 conditions, 50K evts, w   tracker, 102X_upgrade2018_realistic_EcalAging_mid2023_400fb_v1
$PNFS/EcalGen/PROD_SeedingGathering_v10/ --> Run2 conditions, 50K evts, w   tracker, 100X_upgrade2018_realistic_v7 # To be discarded: noise too high
$PNFS/EcalGen/PROD_SeedingGathering_v11/ --> Run2 conditions, 50K evts, w   tracker, 102X_upgrade2018_realistic_v15
$PNFS/EcalGen/PROD_SeedingGathering_v12/ --> Run2 conditions, 50K evts, w/o tracker, 102X_upgrade2018_realistic_v15
```

#### Reco step (after March 2019)
Reco step with different seeding and gathering thresholds submitted to batch

Outputs:

150K

```
$PNFS/EcalGen/PROD_SeedingGathering_v26 --> doublePhoton, 150K evts, 105X_upgrade2018_realistic_v3 + custom 180/fb tags
$PNFS/EcalGen/PROD_SeedingGathering_v25 --> doublePhoton, 150K evts, 105X_upgrade2018_realistic_v3 + custom 450/fb tags

$PNFS/EcalGen/PROD_SeedingGathering_v27 --> doubleEle,    150K evts, 105X_upgrade2018_realistic_v3 + custom 180/fb tags
$PNFS/EcalGen/PROD_SeedingGathering_v28 --> doubleEle,    150K evts, 105X_upgrade2018_realistic_v3 + custom 450/fb tags

```


#### Gen+Sim+Digi+Reco steps all at once for neutrino gun
Gen + Sim + Digi + Reco steps all at once in local

1) create a new dir in ```gen_sim_digi_reco``` with a sensibe name
2) copy there ```ecalGenDigiReco.sh`` and edit it to set what are the parameters you need for the production
3) ```source ecalGenDigiReco.sh```
4) once the job is finished copy output files to the tier3 area with appropriate naming convention

Outputs:
```
$PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run2Cond/100X_upgrade2018_realistic_v7/SingleNuE10_GEN_SIM_DIGI_RECO.root
$PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1/SingleNuE10_GEN_SIM_DIGI_RECO.root
$PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2022_315fb_v1/SingleNuE10_GEN_SIM_DIGI_RECO.root
$PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2023_400fb_v1/SingleNuE10_GEN_SIM_DIGI_RECO.root
$PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run2Cond/102X_upgrade2018_realistic_v15/SingleNuE10_GEN_SIM_DIGI_RECO.root
```

#### Gen+Sim+Digi+Reco steps for neutrino gun (March 2019), with modified tags wrt GT
Gen + Sim + Digi + Reco steps all at once in local, starting from example here https://dmytro.web.cern.ch/dmytro/cmsprodmon/workflows.php?prep_id=CMSSW_10_4_0_pre2__fullsim_noPU_2017_NuGun-1545067222-NuGun

Changed for all steps:
* GT: 105X_upgrade2018_realistic_v3
* local tags, as specified in ```gen_sim_digi_reco/tags_to_override.py``` for two scenarios 180/fb (end of Run-2) and 450/fb (end of Run-3)
* *PFrechits* are still minimal for end-of-Run2, those for end-of-Run3 were provided 

Outputs (non exhaustive list):
```
end-of-run2 50K events UL Pfrechit tresholds:    $PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run2Cond/105X_upgrade2018_realistic_v3/SingleNuE10_GEN_SIM_DIGI_RECO_50K_ULPFRecHits.root
end-of-run3 50K events:    $PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run3Cond/105X_upgrade2018_realistic_v3/SingleNuE10_GEN_SIM_DIGI_RECO_50K.root
```

* Moved to full readout instead of selective readout (non-exhaustive list):
```
end-of-run2 15K events:   $PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run2Cond/105X_upgrade2018_realistic_v3/SingleNuE10_GEN_SIM_DIGI_RECO_FullReadout.root
end-of-run2 15K events UL Pfrechit thresholds: $PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run2Cond/105X_upgrade2018_realistic_v3/SingleNuE10_GEN_SIM_DIGI_RECO_FullReadout_ULPFrecHits.root
end-of-run3 15K events:   $PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run3Cond/105X_upgrade2018_realistic_v3/SingleNuE10_GEN_SIM_DIGI_RECO_FullReadout.root
```

* Corrected alpha tag and added 550/fb conditions, full readout (5K evts)
```
180/fb:  $PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run2Cond/105X_upgrade2018_realistic_v3/SingleNuE10_GEN_SIM_DIGI_RECO_FullReadout_07_06_19.root
450/fb:  $PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run3Cond/105X_upgrade2018_realistic_v3/SingleNuE10_GEN_SIM_DIGI_RECO_FullReadout_07_06_19.root
550/fb:  $PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Run3Cond/105X_upgrade2018_realistic_v3/SingleNuE10_GEN_SIM_DIGI_RECO_FullReadout_07_06_19_550ifb.root
```


### Run time for NuGun in view of preparation of UL conditions 

#### Reco step for RelVal of UL
Submit locally 
```
cd reco
source ecalReco_nugun.sh
```
Outputs
```
/shome/mratti/cmssw_workarea/Generation/CMSSW_10_4_0_pre2/src/ECALGen/private_production/reco/nugun_reco_103X_AB/RelValNuGun_103X_mc2017_realistic_v2_AB_v01_HS-v1.root
/shome/mratti/cmssw_workarea/Generation/CMSSW_10_4_0_pre2/src/ECALGen/private_production/reco/nugun_reco_103X_AC/RelValNuGun_103X_mc2017_realistic_v2_AC_v01_HS-v1.root
```

#### All steps to reproduce sample from Fall17 campaign
Submit locally
```
cd gen_sim_digi_reco
source ecalGenDigiReco_nugun_Fall17.sh
```
Output:
```
$PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Fall17Cond/94X_mc2017_realistic_v10/SingleNuE10_GEN_SIM_DIGI_RECO.root
$PNFS/EcalGen/GEN_SIM_DIGI/SingleNu/Fall17Cond/94X_mc2017_realistic_v10/SingleNuE10_GEN_SIM_DIGI.root
```

