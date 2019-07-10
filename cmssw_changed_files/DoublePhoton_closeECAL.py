import FWCore.ParameterSet.Config as cms



generator = cms.EDProducer("CloseByParticleGunProducer",
     PGunParameters = cms.PSet(PartID = cms.vint32(22, 22),
       NParticles = cms.int32(2),
       EnMin = cms.double(1),
       EnMax = cms.double(100.),
       RMin = cms.double(0.),
       RMax = cms.double(300.),
       ZMin = cms.double(0.),
       ZMax = cms.double(200.),
       Delta = cms.double(100),
       Pointing = cms.bool(True),
       Overlapping = cms.bool(False),
       RandomShoot = cms.bool(False),
       MaxEta = cms.double(3.),
       MaxPhi = cms.double(3.14159265359),
       MinEta = cms.double(-3.),
       MinPhi = cms.double(-3.14159265359),
     ),
     Verbosity = cms.untracked.int32(10),
     psethack = cms.string('two close by particles'),
     AddAntiParticle = cms.bool(False),
     firstRun = cms.untracked.uint32(1)
)
                                                                                                                                                            
