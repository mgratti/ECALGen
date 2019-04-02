# Overriding tags og a global tag
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions#Customization_of_Global_Tags

# First set is 180/fb

### MG: override several tags to new noise conditions
process.GlobalTag.toGet = cms.VPSet(
  cms.PSet(record = cms.string('EcalLaserAPDPNRatiosRcd'),
           tag = cms.string('EcalLaserAPDPNRatios_TL180fb_v1_mc'),
           ),
  cms.PSet(record = cms.string('EcalPedestalsRcd'),
           tag = cms.string('EcalPedestals_TL180fb_v1_mc'),
           ),
  cms.PSet(record = cms.string('EcalSRSettingsRcd'),
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
)
### end override


# Second set is 450/fb

### MG: override several tags to new noise conditions
process.GlobalTag.toGet = cms.VPSet(
  cms.PSet(record = cms.string('EcalLaserAPDPNRatiosRcd'),
           tag = cms.string('EcalLaserAPDPNRatios_TL450fb_v1cor_mc'),
           ),
  cms.PSet(record = cms.string('EcalPedestalsRcd'),
           tag = cms.string('EcalPedestals_TL450fb_v1_mc'),
           ),
  cms.PSet(record = cms.string('EcalSRSettingsRcd'),
           tag = cms.string('EcalSRSettings_TL450fb_v1_mc'),
           ),
  cms.PSet(record = cms.string('EcalIntercalibConstantsMCRcd'),
           tag = cms.string('EcalIntercalibConstantsMC_TL450fb_v1_mc'),
           ),
  cms.PSet(record = cms.string('EcalTPGLinearizationConstRcd'),
           tag = cms.string('EcalTPGLinearizationConst_TL450fb_v1cor_mc'),
           ),
  cms.PSet(record = cms.string('EcalTPGPedestalsRcd'),
           tag = cms.string('EcalTPGPedestals_TL450fb_v1cor_mc'),
           ),
)
### end override

