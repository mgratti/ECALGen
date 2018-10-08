# ECALGen
Bunch of scripts to generate various ecal conditions

### Installation

Use CMSSW_10_0_3 for Run 2 studies
Use CMSSW_10_2_5 for Run 3 studies
```
cmsrel CMSSW_10_2_5
cd CMSSW_10_2_5/src/
git cms-addpkg RecoParticleFlow/Configuration
git clone git@github.com:mgratti/ECALGen.git
cp ECALGen/cmssw_changed_files/RecoParticleFlow_EventContent_cff.py RecoParticleFlow/Configuration/python/RecoParticleFlow_EventContent_cff.py
scram b -j8
```

