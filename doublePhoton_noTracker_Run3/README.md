### Run time for Double Photon no tracker Run-3 conditions

#### Gen+Sim+Digi step
Gen + Sim + Digi steps produced in local in the /input dir
Please edit the production file to set what the parameters you need, then
```
source ecalGenDigi.sh
```

Output files are here
```
#$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run3Cond/EGM-RunIISpring18_GEN_SIM.root
#$PNFS/EcalGen/GEN_SIM_DIGI/doublePhoton_noTracker/Run3Cond/EGM-RunIISpring18_GEN_SIM_DIGI.root
NOT YET AVAILABLE
```
#### Reco step
Reco step with different seeding and gathering thresholds submitted to batch
```
python Evreco_submit.py
```
Outputs:

50K
```
$PNFS/EcalGen/PROD_SeedingGathering_v4/
NOT YET AVAILABLE
```
