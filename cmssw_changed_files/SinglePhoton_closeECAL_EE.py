#https://cmssdt.cern.ch/lxr/source/IOMC/ParticleGuns/src/CloseByParticleGunProducer.cc

import FWCore.ParameterSet.Config as cms


process.generator = cms.EDProducer("CloseByParticleGunProducer",
                                     PGunParameters = cms.PSet(PartID = cms.vint32(22, 22),
                                       NParticles = cms.int32(1),
                                       EnMin = cms.double(1.),   # in GeV
                                       EnMax = cms.double(100.),
                                       RMin = cms.double(31.6),  # in cm
                                       RMax = cms.double(171.1),
                                       ZMin = cms.double(317.0), # in cm
                                       ZMax = cms.double(317.0),
                                       Delta = cms.double(300),  # in cm  -> phi1-phi2 = Delta/R # for Nparticles=1 it is irrelevant 
                                       Pointing = cms.bool(True),# otherwise showers parallel/perpendicular to beam axis
                                       Overlapping = cms.bool(False),
                                       RandomShoot = cms.bool(False),
                                       MaxPhi = cms.double(3.14159265359),
                                       MinPhi = cms.double(-3.14159265359),
                                       MaxEta = cms.double(0.), # dummy, it is not used
                                       MinEta = cms.double(0.), # dummy, it is not used
                                       ),
                                     Verbosity = cms.untracked.int32(1),
                                     psethack = cms.string('two particles close to EE'),
                                     AddAntiParticle = cms.bool(False),
                                     firstRun = cms.untracked.uint32(1)
)


                                                                                                                                                            
