##### TO DO: check the parameters


import FWCore.ParameterSet.Config as cms


process.generator = cms.EDProducer("CloseByParticleGunProducer",
                                     PGunParameters = cms.PSet(PartID = cms.vint32(22, 22),
                                       NParticles = cms.int32(2),
                                       EnMin = cms.double(1.),   # in GeV
                                       EnMax = cms.double(100.),
                                       RMin = cms.double(123.8), # in cm
                                       RMax = cms.double(123.8),
                                       ZMin = cms.double(-304.5),    # in cm
                                       ZMax = cms.double(304.5),
                                       Delta = cms.double(300),  # in cm  -> phi1-phi2 = Delta/R 
                                       Pointing = cms.bool(True),# otherwise showers parallel/perpendicular to beam axis
                                       Overlapping = cms.bool(False),
                                       RandomShoot = cms.bool(False),
                                       MaxPhi = cms.double(3.14159265359),
                                       MinPhi = cms.double(-3.14159265359),
                                       MaxEta = cms.double(0.), # dummy, it is not used
                                       MinEta = cms.double(0.), # dummy, it is not used
                                       ),
                                     Verbosity = cms.untracked.int32(1),
                                     psethack = cms.string('two particles close to EB'),
                                     AddAntiParticle = cms.bool(False),
                                     firstRun = cms.untracked.uint32(1)
)


                                                                                                                                                            
