### Run time for Double Photon no tracker

Gen + Sim + Digi steps produced in local
Please edit the production file to set the number of events
```
source ecalGenDigi.sh
```

#### 50K:
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run2Cond/EGM-RunIISpring18_GEN_SIM.root
$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run2Cond/EGM-RunIISpring18_GEN_SIM_DIGI.root


Reco step with different seeding and gathering thresholds submitted to batch
```
python Evreco_submit.py
```
#### 10K
$PNFS/EcalGen/PROD_SeedingGathering_v1/

#### 50K
$PNFS/EcalGen/PROD_SeedingGathering_v3
