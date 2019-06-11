# Overriding tags on top of a global tag
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions#Customization_of_Global_Tags

# First set is 180/fb

### MG: override several tags to new noise conditions
process.GlobalTag.toGet = cms.VPSet(
  cms.PSet(record = cms.string('EcalLaserAPDPNRatiosRcd'),
           tag = cms.string('EcalLaserAPDPNRatios_TL180fb_v1_mc'),
           ),
  cms.PSet(record = cms.string('EcalPedestalsRcd'),
           tag = cms.string('EcalPedestals_TL180fb_Model190fb_mc'), # obtained from model, like 450/fb
           ),
  #cms.PSet(record = cms.string('EcalSRSettingsRcd'),
  #         tag = cms.string('EcalSRSettings_TL180fb_v1_mc'),
  #         ),
  cms.PSet(record = cms.string("EcalSRSettingsRcd"),
           tag = cms.string('EcalSRSettings_fullreadout_v01_mc'),
           connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
           ),
#  cms.PSet(record = cms.string('EcalIntercalibConstantsRcd'),
#           tag = cms.string('EcalIntercalibConstants_TL180fb_v1_mc'),
#           ),
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
           #tag = cms.string('EcalPFRecHitThresholds_2018_def_mc'), # 80/300 MeV
           tag = cms.string('EcalPFRecHitThresholds_UL_2018_2e3sig'),
           ),
  cms.PSet(record = cms.string('EcalADCToGeVConstantRcd'),
           tag = cms.string('EcalADCToGeVConstant_2010_V2_Bon_mc'),
           ),
  cms.PSet(record = cms.string('EcalLaserAlphasRcd'),
           tag = cms.string('EcalLaserAlphas_EB_sic1_btcp1_EE_sic1_btcp1'),
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
 # cms.PSet(record = cms.string('EcalSRSettingsRcd'),
 #          tag = cms.string('EcalSRSettings_TL450fb_v2_mc'),
 #          ),
  cms.PSet(record = cms.string("EcalSRSettingsRcd"),
           tag = cms.string('EcalSRSettings_fullreadout_v01_mc'),
           connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
           ), 
  cms.PSet(record = cms.string('EcalIntercalibConstantsMCRcd'),
           tag = cms.string('EcalIntercalibConstantsMC_TL450fb_v1_mc'),
           ),
#  cms.PSet(record = cms.string('EcalIntercalibConstantsRcd'),
#           tag = cms.string('EcalIntercalibConstants_TL450fb_v1_mc'),
#           ),
  cms.PSet(record = cms.string('EcalTPGLinearizationConstRcd'),
           tag = cms.string('EcalTPGLinearizationConst_TL450fb_v1cor_mc'),
           ),
  cms.PSet(record = cms.string('EcalTPGPedestalsRcd'),
           tag = cms.string('EcalTPGPedestals_TL450fb_v1cor_mc'),
           ),
  cms.PSet(record = cms.string('EcalPFRecHitThresholdsRcd'),
           #tag = cms.string('EcalPFRecHitThresholds_2018_def_mc'), # 80/300 MeV
           tag = cms.string('EcalPFRecHitThresholds_TL450_mixed'),
           ),
  cms.PSet(record = cms.string('EcalADCToGeVConstantRcd'),
           tag = cms.string('EcalADCToGeVConstant_2010_V2_Bon_mc'), # std for MC
           ),
  cms.PSet(record = cms.string('EcalLaserAlphasRcd'),
           tag = cms.string('EcalLaserAlphas_EB_sic1_btcp1_EE_sic1_btcp1'), # alpha = 1
           ),
)
### end override

# Third set is 550/fb

### MG: override several tags to new noise conditions
process.GlobalTag.toGet = cms.VPSet(
  cms.PSet(record = cms.string('EcalLaserAPDPNRatiosRcd'),
           tag = cms.string('EcalLaserAPDPNRatios_TL550fb_v1_mc'),
           ),
  cms.PSet(record = cms.string('EcalPedestalsRcd'),
           tag = cms.string('EcalPedestals_TL550fb_v1_mc'),
           ),
 # cms.PSet(record = cms.string('EcalSRSettingsRcd'),
 #          tag = cms.string('EcalSRSettings_TL550fb_v2_mc'),
 #          ),
  cms.PSet(record = cms.string("EcalSRSettingsRcd"),
           tag = cms.string('EcalSRSettings_fullreadout_v01_mc'),
           connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
           ), 
#  cms.PSet(record = cms.string('EcalIntercalibConstantsRcd'),
#           tag = cms.string('EcalIntercalibConstants_TL550fb_v1_mc'),
#           ),
  cms.PSet(record = cms.string('EcalIntercalibConstantsMCRcd'),
           tag = cms.string('EcalIntercalibConstantsMC_TL550fb_v1_mc'),
           ),
  cms.PSet(record = cms.string('EcalTPGLinearizationConstRcd'),
           tag = cms.string('EcalTPGLinearizationConst_TL550fb_mc'),
           ),
  cms.PSet(record = cms.string('EcalTPGPedestalsRcd'),
           tag = cms.string('EcalTPGPedestals_TL550fb_mc'),
           ),
  cms.PSet(record = cms.string('EcalPFRecHitThresholdsRcd'),
           #tag = cms.string('EcalPFRecHitThresholds_2018_def_mc'), # 80/300 MeV
           tag = cms.string('EcalPFRecHitThresholds_TL550_mixed'),
           ),
  cms.PSet(record = cms.string('EcalADCToGeVConstantRcd'),
           tag = cms.string('EcalADCToGeVConstant_2010_V2_Bon_mc'), # std for MC
           ),
  cms.PSet(record = cms.string('EcalLaserAlphasRcd'),
           tag = cms.string('EcalLaserAlphas_EB_sic1_btcp1_EE_sic1_btcp1'), # alpha = 1
           ),
)
### end override



