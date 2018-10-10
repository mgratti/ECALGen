import FWCore.ParameterSet.Config as cms


generator = cms.EDProducer("FlatRandomPtGunProducer",
    AddAntiParticle = cms.bool(True),
    PGunParameters = cms.PSet(
        MaxEta = cms.double(3.1),
        MaxPhi = cms.double(3.14159265359),
        MaxPt = cms.double(10.0),
        MinEta = cms.double(-3.1),
        MinPhi = cms.double(-3.14159265359),
        MinPt = cms.double(1),
        PartID = cms.vint32(11)
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('double electron pt 1 to 10')
)


