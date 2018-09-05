# ECALGen
Bunch of scripts to generate various ecal conditions

### Installation
you must be in a valid CMSSW release
and then git clone repo


### Run time

#### Double Photon no tracker
Gen + Sim + Digi steps produced in local
```
source ecalGenDigi.sh
```

Reco step with different seeding and gathering thresholds submitted to batch
```
python Evreco_submit.py
```
