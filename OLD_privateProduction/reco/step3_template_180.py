# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions 102X_upgrade2018_realistic_EcalAging_mid2021_235fb_v1 -n 50000 --geometry DB:ExtendedZeroMaterial --beamspot Realistic25ns13TeVEarly2017Collision --era Run2_2018 --pileup NoPileUp -s RAW2DIGI,L1Reco,RECO,RECOSIM --datatier GEN-SIM-RECO --eventcontent RECOSIM --filein file:FragmenT-RunIISpring18_GEN_SIM_DIGI.root --fileout file:FragmenT-RunIISpring18_GEN_SIM_DIGI_RECO.root --no_exec

from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('analysis')
# define the defaults here, changed from command line
options.maxEvents = -1 # -1 means all events, maxEvents considers the total over files considered
# add costum parameters
options.register ('EBseed',
                  1.0, # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.float,          # string, int, or float
                  "Energy threshold for seeding in ECAL EB")
options.register ('EBseedPt',
                  1.0, # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.float,          # string, int, or float
                  "Pt threshold for seeding in ECAL EB")
options.register ('EEseed',
                  1.0, # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.float,          # string, int, or float
                  "Energy threshold for seeding in ECAL EE")
options.register ('EEseedPt',
                  1.0, # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.float,          # string, int, or float
                  "Pt threshold for seeding in ECAL EE")
options.register ('EBgather',
                  1.0, # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.float,          # string, int, or float
                  "Energy threshold for gathering in ECAL EB")
options.register ('EBgatherPt',
                  1.0, # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.float,          # string, int, or float
                  "Pt threshold for gathering in ECAL EB")
options.register ('EEgather',
                  1.0, # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.float,          # string, int, or float
                  "Energy threshold for gathering in ECAL EE")
options.register ('EEgatherPt',
                  1.0, # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.float,          # string, int, or float
                  "Pt threshold for gathering in ECAL EE")

options.parseArguments()

import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.ErA)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.RecoSim_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(NeventS)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:FragmenT_GEN_SIM_DIGI.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:NeventS'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:FragmenT_GEN_SIM_DIGI_RECO.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'ConditionS', '')


### MG: override several tags to new noise conditions
process.GlobalTag.toGet = cms.VPSet(
  cms.PSet(record = cms.string('EcalLaserAPDPNRatiosRcd'),
           tag = cms.string('EcalLaserAPDPNRatios_TL180fb_v1_mc'),
           ),
  cms.PSet(record = cms.string('EcalPedestalsRcd'),
           tag = cms.string('EcalPedestals_TL180fb_Model190fb_mc'), # obtained from model, like 450/fb
           ),
  cms.PSet(record = cms.string("EcalSRSettingsRcd"),
           tag = cms.string('EcalSRSettings_TL180fb_v1_mc'),
           ),
  cms.PSet(record = cms.string('EcalIntercalibConstantsMCRcd'),
           tag = cms.string('EcalIntercalibConstantsMC_TL180fb_v1_mc'),
           ),
  cms.PSet(record = cms.string('EcalTPGLinearizationConstRcd'),
           tag = cms.string('EcalTPGLinearizationConst_TL180fb_v1_mc'),
           ),
  cms.PSet(record = cms.string('EcalTPGPedestalsRcd'),
           tag = cms.string('EcalTPGPedestals_TL180fb_v1_mc'),
           ),
  cms.PSet(record = cms.string('EcalPFRecHitThresholdsRcd'),
           tag = cms.string('EcalPFRecHitThresholds_UL_2018_2e3sig'),
           ),
)
### end override

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)

# modify parameters in reconstruction
process.particleFlowClusterECALUncorrected.seedFinder.thresholdsByDetector = cms.VPSet(
        cms.PSet( detector = cms.string("ECAL_BARREL"),
               seedingThreshold = cms.double(0.12*options.EBseed),
               seedingThresholdPt = cms.double(0.0*options.EBseedPt)
               ),
        cms.PSet( detector = cms.string("ECAL_ENDCAP"),
               seedingThreshold = cms.double(0.50*options.EEseed),
               seedingThresholdPt = cms.double(0.15*options.EEseedPt)
               )
)
process.particleFlowClusterECALUncorrected.initialClusteringStep.thresholdsByDetector = cms.VPSet(
        cms.PSet( detector = cms.string("ECAL_BARREL"),
               gatheringThreshold = cms.double(0.08*options.EBgather), # with these values they are doing nothing 
               gatheringThresholdPt = cms.double(0.0*options.EBgatherPt) # with these values they are doing nothing
               ),
        cms.PSet( detector = cms.string("ECAL_ENDCAP"),
               gatheringThreshold = cms.double(0.30*options.EEgather), # with these values they are doing very little
               gatheringThresholdPt = cms.double(0.0*options.EEgatherPt) # with these values they are doing very little
               )
)



process.recosim_step = cms.Path(process.recosim)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.recosim_step,process.endjob_step,process.RECOSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)

# Customisation from command line
process.MessageLogger.cerr.FwkReport.reportEvery=1000;

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
