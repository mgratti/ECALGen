### Run time for Double Photon / Double electron in Run 2 / Run 3 conditions

#### Gen+Sim+Digi step
Gen + Sim + Digi steps produced in local in the /input dir
Please edit ecalGenDigi.sh to set what are the parameters you need, then
```
source ecalGenDigi.sh
```
Copy output files to the tier3 area. 
List of available files:
```
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run2Cond
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1
```
#### Reco step
Reco step with different seeding and gathering thresholds submitted to batch
Edit input and output paths in Evreco_submit.py
```
python Evreco_submit.py
```
Outputs:

50K
```
$PNFS/EcalGen/PROD_SeedingGathering_v3/  --> Run2 conditions, 50K evts
$PNFS/EcalGen/PROD_SeedingGathering_v4/  --> Run3 conditions, 50K evtns, 102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1
```
