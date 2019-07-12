# ECALGen
Bunch of scripts to generate samples for ECAL performance studies

### Installation
Use CMSSSW_10_5_0 for March19 Run2/Run3 studies, including clustering studies

Use CMSSW_10_4_0_pre2 for test for UL of 2017
Use CMSSW_9_4_0_patch1 for test of Fall17 of 2017

Use CMSSW_10_0_3 for Nov18 Run 2 clustering studies
Use CMSSW_10_2_5 for Nov18 Run 3 clustering studies

```
cmsrel CMSSW_xx_x_x
cd CMSSW_xx_x_x/src/
cmsenv
git cms-addpkg RecoParticleFlow/Configuration
git cms-addpkg Configuration/Generator 
git clone git@github.com:mgratti/ECALGen.git
cp ECALGen/cmssw_changed_files/RecoParticleFlow_EventContent_cff.py RecoParticleFlow/Configuration/python/RecoParticleFlow_EventContent_cff.py
cp ECALGen/cmssw_changed_files/DoublePhoton.py Configuration/Generator/python/DoublePhoton.py
cp ECALGen/cmssw_changed_files/DoubleElectron.py Configuration/Generator/python/DoubleElectron.py
# cp ECALGen/cmssw_changed_files/DoublePhoton_closeECAL.py Configuration/Generator/python/DoublePhoton_closeECAL.py -> can only be used with 10_6_0
scram b -j8
```

### Workflow
The idea is that everytime you start a new generation, you set-up a new directory in ```private_production``` and write configuration files according to your needs. 
You find examples in ```OLD_private_production```. -> NOTE: I am now writing a cmsDriver writer to automatise this step.

You first test the full chain with few events and then launch the production for all events.

It is always advised to submit the jobs to the batch, so that you can run multi-core. Note: SungridEngine for <=10_5_0, Slurm for >= 10_6_0

The outputs of the generation should be copied to the storage element, following a proper naming scheme.

Currently we submit each step of the generation separately, but you should consider to launch the steps together.

