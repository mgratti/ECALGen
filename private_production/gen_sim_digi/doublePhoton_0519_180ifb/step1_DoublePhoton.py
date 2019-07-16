# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: DoublePhoton.py --conditions 105X_upgrade2018_realistic_v3 --geometry DB:ExtendedZeroMaterial --beamspot Realistic25ns13TeVEarly2017Collision --era Run2_2018 --pileup NoPileUp --step GEN,SIM --datatier GEN-SIM --eventcontent FEVTDEBUG --fileout file:DoublePhoton_GEN_SIM.root -n 50 --python_filename step1_DoublePhoton.py --nThreads 8 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('SIM',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2017Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(150)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('DoublePhoton.py nevts:50'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:EGM_GEN_SIM.root'),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("ExtendedZeroMaterial")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '105X_upgrade2018_realistic_v3', '')

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



process.generator = cms.EDProducer("FlatRandomPtGunProducer",
    AddAntiParticle = cms.bool(True),
    PGunParameters = cms.PSet(
        MaxEta = cms.double(3.1),
        MaxPhi = cms.double(3.14159265359),
        MaxPt = cms.double(100.0),
        MinEta = cms.double(-3.1),
        MinPhi = cms.double(-3.14159265359),
        MinPt = cms.double(1),
        PartID = cms.vint32(22)
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('double photon pt 1 to 10o')
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.FEVTDEBUGoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded 
process.options.numberOfThreads=cms.untracked.uint32(8) 
#will run on 8 nods
process.options.numberOfStreams=cms.untracked.uint32(0) 
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1) 
 
# Customisation from command line 
process.MessageLogger.cerr.FwkReport.reportEvery=1000; 

# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.generator)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
