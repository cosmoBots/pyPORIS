from PORIS import *

class osirisPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysOsiris = PORISSys("Osiris")
        self.setRoot(self.sysOsiris)
        self.sysObservingModes = PORISSys("ObservingModes")
        self.sysAcquisitionModes = PORISSys("AcquisitionModes")
        self.sysFPE = PORISSys("FPE")
        self.prFocalPlaneElement = PORISParam("FocalPlaneElement")
        self.sysDAS = PORISSys("DAS")
        self.sysAcquisition = PORISSys("Acquisition")
        self.prShuffleLines = PORISParam("ShuffleLines")
        self.prShiftNumber = PORISParam("ShiftNumber")
        self.prExpTime = PORISParam("ExpTime")
        self.sysMultipleExposure = PORISSys("MultipleExposure")
        self.prnumOfFrames = PORISParam("numOfFrames")
        self.prPixelSpeed = PORISParam("PixelSpeed")
        self.prCalibGain = PORISParam("CalibGain")
        self.sysOpenShutter = PORISSys("OpenShutter")
        self.sysProcessMonitor = PORISSys("ProcessMonitor")
        self.prCurrentEllapsed = PORISParam("CurrentEllapsed")
        self.prCurrentImg = PORISParam("CurrentImg")
        self.prCurrentPct = PORISParam("CurrentPct")
        self.prOverallPct = PORISParam("OverallPct")
        self.sysPreOptics = PORISSys("PreOptics")
        self.prGrisms = PORISParam("Grisms")
        self.sysRedTF = PORISSys("RedTF")
        self.prRedFWHM = PORISParam("RedFWHM")
        self.prRedLamda = PORISParam("RedLamda")
        self.sysBlueTF = PORISSys("BlueTF")
        self.prBlueFWHM = PORISParam("BlueFWHM")
        self.prBlueLamda = PORISParam("BlueLamda")
        self.przzero = PORISParam("zzero")
        self.mdOsirisMode_Imaging = PORISMode("OsirisMode_Imaging")
        self.mdOsirisMode_Spectroscopy = PORISMode("OsirisMode_Spectroscopy")
        self.mdOsirisMode_Calibration = PORISMode("OsirisMode_Calibration")
        self.mdAcquisitionModesMode_aBBI = PORISMode("AcquisitionModesMode_aBBI")
        self.mdAcquisitionModesMode_aTFI = PORISMode("AcquisitionModesMode_aTFI")
        self.mdAcquisitionModesMode_aLSSpec = PORISMode("AcquisitionModesMode_aLSSpec")
        self.mdAcquisitionModesMode_aMOS = PORISMode("AcquisitionModesMode_aMOS")
        self.mdAcquisitionModesMode_aFastBBI = PORISMode("AcquisitionModesMode_aFastBBI")
        self.mdAcquisitionModesMode_aFrTrBBI = PORISMode("AcquisitionModesMode_aFrTrBBI")
        self.mdAcquisitionModesMode_aFastLSSpec = PORISMode("AcquisitionModesMode_aFastLSSpec")
        self.mdAcquisitionModesMode_aFastTFImage = PORISMode("AcquisitionModesMode_aFastTFImage")
        self.mdAcquisitionModesMode_aFrTrTFI = PORISMode("AcquisitionModesMode_aFrTrTFI")
        self.mdAcquisitionModesMode_aBias = PORISMode("AcquisitionModesMode_aBias")
        self.mdAcquisitionModesMode_aDark = PORISMode("AcquisitionModesMode_aDark")
        self.mdAcquisitionModesMode_aDomeFlat = PORISMode("AcquisitionModesMode_aDomeFlat")
        self.mdAcquisitionModesMode_aSkyFlat = PORISMode("AcquisitionModesMode_aSkyFlat")
        self.mdAcquisitionModesMode_aSpectralFlat = PORISMode("AcquisitionModesMode_aSpectralFlat")
        self.mdAcquisitionModesMode_aCalibLamp = PORISMode("AcquisitionModesMode_aCalibLamp")
        self.mdAcquisitionModesMode_aTFCalib = PORISMode("AcquisitionModesMode_aTFCalib")
        self.mdAcquisitionModesMode_Throughslit = PORISMode("AcquisitionModesMode_Throughslit")
        self.mdObservingModesMode_BBI = PORISMode("ObservingModesMode_BBI")
        self.mdObservingModesMode_TFI = PORISMode("ObservingModesMode_TFI")
        self.mdObservingModesMode_LSSpec = PORISMode("ObservingModesMode_LSSpec")
        self.mdObservingModesMode_MOS = PORISMode("ObservingModesMode_MOS")
        self.mdObservingModesMode_FastBBI = PORISMode("ObservingModesMode_FastBBI")
        self.mdObservingModesMode_FrTrBBI = PORISMode("ObservingModesMode_FrTrBBI")
        self.mdObservingModesMode_FastLSSpec = PORISMode("ObservingModesMode_FastLSSpec")
        self.mdObservingModesMode_FastTFImage = PORISMode("ObservingModesMode_FastTFImage")
        self.mdObservingModesMode_FrTrTFI = PORISMode("ObservingModesMode_FrTrTFI")
        self.mdObservingModesMode_Bias = PORISMode("ObservingModesMode_Bias")
        self.mdObservingModesMode_Dark = PORISMode("ObservingModesMode_Dark")
        self.mdObservingModesMode_DomeFlat = PORISMode("ObservingModesMode_DomeFlat")
        self.mdObservingModesMode_SkyFlat = PORISMode("ObservingModesMode_SkyFlat")
        self.mdObservingModesMode_SpectralFlat = PORISMode("ObservingModesMode_SpectralFlat")
        self.mdObservingModesMode_CalibLamp = PORISMode("ObservingModesMode_CalibLamp")
        self.mdObservingModesMode_TFCalib = PORISMode("ObservingModesMode_TFCalib")
        self.sysFilters = PORISSys("Filters")
        self.prUFilters = PORISParam("UFilters")
        self.prOS = PORISParam("OS")
        self.prBroad = PORISParam("Broad")
        self.mdFocalPlaneElementMode_Disabled = PORISMode("FocalPlaneElementMode_Disabled")
        self.vlFocalPlaneElement_LS0_4 = PORISValue("FocalPlaneElement_LS0_4")
        self.vlFocalPlaneElement_LS0_6 = PORISValue("FocalPlaneElement_LS0_6")
        self.vlFocalPlaneElement_LS0_8 = PORISValue("FocalPlaneElement_LS0_8")
        self.vlFocalPlaneElement_LS1_0 = PORISValue("FocalPlaneElement_LS1_0")
        self.vlFocalPlaneElement_LS1_2 = PORISValue("FocalPlaneElement_LS1_2")
        self.vlFocalPlaneElement_LS1_5 = PORISValue("FocalPlaneElement_LS1_5")
        self.vlFocalPlaneElement_LS1_8 = PORISValue("FocalPlaneElement_LS1_8")
        self.vlFocalPlaneElement_LS2_5 = PORISValue("FocalPlaneElement_LS2_5")
        self.vlFocalPlaneElement_LS3_0 = PORISValue("FocalPlaneElement_LS3_0")
        self.vlFocalPlaneElement_LS5_0 = PORISValue("FocalPlaneElement_LS5_0")
        self.vlFocalPlaneElement_LS10_0 = PORISValue("FocalPlaneElement_LS10_0")
        self.vlFocalPlaneElement_LS12_0 = PORISValue("FocalPlaneElement_LS12_0")
        self.vlFocalPlaneElement_LS40_0 = PORISValue("FocalPlaneElement_LS40_0")
        self.mdFocalPlaneElementMode_MOS = PORISMode("FocalPlaneElementMode_MOS")
        self.mdFocalPlaneElementMode_FastPhotometry = PORISMode("FocalPlaneElementMode_FastPhotometry")
        self.mdFocalPlaneElementMode_FrameTransfer = PORISMode("FocalPlaneElementMode_FrameTransfer")
        self.mdFocalPlaneElementMode_LS = PORISMode("FocalPlaneElementMode_LS")
        self.vlFocalPlaneElement_FrameTransferMask = PORISValue("FocalPlaneElement_FrameTransferMask")
        self.vlFocalPlaneElement_FastPhotometryMask = PORISValue("FocalPlaneElement_FastPhotometryMask")
        self.vlFocalPlaneElement_MOSmask = PORISValue("FocalPlaneElement_MOSmask")
        self.vlFocalPlaneElement_NoFPE = PORISValue("FocalPlaneElement_NoFPE")
        self.mdFPEMode_NoFPE = PORISMode("FPEMode_NoFPE")
        self.mdFPEMode_MOSmask = PORISMode("FPEMode_MOSmask")
        self.mdFPEMode_FastPhotometryMask = PORISMode("FPEMode_FastPhotometryMask")
        self.mdFPEMode_FrameTransferMask = PORISMode("FPEMode_FrameTransferMask")
        self.mdFPEMode_LSMask = PORISMode("FPEMode_LSMask")
        self.sysDetector = PORISSys("Detector")
        self.sysOutputSource = PORISSys("OutputSource")
        self.sysRecomposition = PORISSys("Recomposition")
        self.prBinning = PORISParam("Binning")
        self.sysWindow = PORISSys("Window")
        self.prRows = PORISParam("Rows")
        self.prCols = PORISParam("Cols")
        self.proffsetRow = PORISParam("offsetRow")
        self.proffsetCol = PORISParam("offsetCol")
        self.mdAcquisitionMode_Normal = PORISMode("AcquisitionMode_Normal")
        self.mdAcquisitionMode_FrameTransfer = PORISMode("AcquisitionMode_FrameTransfer")
        self.mdAcquisitionMode_Shuffling = PORISMode("AcquisitionMode_Shuffling")
        self.vlShuffleLines_FullRange = PORISValueFloat("ShuffleLines_FullRange",0.0,200.0,1000.0)
        self.mdShuffleLinesMode_Normal = PORISMode("ShuffleLinesMode_Normal")
        self.vlShiftNumber_FullRange = PORISValueFloat("ShiftNumber_FullRange",0.0,5.0,1000.0)
        self.mdShiftNumberMode_Normal = PORISMode("ShiftNumberMode_Normal")
        self.vlExpTime_FullRange = PORISValueFloat("ExpTime_FullRange",0.0,1.0,10000.0)
        self.mdExpTimeMode_Normal = PORISMode("ExpTimeMode_Normal")
        self.mdExpTimeMode_Bias = PORISMode("ExpTimeMode_Bias")
        self.vlExpTime_0_0 = PORISValue("ExpTime_0_0")
        self.mdExpTimeMode_FT = PORISMode("ExpTimeMode_FT")
        self.vlExpTime_FTRange = PORISValueFloat("ExpTime_FTRange",0.0,0.0,360.0)
        self.mdnumOfFramesMode_Normal = PORISMode("numOfFramesMode_Normal")
        self.vlnumOfFrames_FullRange = PORISValueFloat("numOfFrames_FullRange",0.0,10.0,4294967295.0)
        self.mdMultipleExposureMode_On = PORISMode("MultipleExposureMode_On")
        self.mdMultipleExposureMode_Single = PORISMode("MultipleExposureMode_Single")
        self.vlPixelSpeed_SLW = PORISValue("PixelSpeed_SLW")
        self.vlPixelSpeed_MED = PORISValue("PixelSpeed_MED")
        self.vlPixelSpeed_FST = PORISValue("PixelSpeed_FST")
        self.mdPixelSpeedMode_All = PORISMode("PixelSpeedMode_All")
        self.mdAcquisitionMode_FTBias = PORISMode("AcquisitionMode_FTBias")
        self.mdAcquisitionMode_NormalBias = PORISMode("AcquisitionMode_NormalBias")
        self.mdAcquisitionMode_ShufflingBias = PORISMode("AcquisitionMode_ShufflingBias")
        self.mdAcquisitionMode_NormalSquare = PORISMode("AcquisitionMode_NormalSquare")
        self.mdAcquisitionMode_ShufflingSquare = PORISMode("AcquisitionMode_ShufflingSquare")
        self.mdAcquisitionMode_GainCalib = PORISMode("AcquisitionMode_GainCalib")
        self.vlCalibGain_FullRange = PORISValueFloat("CalibGain_FullRange",0.0,2.0,15.0)
        self.mdCalibGainMode_Normal = PORISMode("CalibGainMode_Normal")
        self.mdDASMode_SimpleImg = PORISMode("DASMode_SimpleImg")
        self.mdDASMode_SimpleSpec = PORISMode("DASMode_SimpleSpec")
        self.mdDASMode_ShufffingSpec = PORISMode("DASMode_ShufffingSpec")
        self.mdOpenShutterMode_On = PORISMode("OpenShutterMode_On")
        self.mdOpenShutterMode_Off = PORISMode("OpenShutterMode_Off")
        self.mdDASMode_FTImg = PORISMode("DASMode_FTImg")
        self.mdDASMode_FTDark = PORISMode("DASMode_FTDark")
        self.mdDASMode_FTBias = PORISMode("DASMode_FTBias")
        self.mdDASMode_SimpleBias = PORISMode("DASMode_SimpleBias")
        self.mdDASMode_SimpleDark = PORISMode("DASMode_SimpleDark")
        self.mdDASMode_ShufffingDark = PORISMode("DASMode_ShufffingDark")
        self.mdDASMode_ShufffingBias = PORISMode("DASMode_ShufffingBias")
        self.mdDASMode_ShufffingImage = PORISMode("DASMode_ShufffingImage")
        self.mdDASMode_SimpleCalib = PORISMode("DASMode_SimpleCalib")
        self.mdDASMode_GainCalib = PORISMode("DASMode_GainCalib")
        self.vlCurrentEllapsed_Range = PORISValueFloat("CurrentEllapsed_Range",0.0,0.0,10000.0)
        self.mdCurrentEllapsedMode_Normal = PORISMode("CurrentEllapsedMode_Normal")
        self.vlCurrentImg_Range = PORISValueFloat("CurrentImg_Range",0.0,0.0,10000.0)
        self.mdCurrentImgMode_Normal = PORISMode("CurrentImgMode_Normal")
        self.vlCurrentPct_Range = PORISValueFloat("CurrentPct_Range",0.0,0.0,100.0)
        self.mdCurrentPctMode_Normal = PORISMode("CurrentPctMode_Normal")
        self.vlOverallPct_Range = PORISValueFloat("OverallPct_Range",0.0,0.0,100.0)
        self.mdOverallPctMode_Normal = PORISMode("OverallPctMode_Normal")
        self.mdProcessMonitorMode_Normal = PORISMode("ProcessMonitorMode_Normal")
        self.mdPreOpticsMode_NoDispersion = PORISMode("PreOpticsMode_NoDispersion")
        self.mdPreOpticsMode_RTF = PORISMode("PreOpticsMode_RTF")
        self.mdPreOpticsMode_GrismR = PORISMode("PreOpticsMode_GrismR")
        self.mdPreOpticsMode_BTF = PORISMode("PreOpticsMode_BTF")
        self.vlGrisms_R300B = PORISValue("Grisms_R300B")
        self.vlGrisms_R300R = PORISValue("Grisms_R300R")
        self.vlGrisms_R500B = PORISValue("Grisms_R500B")
        self.vlGrisms_R500R = PORISValue("Grisms_R500R")
        self.vlGrisms_R1000B = PORISValue("Grisms_R1000B")
        self.vlGrisms_R1000R = PORISValue("Grisms_R1000R")
        self.vlGrisms_R2000B = PORISValue("Grisms_R2000B")
        self.vlGrisms_R2500U = PORISValue("Grisms_R2500U")
        self.vlGrisms_R2500V = PORISValue("Grisms_R2500V")
        self.vlGrisms_R2500R = PORISValue("Grisms_R2500R")
        self.vlGrisms_R2500I = PORISValue("Grisms_R2500I")
        self.mdGrismsMode_GrismsB = PORISMode("GrismsMode_GrismsB")
        self.mdGrismsMode_GrismsR = PORISMode("GrismsMode_GrismsR")
        self.mdPreOpticsMode_GrismB = PORISMode("PreOpticsMode_GrismB")
        self.mdPreOpticsMode_GrismBMOS = PORISMode("PreOpticsMode_GrismBMOS")
        self.vlRedFWHM_Range2_0 = PORISValueFloat("RedFWHM_Range2_0",1.2,1.6,2.0)
        self.mdRedFWHMMode_l2_0 = PORISMode("RedFWHMMode_l2_0")
        self.mdRedFWHMMode_l1_5 = PORISMode("RedFWHMMode_l1_5")
        self.mdRedFWHMMode_l1_4 = PORISMode("RedFWHMMode_l1_4")
        self.mdRedFWHMMode_l1_3 = PORISMode("RedFWHMMode_l1_3")
        self.mdRedFWHMMode_l1_2 = PORISMode("RedFWHMMode_l1_2")
        self.mdRedFWHMMode_l1_2b = PORISMode("RedFWHMMode_l1_2b")
        self.vlRedFWHM_Range1_5 = PORISValueFloat("RedFWHM_Range1_5",1.0,1.25,1.5)
        self.vlRedFWHM_Range1_4 = PORISValueFloat("RedFWHM_Range1_4",0.9,1.2,1.4)
        self.vlRedFWHM_Range1_3 = PORISValueFloat("RedFWHM_Range1_3",0.8,1.1,1.3)
        self.vlRedFWHM_Range1_2 = PORISValueFloat("RedFWHM_Range1_2",0.85,1.0,1.2)
        self.vlRedFWHM_Range1_2b = PORISValueFloat("RedFWHM_Range1_2b",0.9,1.0,1.2)
        self.mdRedTFMode_l651_799 = PORISMode("RedTFMode_l651_799")
        self.mdRedTFMode_l800_819 = PORISMode("RedTFMode_l800_819")
        self.mdRedTFMode_l820_839 = PORISMode("RedTFMode_l820_839")
        self.mdRedTFMode_l840_879 = PORISMode("RedTFMode_l840_879")
        self.mdRedTFMode_l880_909 = PORISMode("RedTFMode_l880_909")
        self.mdRedTFMode_l910_934 = PORISMode("RedTFMode_l910_934")
        self.vlRedLamda_Range651 = PORISValueFloat("RedLamda_Range651",651.0,700.0,799.9)
        self.mdRedLamdaMode_l651_799 = PORISMode("RedLamdaMode_l651_799")
        self.mdRedLamdaMode_l800_819 = PORISMode("RedLamdaMode_l800_819")
        self.mdRedLamdaMode_l820_839 = PORISMode("RedLamdaMode_l820_839")
        self.mdRedLamdaMode_l840_879 = PORISMode("RedLamdaMode_l840_879")
        self.mdRedLamdaMode_l880_909 = PORISMode("RedLamdaMode_l880_909")
        self.mdRedLamdaMode_l910_934 = PORISMode("RedLamdaMode_l910_934")
        self.vlRedLamda_Range800 = PORISValueFloat("RedLamda_Range800",800.0,810.0,819.9)
        self.vlRedLamda_Range820 = PORISValueFloat("RedLamda_Range820",820.0,830.0,839.9)
        self.vlRedLamda_Range840 = PORISValueFloat("RedLamda_Range840",840.0,860.0,879.9)
        self.vlRedLamda_Range880 = PORISValueFloat("RedLamda_Range880",880.0,895.0,909.9)
        self.vlRedLamda_Range910 = PORISValueFloat("RedLamda_Range910",910.0,920.0,934.5)
        self.vlBlueFWHM_0_8 = PORISValue("BlueFWHM_0_8")
        self.mdBlueFWHMMode_l0_8 = PORISMode("BlueFWHMMode_l0_8")
        self.mdBlueFWHMMode_l0_85 = PORISMode("BlueFWHMMode_l0_85")
        self.mdBlueFWHMMode_l0_50 = PORISMode("BlueFWHMMode_l0_50")
        self.mdBlueFWHMMode_l0_45 = PORISMode("BlueFWHMMode_l0_45")
        self.vlBlueFWHM_0_85 = PORISValue("BlueFWHM_0_85")
        self.vlBlueFWHM_0_50 = PORISValue("BlueFWHM_0_50")
        self.vlBlueFWHM_0_45 = PORISValue("BlueFWHM_0_45")
        self.vlBlueFWHM_0_70 = PORISValue("BlueFWHM_0_70")
        self.mdBlueFWHMMode_l0_70 = PORISMode("BlueFWHMMode_l0_70")
        self.mdBlueFWHMMode_l0_90 = PORISMode("BlueFWHMMode_l0_90")
        self.mdBlueFWHMMode_l1_10 = PORISMode("BlueFWHMMode_l1_10")
        self.vlBlueFWHM_0_90 = PORISValue("BlueFWHM_0_90")
        self.vlBlueFWHM_1_10 = PORISValue("BlueFWHM_1_10")
        self.mdBlueTFMode_l448_463 = PORISMode("BlueTFMode_l448_463")
        self.mdBlueTFMode_l464_480 = PORISMode("BlueTFMode_l464_480")
        self.mdBlueTFMode_l481_502 = PORISMode("BlueTFMode_l481_502")
        self.mdBlueTFMode_l503_521 = PORISMode("BlueTFMode_l503_521")
        self.mdBlueTFMode_l522_542 = PORISMode("BlueTFMode_l522_542")
        self.mdBlueTFMode_l543_583 = PORISMode("BlueTFMode_l543_583")
        self.vlBlueLamda_Range448 = PORISValueFloat("BlueLamda_Range448",448.0,454.0,463.9)
        self.mdBlueLamdaMode_l448_463 = PORISMode("BlueLamdaMode_l448_463")
        self.mdBlueLamdaMode_l464_480 = PORISMode("BlueLamdaMode_l464_480")
        self.mdBlueLamdaMode_l481_502 = PORISMode("BlueLamdaMode_l481_502")
        self.mdBlueLamdaMode_l503_521 = PORISMode("BlueLamdaMode_l503_521")
        self.mdBlueLamdaMode_l522_542 = PORISMode("BlueLamdaMode_l522_542")
        self.mdBlueLamdaMode_l543_583 = PORISMode("BlueLamdaMode_l543_583")
        self.vlBlueLamda_Range464 = PORISValueFloat("BlueLamda_Range464",464.0,472.0,480.9)
        self.vlBlueLamda_Range481 = PORISValueFloat("BlueLamda_Range481",481.0,492.0,502.9)
        self.vlBlueLamda_Range503 = PORISValueFloat("BlueLamda_Range503",503.0,514.0,521.9)
        self.vlBlueLamda_Range522 = PORISValueFloat("BlueLamda_Range522",522.0,536.0,542.9)
        self.vlBlueLamda_Range543 = PORISValueFloat("BlueLamda_Range543",543.0,565.0,583.9)
        self.mdBlueLamdaMode_l584_609 = PORISMode("BlueLamdaMode_l584_609")
        self.mdBlueLamdaMode_l610_637 = PORISMode("BlueLamdaMode_l610_637")
        self.mdBlueLamdaMode_l638_671 = PORISMode("BlueLamdaMode_l638_671")
        self.vlBlueLamda_Range584 = PORISValueFloat("BlueLamda_Range584",584.0,602.0,609.9)
        self.vlBlueLamda_Range610 = PORISValueFloat("BlueLamda_Range610",610.0,622.0,637.9)
        self.vlBlueLamda_Range638 = PORISValueFloat("BlueLamda_Range638",638.0,654.0,671.0)
        self.mdBlueTFMode_l584_609 = PORISMode("BlueTFMode_l584_609")
        self.mdBlueTFMode_l610_637 = PORISMode("BlueTFMode_l610_637")
        self.mdBlueTFMode_l638_671 = PORISMode("BlueTFMode_l638_671")
        self.mdPreOpticsMode_RTFCalib = PORISMode("PreOpticsMode_RTFCalib")
        self.mdPreOpticsMode_BTFCalib = PORISMode("PreOpticsMode_BTFCalib")
        self.vlzzero_NormalRange = PORISValueFloat("zzero_NormalRange",25000.0,29000.0,45000.0)
        self.mdzzeroMode_Normal = PORISMode("zzeroMode_Normal")
        self.mdFiltersMode_OS = PORISMode("FiltersMode_OS")
        self.mdFiltersMode_UFilter = PORISMode("FiltersMode_UFilter")
        self.vlUFilters_U500_17 = PORISValue("UFilters_U500_17")
        self.vlUFilters_U517_17 = PORISValue("UFilters_U517_17")
        self.vlUFilters_U534_17 = PORISValue("UFilters_U534_17")
        self.vlUFilters_U551_17 = PORISValue("UFilters_U551_17")
        self.vlUFilters_U568_17 = PORISValue("UFilters_U568_17")
        self.vlUFilters_U585_17 = PORISValue("UFilters_U585_17")
        self.vlUFilters_U602_17 = PORISValue("UFilters_U602_17")
        self.vlUFilters_U619_17 = PORISValue("UFilters_U619_17")
        self.vlUFilters_U636_17 = PORISValue("UFilters_U636_17")
        self.vlUFilters_U653_17 = PORISValue("UFilters_U653_17")
        self.vlUFilters_U670_17 = PORISValue("UFilters_U670_17")
        self.vlUFilters_U687_17 = PORISValue("UFilters_U687_17")
        self.vlUFilters_U704_17 = PORISValue("UFilters_U704_17")
        self.vlUFilters_U721_17 = PORISValue("UFilters_U721_17")
        self.vlUFilters_U738_17 = PORISValue("UFilters_U738_17")
        self.vlUFilters_U755_17 = PORISValue("UFilters_U755_17")
        self.vlUFilters_U772_17 = PORISValue("UFilters_U772_17")
        self.vlUFilters_U789_17 = PORISValue("UFilters_U789_17")
        self.vlUFilters_U806_17 = PORISValue("UFilters_U806_17")
        self.vlUFilters_U823_17 = PORISValue("UFilters_U823_17")
        self.vlUFilters_U840_17 = PORISValue("UFilters_U840_17")
        self.vlUFilters_U857_17 = PORISValue("UFilters_U857_17")
        self.vlUFilters_U883_35 = PORISValue("UFilters_U883_35")
        self.vlUFilters_U913_25 = PORISValue("UFilters_U913_25")
        self.vlUFilters_U941_33 = PORISValue("UFilters_U941_33")
        self.mdUFiltersMode_U5xx = PORISMode("UFiltersMode_U5xx")
        self.mdUFiltersMode_U6xx = PORISMode("UFiltersMode_U6xx")
        self.mdUFiltersMode_U7xx = PORISMode("UFiltersMode_U7xx")
        self.mdUFiltersMode_U8xx = PORISMode("UFiltersMode_U8xx")
        self.mdUFiltersMode_U9xx = PORISMode("UFiltersMode_U9xx")
        self.vlOS_f504_16 = PORISValue("OS_f504_16")
        self.vlOS_f509_16 = PORISValue("OS_f509_16")
        self.vlOS_f514_16 = PORISValue("OS_f514_16")
        self.vlOS_f519_16 = PORISValue("OS_f519_16")
        self.vlOS_f525_17 = PORISValue("OS_f525_17")
        self.vlOS_f530_17 = PORISValue("OS_f530_17")
        self.vlOS_f536_17 = PORISValue("OS_f536_17")
        self.vlOS_f542_18 = PORISValue("OS_f542_18")
        self.vlOS_f548_18 = PORISValue("OS_f548_18")
        self.vlOS_f554_18 = PORISValue("OS_f554_18")
        self.vlOS_f561_19 = PORISValue("OS_f561_19")
        self.vlOS_f568_19 = PORISValue("OS_f568_19")
        self.vlOS_f575_19 = PORISValue("OS_f575_19")
        self.vlOS_f583_20 = PORISValue("OS_f583_20")
        self.vlOS_f591_21 = PORISValue("OS_f591_21")
        self.vlOS_f599_22 = PORISValue("OS_f599_22")
        self.mdOSMode_f5xx = PORISMode("OSMode_f5xx")
        self.vlOS_f477_14 = PORISValue("OS_f477_14")
        self.vlOS_f481_14 = PORISValue("OS_f481_14")
        self.mdOSMode_f4xx = PORISMode("OSMode_f4xx")
        self.vlOS_f486_14 = PORISValue("OS_f486_14")
        self.vlOS_f469_14 = PORISValue("OS_f469_14")
        self.vlOS_f461_13 = PORISValue("OS_f461_13")
        self.vlOS_f499_15 = PORISValue("OS_f499_15")
        self.vlOS_f454_13 = PORISValue("OS_f454_13")
        self.vlOS_f451_13 = PORISValue("OS_f451_13")
        self.vlOS_f495_15 = PORISValue("OS_f495_15")
        self.vlOS_f465_13 = PORISValue("OS_f465_13")
        self.vlOS_f490_15 = PORISValue("OS_f490_15")
        self.vlOS_f458_13 = PORISValue("OS_f458_13")
        self.vlOS_f473_14 = PORISValue("OS_f473_14")
        self.vlOS_f638_25 = PORISValue("OS_f638_25")
        self.vlOS_f680_43 = PORISValue("OS_f680_43")
        self.vlOS_f608_22 = PORISValue("OS_f608_22")
        self.vlOS_f627_24 = PORISValue("OS_f627_24")
        self.vlOS_f694_44 = PORISValue("OS_f694_44")
        self.vlOS_f617_23 = PORISValue("OS_f617_23")
        self.vlOS_f666_36 = PORISValue("OS_f666_36")
        self.vlOS_f649_25 = PORISValue("OS_f649_25")
        self.vlOS_f657_35 = PORISValue("OS_f657_35")
        self.mdOSMode_f6xx = PORISMode("OSMode_f6xx")
        self.vlOS_f661_27 = PORISValue("OS_f661_27")
        self.vlOS_f723_45 = PORISValue("OS_f723_45")
        self.mdOSMode_f7xx = PORISMode("OSMode_f7xx")
        self.vlOS_f770_50 = PORISValue("OS_f770_50")
        self.vlOS_f738_49 = PORISValue("OS_f738_49")
        self.vlOS_f709_45 = PORISValue("OS_f709_45")
        self.vlOS_f754_50 = PORISValue("OS_f754_50")
        self.vlOS_f785_48 = PORISValue("OS_f785_48")
        self.vlOS_f923_34 = PORISValue("OS_f923_34")
        self.mdOSMode_f9xx = PORISMode("OSMode_f9xx")
        self.vlOS_f932_34 = PORISValue("OS_f932_34")
        self.vlOS_f927_34 = PORISValue("OS_f927_34")
        self.vlOS_f902_44 = PORISValue("OS_f902_44")
        self.vlOS_f919_41 = PORISValue("OS_f919_41")
        self.vlOS_f910_40 = PORISValue("OS_f910_40")
        self.vlOS_f802_51 = PORISValue("OS_f802_51")
        self.vlOS_f878_59 = PORISValue("OS_f878_59")
        self.vlOS_f858_58 = PORISValue("OS_f858_58")
        self.vlOS_f893_50 = PORISValue("OS_f893_50")
        self.vlOS_f838_58 = PORISValue("OS_f838_58")
        self.vlOS_f819_52 = PORISValue("OS_f819_52")
        self.mdOSMode_f8xx = PORISMode("OSMode_f8xx")
        self.mdFiltersMode_NoFilter = PORISMode("FiltersMode_NoFilter")
        self.mdFiltersMode_GR = PORISMode("FiltersMode_GR")
        self.vlBroad_Sloan_u = PORISValue("Broad_Sloan_u")
        self.vlBroad_Sloan_g = PORISValue("Broad_Sloan_g")
        self.vlBroad_Sloan_r = PORISValue("Broad_Sloan_r")
        self.vlBroad_Sloan_i = PORISValue("Broad_Sloan_i")
        self.vlBroad_Sloan_z = PORISValue("Broad_Sloan_z")
        self.mdBroadMode_All = PORISMode("BroadMode_All")
        self.mdFiltersMode_Broad = PORISMode("FiltersMode_Broad")
        self.mdFiltersMode_OSCalc = PORISMode("FiltersMode_OSCalc")
        self.mdDetectorMode_FT = PORISMode("DetectorMode_FT")
        self.mdDetectorMode_Window = PORISMode("DetectorMode_Window")
        self.mdOutputSourceMode_0x0 = PORISMode("OutputSourceMode_0x0")
        self.mdOutputSourceMode_0x1 = PORISMode("OutputSourceMode_0x1")
        self.mdOutputSourceMode_0x2 = PORISMode("OutputSourceMode_0x2")
        self.mdOutputSourceMode_0x3 = PORISMode("OutputSourceMode_0x3")
        self.mdOutputSourceMode_ALL = PORISMode("OutputSourceMode_ALL")
        self.mdOutputSourceMode_TWO = PORISMode("OutputSourceMode_TWO")
        self.mdRecompositionMode_None = PORISMode("RecompositionMode_None")
        self.mdRecompositionMode_Serial = PORISMode("RecompositionMode_Serial")
        self.mdRecompositionMode_QuadCCD = PORISMode("RecompositionMode_QuadCCD")
        self.mdDetectorMode_FullDetector = PORISMode("DetectorMode_FullDetector")
        self.mdDetectorMode_WindowSq = PORISMode("DetectorMode_WindowSq")
        self.mdDetectorMode_FullDetectorSq = PORISMode("DetectorMode_FullDetectorSq")
        self.vlBinning_1x1 = PORISValue("Binning_1x1")
        self.vlBinning_1x2 = PORISValue("Binning_1x2")
        self.vlBinning_2x1 = PORISValue("Binning_2x1")
        self.vlBinning_2x2 = PORISValue("Binning_2x2")
        self.mdBinningMode_All = PORISMode("BinningMode_All")
        self.mdBinningMode_Square = PORISMode("BinningMode_Square")
        self.mdBinningMode_Off = PORISMode("BinningMode_Off")
        self.mdWindowMode_Enabled = PORISMode("WindowMode_Enabled")
        self.mdRowsMode_Normal = PORISMode("RowsMode_Normal")
        self.vlRows_FullRange = PORISValueFloat("Rows_FullRange",0.0,2056.0,4112.0)
        self.mdColsMode_Normal = PORISMode("ColsMode_Normal")
        self.vlCols_FullRange = PORISValueFloat("Cols_FullRange",0.0,2048.0,4096.0)
        self.mdoffsetRowMode_Normal = PORISMode("offsetRowMode_Normal")
        self.vloffsetRow_FullRange = PORISValueFloat("offsetRow_FullRange",0.0,1028.0,4112.0)
        self.mdoffsetColMode_Normal = PORISMode("offsetColMode_Normal")
        self.vloffsetCol_FullRange = PORISValueFloat("offsetCol_FullRange",0.0,1024.0,4096.0)
        self.mdWindowMode_Disabled = PORISMode("WindowMode_Disabled")
        self.mdDetectorMode_Engineering = PORISMode("DetectorMode_Engineering")
        self.mdOutputSourceMode_Engineering = PORISMode("OutputSourceMode_Engineering")
        self.mdWindowMode_Engineering = PORISMode("WindowMode_Engineering")
        self.mdDASMode_Engineering = PORISMode("DASMode_Engineering")
        self.mdAcquisitionMode_Engineering = PORISMode("AcquisitionMode_Engineering")
        self.mdMultipleExposureMode_Engineering = PORISMode("MultipleExposureMode_Engineering")
        self.mdProcessMonitorMode_Engineering = PORISMode("ProcessMonitorMode_Engineering")
        self.mdPreOpticsMode_Engineering = PORISMode("PreOpticsMode_Engineering")
        self.mdRedTFMode_Engineering = PORISMode("RedTFMode_Engineering")
        self.mdBlueTFMode_Engineering = PORISMode("BlueTFMode_Engineering")
        self.mdOsirisMode_Engineering = PORISMode("OsirisMode_Engineering")
        self.mdObservingModesMode_Engineering = PORISMode("ObservingModesMode_Engineering")
        self.mdAcquisitionModesMode_Engineering = PORISMode("AcquisitionModesMode_Engineering")
        self.mdFiltersMode_Engineering = PORISMode("FiltersMode_Engineering")
        self.mdFPEMode_Engineering = PORISMode("FPEMode_Engineering")
        self.addItem(self.sysOsiris)
        self.sysOsiris.ident = "OSI-0474"
        self.sysOsiris.description = ""
        self.addItem(self.sysObservingModes)
        self.sysObservingModes.ident = "OSI-0733"
        self.sysObservingModes.description = ""
        self.sysOsiris.addSubsystem(self.sysObservingModes)
        self.addItem(self.sysAcquisitionModes)
        self.sysAcquisitionModes.ident = "OSI-0133"
        self.sysAcquisitionModes.description = ""
        self.sysObservingModes.addSubsystem(self.sysAcquisitionModes)
        self.addItem(self.sysFPE)
        self.sysFPE.ident = "FP-0006"
        self.sysFPE.description = ""
        self.sysAcquisitionModes.addSubsystem(self.sysFPE)
        self.addItem(self.prFocalPlaneElement)
        self.prFocalPlaneElement.ident = "OSI-0138"
        self.prFocalPlaneElement.description = ""
        self.sysFPE.addParam(self.prFocalPlaneElement)
        self.addItem(self.sysDAS)
        self.sysDAS.ident = "OSI-0476"
        self.sysDAS.description = ""
        self.sysAcquisitionModes.addSubsystem(self.sysDAS)
        self.addItem(self.sysAcquisition)
        self.sysAcquisition.ident = "OSI-0477"
        self.sysAcquisition.description = ""
        self.sysDAS.addSubsystem(self.sysAcquisition)
        self.addItem(self.prShuffleLines)
        self.prShuffleLines.ident = "OSI-0479"
        self.prShuffleLines.description = ""
        self.sysAcquisition.addParam(self.prShuffleLines)
        self.addItem(self.prShiftNumber)
        self.prShiftNumber.ident = "OSI-0480"
        self.prShiftNumber.description = ""
        self.sysAcquisition.addParam(self.prShiftNumber)
        self.addItem(self.prExpTime)
        self.prExpTime.ident = "OSI-0487"
        self.prExpTime.description = ""
        self.sysAcquisition.addParam(self.prExpTime)
        self.addItem(self.sysMultipleExposure)
        self.sysMultipleExposure.ident = "OSI-0488"
        self.sysMultipleExposure.description = ""
        self.sysAcquisition.addSubsystem(self.sysMultipleExposure)
        self.addItem(self.prnumOfFrames)
        self.prnumOfFrames.ident = "OSI-0489"
        self.prnumOfFrames.description = ""
        self.sysMultipleExposure.addParam(self.prnumOfFrames)
        self.addItem(self.prPixelSpeed)
        self.prPixelSpeed.ident = "OSI-0491"
        self.prPixelSpeed.description = ""
        self.sysAcquisition.addParam(self.prPixelSpeed)
        self.addItem(self.prCalibGain)
        self.prCalibGain.ident = "DAS-0006"
        self.prCalibGain.description = ""
        self.sysAcquisition.addParam(self.prCalibGain)
        self.addItem(self.sysOpenShutter)
        self.sysOpenShutter.ident = "OSI-0499"
        self.sysOpenShutter.description = ""
        self.sysDAS.addSubsystem(self.sysOpenShutter)
        self.addItem(self.sysProcessMonitor)
        self.sysProcessMonitor.ident = "DAS-0036"
        self.sysProcessMonitor.description = ""
        self.sysDAS.addSubsystem(self.sysProcessMonitor)
        self.addItem(self.prCurrentEllapsed)
        self.prCurrentEllapsed.ident = "DAS-0037"
        self.prCurrentEllapsed.description = ""
        self.sysProcessMonitor.addParam(self.prCurrentEllapsed)
        self.addItem(self.prCurrentImg)
        self.prCurrentImg.ident = "DAS-0038"
        self.prCurrentImg.description = ""
        self.sysProcessMonitor.addParam(self.prCurrentImg)
        self.addItem(self.prCurrentPct)
        self.prCurrentPct.ident = "DAS-0039"
        self.prCurrentPct.description = ""
        self.sysProcessMonitor.addParam(self.prCurrentPct)
        self.addItem(self.prOverallPct)
        self.prOverallPct.ident = "DAS-0040"
        self.prOverallPct.description = ""
        self.sysProcessMonitor.addParam(self.prOverallPct)
        self.addItem(self.sysPreOptics)
        self.sysPreOptics.ident = "OSI-0136"
        self.sysPreOptics.description = ""
        self.sysAcquisitionModes.addSubsystem(self.sysPreOptics)
        self.addItem(self.prGrisms)
        self.prGrisms.ident = "OSI-0475"
        self.prGrisms.description = ""
        self.sysPreOptics.addParam(self.prGrisms)
        self.addItem(self.sysRedTF)
        self.sysRedTF.ident = "OSI-0575"
        self.sysRedTF.description = ""
        self.sysPreOptics.addSubsystem(self.sysRedTF)
        self.addItem(self.prRedFWHM)
        self.prRedFWHM.ident = "OSI-0576"
        self.prRedFWHM.description = ""
        self.sysRedTF.addParam(self.prRedFWHM)
        self.addItem(self.prRedLamda)
        self.prRedLamda.ident = "OSI-0577"
        self.prRedLamda.description = ""
        self.sysRedTF.addParam(self.prRedLamda)
        self.addItem(self.sysBlueTF)
        self.sysBlueTF.ident = "OSI-0578"
        self.sysBlueTF.description = ""
        self.sysPreOptics.addSubsystem(self.sysBlueTF)
        self.addItem(self.prBlueFWHM)
        self.prBlueFWHM.ident = "OSI-0579"
        self.prBlueFWHM.description = ""
        self.sysBlueTF.addParam(self.prBlueFWHM)
        self.addItem(self.prBlueLamda)
        self.prBlueLamda.ident = "OSI-0580"
        self.prBlueLamda.description = ""
        self.sysBlueTF.addParam(self.prBlueLamda)
        self.addItem(self.przzero)
        self.przzero.ident = "OP-0109"
        self.przzero.description = ""
        self.sysPreOptics.addParam(self.przzero)
        self.addItem(self.mdOsirisMode_Imaging)
        self.mdOsirisMode_Imaging.ident = "OSI-0471"
        self.mdOsirisMode_Imaging.description = ""
        self.sysOsiris.addMode(self.mdOsirisMode_Imaging)
        self.addItem(self.mdOsirisMode_Spectroscopy)
        self.mdOsirisMode_Spectroscopy.ident = "OSI-0472"
        self.mdOsirisMode_Spectroscopy.description = ""
        self.sysOsiris.addMode(self.mdOsirisMode_Spectroscopy)
        self.addItem(self.mdOsirisMode_Calibration)
        self.mdOsirisMode_Calibration.ident = "OSI-0473"
        self.mdOsirisMode_Calibration.description = ""
        self.sysOsiris.addMode(self.mdOsirisMode_Calibration)
        self.addItem(self.mdAcquisitionModesMode_aBBI)
        self.mdAcquisitionModesMode_aBBI.ident = "OSI-0001"
        self.mdAcquisitionModesMode_aBBI.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aBBI)
        self.addItem(self.mdAcquisitionModesMode_aTFI)
        self.mdAcquisitionModesMode_aTFI.ident = "OSI-0002"
        self.mdAcquisitionModesMode_aTFI.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aTFI)
        self.addItem(self.mdAcquisitionModesMode_aLSSpec)
        self.mdAcquisitionModesMode_aLSSpec.ident = "OSI-0003"
        self.mdAcquisitionModesMode_aLSSpec.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aLSSpec)
        self.addItem(self.mdAcquisitionModesMode_aMOS)
        self.mdAcquisitionModesMode_aMOS.ident = "OSI-0004"
        self.mdAcquisitionModesMode_aMOS.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aMOS)
        self.addItem(self.mdAcquisitionModesMode_aFastBBI)
        self.mdAcquisitionModesMode_aFastBBI.ident = "OSI-0005"
        self.mdAcquisitionModesMode_aFastBBI.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aFastBBI)
        self.addItem(self.mdAcquisitionModesMode_aFrTrBBI)
        self.mdAcquisitionModesMode_aFrTrBBI.ident = "OSI-0006"
        self.mdAcquisitionModesMode_aFrTrBBI.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aFrTrBBI)
        self.addItem(self.mdAcquisitionModesMode_aFastLSSpec)
        self.mdAcquisitionModesMode_aFastLSSpec.ident = "OSI-0007"
        self.mdAcquisitionModesMode_aFastLSSpec.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aFastLSSpec)
        self.addItem(self.mdAcquisitionModesMode_aFastTFImage)
        self.mdAcquisitionModesMode_aFastTFImage.ident = "OSI-0395"
        self.mdAcquisitionModesMode_aFastTFImage.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aFastTFImage)
        self.addItem(self.mdAcquisitionModesMode_aFrTrTFI)
        self.mdAcquisitionModesMode_aFrTrTFI.ident = "OSI-0396"
        self.mdAcquisitionModesMode_aFrTrTFI.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aFrTrTFI)
        self.addItem(self.mdAcquisitionModesMode_aBias)
        self.mdAcquisitionModesMode_aBias.ident = "OSI-0397"
        self.mdAcquisitionModesMode_aBias.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aBias)
        self.addItem(self.mdAcquisitionModesMode_aDark)
        self.mdAcquisitionModesMode_aDark.ident = "OSI-0398"
        self.mdAcquisitionModesMode_aDark.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aDark)
        self.addItem(self.mdAcquisitionModesMode_aDomeFlat)
        self.mdAcquisitionModesMode_aDomeFlat.ident = "OSI-0399"
        self.mdAcquisitionModesMode_aDomeFlat.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aDomeFlat)
        self.addItem(self.mdAcquisitionModesMode_aSkyFlat)
        self.mdAcquisitionModesMode_aSkyFlat.ident = "OSI-0400"
        self.mdAcquisitionModesMode_aSkyFlat.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aSkyFlat)
        self.addItem(self.mdAcquisitionModesMode_aSpectralFlat)
        self.mdAcquisitionModesMode_aSpectralFlat.ident = "OSI-0401"
        self.mdAcquisitionModesMode_aSpectralFlat.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aSpectralFlat)
        self.addItem(self.mdAcquisitionModesMode_aCalibLamp)
        self.mdAcquisitionModesMode_aCalibLamp.ident = "OSI-0402"
        self.mdAcquisitionModesMode_aCalibLamp.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aCalibLamp)
        self.addItem(self.mdAcquisitionModesMode_aTFCalib)
        self.mdAcquisitionModesMode_aTFCalib.ident = "OSI-0403"
        self.mdAcquisitionModesMode_aTFCalib.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aTFCalib)
        self.addItem(self.mdAcquisitionModesMode_Throughslit)
        self.mdAcquisitionModesMode_Throughslit.ident = "OSI-0772"
        self.mdAcquisitionModesMode_Throughslit.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_Throughslit)
        self.addItem(self.mdObservingModesMode_BBI)
        self.mdObservingModesMode_BBI.ident = "OSI-0717"
        self.mdObservingModesMode_BBI.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_BBI)
        self.addItem(self.mdObservingModesMode_TFI)
        self.mdObservingModesMode_TFI.ident = "OSI-0718"
        self.mdObservingModesMode_TFI.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_TFI)
        self.addItem(self.mdObservingModesMode_LSSpec)
        self.mdObservingModesMode_LSSpec.ident = "OSI-0719"
        self.mdObservingModesMode_LSSpec.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_LSSpec)
        self.addItem(self.mdObservingModesMode_MOS)
        self.mdObservingModesMode_MOS.ident = "OSI-0720"
        self.mdObservingModesMode_MOS.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_MOS)
        self.addItem(self.mdObservingModesMode_FastBBI)
        self.mdObservingModesMode_FastBBI.ident = "OSI-0721"
        self.mdObservingModesMode_FastBBI.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_FastBBI)
        self.addItem(self.mdObservingModesMode_FrTrBBI)
        self.mdObservingModesMode_FrTrBBI.ident = "OSI-0722"
        self.mdObservingModesMode_FrTrBBI.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_FrTrBBI)
        self.addItem(self.mdObservingModesMode_FastLSSpec)
        self.mdObservingModesMode_FastLSSpec.ident = "OSI-0723"
        self.mdObservingModesMode_FastLSSpec.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_FastLSSpec)
        self.addItem(self.mdObservingModesMode_FastTFImage)
        self.mdObservingModesMode_FastTFImage.ident = "OSI-0724"
        self.mdObservingModesMode_FastTFImage.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_FastTFImage)
        self.addItem(self.mdObservingModesMode_FrTrTFI)
        self.mdObservingModesMode_FrTrTFI.ident = "OSI-0725"
        self.mdObservingModesMode_FrTrTFI.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_FrTrTFI)
        self.addItem(self.mdObservingModesMode_Bias)
        self.mdObservingModesMode_Bias.ident = "OSI-0726"
        self.mdObservingModesMode_Bias.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_Bias)
        self.addItem(self.mdObservingModesMode_Dark)
        self.mdObservingModesMode_Dark.ident = "OSI-0727"
        self.mdObservingModesMode_Dark.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_Dark)
        self.addItem(self.mdObservingModesMode_DomeFlat)
        self.mdObservingModesMode_DomeFlat.ident = "OSI-0728"
        self.mdObservingModesMode_DomeFlat.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_DomeFlat)
        self.addItem(self.mdObservingModesMode_SkyFlat)
        self.mdObservingModesMode_SkyFlat.ident = "OSI-0729"
        self.mdObservingModesMode_SkyFlat.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_SkyFlat)
        self.addItem(self.mdObservingModesMode_SpectralFlat)
        self.mdObservingModesMode_SpectralFlat.ident = "OSI-0730"
        self.mdObservingModesMode_SpectralFlat.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_SpectralFlat)
        self.addItem(self.mdObservingModesMode_CalibLamp)
        self.mdObservingModesMode_CalibLamp.ident = "OSI-0731"
        self.mdObservingModesMode_CalibLamp.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_CalibLamp)
        self.addItem(self.mdObservingModesMode_TFCalib)
        self.mdObservingModesMode_TFCalib.ident = "OSI-0732"
        self.mdObservingModesMode_TFCalib.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_TFCalib)
        self.addItem(self.sysFilters)
        self.sysFilters.ident = "OSI-0137"
        self.sysFilters.description = ""
        self.sysPreOptics.addSubsystem(self.sysFilters)
        self.addItem(self.prUFilters)
        self.prUFilters.ident = "OSI-0159"
        self.prUFilters.description = ""
        self.sysFilters.addParam(self.prUFilters)
        self.addItem(self.prOS)
        self.prOS.ident = "OSI-0160"
        self.prOS.description = ""
        self.sysFilters.addParam(self.prOS)
        self.addItem(self.prBroad)
        self.prBroad.ident = "OSI-0619"
        self.prBroad.description = ""
        self.sysFilters.addParam(self.prBroad)
        self.addItem(self.mdFocalPlaneElementMode_Disabled)
        self.mdFocalPlaneElementMode_Disabled.ident = "FP-0001"
        self.mdFocalPlaneElementMode_Disabled.description = ""
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_Disabled)
        self.addItem(self.vlFocalPlaneElement_LS0_4)
        self.vlFocalPlaneElement_LS0_4.ident = "OSI-0117"
        self.vlFocalPlaneElement_LS0_4.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS0_4)
        self.addItem(self.vlFocalPlaneElement_LS0_6)
        self.vlFocalPlaneElement_LS0_6.ident = "OSI-0118"
        self.vlFocalPlaneElement_LS0_6.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS0_6)
        self.addItem(self.vlFocalPlaneElement_LS0_8)
        self.vlFocalPlaneElement_LS0_8.ident = "OSI-0119"
        self.vlFocalPlaneElement_LS0_8.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS0_8)
        self.addItem(self.vlFocalPlaneElement_LS1_0)
        self.vlFocalPlaneElement_LS1_0.ident = "OSI-0120"
        self.vlFocalPlaneElement_LS1_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS1_0)
        self.addItem(self.vlFocalPlaneElement_LS1_2)
        self.vlFocalPlaneElement_LS1_2.ident = "OSI-0121"
        self.vlFocalPlaneElement_LS1_2.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS1_2)
        self.addItem(self.vlFocalPlaneElement_LS1_5)
        self.vlFocalPlaneElement_LS1_5.ident = "OSI-0122"
        self.vlFocalPlaneElement_LS1_5.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS1_5)
        self.addItem(self.vlFocalPlaneElement_LS1_8)
        self.vlFocalPlaneElement_LS1_8.ident = "OSI-0123"
        self.vlFocalPlaneElement_LS1_8.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS1_8)
        self.addItem(self.vlFocalPlaneElement_LS2_5)
        self.vlFocalPlaneElement_LS2_5.ident = "OSI-0124"
        self.vlFocalPlaneElement_LS2_5.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS2_5)
        self.addItem(self.vlFocalPlaneElement_LS3_0)
        self.vlFocalPlaneElement_LS3_0.ident = "OSI-0125"
        self.vlFocalPlaneElement_LS3_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS3_0)
        self.addItem(self.vlFocalPlaneElement_LS5_0)
        self.vlFocalPlaneElement_LS5_0.ident = "OSI-0126"
        self.vlFocalPlaneElement_LS5_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS5_0)
        self.addItem(self.vlFocalPlaneElement_LS10_0)
        self.vlFocalPlaneElement_LS10_0.ident = "OSI-0127"
        self.vlFocalPlaneElement_LS10_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS10_0)
        self.addItem(self.vlFocalPlaneElement_LS12_0)
        self.vlFocalPlaneElement_LS12_0.ident = "OSI-0128"
        self.vlFocalPlaneElement_LS12_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS12_0)
        self.addItem(self.vlFocalPlaneElement_LS40_0)
        self.vlFocalPlaneElement_LS40_0.ident = "OSI-0129"
        self.vlFocalPlaneElement_LS40_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS40_0)
        self.addItem(self.mdFocalPlaneElementMode_MOS)
        self.mdFocalPlaneElementMode_MOS.ident = "FP-0002"
        self.mdFocalPlaneElementMode_MOS.description = ""
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_MOS)
        self.addItem(self.mdFocalPlaneElementMode_FastPhotometry)
        self.mdFocalPlaneElementMode_FastPhotometry.ident = "FP-0003"
        self.mdFocalPlaneElementMode_FastPhotometry.description = ""
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_FastPhotometry)
        self.addItem(self.mdFocalPlaneElementMode_FrameTransfer)
        self.mdFocalPlaneElementMode_FrameTransfer.ident = "FP-0004"
        self.mdFocalPlaneElementMode_FrameTransfer.description = ""
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_FrameTransfer)
        self.addItem(self.mdFocalPlaneElementMode_LS)
        self.mdFocalPlaneElementMode_LS.ident = "FP-0005"
        self.mdFocalPlaneElementMode_LS.description = ""
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_LS)
        self.addItem(self.vlFocalPlaneElement_FrameTransferMask)
        self.vlFocalPlaneElement_FrameTransferMask.ident = "OSI-0586"
        self.vlFocalPlaneElement_FrameTransferMask.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_FrameTransferMask)
        self.addItem(self.vlFocalPlaneElement_FastPhotometryMask)
        self.vlFocalPlaneElement_FastPhotometryMask.ident = "OSI-0585"
        self.vlFocalPlaneElement_FastPhotometryMask.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_FastPhotometryMask)
        self.addItem(self.vlFocalPlaneElement_MOSmask)
        self.vlFocalPlaneElement_MOSmask.ident = "OSI-0584"
        self.vlFocalPlaneElement_MOSmask.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_MOSmask)
        self.addItem(self.vlFocalPlaneElement_NoFPE)
        self.vlFocalPlaneElement_NoFPE.ident = "OSI-0583"
        self.vlFocalPlaneElement_NoFPE.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_NoFPE)
        self.addItem(self.mdFPEMode_NoFPE)
        self.mdFPEMode_NoFPE.ident = "OSI-0116"
        self.mdFPEMode_NoFPE.description = ""
        self.sysFPE.addMode(self.mdFPEMode_NoFPE)
        self.addItem(self.mdFPEMode_MOSmask)
        self.mdFPEMode_MOSmask.ident = "OSI-0130"
        self.mdFPEMode_MOSmask.description = ""
        self.sysFPE.addMode(self.mdFPEMode_MOSmask)
        self.addItem(self.mdFPEMode_FastPhotometryMask)
        self.mdFPEMode_FastPhotometryMask.ident = "OSI-0131"
        self.mdFPEMode_FastPhotometryMask.description = ""
        self.sysFPE.addMode(self.mdFPEMode_FastPhotometryMask)
        self.addItem(self.mdFPEMode_FrameTransferMask)
        self.mdFPEMode_FrameTransferMask.ident = "OSI-0132"
        self.mdFPEMode_FrameTransferMask.description = ""
        self.sysFPE.addMode(self.mdFPEMode_FrameTransferMask)
        self.addItem(self.mdFPEMode_LSMask)
        self.mdFPEMode_LSMask.ident = "OSI-0142"
        self.mdFPEMode_LSMask.description = ""
        self.sysFPE.addMode(self.mdFPEMode_LSMask)
        self.addItem(self.sysDetector)
        self.sysDetector.ident = "OSI-0481"
        self.sysDetector.description = ""
        self.sysAcquisition.addSubsystem(self.sysDetector)
        self.addItem(self.sysOutputSource)
        self.sysOutputSource.ident = "OSI-0493"
        self.sysOutputSource.description = ""
        self.sysDetector.addSubsystem(self.sysOutputSource)
        self.addItem(self.sysRecomposition)
        self.sysRecomposition.ident = "OSI-0494"
        self.sysRecomposition.description = ""
        self.sysOutputSource.addSubsystem(self.sysRecomposition)
        self.addItem(self.prBinning)
        self.prBinning.ident = "OSI-0641"
        self.prBinning.description = ""
        self.sysDetector.addParam(self.prBinning)
        self.addItem(self.sysWindow)
        self.sysWindow.ident = "OSI-0640"
        self.sysWindow.description = ""
        self.sysDetector.addSubsystem(self.sysWindow)
        self.addItem(self.prRows)
        self.prRows.ident = "OSI-0484"
        self.prRows.description = ""
        self.sysWindow.addParam(self.prRows)
        self.addItem(self.prCols)
        self.prCols.ident = "OSI-0482"
        self.prCols.description = ""
        self.sysWindow.addParam(self.prCols)
        self.addItem(self.proffsetRow)
        self.proffsetRow.ident = "OSI-0483"
        self.proffsetRow.description = ""
        self.sysWindow.addParam(self.proffsetRow)
        self.addItem(self.proffsetCol)
        self.proffsetCol.ident = "OSI-0485"
        self.proffsetCol.description = ""
        self.sysWindow.addParam(self.proffsetCol)
        self.addItem(self.mdAcquisitionMode_Normal)
        self.mdAcquisitionMode_Normal.ident = "OSI-0406"
        self.mdAcquisitionMode_Normal.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Normal)
        self.addItem(self.mdAcquisitionMode_FrameTransfer)
        self.mdAcquisitionMode_FrameTransfer.ident = "OSI-0407"
        self.mdAcquisitionMode_FrameTransfer.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_FrameTransfer)
        self.addItem(self.mdAcquisitionMode_Shuffling)
        self.mdAcquisitionMode_Shuffling.ident = "OSI-0408"
        self.mdAcquisitionMode_Shuffling.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Shuffling)
        self.addItem(self.vlShuffleLines_FullRange)
        self.vlShuffleLines_FullRange.ident = "OSI-0409"
        self.vlShuffleLines_FullRange.description = ""
        self.prShuffleLines.addValue(self.vlShuffleLines_FullRange)
        self.addItem(self.mdShuffleLinesMode_Normal)
        self.mdShuffleLinesMode_Normal.ident = "OSI-0410"
        self.mdShuffleLinesMode_Normal.description = ""
        self.prShuffleLines.addMode(self.mdShuffleLinesMode_Normal)
        self.addItem(self.vlShiftNumber_FullRange)
        self.vlShiftNumber_FullRange.ident = "OSI-0411"
        self.vlShiftNumber_FullRange.description = ""
        self.prShiftNumber.addValue(self.vlShiftNumber_FullRange)
        self.addItem(self.mdShiftNumberMode_Normal)
        self.mdShiftNumberMode_Normal.ident = "OSI-0412"
        self.mdShiftNumberMode_Normal.description = ""
        self.prShiftNumber.addMode(self.mdShiftNumberMode_Normal)
        self.addItem(self.vlExpTime_FullRange)
        self.vlExpTime_FullRange.ident = "OSI-0423"
        self.vlExpTime_FullRange.description = ""
        self.prExpTime.addValue(self.vlExpTime_FullRange)
        self.addItem(self.mdExpTimeMode_Normal)
        self.mdExpTimeMode_Normal.ident = "OSI-0424"
        self.mdExpTimeMode_Normal.description = ""
        self.prExpTime.addMode(self.mdExpTimeMode_Normal)
        self.addItem(self.mdExpTimeMode_Bias)
        self.mdExpTimeMode_Bias.ident = "OSI-0603"
        self.mdExpTimeMode_Bias.description = ""
        self.prExpTime.addMode(self.mdExpTimeMode_Bias)
        self.addItem(self.vlExpTime_0_0)
        self.vlExpTime_0_0.ident = "OSI-0604"
        self.vlExpTime_0_0.description = ""
        self.prExpTime.addValue(self.vlExpTime_0_0)
        self.addItem(self.mdExpTimeMode_FT)
        self.mdExpTimeMode_FT.ident = "OSI-0436"
        self.mdExpTimeMode_FT.description = ""
        self.prExpTime.addMode(self.mdExpTimeMode_FT)
        self.addItem(self.vlExpTime_FTRange)
        self.vlExpTime_FTRange.ident = "OSI-0437"
        self.vlExpTime_FTRange.description = ""
        self.prExpTime.addValue(self.vlExpTime_FTRange)
        self.addItem(self.mdnumOfFramesMode_Normal)
        self.mdnumOfFramesMode_Normal.ident = "OSI-0425"
        self.mdnumOfFramesMode_Normal.description = ""
        self.prnumOfFrames.addMode(self.mdnumOfFramesMode_Normal)
        self.addItem(self.vlnumOfFrames_FullRange)
        self.vlnumOfFrames_FullRange.ident = "OSI-0426"
        self.vlnumOfFrames_FullRange.description = ""
        self.prnumOfFrames.addValue(self.vlnumOfFrames_FullRange)
        self.addItem(self.mdMultipleExposureMode_On)
        self.mdMultipleExposureMode_On.ident = "OSI-0428"
        self.mdMultipleExposureMode_On.description = ""
        self.sysMultipleExposure.addMode(self.mdMultipleExposureMode_On)
        self.addItem(self.mdMultipleExposureMode_Single)
        self.mdMultipleExposureMode_Single.ident = "OSI-0427"
        self.mdMultipleExposureMode_Single.description = ""
        self.sysMultipleExposure.addMode(self.mdMultipleExposureMode_Single)
        self.addItem(self.vlPixelSpeed_SLW)
        self.vlPixelSpeed_SLW.ident = "OSI-0431"
        self.vlPixelSpeed_SLW.description = ""
        self.prPixelSpeed.addValue(self.vlPixelSpeed_SLW)
        self.addItem(self.vlPixelSpeed_MED)
        self.vlPixelSpeed_MED.ident = "OSI-0432"
        self.vlPixelSpeed_MED.description = ""
        self.prPixelSpeed.addValue(self.vlPixelSpeed_MED)
        self.addItem(self.vlPixelSpeed_FST)
        self.vlPixelSpeed_FST.ident = "OSI-0433"
        self.vlPixelSpeed_FST.description = ""
        self.prPixelSpeed.addValue(self.vlPixelSpeed_FST)
        self.addItem(self.mdPixelSpeedMode_All)
        self.mdPixelSpeedMode_All.ident = "OSI-0646"
        self.mdPixelSpeedMode_All.description = ""
        self.prPixelSpeed.addMode(self.mdPixelSpeedMode_All)
        self.addItem(self.mdAcquisitionMode_FTBias)
        self.mdAcquisitionMode_FTBias.ident = "OSI-0607"
        self.mdAcquisitionMode_FTBias.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_FTBias)
        self.addItem(self.mdAcquisitionMode_NormalBias)
        self.mdAcquisitionMode_NormalBias.ident = "OSI-0608"
        self.mdAcquisitionMode_NormalBias.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_NormalBias)
        self.addItem(self.mdAcquisitionMode_ShufflingBias)
        self.mdAcquisitionMode_ShufflingBias.ident = "OSI-0609"
        self.mdAcquisitionMode_ShufflingBias.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_ShufflingBias)
        self.addItem(self.mdAcquisitionMode_NormalSquare)
        self.mdAcquisitionMode_NormalSquare.ident = "OSI-0637"
        self.mdAcquisitionMode_NormalSquare.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_NormalSquare)
        self.addItem(self.mdAcquisitionMode_ShufflingSquare)
        self.mdAcquisitionMode_ShufflingSquare.ident = "OSI-0638"
        self.mdAcquisitionMode_ShufflingSquare.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_ShufflingSquare)
        self.addItem(self.mdAcquisitionMode_GainCalib)
        self.mdAcquisitionMode_GainCalib.ident = "DAS-0002"
        self.mdAcquisitionMode_GainCalib.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_GainCalib)
        self.addItem(self.vlCalibGain_FullRange)
        self.vlCalibGain_FullRange.ident = "DAS-0003"
        self.vlCalibGain_FullRange.description = ""
        self.prCalibGain.addValue(self.vlCalibGain_FullRange)
        self.addItem(self.mdCalibGainMode_Normal)
        self.mdCalibGainMode_Normal.ident = "DAS-0004"
        self.mdCalibGainMode_Normal.description = ""
        self.prCalibGain.addMode(self.mdCalibGainMode_Normal)
        self.addItem(self.mdDASMode_SimpleImg)
        self.mdDASMode_SimpleImg.ident = "OSI-0439"
        self.mdDASMode_SimpleImg.description = ""
        self.sysDAS.addMode(self.mdDASMode_SimpleImg)
        self.addItem(self.mdDASMode_SimpleSpec)
        self.mdDASMode_SimpleSpec.ident = "OSI-0455"
        self.mdDASMode_SimpleSpec.description = ""
        self.sysDAS.addMode(self.mdDASMode_SimpleSpec)
        self.addItem(self.mdDASMode_ShufffingSpec)
        self.mdDASMode_ShufffingSpec.ident = "OSI-0639"
        self.mdDASMode_ShufffingSpec.description = ""
        self.sysDAS.addMode(self.mdDASMode_ShufffingSpec)
        self.addItem(self.mdOpenShutterMode_On)
        self.mdOpenShutterMode_On.ident = "OSI-0468"
        self.mdOpenShutterMode_On.description = ""
        self.sysOpenShutter.addMode(self.mdOpenShutterMode_On)
        self.addItem(self.mdOpenShutterMode_Off)
        self.mdOpenShutterMode_Off.ident = "OSI-0469"
        self.mdOpenShutterMode_Off.description = ""
        self.sysOpenShutter.addMode(self.mdOpenShutterMode_Off)
        self.addItem(self.mdDASMode_FTImg)
        self.mdDASMode_FTImg.ident = "OSI-0500"
        self.mdDASMode_FTImg.description = ""
        self.sysDAS.addMode(self.mdDASMode_FTImg)
        self.addItem(self.mdDASMode_FTDark)
        self.mdDASMode_FTDark.ident = "OSI-0610"
        self.mdDASMode_FTDark.description = ""
        self.sysDAS.addMode(self.mdDASMode_FTDark)
        self.addItem(self.mdDASMode_FTBias)
        self.mdDASMode_FTBias.ident = "OSI-0611"
        self.mdDASMode_FTBias.description = ""
        self.sysDAS.addMode(self.mdDASMode_FTBias)
        self.addItem(self.mdDASMode_SimpleBias)
        self.mdDASMode_SimpleBias.ident = "OSI-0613"
        self.mdDASMode_SimpleBias.description = ""
        self.sysDAS.addMode(self.mdDASMode_SimpleBias)
        self.addItem(self.mdDASMode_SimpleDark)
        self.mdDASMode_SimpleDark.ident = "OSI-0614"
        self.mdDASMode_SimpleDark.description = ""
        self.sysDAS.addMode(self.mdDASMode_SimpleDark)
        self.addItem(self.mdDASMode_ShufffingDark)
        self.mdDASMode_ShufffingDark.ident = "OSI-0616"
        self.mdDASMode_ShufffingDark.description = ""
        self.sysDAS.addMode(self.mdDASMode_ShufffingDark)
        self.addItem(self.mdDASMode_ShufffingBias)
        self.mdDASMode_ShufffingBias.ident = "OSI-0617"
        self.mdDASMode_ShufffingBias.description = ""
        self.sysDAS.addMode(self.mdDASMode_ShufffingBias)
        self.addItem(self.mdDASMode_ShufffingImage)
        self.mdDASMode_ShufffingImage.ident = "OSI-0467"
        self.mdDASMode_ShufffingImage.description = ""
        self.sysDAS.addMode(self.mdDASMode_ShufffingImage)
        self.addItem(self.mdDASMode_SimpleCalib)
        self.mdDASMode_SimpleCalib.ident = "DAS-0005"
        self.mdDASMode_SimpleCalib.description = ""
        self.sysDAS.addMode(self.mdDASMode_SimpleCalib)
        self.addItem(self.mdDASMode_GainCalib)
        self.mdDASMode_GainCalib.ident = "DAS-0018"
        self.mdDASMode_GainCalib.description = ""
        self.sysDAS.addMode(self.mdDASMode_GainCalib)
        self.addItem(self.vlCurrentEllapsed_Range)
        self.vlCurrentEllapsed_Range.ident = "DAS-0026"
        self.vlCurrentEllapsed_Range.description = ""
        self.prCurrentEllapsed.addValue(self.vlCurrentEllapsed_Range)
        self.addItem(self.mdCurrentEllapsedMode_Normal)
        self.mdCurrentEllapsedMode_Normal.ident = "DAS-0027"
        self.mdCurrentEllapsedMode_Normal.description = ""
        self.prCurrentEllapsed.addMode(self.mdCurrentEllapsedMode_Normal)
        self.addItem(self.vlCurrentImg_Range)
        self.vlCurrentImg_Range.ident = "DAS-0028"
        self.vlCurrentImg_Range.description = ""
        self.prCurrentImg.addValue(self.vlCurrentImg_Range)
        self.addItem(self.mdCurrentImgMode_Normal)
        self.mdCurrentImgMode_Normal.ident = "DAS-0029"
        self.mdCurrentImgMode_Normal.description = ""
        self.prCurrentImg.addMode(self.mdCurrentImgMode_Normal)
        self.addItem(self.vlCurrentPct_Range)
        self.vlCurrentPct_Range.ident = "DAS-0030"
        self.vlCurrentPct_Range.description = ""
        self.prCurrentPct.addValue(self.vlCurrentPct_Range)
        self.addItem(self.mdCurrentPctMode_Normal)
        self.mdCurrentPctMode_Normal.ident = "DAS-0031"
        self.mdCurrentPctMode_Normal.description = ""
        self.prCurrentPct.addMode(self.mdCurrentPctMode_Normal)
        self.addItem(self.vlOverallPct_Range)
        self.vlOverallPct_Range.ident = "DAS-0032"
        self.vlOverallPct_Range.description = ""
        self.prOverallPct.addValue(self.vlOverallPct_Range)
        self.addItem(self.mdOverallPctMode_Normal)
        self.mdOverallPctMode_Normal.ident = "DAS-0033"
        self.mdOverallPctMode_Normal.description = ""
        self.prOverallPct.addMode(self.mdOverallPctMode_Normal)
        self.addItem(self.mdProcessMonitorMode_Normal)
        self.mdProcessMonitorMode_Normal.ident = "DAS-0034"
        self.mdProcessMonitorMode_Normal.description = ""
        self.sysProcessMonitor.addMode(self.mdProcessMonitorMode_Normal)
        self.addItem(self.mdPreOpticsMode_NoDispersion)
        self.mdPreOpticsMode_NoDispersion.ident = "OSI-0014"
        self.mdPreOpticsMode_NoDispersion.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_NoDispersion)
        self.addItem(self.mdPreOpticsMode_RTF)
        self.mdPreOpticsMode_RTF.ident = "OSI-0015"
        self.mdPreOpticsMode_RTF.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_RTF)
        self.addItem(self.mdPreOpticsMode_GrismR)
        self.mdPreOpticsMode_GrismR.ident = "OSI-0146"
        self.mdPreOpticsMode_GrismR.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_GrismR)
        self.addItem(self.mdPreOpticsMode_BTF)
        self.mdPreOpticsMode_BTF.ident = "OSI-0016"
        self.mdPreOpticsMode_BTF.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_BTF)
        self.addItem(self.vlGrisms_R300B)
        self.vlGrisms_R300B.ident = "OSI-0017"
        self.vlGrisms_R300B.description = ""
        self.prGrisms.addValue(self.vlGrisms_R300B)
        self.addItem(self.vlGrisms_R300R)
        self.vlGrisms_R300R.ident = "OSI-0018"
        self.vlGrisms_R300R.description = ""
        self.prGrisms.addValue(self.vlGrisms_R300R)
        self.addItem(self.vlGrisms_R500B)
        self.vlGrisms_R500B.ident = "OSI-0019"
        self.vlGrisms_R500B.description = ""
        self.prGrisms.addValue(self.vlGrisms_R500B)
        self.addItem(self.vlGrisms_R500R)
        self.vlGrisms_R500R.ident = "OSI-0020"
        self.vlGrisms_R500R.description = ""
        self.prGrisms.addValue(self.vlGrisms_R500R)
        self.addItem(self.vlGrisms_R1000B)
        self.vlGrisms_R1000B.ident = "OSI-0021"
        self.vlGrisms_R1000B.description = ""
        self.prGrisms.addValue(self.vlGrisms_R1000B)
        self.addItem(self.vlGrisms_R1000R)
        self.vlGrisms_R1000R.ident = "OSI-0022"
        self.vlGrisms_R1000R.description = ""
        self.prGrisms.addValue(self.vlGrisms_R1000R)
        self.addItem(self.vlGrisms_R2000B)
        self.vlGrisms_R2000B.ident = "OSI-0023"
        self.vlGrisms_R2000B.description = ""
        self.prGrisms.addValue(self.vlGrisms_R2000B)
        self.addItem(self.vlGrisms_R2500U)
        self.vlGrisms_R2500U.ident = "OSI-0024"
        self.vlGrisms_R2500U.description = ""
        self.prGrisms.addValue(self.vlGrisms_R2500U)
        self.addItem(self.vlGrisms_R2500V)
        self.vlGrisms_R2500V.ident = "OSI-0025"
        self.vlGrisms_R2500V.description = ""
        self.prGrisms.addValue(self.vlGrisms_R2500V)
        self.addItem(self.vlGrisms_R2500R)
        self.vlGrisms_R2500R.ident = "OSI-0026"
        self.vlGrisms_R2500R.description = ""
        self.prGrisms.addValue(self.vlGrisms_R2500R)
        self.addItem(self.vlGrisms_R2500I)
        self.vlGrisms_R2500I.ident = "OSI-0027"
        self.vlGrisms_R2500I.description = ""
        self.prGrisms.addValue(self.vlGrisms_R2500I)
        self.addItem(self.mdGrismsMode_GrismsB)
        self.mdGrismsMode_GrismsB.ident = "OSI-0140"
        self.mdGrismsMode_GrismsB.description = ""
        self.prGrisms.addMode(self.mdGrismsMode_GrismsB)
        self.addItem(self.mdGrismsMode_GrismsR)
        self.mdGrismsMode_GrismsR.ident = "OSI-0393"
        self.mdGrismsMode_GrismsR.description = ""
        self.prGrisms.addMode(self.mdGrismsMode_GrismsR)
        self.addItem(self.mdPreOpticsMode_GrismB)
        self.mdPreOpticsMode_GrismB.ident = "OSI-0394"
        self.mdPreOpticsMode_GrismB.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_GrismB)
        self.addItem(self.mdPreOpticsMode_GrismBMOS)
        self.mdPreOpticsMode_GrismBMOS.ident = "OSI-0501"
        self.mdPreOpticsMode_GrismBMOS.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_GrismBMOS)
        self.addItem(self.vlRedFWHM_Range2_0)
        self.vlRedFWHM_Range2_0.ident = "OSI-0502"
        self.vlRedFWHM_Range2_0.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range2_0)
        self.addItem(self.mdRedFWHMMode_l2_0)
        self.mdRedFWHMMode_l2_0.ident = "OSI-0503"
        self.mdRedFWHMMode_l2_0.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l2_0)
        self.addItem(self.mdRedFWHMMode_l1_5)
        self.mdRedFWHMMode_l1_5.ident = "OSI-0504"
        self.mdRedFWHMMode_l1_5.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l1_5)
        self.addItem(self.mdRedFWHMMode_l1_4)
        self.mdRedFWHMMode_l1_4.ident = "OSI-0505"
        self.mdRedFWHMMode_l1_4.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l1_4)
        self.addItem(self.mdRedFWHMMode_l1_3)
        self.mdRedFWHMMode_l1_3.ident = "OSI-0506"
        self.mdRedFWHMMode_l1_3.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l1_3)
        self.addItem(self.mdRedFWHMMode_l1_2)
        self.mdRedFWHMMode_l1_2.ident = "OSI-0507"
        self.mdRedFWHMMode_l1_2.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l1_2)
        self.addItem(self.mdRedFWHMMode_l1_2b)
        self.mdRedFWHMMode_l1_2b.ident = "OSI-0508"
        self.mdRedFWHMMode_l1_2b.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l1_2b)
        self.addItem(self.vlRedFWHM_Range1_5)
        self.vlRedFWHM_Range1_5.ident = "OSI-0509"
        self.vlRedFWHM_Range1_5.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range1_5)
        self.addItem(self.vlRedFWHM_Range1_4)
        self.vlRedFWHM_Range1_4.ident = "OSI-0510"
        self.vlRedFWHM_Range1_4.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range1_4)
        self.addItem(self.vlRedFWHM_Range1_3)
        self.vlRedFWHM_Range1_3.ident = "OSI-0511"
        self.vlRedFWHM_Range1_3.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range1_3)
        self.addItem(self.vlRedFWHM_Range1_2)
        self.vlRedFWHM_Range1_2.ident = "OSI-0512"
        self.vlRedFWHM_Range1_2.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range1_2)
        self.addItem(self.vlRedFWHM_Range1_2b)
        self.vlRedFWHM_Range1_2b.ident = "OSI-0513"
        self.vlRedFWHM_Range1_2b.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range1_2b)
        self.addItem(self.mdRedTFMode_l651_799)
        self.mdRedTFMode_l651_799.ident = "OSI-0514"
        self.mdRedTFMode_l651_799.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l651_799)
        self.addItem(self.mdRedTFMode_l800_819)
        self.mdRedTFMode_l800_819.ident = "OSI-0515"
        self.mdRedTFMode_l800_819.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l800_819)
        self.addItem(self.mdRedTFMode_l820_839)
        self.mdRedTFMode_l820_839.ident = "OSI-0516"
        self.mdRedTFMode_l820_839.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l820_839)
        self.addItem(self.mdRedTFMode_l840_879)
        self.mdRedTFMode_l840_879.ident = "OSI-0517"
        self.mdRedTFMode_l840_879.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l840_879)
        self.addItem(self.mdRedTFMode_l880_909)
        self.mdRedTFMode_l880_909.ident = "OSI-0518"
        self.mdRedTFMode_l880_909.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l880_909)
        self.addItem(self.mdRedTFMode_l910_934)
        self.mdRedTFMode_l910_934.ident = "OSI-0519"
        self.mdRedTFMode_l910_934.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l910_934)
        self.addItem(self.vlRedLamda_Range651)
        self.vlRedLamda_Range651.ident = "OSI-0520"
        self.vlRedLamda_Range651.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range651)
        self.addItem(self.mdRedLamdaMode_l651_799)
        self.mdRedLamdaMode_l651_799.ident = "OSI-0521"
        self.mdRedLamdaMode_l651_799.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l651_799)
        self.addItem(self.mdRedLamdaMode_l800_819)
        self.mdRedLamdaMode_l800_819.ident = "OSI-0522"
        self.mdRedLamdaMode_l800_819.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l800_819)
        self.addItem(self.mdRedLamdaMode_l820_839)
        self.mdRedLamdaMode_l820_839.ident = "OSI-0523"
        self.mdRedLamdaMode_l820_839.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l820_839)
        self.addItem(self.mdRedLamdaMode_l840_879)
        self.mdRedLamdaMode_l840_879.ident = "OSI-0524"
        self.mdRedLamdaMode_l840_879.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l840_879)
        self.addItem(self.mdRedLamdaMode_l880_909)
        self.mdRedLamdaMode_l880_909.ident = "OSI-0525"
        self.mdRedLamdaMode_l880_909.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l880_909)
        self.addItem(self.mdRedLamdaMode_l910_934)
        self.mdRedLamdaMode_l910_934.ident = "OSI-0526"
        self.mdRedLamdaMode_l910_934.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l910_934)
        self.addItem(self.vlRedLamda_Range800)
        self.vlRedLamda_Range800.ident = "OSI-0527"
        self.vlRedLamda_Range800.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range800)
        self.addItem(self.vlRedLamda_Range820)
        self.vlRedLamda_Range820.ident = "OSI-0528"
        self.vlRedLamda_Range820.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range820)
        self.addItem(self.vlRedLamda_Range840)
        self.vlRedLamda_Range840.ident = "OSI-0529"
        self.vlRedLamda_Range840.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range840)
        self.addItem(self.vlRedLamda_Range880)
        self.vlRedLamda_Range880.ident = "OSI-0530"
        self.vlRedLamda_Range880.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range880)
        self.addItem(self.vlRedLamda_Range910)
        self.vlRedLamda_Range910.ident = "OSI-0531"
        self.vlRedLamda_Range910.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range910)
        self.addItem(self.vlBlueFWHM_0_8)
        self.vlBlueFWHM_0_8.ident = "OSI-0532"
        self.vlBlueFWHM_0_8.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_8)
        self.addItem(self.mdBlueFWHMMode_l0_8)
        self.mdBlueFWHMMode_l0_8.ident = "OSI-0533"
        self.mdBlueFWHMMode_l0_8.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_8)
        self.addItem(self.mdBlueFWHMMode_l0_85)
        self.mdBlueFWHMMode_l0_85.ident = "OSI-0534"
        self.mdBlueFWHMMode_l0_85.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_85)
        self.addItem(self.mdBlueFWHMMode_l0_50)
        self.mdBlueFWHMMode_l0_50.ident = "OSI-0536"
        self.mdBlueFWHMMode_l0_50.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_50)
        self.addItem(self.mdBlueFWHMMode_l0_45)
        self.mdBlueFWHMMode_l0_45.ident = "OSI-0537"
        self.mdBlueFWHMMode_l0_45.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_45)
        self.addItem(self.vlBlueFWHM_0_85)
        self.vlBlueFWHM_0_85.ident = "OSI-0539"
        self.vlBlueFWHM_0_85.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_85)
        self.addItem(self.vlBlueFWHM_0_50)
        self.vlBlueFWHM_0_50.ident = "OSI-0540"
        self.vlBlueFWHM_0_50.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_50)
        self.addItem(self.vlBlueFWHM_0_45)
        self.vlBlueFWHM_0_45.ident = "OSI-0541"
        self.vlBlueFWHM_0_45.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_45)
        self.addItem(self.vlBlueFWHM_0_70)
        self.vlBlueFWHM_0_70.ident = "OSI-0542"
        self.vlBlueFWHM_0_70.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_70)
        self.addItem(self.mdBlueFWHMMode_l0_70)
        self.mdBlueFWHMMode_l0_70.ident = "OSI-0543"
        self.mdBlueFWHMMode_l0_70.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_70)
        self.addItem(self.mdBlueFWHMMode_l0_90)
        self.mdBlueFWHMMode_l0_90.ident = "OSI-0544"
        self.mdBlueFWHMMode_l0_90.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_90)
        self.addItem(self.mdBlueFWHMMode_l1_10)
        self.mdBlueFWHMMode_l1_10.ident = "OSI-0545"
        self.mdBlueFWHMMode_l1_10.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l1_10)
        self.addItem(self.vlBlueFWHM_0_90)
        self.vlBlueFWHM_0_90.ident = "OSI-0546"
        self.vlBlueFWHM_0_90.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_90)
        self.addItem(self.vlBlueFWHM_1_10)
        self.vlBlueFWHM_1_10.ident = "OSI-0547"
        self.vlBlueFWHM_1_10.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_1_10)
        self.addItem(self.mdBlueTFMode_l448_463)
        self.mdBlueTFMode_l448_463.ident = "OSI-0548"
        self.mdBlueTFMode_l448_463.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l448_463)
        self.addItem(self.mdBlueTFMode_l464_480)
        self.mdBlueTFMode_l464_480.ident = "OSI-0549"
        self.mdBlueTFMode_l464_480.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l464_480)
        self.addItem(self.mdBlueTFMode_l481_502)
        self.mdBlueTFMode_l481_502.ident = "OSI-0550"
        self.mdBlueTFMode_l481_502.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l481_502)
        self.addItem(self.mdBlueTFMode_l503_521)
        self.mdBlueTFMode_l503_521.ident = "OSI-0551"
        self.mdBlueTFMode_l503_521.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l503_521)
        self.addItem(self.mdBlueTFMode_l522_542)
        self.mdBlueTFMode_l522_542.ident = "OSI-0552"
        self.mdBlueTFMode_l522_542.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l522_542)
        self.addItem(self.mdBlueTFMode_l543_583)
        self.mdBlueTFMode_l543_583.ident = "OSI-0553"
        self.mdBlueTFMode_l543_583.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l543_583)
        self.addItem(self.vlBlueLamda_Range448)
        self.vlBlueLamda_Range448.ident = "OSI-0554"
        self.vlBlueLamda_Range448.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range448)
        self.addItem(self.mdBlueLamdaMode_l448_463)
        self.mdBlueLamdaMode_l448_463.ident = "OSI-0555"
        self.mdBlueLamdaMode_l448_463.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l448_463)
        self.addItem(self.mdBlueLamdaMode_l464_480)
        self.mdBlueLamdaMode_l464_480.ident = "OSI-0556"
        self.mdBlueLamdaMode_l464_480.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l464_480)
        self.addItem(self.mdBlueLamdaMode_l481_502)
        self.mdBlueLamdaMode_l481_502.ident = "OSI-0557"
        self.mdBlueLamdaMode_l481_502.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l481_502)
        self.addItem(self.mdBlueLamdaMode_l503_521)
        self.mdBlueLamdaMode_l503_521.ident = "OSI-0558"
        self.mdBlueLamdaMode_l503_521.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l503_521)
        self.addItem(self.mdBlueLamdaMode_l522_542)
        self.mdBlueLamdaMode_l522_542.ident = "OSI-0559"
        self.mdBlueLamdaMode_l522_542.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l522_542)
        self.addItem(self.mdBlueLamdaMode_l543_583)
        self.mdBlueLamdaMode_l543_583.ident = "OSI-0560"
        self.mdBlueLamdaMode_l543_583.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l543_583)
        self.addItem(self.vlBlueLamda_Range464)
        self.vlBlueLamda_Range464.ident = "OSI-0561"
        self.vlBlueLamda_Range464.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range464)
        self.addItem(self.vlBlueLamda_Range481)
        self.vlBlueLamda_Range481.ident = "OSI-0562"
        self.vlBlueLamda_Range481.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range481)
        self.addItem(self.vlBlueLamda_Range503)
        self.vlBlueLamda_Range503.ident = "OSI-0563"
        self.vlBlueLamda_Range503.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range503)
        self.addItem(self.vlBlueLamda_Range522)
        self.vlBlueLamda_Range522.ident = "OSI-0564"
        self.vlBlueLamda_Range522.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range522)
        self.addItem(self.vlBlueLamda_Range543)
        self.vlBlueLamda_Range543.ident = "OSI-0565"
        self.vlBlueLamda_Range543.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range543)
        self.addItem(self.mdBlueLamdaMode_l584_609)
        self.mdBlueLamdaMode_l584_609.ident = "OSI-0566"
        self.mdBlueLamdaMode_l584_609.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l584_609)
        self.addItem(self.mdBlueLamdaMode_l610_637)
        self.mdBlueLamdaMode_l610_637.ident = "OSI-0567"
        self.mdBlueLamdaMode_l610_637.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l610_637)
        self.addItem(self.mdBlueLamdaMode_l638_671)
        self.mdBlueLamdaMode_l638_671.ident = "OSI-0568"
        self.mdBlueLamdaMode_l638_671.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l638_671)
        self.addItem(self.vlBlueLamda_Range584)
        self.vlBlueLamda_Range584.ident = "OSI-0569"
        self.vlBlueLamda_Range584.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range584)
        self.addItem(self.vlBlueLamda_Range610)
        self.vlBlueLamda_Range610.ident = "OSI-0570"
        self.vlBlueLamda_Range610.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range610)
        self.addItem(self.vlBlueLamda_Range638)
        self.vlBlueLamda_Range638.ident = "OSI-0571"
        self.vlBlueLamda_Range638.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range638)
        self.addItem(self.mdBlueTFMode_l584_609)
        self.mdBlueTFMode_l584_609.ident = "OSI-0572"
        self.mdBlueTFMode_l584_609.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l584_609)
        self.addItem(self.mdBlueTFMode_l610_637)
        self.mdBlueTFMode_l610_637.ident = "OSI-0573"
        self.mdBlueTFMode_l610_637.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l610_637)
        self.addItem(self.mdBlueTFMode_l638_671)
        self.mdBlueTFMode_l638_671.ident = "OSI-0574"
        self.mdBlueTFMode_l638_671.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l638_671)
        self.addItem(self.mdPreOpticsMode_RTFCalib)
        self.mdPreOpticsMode_RTFCalib.ident = "OP-0105"
        self.mdPreOpticsMode_RTFCalib.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_RTFCalib)
        self.addItem(self.mdPreOpticsMode_BTFCalib)
        self.mdPreOpticsMode_BTFCalib.ident = "OP-0106"
        self.mdPreOpticsMode_BTFCalib.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_BTFCalib)
        self.addItem(self.vlzzero_NormalRange)
        self.vlzzero_NormalRange.ident = "OP-0107"
        self.vlzzero_NormalRange.description = ""
        self.przzero.addValue(self.vlzzero_NormalRange)
        self.addItem(self.mdzzeroMode_Normal)
        self.mdzzeroMode_Normal.ident = "OP-0108"
        self.mdzzeroMode_Normal.description = ""
        self.przzero.addMode(self.mdzzeroMode_Normal)
        self.addItem(self.mdFiltersMode_OS)
        self.mdFiltersMode_OS.ident = "OSI-0143"
        self.mdFiltersMode_OS.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_OS)
        self.addItem(self.mdFiltersMode_UFilter)
        self.mdFiltersMode_UFilter.ident = "OSI-0145"
        self.mdFiltersMode_UFilter.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_UFilter)
        self.addItem(self.vlUFilters_U500_17)
        self.vlUFilters_U500_17.ident = "OSI-0033"
        self.vlUFilters_U500_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U500_17)
        self.addItem(self.vlUFilters_U517_17)
        self.vlUFilters_U517_17.ident = "OSI-0034"
        self.vlUFilters_U517_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U517_17)
        self.addItem(self.vlUFilters_U534_17)
        self.vlUFilters_U534_17.ident = "OSI-0035"
        self.vlUFilters_U534_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U534_17)
        self.addItem(self.vlUFilters_U551_17)
        self.vlUFilters_U551_17.ident = "OSI-0036"
        self.vlUFilters_U551_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U551_17)
        self.addItem(self.vlUFilters_U568_17)
        self.vlUFilters_U568_17.ident = "OSI-0037"
        self.vlUFilters_U568_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U568_17)
        self.addItem(self.vlUFilters_U585_17)
        self.vlUFilters_U585_17.ident = "OSI-0038"
        self.vlUFilters_U585_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U585_17)
        self.addItem(self.vlUFilters_U602_17)
        self.vlUFilters_U602_17.ident = "OSI-0039"
        self.vlUFilters_U602_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U602_17)
        self.addItem(self.vlUFilters_U619_17)
        self.vlUFilters_U619_17.ident = "OSI-0040"
        self.vlUFilters_U619_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U619_17)
        self.addItem(self.vlUFilters_U636_17)
        self.vlUFilters_U636_17.ident = "OSI-0041"
        self.vlUFilters_U636_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U636_17)
        self.addItem(self.vlUFilters_U653_17)
        self.vlUFilters_U653_17.ident = "OSI-0042"
        self.vlUFilters_U653_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U653_17)
        self.addItem(self.vlUFilters_U670_17)
        self.vlUFilters_U670_17.ident = "OSI-0043"
        self.vlUFilters_U670_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U670_17)
        self.addItem(self.vlUFilters_U687_17)
        self.vlUFilters_U687_17.ident = "OSI-0044"
        self.vlUFilters_U687_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U687_17)
        self.addItem(self.vlUFilters_U704_17)
        self.vlUFilters_U704_17.ident = "OSI-0045"
        self.vlUFilters_U704_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U704_17)
        self.addItem(self.vlUFilters_U721_17)
        self.vlUFilters_U721_17.ident = "OSI-0046"
        self.vlUFilters_U721_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U721_17)
        self.addItem(self.vlUFilters_U738_17)
        self.vlUFilters_U738_17.ident = "OSI-0047"
        self.vlUFilters_U738_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U738_17)
        self.addItem(self.vlUFilters_U755_17)
        self.vlUFilters_U755_17.ident = "OSI-0048"
        self.vlUFilters_U755_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U755_17)
        self.addItem(self.vlUFilters_U772_17)
        self.vlUFilters_U772_17.ident = "OSI-0049"
        self.vlUFilters_U772_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U772_17)
        self.addItem(self.vlUFilters_U789_17)
        self.vlUFilters_U789_17.ident = "OSI-0050"
        self.vlUFilters_U789_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U789_17)
        self.addItem(self.vlUFilters_U806_17)
        self.vlUFilters_U806_17.ident = "OSI-0051"
        self.vlUFilters_U806_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U806_17)
        self.addItem(self.vlUFilters_U823_17)
        self.vlUFilters_U823_17.ident = "OSI-0052"
        self.vlUFilters_U823_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U823_17)
        self.addItem(self.vlUFilters_U840_17)
        self.vlUFilters_U840_17.ident = "OSI-0053"
        self.vlUFilters_U840_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U840_17)
        self.addItem(self.vlUFilters_U857_17)
        self.vlUFilters_U857_17.ident = "OSI-0054"
        self.vlUFilters_U857_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U857_17)
        self.addItem(self.vlUFilters_U883_35)
        self.vlUFilters_U883_35.ident = "OSI-0055"
        self.vlUFilters_U883_35.description = ""
        self.prUFilters.addValue(self.vlUFilters_U883_35)
        self.addItem(self.vlUFilters_U913_25)
        self.vlUFilters_U913_25.ident = "OSI-0056"
        self.vlUFilters_U913_25.description = ""
        self.prUFilters.addValue(self.vlUFilters_U913_25)
        self.addItem(self.vlUFilters_U941_33)
        self.vlUFilters_U941_33.ident = "OSI-0057"
        self.vlUFilters_U941_33.description = ""
        self.prUFilters.addValue(self.vlUFilters_U941_33)
        self.addItem(self.mdUFiltersMode_U5xx)
        self.mdUFiltersMode_U5xx.ident = "OSI-0148"
        self.mdUFiltersMode_U5xx.description = ""
        self.prUFilters.addMode(self.mdUFiltersMode_U5xx)
        self.addItem(self.mdUFiltersMode_U6xx)
        self.mdUFiltersMode_U6xx.ident = "OSI-0149"
        self.mdUFiltersMode_U6xx.description = ""
        self.prUFilters.addMode(self.mdUFiltersMode_U6xx)
        self.addItem(self.mdUFiltersMode_U7xx)
        self.mdUFiltersMode_U7xx.ident = "OSI-0150"
        self.mdUFiltersMode_U7xx.description = ""
        self.prUFilters.addMode(self.mdUFiltersMode_U7xx)
        self.addItem(self.mdUFiltersMode_U8xx)
        self.mdUFiltersMode_U8xx.ident = "OSI-0151"
        self.mdUFiltersMode_U8xx.description = ""
        self.prUFilters.addMode(self.mdUFiltersMode_U8xx)
        self.addItem(self.mdUFiltersMode_U9xx)
        self.mdUFiltersMode_U9xx.ident = "OSI-0152"
        self.mdUFiltersMode_U9xx.description = ""
        self.prUFilters.addMode(self.mdUFiltersMode_U9xx)
        self.addItem(self.vlOS_f504_16)
        self.vlOS_f504_16.ident = "OSI-0071"
        self.vlOS_f504_16.description = ""
        self.prOS.addValue(self.vlOS_f504_16)
        self.addItem(self.vlOS_f509_16)
        self.vlOS_f509_16.ident = "OSI-0072"
        self.vlOS_f509_16.description = ""
        self.prOS.addValue(self.vlOS_f509_16)
        self.addItem(self.vlOS_f514_16)
        self.vlOS_f514_16.ident = "OSI-0073"
        self.vlOS_f514_16.description = ""
        self.prOS.addValue(self.vlOS_f514_16)
        self.addItem(self.vlOS_f519_16)
        self.vlOS_f519_16.ident = "OSI-0074"
        self.vlOS_f519_16.description = ""
        self.prOS.addValue(self.vlOS_f519_16)
        self.addItem(self.vlOS_f525_17)
        self.vlOS_f525_17.ident = "OSI-0075"
        self.vlOS_f525_17.description = ""
        self.prOS.addValue(self.vlOS_f525_17)
        self.addItem(self.vlOS_f530_17)
        self.vlOS_f530_17.ident = "OSI-0076"
        self.vlOS_f530_17.description = ""
        self.prOS.addValue(self.vlOS_f530_17)
        self.addItem(self.vlOS_f536_17)
        self.vlOS_f536_17.ident = "OSI-0077"
        self.vlOS_f536_17.description = ""
        self.prOS.addValue(self.vlOS_f536_17)
        self.addItem(self.vlOS_f542_18)
        self.vlOS_f542_18.ident = "OSI-0078"
        self.vlOS_f542_18.description = ""
        self.prOS.addValue(self.vlOS_f542_18)
        self.addItem(self.vlOS_f548_18)
        self.vlOS_f548_18.ident = "OSI-0079"
        self.vlOS_f548_18.description = ""
        self.prOS.addValue(self.vlOS_f548_18)
        self.addItem(self.vlOS_f554_18)
        self.vlOS_f554_18.ident = "OSI-0080"
        self.vlOS_f554_18.description = ""
        self.prOS.addValue(self.vlOS_f554_18)
        self.addItem(self.vlOS_f561_19)
        self.vlOS_f561_19.ident = "OSI-0081"
        self.vlOS_f561_19.description = ""
        self.prOS.addValue(self.vlOS_f561_19)
        self.addItem(self.vlOS_f568_19)
        self.vlOS_f568_19.ident = "OSI-0082"
        self.vlOS_f568_19.description = ""
        self.prOS.addValue(self.vlOS_f568_19)
        self.addItem(self.vlOS_f575_19)
        self.vlOS_f575_19.ident = "OSI-0083"
        self.vlOS_f575_19.description = ""
        self.prOS.addValue(self.vlOS_f575_19)
        self.addItem(self.vlOS_f583_20)
        self.vlOS_f583_20.ident = "OSI-0084"
        self.vlOS_f583_20.description = ""
        self.prOS.addValue(self.vlOS_f583_20)
        self.addItem(self.vlOS_f591_21)
        self.vlOS_f591_21.ident = "OSI-0085"
        self.vlOS_f591_21.description = ""
        self.prOS.addValue(self.vlOS_f591_21)
        self.addItem(self.vlOS_f599_22)
        self.vlOS_f599_22.ident = "OSI-0086"
        self.vlOS_f599_22.description = ""
        self.prOS.addValue(self.vlOS_f599_22)
        self.addItem(self.mdOSMode_f5xx)
        self.mdOSMode_f5xx.ident = "OSI-0153"
        self.mdOSMode_f5xx.description = ""
        self.prOS.addMode(self.mdOSMode_f5xx)
        self.addItem(self.vlOS_f477_14)
        self.vlOS_f477_14.ident = "OSI-0065"
        self.vlOS_f477_14.description = ""
        self.prOS.addValue(self.vlOS_f477_14)
        self.addItem(self.vlOS_f481_14)
        self.vlOS_f481_14.ident = "OSI-0066"
        self.vlOS_f481_14.description = ""
        self.prOS.addValue(self.vlOS_f481_14)
        self.addItem(self.mdOSMode_f4xx)
        self.mdOSMode_f4xx.ident = "OSI-0154"
        self.mdOSMode_f4xx.description = ""
        self.prOS.addMode(self.mdOSMode_f4xx)
        self.addItem(self.vlOS_f486_14)
        self.vlOS_f486_14.ident = "OSI-0067"
        self.vlOS_f486_14.description = ""
        self.prOS.addValue(self.vlOS_f486_14)
        self.addItem(self.vlOS_f469_14)
        self.vlOS_f469_14.ident = "OSI-0063"
        self.vlOS_f469_14.description = ""
        self.prOS.addValue(self.vlOS_f469_14)
        self.addItem(self.vlOS_f461_13)
        self.vlOS_f461_13.ident = "OSI-0061"
        self.vlOS_f461_13.description = ""
        self.prOS.addValue(self.vlOS_f461_13)
        self.addItem(self.vlOS_f499_15)
        self.vlOS_f499_15.ident = "OSI-0070"
        self.vlOS_f499_15.description = ""
        self.prOS.addValue(self.vlOS_f499_15)
        self.addItem(self.vlOS_f454_13)
        self.vlOS_f454_13.ident = "OSI-0059"
        self.vlOS_f454_13.description = ""
        self.prOS.addValue(self.vlOS_f454_13)
        self.addItem(self.vlOS_f451_13)
        self.vlOS_f451_13.ident = "OSI-0058"
        self.vlOS_f451_13.description = ""
        self.prOS.addValue(self.vlOS_f451_13)
        self.addItem(self.vlOS_f495_15)
        self.vlOS_f495_15.ident = "OSI-0069"
        self.vlOS_f495_15.description = ""
        self.prOS.addValue(self.vlOS_f495_15)
        self.addItem(self.vlOS_f465_13)
        self.vlOS_f465_13.ident = "OSI-0062"
        self.vlOS_f465_13.description = ""
        self.prOS.addValue(self.vlOS_f465_13)
        self.addItem(self.vlOS_f490_15)
        self.vlOS_f490_15.ident = "OSI-0068"
        self.vlOS_f490_15.description = ""
        self.prOS.addValue(self.vlOS_f490_15)
        self.addItem(self.vlOS_f458_13)
        self.vlOS_f458_13.ident = "OSI-0060"
        self.vlOS_f458_13.description = ""
        self.prOS.addValue(self.vlOS_f458_13)
        self.addItem(self.vlOS_f473_14)
        self.vlOS_f473_14.ident = "OSI-0064"
        self.vlOS_f473_14.description = ""
        self.prOS.addValue(self.vlOS_f473_14)
        self.addItem(self.vlOS_f638_25)
        self.vlOS_f638_25.ident = "OSI-0090"
        self.vlOS_f638_25.description = ""
        self.prOS.addValue(self.vlOS_f638_25)
        self.addItem(self.vlOS_f680_43)
        self.vlOS_f680_43.ident = "OSI-0095"
        self.vlOS_f680_43.description = ""
        self.prOS.addValue(self.vlOS_f680_43)
        self.addItem(self.vlOS_f608_22)
        self.vlOS_f608_22.ident = "OSI-0087"
        self.vlOS_f608_22.description = ""
        self.prOS.addValue(self.vlOS_f608_22)
        self.addItem(self.vlOS_f627_24)
        self.vlOS_f627_24.ident = "OSI-0089"
        self.vlOS_f627_24.description = ""
        self.prOS.addValue(self.vlOS_f627_24)
        self.addItem(self.vlOS_f694_44)
        self.vlOS_f694_44.ident = "OSI-0096"
        self.vlOS_f694_44.description = ""
        self.prOS.addValue(self.vlOS_f694_44)
        self.addItem(self.vlOS_f617_23)
        self.vlOS_f617_23.ident = "OSI-0088"
        self.vlOS_f617_23.description = ""
        self.prOS.addValue(self.vlOS_f617_23)
        self.addItem(self.vlOS_f666_36)
        self.vlOS_f666_36.ident = "OSI-0094"
        self.vlOS_f666_36.description = ""
        self.prOS.addValue(self.vlOS_f666_36)
        self.addItem(self.vlOS_f649_25)
        self.vlOS_f649_25.ident = "OSI-0091"
        self.vlOS_f649_25.description = ""
        self.prOS.addValue(self.vlOS_f649_25)
        self.addItem(self.vlOS_f657_35)
        self.vlOS_f657_35.ident = "OSI-0093"
        self.vlOS_f657_35.description = ""
        self.prOS.addValue(self.vlOS_f657_35)
        self.addItem(self.mdOSMode_f6xx)
        self.mdOSMode_f6xx.ident = "OSI-0155"
        self.mdOSMode_f6xx.description = ""
        self.prOS.addMode(self.mdOSMode_f6xx)
        self.addItem(self.vlOS_f661_27)
        self.vlOS_f661_27.ident = "OSI-0092"
        self.vlOS_f661_27.description = ""
        self.prOS.addValue(self.vlOS_f661_27)
        self.addItem(self.vlOS_f723_45)
        self.vlOS_f723_45.ident = "OSI-0098"
        self.vlOS_f723_45.description = ""
        self.prOS.addValue(self.vlOS_f723_45)
        self.addItem(self.mdOSMode_f7xx)
        self.mdOSMode_f7xx.ident = "OSI-0156"
        self.mdOSMode_f7xx.description = ""
        self.prOS.addMode(self.mdOSMode_f7xx)
        self.addItem(self.vlOS_f770_50)
        self.vlOS_f770_50.ident = "OSI-0101"
        self.vlOS_f770_50.description = ""
        self.prOS.addValue(self.vlOS_f770_50)
        self.addItem(self.vlOS_f738_49)
        self.vlOS_f738_49.ident = "OSI-0099"
        self.vlOS_f738_49.description = ""
        self.prOS.addValue(self.vlOS_f738_49)
        self.addItem(self.vlOS_f709_45)
        self.vlOS_f709_45.ident = "OSI-0097"
        self.vlOS_f709_45.description = ""
        self.prOS.addValue(self.vlOS_f709_45)
        self.addItem(self.vlOS_f754_50)
        self.vlOS_f754_50.ident = "OSI-0100"
        self.vlOS_f754_50.description = ""
        self.prOS.addValue(self.vlOS_f754_50)
        self.addItem(self.vlOS_f785_48)
        self.vlOS_f785_48.ident = "OSI-0102"
        self.vlOS_f785_48.description = ""
        self.prOS.addValue(self.vlOS_f785_48)
        self.addItem(self.vlOS_f923_34)
        self.vlOS_f923_34.ident = "OSI-0112"
        self.vlOS_f923_34.description = ""
        self.prOS.addValue(self.vlOS_f923_34)
        self.addItem(self.mdOSMode_f9xx)
        self.mdOSMode_f9xx.ident = "OSI-0157"
        self.mdOSMode_f9xx.description = ""
        self.prOS.addMode(self.mdOSMode_f9xx)
        self.addItem(self.vlOS_f932_34)
        self.vlOS_f932_34.ident = "OSI-0114"
        self.vlOS_f932_34.description = ""
        self.prOS.addValue(self.vlOS_f932_34)
        self.addItem(self.vlOS_f927_34)
        self.vlOS_f927_34.ident = "OSI-0113"
        self.vlOS_f927_34.description = ""
        self.prOS.addValue(self.vlOS_f927_34)
        self.addItem(self.vlOS_f902_44)
        self.vlOS_f902_44.ident = "OSI-0109"
        self.vlOS_f902_44.description = ""
        self.prOS.addValue(self.vlOS_f902_44)
        self.addItem(self.vlOS_f919_41)
        self.vlOS_f919_41.ident = "OSI-0111"
        self.vlOS_f919_41.description = ""
        self.prOS.addValue(self.vlOS_f919_41)
        self.addItem(self.vlOS_f910_40)
        self.vlOS_f910_40.ident = "OSI-0110"
        self.vlOS_f910_40.description = ""
        self.prOS.addValue(self.vlOS_f910_40)
        self.addItem(self.vlOS_f802_51)
        self.vlOS_f802_51.ident = "OSI-0103"
        self.vlOS_f802_51.description = ""
        self.prOS.addValue(self.vlOS_f802_51)
        self.addItem(self.vlOS_f878_59)
        self.vlOS_f878_59.ident = "OSI-0107"
        self.vlOS_f878_59.description = ""
        self.prOS.addValue(self.vlOS_f878_59)
        self.addItem(self.vlOS_f858_58)
        self.vlOS_f858_58.ident = "OSI-0106"
        self.vlOS_f858_58.description = ""
        self.prOS.addValue(self.vlOS_f858_58)
        self.addItem(self.vlOS_f893_50)
        self.vlOS_f893_50.ident = "OSI-0108"
        self.vlOS_f893_50.description = ""
        self.prOS.addValue(self.vlOS_f893_50)
        self.addItem(self.vlOS_f838_58)
        self.vlOS_f838_58.ident = "OSI-0105"
        self.vlOS_f838_58.description = ""
        self.prOS.addValue(self.vlOS_f838_58)
        self.addItem(self.vlOS_f819_52)
        self.vlOS_f819_52.ident = "OSI-0104"
        self.vlOS_f819_52.description = ""
        self.prOS.addValue(self.vlOS_f819_52)
        self.addItem(self.mdOSMode_f8xx)
        self.mdOSMode_f8xx.ident = "OSI-0158"
        self.mdOSMode_f8xx.description = ""
        self.prOS.addMode(self.mdOSMode_f8xx)
        self.addItem(self.mdFiltersMode_NoFilter)
        self.mdFiltersMode_NoFilter.ident = "OSI-0389"
        self.mdFiltersMode_NoFilter.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_NoFilter)
        self.addItem(self.mdFiltersMode_GR)
        self.mdFiltersMode_GR.ident = "OSI-0390"
        self.mdFiltersMode_GR.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_GR)
        self.addItem(self.vlBroad_Sloan_u)
        self.vlBroad_Sloan_u.ident = "OSI-0028"
        self.vlBroad_Sloan_u.description = ""
        self.prBroad.addValue(self.vlBroad_Sloan_u)
        self.addItem(self.vlBroad_Sloan_g)
        self.vlBroad_Sloan_g.ident = "OSI-0029"
        self.vlBroad_Sloan_g.description = ""
        self.prBroad.addValue(self.vlBroad_Sloan_g)
        self.addItem(self.vlBroad_Sloan_r)
        self.vlBroad_Sloan_r.ident = "OSI-0030"
        self.vlBroad_Sloan_r.description = ""
        self.prBroad.addValue(self.vlBroad_Sloan_r)
        self.addItem(self.vlBroad_Sloan_i)
        self.vlBroad_Sloan_i.ident = "OSI-0031"
        self.vlBroad_Sloan_i.description = ""
        self.prBroad.addValue(self.vlBroad_Sloan_i)
        self.addItem(self.vlBroad_Sloan_z)
        self.vlBroad_Sloan_z.ident = "OSI-0032"
        self.vlBroad_Sloan_z.description = ""
        self.prBroad.addValue(self.vlBroad_Sloan_z)
        self.addItem(self.mdBroadMode_All)
        self.mdBroadMode_All.ident = "OSI-0618"
        self.mdBroadMode_All.description = ""
        self.prBroad.addMode(self.mdBroadMode_All)
        self.addItem(self.mdFiltersMode_Broad)
        self.mdFiltersMode_Broad.ident = "OSI-0144"
        self.mdFiltersMode_Broad.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_Broad)
        self.addItem(self.mdFiltersMode_OSCalc)
        self.mdFiltersMode_OSCalc.ident = "FILT-0018"
        self.mdFiltersMode_OSCalc.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_OSCalc)
        self.addItem(self.mdDetectorMode_FT)
        self.mdDetectorMode_FT.ident = "OSI-0606"
        self.mdDetectorMode_FT.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_FT)
        self.addItem(self.mdDetectorMode_Window)
        self.mdDetectorMode_Window.ident = "OSI-0414"
        self.mdDetectorMode_Window.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_Window)
        self.addItem(self.mdOutputSourceMode_0x0)
        self.mdOutputSourceMode_0x0.ident = "OSI-0440"
        self.mdOutputSourceMode_0x0.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x0)
        self.addItem(self.mdOutputSourceMode_0x1)
        self.mdOutputSourceMode_0x1.ident = "OSI-0441"
        self.mdOutputSourceMode_0x1.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x1)
        self.addItem(self.mdOutputSourceMode_0x2)
        self.mdOutputSourceMode_0x2.ident = "OSI-0442"
        self.mdOutputSourceMode_0x2.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x2)
        self.addItem(self.mdOutputSourceMode_0x3)
        self.mdOutputSourceMode_0x3.ident = "OSI-0443"
        self.mdOutputSourceMode_0x3.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x3)
        self.addItem(self.mdOutputSourceMode_ALL)
        self.mdOutputSourceMode_ALL.ident = "OSI-0444"
        self.mdOutputSourceMode_ALL.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_ALL)
        self.addItem(self.mdOutputSourceMode_TWO)
        self.mdOutputSourceMode_TWO.ident = "OSI-0445"
        self.mdOutputSourceMode_TWO.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_TWO)
        self.addItem(self.mdRecompositionMode_None)
        self.mdRecompositionMode_None.ident = "OSI-0446"
        self.mdRecompositionMode_None.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_None)
        self.addItem(self.mdRecompositionMode_Serial)
        self.mdRecompositionMode_Serial.ident = "OSI-0448"
        self.mdRecompositionMode_Serial.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_Serial)
        self.addItem(self.mdRecompositionMode_QuadCCD)
        self.mdRecompositionMode_QuadCCD.ident = "OSI-0449"
        self.mdRecompositionMode_QuadCCD.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_QuadCCD)
        self.addItem(self.mdDetectorMode_FullDetector)
        self.mdDetectorMode_FullDetector.ident = "OSI-0413"
        self.mdDetectorMode_FullDetector.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_FullDetector)
        self.addItem(self.mdDetectorMode_WindowSq)
        self.mdDetectorMode_WindowSq.ident = "OSI-0628"
        self.mdDetectorMode_WindowSq.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_WindowSq)
        self.addItem(self.mdDetectorMode_FullDetectorSq)
        self.mdDetectorMode_FullDetectorSq.ident = "OSI-0629"
        self.mdDetectorMode_FullDetectorSq.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_FullDetectorSq)
        self.addItem(self.vlBinning_1x1)
        self.vlBinning_1x1.ident = "OSI-0630"
        self.vlBinning_1x1.description = ""
        self.prBinning.addValue(self.vlBinning_1x1)
        self.addItem(self.vlBinning_1x2)
        self.vlBinning_1x2.ident = "OSI-0631"
        self.vlBinning_1x2.description = ""
        self.prBinning.addValue(self.vlBinning_1x2)
        self.addItem(self.vlBinning_2x1)
        self.vlBinning_2x1.ident = "OSI-0632"
        self.vlBinning_2x1.description = ""
        self.prBinning.addValue(self.vlBinning_2x1)
        self.addItem(self.vlBinning_2x2)
        self.vlBinning_2x2.ident = "OSI-0633"
        self.vlBinning_2x2.description = ""
        self.prBinning.addValue(self.vlBinning_2x2)
        self.addItem(self.mdBinningMode_All)
        self.mdBinningMode_All.ident = "OSI-0634"
        self.mdBinningMode_All.description = ""
        self.prBinning.addMode(self.mdBinningMode_All)
        self.addItem(self.mdBinningMode_Square)
        self.mdBinningMode_Square.ident = "OSI-0635"
        self.mdBinningMode_Square.description = ""
        self.prBinning.addMode(self.mdBinningMode_Square)
        self.addItem(self.mdBinningMode_Off)
        self.mdBinningMode_Off.ident = "OSI-0636"
        self.mdBinningMode_Off.description = ""
        self.prBinning.addMode(self.mdBinningMode_Off)
        self.addItem(self.mdWindowMode_Enabled)
        self.mdWindowMode_Enabled.ident = "OSI-0460"
        self.mdWindowMode_Enabled.description = ""
        self.sysWindow.addMode(self.mdWindowMode_Enabled)
        self.addItem(self.mdRowsMode_Normal)
        self.mdRowsMode_Normal.ident = "OSI-0419"
        self.mdRowsMode_Normal.description = ""
        self.prRows.addMode(self.mdRowsMode_Normal)
        self.addItem(self.vlRows_FullRange)
        self.vlRows_FullRange.ident = "OSI-0420"
        self.vlRows_FullRange.description = ""
        self.prRows.addValue(self.vlRows_FullRange)
        self.addItem(self.mdColsMode_Normal)
        self.mdColsMode_Normal.ident = "OSI-0415"
        self.mdColsMode_Normal.description = ""
        self.prCols.addMode(self.mdColsMode_Normal)
        self.addItem(self.vlCols_FullRange)
        self.vlCols_FullRange.ident = "OSI-0416"
        self.vlCols_FullRange.description = ""
        self.prCols.addValue(self.vlCols_FullRange)
        self.addItem(self.mdoffsetRowMode_Normal)
        self.mdoffsetRowMode_Normal.ident = "OSI-0417"
        self.mdoffsetRowMode_Normal.description = ""
        self.proffsetRow.addMode(self.mdoffsetRowMode_Normal)
        self.addItem(self.vloffsetRow_FullRange)
        self.vloffsetRow_FullRange.ident = "OSI-0418"
        self.vloffsetRow_FullRange.description = ""
        self.proffsetRow.addValue(self.vloffsetRow_FullRange)
        self.addItem(self.mdoffsetColMode_Normal)
        self.mdoffsetColMode_Normal.ident = "OSI-0421"
        self.mdoffsetColMode_Normal.description = ""
        self.proffsetCol.addMode(self.mdoffsetColMode_Normal)
        self.addItem(self.vloffsetCol_FullRange)
        self.vloffsetCol_FullRange.ident = "OSI-0422"
        self.vloffsetCol_FullRange.description = ""
        self.proffsetCol.addValue(self.vloffsetCol_FullRange)
        self.addItem(self.mdWindowMode_Disabled)
        self.mdWindowMode_Disabled.ident = "GEOM-0002"
        self.mdWindowMode_Disabled.description = ""
        self.sysWindow.addMode(self.mdWindowMode_Disabled)
        self.addItem(self.mdDetectorMode_Engineering)
        self.mdDetectorMode_Engineering.ident = "ENG-1"
        self.mdDetectorMode_Engineering.description = "Detector engineering mode"
        self.sysDetector.addMode(self.mdDetectorMode_Engineering)
        self.addItem(self.mdOutputSourceMode_Engineering)
        self.mdOutputSourceMode_Engineering.ident = "ENG-2"
        self.mdOutputSourceMode_Engineering.description = "OutputSource engineering mode"
        self.sysOutputSource.addMode(self.mdOutputSourceMode_Engineering)
        self.addItem(self.mdWindowMode_Engineering)
        self.mdWindowMode_Engineering.ident = "ENG-3"
        self.mdWindowMode_Engineering.description = "Window engineering mode"
        self.sysWindow.addMode(self.mdWindowMode_Engineering)
        self.addItem(self.mdDASMode_Engineering)
        self.mdDASMode_Engineering.ident = "ENG-4"
        self.mdDASMode_Engineering.description = "DAS engineering mode"
        self.sysDAS.addMode(self.mdDASMode_Engineering)
        self.addItem(self.mdAcquisitionMode_Engineering)
        self.mdAcquisitionMode_Engineering.ident = "ENG-5"
        self.mdAcquisitionMode_Engineering.description = "Acquisition engineering mode"
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Engineering)
        self.addItem(self.mdMultipleExposureMode_Engineering)
        self.mdMultipleExposureMode_Engineering.ident = "ENG-6"
        self.mdMultipleExposureMode_Engineering.description = "MultipleExposure engineering mode"
        self.sysMultipleExposure.addMode(self.mdMultipleExposureMode_Engineering)
        self.addItem(self.mdProcessMonitorMode_Engineering)
        self.mdProcessMonitorMode_Engineering.ident = "ENG-7"
        self.mdProcessMonitorMode_Engineering.description = "ProcessMonitor engineering mode"
        self.sysProcessMonitor.addMode(self.mdProcessMonitorMode_Engineering)
        self.addItem(self.mdPreOpticsMode_Engineering)
        self.mdPreOpticsMode_Engineering.ident = "ENG-8"
        self.mdPreOpticsMode_Engineering.description = "PreOptics engineering mode"
        self.sysPreOptics.addMode(self.mdPreOpticsMode_Engineering)
        self.addItem(self.mdRedTFMode_Engineering)
        self.mdRedTFMode_Engineering.ident = "ENG-9"
        self.mdRedTFMode_Engineering.description = "RedTF engineering mode"
        self.sysRedTF.addMode(self.mdRedTFMode_Engineering)
        self.addItem(self.mdBlueTFMode_Engineering)
        self.mdBlueTFMode_Engineering.ident = "ENG-10"
        self.mdBlueTFMode_Engineering.description = "BlueTF engineering mode"
        self.sysBlueTF.addMode(self.mdBlueTFMode_Engineering)
        self.addItem(self.mdOsirisMode_Engineering)
        self.mdOsirisMode_Engineering.ident = "ENG-11"
        self.mdOsirisMode_Engineering.description = "Osiris engineering mode"
        self.sysOsiris.addMode(self.mdOsirisMode_Engineering)
        self.addItem(self.mdObservingModesMode_Engineering)
        self.mdObservingModesMode_Engineering.ident = "ENG-12"
        self.mdObservingModesMode_Engineering.description = "ObservingModes engineering mode"
        self.sysObservingModes.addMode(self.mdObservingModesMode_Engineering)
        self.addItem(self.mdAcquisitionModesMode_Engineering)
        self.mdAcquisitionModesMode_Engineering.ident = "ENG-13"
        self.mdAcquisitionModesMode_Engineering.description = "AcquisitionModes engineering mode"
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_Engineering)
        self.addItem(self.mdFiltersMode_Engineering)
        self.mdFiltersMode_Engineering.ident = "ENG-14"
        self.mdFiltersMode_Engineering.description = "Filters engineering mode"
        self.sysFilters.addMode(self.mdFiltersMode_Engineering)
        self.addItem(self.mdFPEMode_Engineering)
        self.mdFPEMode_Engineering.ident = "ENG-15"
        self.mdFPEMode_Engineering.description = "FPE engineering mode"
        self.sysFPE.addMode(self.mdFPEMode_Engineering)
        # Marcamos ObservingModesMode_FastBBI como elegible para OsirisMode_Imaging
        self.mdOsirisMode_Imaging.addSubMode(self.mdObservingModesMode_FastBBI)
        # Marcamos ObservingModesMode_TFI como elegible para OsirisMode_Imaging
        self.mdOsirisMode_Imaging.addSubMode(self.mdObservingModesMode_TFI)
        # Marcamos ObservingModesMode_BBI como elegible para OsirisMode_Imaging
        self.mdOsirisMode_Imaging.addSubMode(self.mdObservingModesMode_BBI)
        # Marcamos ObservingModesMode_FrTrTFI como elegible para OsirisMode_Imaging
        self.mdOsirisMode_Imaging.addSubMode(self.mdObservingModesMode_FrTrTFI)
        # Marcamos ObservingModesMode_FastTFImage como elegible para OsirisMode_Imaging
        self.mdOsirisMode_Imaging.addSubMode(self.mdObservingModesMode_FastTFImage)
        # Marcamos ObservingModesMode_FrTrBBI como elegible para OsirisMode_Imaging
        self.mdOsirisMode_Imaging.addSubMode(self.mdObservingModesMode_FrTrBBI)
        # Marcamos ObservingModesMode_FastLSSpec como elegible para OsirisMode_Spectroscopy
        self.mdOsirisMode_Spectroscopy.addSubMode(self.mdObservingModesMode_FastLSSpec)
        # Marcamos ObservingModesMode_MOS como elegible para OsirisMode_Spectroscopy
        self.mdOsirisMode_Spectroscopy.addSubMode(self.mdObservingModesMode_MOS)
        # Marcamos ObservingModesMode_LSSpec como elegible para OsirisMode_Spectroscopy
        self.mdOsirisMode_Spectroscopy.addSubMode(self.mdObservingModesMode_LSSpec)
        # Marcamos ObservingModesMode_CalibLamp como elegible para OsirisMode_Calibration
        self.mdOsirisMode_Calibration.addSubMode(self.mdObservingModesMode_CalibLamp)
        # Marcamos ObservingModesMode_TFCalib como elegible para OsirisMode_Calibration
        self.mdOsirisMode_Calibration.addSubMode(self.mdObservingModesMode_TFCalib)
        # Marcamos ObservingModesMode_SkyFlat como elegible para OsirisMode_Calibration
        self.mdOsirisMode_Calibration.addSubMode(self.mdObservingModesMode_SkyFlat)
        # Marcamos ObservingModesMode_SpectralFlat como elegible para OsirisMode_Calibration
        self.mdOsirisMode_Calibration.addSubMode(self.mdObservingModesMode_SpectralFlat)
        # Marcamos ObservingModesMode_Bias como elegible para OsirisMode_Calibration
        self.mdOsirisMode_Calibration.addSubMode(self.mdObservingModesMode_Bias)
        # Marcamos ObservingModesMode_Dark como elegible para OsirisMode_Calibration
        self.mdOsirisMode_Calibration.addSubMode(self.mdObservingModesMode_Dark)
        # Marcamos ObservingModesMode_DomeFlat como elegible para OsirisMode_Calibration
        self.mdOsirisMode_Calibration.addSubMode(self.mdObservingModesMode_DomeFlat)
        # Marcamos ObservingModesMode_BBI como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_BBI)
        # Marcamos ObservingModesMode_TFI como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_TFI)
        # Marcamos ObservingModesMode_LSSpec como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_LSSpec)
        # Marcamos ObservingModesMode_MOS como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_MOS)
        # Marcamos ObservingModesMode_FastBBI como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_FastBBI)
        # Marcamos ObservingModesMode_FrTrBBI como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_FrTrBBI)
        # Marcamos ObservingModesMode_FastLSSpec como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_FastLSSpec)
        # Marcamos ObservingModesMode_FastTFImage como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_FastTFImage)
        # Marcamos ObservingModesMode_FrTrTFI como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_FrTrTFI)
        # Marcamos ObservingModesMode_Bias como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_Bias)
        # Marcamos ObservingModesMode_Dark como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_Dark)
        # Marcamos ObservingModesMode_DomeFlat como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_DomeFlat)
        # Marcamos ObservingModesMode_SkyFlat como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_SkyFlat)
        # Marcamos ObservingModesMode_SpectralFlat como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_SpectralFlat)
        # Marcamos ObservingModesMode_CalibLamp como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_CalibLamp)
        # Marcamos ObservingModesMode_TFCalib como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_TFCalib)
        # Marcamos ObservingModesMode_Engineering como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_Engineering)
        # Marcamos AcquisitionModesMode_aBBI como elegible para ObservingModesMode_BBI
        self.mdObservingModesMode_BBI.addSubMode(self.mdAcquisitionModesMode_aBBI)
        # Marcamos AcquisitionModesMode_aTFI como elegible para ObservingModesMode_TFI
        self.mdObservingModesMode_TFI.addSubMode(self.mdAcquisitionModesMode_aTFI)
        # Marcamos AcquisitionModesMode_aLSSpec como elegible para ObservingModesMode_LSSpec
        self.mdObservingModesMode_LSSpec.addSubMode(self.mdAcquisitionModesMode_aLSSpec)
        # Marcamos AcquisitionModesMode_aBBI como elegible para ObservingModesMode_LSSpec
        self.mdObservingModesMode_LSSpec.addSubMode(self.mdAcquisitionModesMode_aBBI)
        # Marcamos AcquisitionModesMode_Throughslit como elegible para ObservingModesMode_LSSpec
        self.mdObservingModesMode_LSSpec.addSubMode(self.mdAcquisitionModesMode_Throughslit)
        # Marcamos AcquisitionModesMode_aMOS como elegible para ObservingModesMode_MOS
        self.mdObservingModesMode_MOS.addSubMode(self.mdAcquisitionModesMode_aMOS)
        # Marcamos AcquisitionModesMode_aBBI como elegible para ObservingModesMode_MOS
        self.mdObservingModesMode_MOS.addSubMode(self.mdAcquisitionModesMode_aBBI)
        # Marcamos AcquisitionModesMode_Throughslit como elegible para ObservingModesMode_MOS
        self.mdObservingModesMode_MOS.addSubMode(self.mdAcquisitionModesMode_Throughslit)
        # Marcamos AcquisitionModesMode_aFastBBI como elegible para ObservingModesMode_FastBBI
        self.mdObservingModesMode_FastBBI.addSubMode(self.mdAcquisitionModesMode_aFastBBI)
        # Marcamos AcquisitionModesMode_aFrTrBBI como elegible para ObservingModesMode_FrTrBBI
        self.mdObservingModesMode_FrTrBBI.addSubMode(self.mdAcquisitionModesMode_aFrTrBBI)
        # Marcamos AcquisitionModesMode_aFastLSSpec como elegible para ObservingModesMode_FastLSSpec
        self.mdObservingModesMode_FastLSSpec.addSubMode(self.mdAcquisitionModesMode_aFastLSSpec)
        # Marcamos AcquisitionModesMode_aBBI como elegible para ObservingModesMode_FastLSSpec
        self.mdObservingModesMode_FastLSSpec.addSubMode(self.mdAcquisitionModesMode_aBBI)
        # Marcamos AcquisitionModesMode_Throughslit como elegible para ObservingModesMode_FastLSSpec
        self.mdObservingModesMode_FastLSSpec.addSubMode(self.mdAcquisitionModesMode_Throughslit)
        # Marcamos AcquisitionModesMode_aFastTFImage como elegible para ObservingModesMode_FastTFImage
        self.mdObservingModesMode_FastTFImage.addSubMode(self.mdAcquisitionModesMode_aFastTFImage)
        # Marcamos AcquisitionModesMode_aFrTrTFI como elegible para ObservingModesMode_FrTrTFI
        self.mdObservingModesMode_FrTrTFI.addSubMode(self.mdAcquisitionModesMode_aFrTrTFI)
        # Marcamos AcquisitionModesMode_aBias como elegible para ObservingModesMode_Bias
        self.mdObservingModesMode_Bias.addSubMode(self.mdAcquisitionModesMode_aBias)
        # Marcamos AcquisitionModesMode_aDark como elegible para ObservingModesMode_Dark
        self.mdObservingModesMode_Dark.addSubMode(self.mdAcquisitionModesMode_aDark)
        # Marcamos AcquisitionModesMode_aDomeFlat como elegible para ObservingModesMode_DomeFlat
        self.mdObservingModesMode_DomeFlat.addSubMode(self.mdAcquisitionModesMode_aDomeFlat)
        # Marcamos AcquisitionModesMode_aSkyFlat como elegible para ObservingModesMode_SkyFlat
        self.mdObservingModesMode_SkyFlat.addSubMode(self.mdAcquisitionModesMode_aSkyFlat)
        # Marcamos AcquisitionModesMode_aSpectralFlat como elegible para ObservingModesMode_SpectralFlat
        self.mdObservingModesMode_SpectralFlat.addSubMode(self.mdAcquisitionModesMode_aSpectralFlat)
        # Marcamos AcquisitionModesMode_aCalibLamp como elegible para ObservingModesMode_CalibLamp
        self.mdObservingModesMode_CalibLamp.addSubMode(self.mdAcquisitionModesMode_aCalibLamp)
        # Marcamos AcquisitionModesMode_aTFCalib como elegible para ObservingModesMode_TFCalib
        self.mdObservingModesMode_TFCalib.addSubMode(self.mdAcquisitionModesMode_aTFCalib)
        # Marcamos AcquisitionModesMode_aBBI como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aBBI)
        # Marcamos AcquisitionModesMode_aTFI como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aTFI)
        # Marcamos AcquisitionModesMode_aLSSpec como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aLSSpec)
        # Marcamos AcquisitionModesMode_aMOS como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aMOS)
        # Marcamos AcquisitionModesMode_aFastBBI como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aFastBBI)
        # Marcamos AcquisitionModesMode_aFrTrBBI como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aFrTrBBI)
        # Marcamos AcquisitionModesMode_aFastLSSpec como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aFastLSSpec)
        # Marcamos AcquisitionModesMode_aFastTFImage como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aFastTFImage)
        # Marcamos AcquisitionModesMode_aFrTrTFI como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aFrTrTFI)
        # Marcamos AcquisitionModesMode_aBias como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aBias)
        # Marcamos AcquisitionModesMode_aDark como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aDark)
        # Marcamos AcquisitionModesMode_aDomeFlat como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aDomeFlat)
        # Marcamos AcquisitionModesMode_aSkyFlat como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aSkyFlat)
        # Marcamos AcquisitionModesMode_aSpectralFlat como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aSpectralFlat)
        # Marcamos AcquisitionModesMode_aCalibLamp como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aCalibLamp)
        # Marcamos AcquisitionModesMode_aTFCalib como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aTFCalib)
        # Marcamos AcquisitionModesMode_Throughslit como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_Throughslit)
        # Marcamos AcquisitionModesMode_Engineering como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_Engineering)
        # Marcamos FPEMode_NoFPE como elegible para AcquisitionModesMode_aBBI
        self.mdAcquisitionModesMode_aBBI.addSubMode(self.mdFPEMode_NoFPE)
        # Marcamos FPEMode_NoFPE como elegible para AcquisitionModesMode_aTFI
        self.mdAcquisitionModesMode_aTFI.addSubMode(self.mdFPEMode_NoFPE)
        # Marcamos FPEMode_LSMask como elegible para AcquisitionModesMode_aLSSpec
        self.mdAcquisitionModesMode_aLSSpec.addSubMode(self.mdFPEMode_LSMask)
        # Marcamos FPEMode_MOSmask como elegible para AcquisitionModesMode_aMOS
        self.mdAcquisitionModesMode_aMOS.addSubMode(self.mdFPEMode_MOSmask)
        # Marcamos FPEMode_FastPhotometryMask como elegible para AcquisitionModesMode_aFastBBI
        self.mdAcquisitionModesMode_aFastBBI.addSubMode(self.mdFPEMode_FastPhotometryMask)
        # Marcamos FPEMode_FrameTransferMask como elegible para AcquisitionModesMode_aFrTrBBI
        self.mdAcquisitionModesMode_aFrTrBBI.addSubMode(self.mdFPEMode_FrameTransferMask)
        # Marcamos FPEMode_LSMask como elegible para AcquisitionModesMode_aFastLSSpec
        self.mdAcquisitionModesMode_aFastLSSpec.addSubMode(self.mdFPEMode_LSMask)
        # Marcamos FPEMode_FastPhotometryMask como elegible para AcquisitionModesMode_aFastTFImage
        self.mdAcquisitionModesMode_aFastTFImage.addSubMode(self.mdFPEMode_FastPhotometryMask)
        # Marcamos FPEMode_FrameTransferMask como elegible para AcquisitionModesMode_aFrTrTFI
        self.mdAcquisitionModesMode_aFrTrTFI.addSubMode(self.mdFPEMode_FrameTransferMask)
        # Marcamos FPEMode_NoFPE como elegible para AcquisitionModesMode_aTFCalib
        self.mdAcquisitionModesMode_aTFCalib.addSubMode(self.mdFPEMode_NoFPE)
        # Marcamos FPEMode_MOSmask como elegible para AcquisitionModesMode_Throughslit
        self.mdAcquisitionModesMode_Throughslit.addSubMode(self.mdFPEMode_MOSmask)
        # Marcamos FPEMode_NoFPE como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdFPEMode_NoFPE)
        # Marcamos FPEMode_MOSmask como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdFPEMode_MOSmask)
        # Marcamos FPEMode_FastPhotometryMask como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdFPEMode_FastPhotometryMask)
        # Marcamos FPEMode_FrameTransferMask como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdFPEMode_FrameTransferMask)
        # Marcamos FPEMode_LSMask como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdFPEMode_LSMask)
        # Marcamos FPEMode_Engineering como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdFPEMode_Engineering)
        # Marcamos FocalPlaneElementMode_Disabled como elegible para FPEMode_NoFPE
        self.mdFPEMode_NoFPE.addSubMode(self.mdFocalPlaneElementMode_Disabled)
        # Marcamos FocalPlaneElementMode_MOS como elegible para FPEMode_MOSmask
        self.mdFPEMode_MOSmask.addSubMode(self.mdFocalPlaneElementMode_MOS)
        # Marcamos FocalPlaneElementMode_FastPhotometry como elegible para FPEMode_FastPhotometryMask
        self.mdFPEMode_FastPhotometryMask.addSubMode(self.mdFocalPlaneElementMode_FastPhotometry)
        # Marcamos FocalPlaneElementMode_FrameTransfer como elegible para FPEMode_FrameTransferMask
        self.mdFPEMode_FrameTransferMask.addSubMode(self.mdFocalPlaneElementMode_FrameTransfer)
        # Marcamos FocalPlaneElementMode_LS como elegible para FPEMode_LSMask
        self.mdFPEMode_LSMask.addSubMode(self.mdFocalPlaneElementMode_LS)
        # Marcamos FocalPlaneElementMode_Disabled como elegible para FPEMode_Engineering
        self.mdFPEMode_Engineering.addSubMode(self.mdFocalPlaneElementMode_Disabled)
        # Marcamos FocalPlaneElementMode_MOS como elegible para FPEMode_Engineering
        self.mdFPEMode_Engineering.addSubMode(self.mdFocalPlaneElementMode_MOS)
        # Marcamos FocalPlaneElementMode_FastPhotometry como elegible para FPEMode_Engineering
        self.mdFPEMode_Engineering.addSubMode(self.mdFocalPlaneElementMode_FastPhotometry)
        # Marcamos FocalPlaneElementMode_FrameTransfer como elegible para FPEMode_Engineering
        self.mdFPEMode_Engineering.addSubMode(self.mdFocalPlaneElementMode_FrameTransfer)
        # Marcamos FocalPlaneElementMode_LS como elegible para FPEMode_Engineering
        self.mdFPEMode_Engineering.addSubMode(self.mdFocalPlaneElementMode_LS)
        # Marcamos FocalPlaneElement_NoFPE como elegible para FocalPlaneElementMode_Disabled
        self.mdFocalPlaneElementMode_Disabled.addValue(self.vlFocalPlaneElement_NoFPE)
        # Marcamos FocalPlaneElement_MOSmask como elegible para FocalPlaneElementMode_MOS
        self.mdFocalPlaneElementMode_MOS.addValue(self.vlFocalPlaneElement_MOSmask)
        # Marcamos FocalPlaneElement_FastPhotometryMask como elegible para FocalPlaneElementMode_FastPhotometry
        self.mdFocalPlaneElementMode_FastPhotometry.addValue(self.vlFocalPlaneElement_FastPhotometryMask)
        # Marcamos FocalPlaneElement_FrameTransferMask como elegible para FocalPlaneElementMode_FrameTransfer
        self.mdFocalPlaneElementMode_FrameTransfer.addValue(self.vlFocalPlaneElement_FrameTransferMask)
        # Marcamos FocalPlaneElement_LS1_5 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS1_5)
        # Marcamos FocalPlaneElement_LS1_8 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS1_8)
        # Marcamos FocalPlaneElement_LS1_0 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS1_0)
        # Marcamos FocalPlaneElement_LS5_0 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS5_0)
        # Marcamos FocalPlaneElement_LS40_0 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS40_0)
        # Marcamos FocalPlaneElement_LS0_8 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS0_8)
        # Marcamos FocalPlaneElement_LS1_2 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS1_2)
        # Marcamos FocalPlaneElement_LS12_0 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS12_0)
        # Marcamos FocalPlaneElement_LS0_4 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS0_4)
        # Marcamos FocalPlaneElement_LS2_5 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS2_5)
        # Marcamos FocalPlaneElement_LS3_0 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS3_0)
        # Marcamos FocalPlaneElement_LS10_0 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS10_0)
        # Marcamos FocalPlaneElement_LS0_6 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS0_6)
        # Marcamos DASMode_SimpleImg como elegible para AcquisitionModesMode_aBBI
        self.mdAcquisitionModesMode_aBBI.addSubMode(self.mdDASMode_SimpleImg)
        # Marcamos DASMode_SimpleImg como elegible para AcquisitionModesMode_aTFI
        self.mdAcquisitionModesMode_aTFI.addSubMode(self.mdDASMode_SimpleImg)
        # Marcamos DASMode_SimpleSpec como elegible para AcquisitionModesMode_aLSSpec
        self.mdAcquisitionModesMode_aLSSpec.addSubMode(self.mdDASMode_SimpleSpec)
        # Marcamos DASMode_SimpleCalib como elegible para AcquisitionModesMode_aLSSpec
        self.mdAcquisitionModesMode_aLSSpec.addSubMode(self.mdDASMode_SimpleCalib)
        # Marcamos DASMode_SimpleSpec como elegible para AcquisitionModesMode_aMOS
        self.mdAcquisitionModesMode_aMOS.addSubMode(self.mdDASMode_SimpleSpec)
        # Marcamos DASMode_ShufffingImage como elegible para AcquisitionModesMode_aFastBBI
        self.mdAcquisitionModesMode_aFastBBI.addSubMode(self.mdDASMode_ShufffingImage)
        # Marcamos DASMode_FTImg como elegible para AcquisitionModesMode_aFrTrBBI
        self.mdAcquisitionModesMode_aFrTrBBI.addSubMode(self.mdDASMode_FTImg)
        # Marcamos DASMode_ShufffingSpec como elegible para AcquisitionModesMode_aFastLSSpec
        self.mdAcquisitionModesMode_aFastLSSpec.addSubMode(self.mdDASMode_ShufffingSpec)
        # Marcamos DASMode_ShufffingImage como elegible para AcquisitionModesMode_aFastTFImage
        self.mdAcquisitionModesMode_aFastTFImage.addSubMode(self.mdDASMode_ShufffingImage)
        # Marcamos DASMode_FTImg como elegible para AcquisitionModesMode_aFrTrTFI
        self.mdAcquisitionModesMode_aFrTrTFI.addSubMode(self.mdDASMode_FTImg)
        # Marcamos DASMode_ShufffingBias como elegible para AcquisitionModesMode_aBias
        self.mdAcquisitionModesMode_aBias.addSubMode(self.mdDASMode_ShufffingBias)
        # Marcamos DASMode_SimpleBias como elegible para AcquisitionModesMode_aBias
        self.mdAcquisitionModesMode_aBias.addSubMode(self.mdDASMode_SimpleBias)
        # Marcamos DASMode_FTBias como elegible para AcquisitionModesMode_aBias
        self.mdAcquisitionModesMode_aBias.addSubMode(self.mdDASMode_FTBias)
        # Marcamos DASMode_ShufffingDark como elegible para AcquisitionModesMode_aDark
        self.mdAcquisitionModesMode_aDark.addSubMode(self.mdDASMode_ShufffingDark)
        # Marcamos DASMode_SimpleDark como elegible para AcquisitionModesMode_aDark
        self.mdAcquisitionModesMode_aDark.addSubMode(self.mdDASMode_SimpleDark)
        # Marcamos DASMode_FTDark como elegible para AcquisitionModesMode_aDark
        self.mdAcquisitionModesMode_aDark.addSubMode(self.mdDASMode_FTDark)
        # Marcamos DASMode_FTImg como elegible para AcquisitionModesMode_aDomeFlat
        self.mdAcquisitionModesMode_aDomeFlat.addSubMode(self.mdDASMode_FTImg)
        # Marcamos DASMode_SimpleImg como elegible para AcquisitionModesMode_aDomeFlat
        self.mdAcquisitionModesMode_aDomeFlat.addSubMode(self.mdDASMode_SimpleImg)
        # Marcamos DASMode_FTImg como elegible para AcquisitionModesMode_aSkyFlat
        self.mdAcquisitionModesMode_aSkyFlat.addSubMode(self.mdDASMode_FTImg)
        # Marcamos DASMode_SimpleImg como elegible para AcquisitionModesMode_aSkyFlat
        self.mdAcquisitionModesMode_aSkyFlat.addSubMode(self.mdDASMode_SimpleImg)
        # Marcamos DASMode_SimpleCalib como elegible para AcquisitionModesMode_aSpectralFlat
        self.mdAcquisitionModesMode_aSpectralFlat.addSubMode(self.mdDASMode_SimpleCalib)
        # Marcamos DASMode_GainCalib como elegible para AcquisitionModesMode_aCalibLamp
        self.mdAcquisitionModesMode_aCalibLamp.addSubMode(self.mdDASMode_GainCalib)
        # Marcamos DASMode_ShufffingImage como elegible para AcquisitionModesMode_aTFCalib
        self.mdAcquisitionModesMode_aTFCalib.addSubMode(self.mdDASMode_ShufffingImage)
        # Marcamos DASMode_SimpleSpec como elegible para AcquisitionModesMode_Throughslit
        self.mdAcquisitionModesMode_Throughslit.addSubMode(self.mdDASMode_SimpleSpec)
        # Marcamos DASMode_SimpleImg como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_SimpleImg)
        # Marcamos DASMode_SimpleSpec como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_SimpleSpec)
        # Marcamos DASMode_ShufffingSpec como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_ShufffingSpec)
        # Marcamos DASMode_FTImg como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_FTImg)
        # Marcamos DASMode_FTDark como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_FTDark)
        # Marcamos DASMode_FTBias como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_FTBias)
        # Marcamos DASMode_SimpleBias como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_SimpleBias)
        # Marcamos DASMode_SimpleDark como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_SimpleDark)
        # Marcamos DASMode_ShufffingDark como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_ShufffingDark)
        # Marcamos DASMode_ShufffingBias como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_ShufffingBias)
        # Marcamos DASMode_ShufffingImage como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_ShufffingImage)
        # Marcamos DASMode_SimpleCalib como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_SimpleCalib)
        # Marcamos DASMode_GainCalib como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_GainCalib)
        # Marcamos DASMode_Engineering como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_Engineering)
        # Marcamos AcquisitionMode_NormalSquare como elegible para DASMode_SimpleImg
        self.mdDASMode_SimpleImg.addSubMode(self.mdAcquisitionMode_NormalSquare)
        # Marcamos AcquisitionMode_Normal como elegible para DASMode_SimpleSpec
        self.mdDASMode_SimpleSpec.addSubMode(self.mdAcquisitionMode_Normal)
        # Marcamos AcquisitionMode_Shuffling como elegible para DASMode_ShufffingSpec
        self.mdDASMode_ShufffingSpec.addSubMode(self.mdAcquisitionMode_Shuffling)
        # Marcamos AcquisitionMode_FrameTransfer como elegible para DASMode_FTImg
        self.mdDASMode_FTImg.addSubMode(self.mdAcquisitionMode_FrameTransfer)
        # Marcamos AcquisitionMode_FrameTransfer como elegible para DASMode_FTDark
        self.mdDASMode_FTDark.addSubMode(self.mdAcquisitionMode_FrameTransfer)
        # Marcamos AcquisitionMode_FTBias como elegible para DASMode_FTBias
        self.mdDASMode_FTBias.addSubMode(self.mdAcquisitionMode_FTBias)
        # Marcamos AcquisitionMode_NormalBias como elegible para DASMode_SimpleBias
        self.mdDASMode_SimpleBias.addSubMode(self.mdAcquisitionMode_NormalBias)
        # Marcamos AcquisitionMode_Normal como elegible para DASMode_SimpleDark
        self.mdDASMode_SimpleDark.addSubMode(self.mdAcquisitionMode_Normal)
        # Marcamos AcquisitionMode_Shuffling como elegible para DASMode_ShufffingDark
        self.mdDASMode_ShufffingDark.addSubMode(self.mdAcquisitionMode_Shuffling)
        # Marcamos AcquisitionMode_ShufflingBias como elegible para DASMode_ShufffingBias
        self.mdDASMode_ShufffingBias.addSubMode(self.mdAcquisitionMode_ShufflingBias)
        # Marcamos AcquisitionMode_ShufflingSquare como elegible para DASMode_ShufffingImage
        self.mdDASMode_ShufffingImage.addSubMode(self.mdAcquisitionMode_ShufflingSquare)
        # Marcamos AcquisitionMode_Normal como elegible para DASMode_SimpleCalib
        self.mdDASMode_SimpleCalib.addSubMode(self.mdAcquisitionMode_Normal)
        # Marcamos AcquisitionMode_GainCalib como elegible para DASMode_GainCalib
        self.mdDASMode_GainCalib.addSubMode(self.mdAcquisitionMode_GainCalib)
        # Marcamos AcquisitionMode_Normal como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_Normal)
        # Marcamos AcquisitionMode_FrameTransfer como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_FrameTransfer)
        # Marcamos AcquisitionMode_Shuffling como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_Shuffling)
        # Marcamos AcquisitionMode_FTBias como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_FTBias)
        # Marcamos AcquisitionMode_NormalBias como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_NormalBias)
        # Marcamos AcquisitionMode_ShufflingBias como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_ShufflingBias)
        # Marcamos AcquisitionMode_NormalSquare como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_NormalSquare)
        # Marcamos AcquisitionMode_ShufflingSquare como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_ShufflingSquare)
        # Marcamos AcquisitionMode_GainCalib como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_GainCalib)
        # Marcamos AcquisitionMode_Engineering como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_Engineering)
        # Marcamos ShuffleLinesMode_Normal como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdShuffleLinesMode_Normal)
        # Marcamos ShuffleLinesMode_Normal como elegible para AcquisitionMode_ShufflingBias
        self.mdAcquisitionMode_ShufflingBias.addSubMode(self.mdShuffleLinesMode_Normal)
        # Marcamos ShuffleLinesMode_Normal como elegible para AcquisitionMode_ShufflingSquare
        self.mdAcquisitionMode_ShufflingSquare.addSubMode(self.mdShuffleLinesMode_Normal)
        # Marcamos ShuffleLinesMode_Normal como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdShuffleLinesMode_Normal)
        # Marcamos ShuffleLines_FullRange como elegible para ShuffleLinesMode_Normal
        self.mdShuffleLinesMode_Normal.addValue(self.vlShuffleLines_FullRange)
        # Marcamos ShiftNumberMode_Normal como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdShiftNumberMode_Normal)
        # Marcamos ShiftNumberMode_Normal como elegible para AcquisitionMode_ShufflingBias
        self.mdAcquisitionMode_ShufflingBias.addSubMode(self.mdShiftNumberMode_Normal)
        # Marcamos ShiftNumberMode_Normal como elegible para AcquisitionMode_ShufflingSquare
        self.mdAcquisitionMode_ShufflingSquare.addSubMode(self.mdShiftNumberMode_Normal)
        # Marcamos ShiftNumberMode_Normal como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdShiftNumberMode_Normal)
        # Marcamos ShiftNumber_FullRange como elegible para ShiftNumberMode_Normal
        self.mdShiftNumberMode_Normal.addValue(self.vlShiftNumber_FullRange)
        # Marcamos ExpTimeMode_Normal como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_FT como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdExpTimeMode_FT)
        # Marcamos ExpTimeMode_Normal como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_Bias como elegible para AcquisitionMode_FTBias
        self.mdAcquisitionMode_FTBias.addSubMode(self.mdExpTimeMode_Bias)
        # Marcamos ExpTimeMode_Bias como elegible para AcquisitionMode_NormalBias
        self.mdAcquisitionMode_NormalBias.addSubMode(self.mdExpTimeMode_Bias)
        # Marcamos ExpTimeMode_Bias como elegible para AcquisitionMode_ShufflingBias
        self.mdAcquisitionMode_ShufflingBias.addSubMode(self.mdExpTimeMode_Bias)
        # Marcamos ExpTimeMode_Normal como elegible para AcquisitionMode_NormalSquare
        self.mdAcquisitionMode_NormalSquare.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_Normal como elegible para AcquisitionMode_ShufflingSquare
        self.mdAcquisitionMode_ShufflingSquare.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_Normal como elegible para AcquisitionMode_GainCalib
        self.mdAcquisitionMode_GainCalib.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_Normal como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_Bias como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdExpTimeMode_Bias)
        # Marcamos ExpTimeMode_FT como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdExpTimeMode_FT)
        # Marcamos ExpTime_FullRange como elegible para ExpTimeMode_Normal
        self.mdExpTimeMode_Normal.addValue(self.vlExpTime_FullRange)
        # Marcamos ExpTime_0_0 como elegible para ExpTimeMode_Bias
        self.mdExpTimeMode_Bias.addValue(self.vlExpTime_0_0)
        # Marcamos ExpTime_FTRange como elegible para ExpTimeMode_FT
        self.mdExpTimeMode_FT.addValue(self.vlExpTime_FTRange)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_FTBias
        self.mdAcquisitionMode_FTBias.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_FTBias
        self.mdAcquisitionMode_FTBias.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_NormalBias
        self.mdAcquisitionMode_NormalBias.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_NormalBias
        self.mdAcquisitionMode_NormalBias.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_ShufflingBias
        self.mdAcquisitionMode_ShufflingBias.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_ShufflingBias
        self.mdAcquisitionMode_ShufflingBias.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_NormalSquare
        self.mdAcquisitionMode_NormalSquare.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_NormalSquare
        self.mdAcquisitionMode_NormalSquare.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_ShufflingSquare
        self.mdAcquisitionMode_ShufflingSquare.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_ShufflingSquare
        self.mdAcquisitionMode_ShufflingSquare.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_GainCalib
        self.mdAcquisitionMode_GainCalib.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_GainCalib
        self.mdAcquisitionMode_GainCalib.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_Engineering como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdMultipleExposureMode_Engineering)
        # Marcamos numOfFramesMode_Normal como elegible para MultipleExposureMode_On
        self.mdMultipleExposureMode_On.addSubMode(self.mdnumOfFramesMode_Normal)
        # Marcamos numOfFramesMode_Normal como elegible para MultipleExposureMode_Engineering
        self.mdMultipleExposureMode_Engineering.addSubMode(self.mdnumOfFramesMode_Normal)
        # Marcamos numOfFrames_FullRange como elegible para numOfFramesMode_Normal
        self.mdnumOfFramesMode_Normal.addValue(self.vlnumOfFrames_FullRange)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_FTBias
        self.mdAcquisitionMode_FTBias.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_NormalBias
        self.mdAcquisitionMode_NormalBias.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_ShufflingBias
        self.mdAcquisitionMode_ShufflingBias.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_NormalSquare
        self.mdAcquisitionMode_NormalSquare.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_ShufflingSquare
        self.mdAcquisitionMode_ShufflingSquare.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_GainCalib
        self.mdAcquisitionMode_GainCalib.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeed_FST como elegible para PixelSpeedMode_All
        self.mdPixelSpeedMode_All.addValue(self.vlPixelSpeed_FST)
        # Marcamos PixelSpeed_MED como elegible para PixelSpeedMode_All
        self.mdPixelSpeedMode_All.addValue(self.vlPixelSpeed_MED)
        # Marcamos PixelSpeed_SLW como elegible para PixelSpeedMode_All
        self.mdPixelSpeedMode_All.addValue(self.vlPixelSpeed_SLW)
        # Marcamos CalibGainMode_Normal como elegible para AcquisitionMode_GainCalib
        self.mdAcquisitionMode_GainCalib.addSubMode(self.mdCalibGainMode_Normal)
        # Marcamos CalibGainMode_Normal como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdCalibGainMode_Normal)
        # Marcamos CalibGain_FullRange como elegible para CalibGainMode_Normal
        self.mdCalibGainMode_Normal.addValue(self.vlCalibGain_FullRange)
        # Marcamos OpenShutterMode_On como elegible para DASMode_SimpleImg
        self.mdDASMode_SimpleImg.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_On como elegible para DASMode_SimpleSpec
        self.mdDASMode_SimpleSpec.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_On como elegible para DASMode_ShufffingSpec
        self.mdDASMode_ShufffingSpec.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_On como elegible para DASMode_FTImg
        self.mdDASMode_FTImg.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_Off como elegible para DASMode_FTDark
        self.mdDASMode_FTDark.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_Off como elegible para DASMode_FTBias
        self.mdDASMode_FTBias.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_Off como elegible para DASMode_SimpleBias
        self.mdDASMode_SimpleBias.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_Off como elegible para DASMode_SimpleDark
        self.mdDASMode_SimpleDark.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_Off como elegible para DASMode_ShufffingDark
        self.mdDASMode_ShufffingDark.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_Off como elegible para DASMode_ShufffingBias
        self.mdDASMode_ShufffingBias.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_On como elegible para DASMode_ShufffingImage
        self.mdDASMode_ShufffingImage.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_On como elegible para DASMode_SimpleCalib
        self.mdDASMode_SimpleCalib.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_On como elegible para DASMode_GainCalib
        self.mdDASMode_GainCalib.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_On como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_Off como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos ProcessMonitorMode_Normal como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdProcessMonitorMode_Normal)
        # Marcamos ProcessMonitorMode_Engineering como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdProcessMonitorMode_Engineering)
        # Marcamos CurrentEllapsedMode_Normal como elegible para ProcessMonitorMode_Normal
        self.mdProcessMonitorMode_Normal.addSubMode(self.mdCurrentEllapsedMode_Normal)
        # Marcamos CurrentEllapsedMode_Normal como elegible para ProcessMonitorMode_Engineering
        self.mdProcessMonitorMode_Engineering.addSubMode(self.mdCurrentEllapsedMode_Normal)
        # Marcamos CurrentEllapsed_Range como elegible para CurrentEllapsedMode_Normal
        self.mdCurrentEllapsedMode_Normal.addValue(self.vlCurrentEllapsed_Range)
        # Marcamos CurrentImgMode_Normal como elegible para ProcessMonitorMode_Normal
        self.mdProcessMonitorMode_Normal.addSubMode(self.mdCurrentImgMode_Normal)
        # Marcamos CurrentImgMode_Normal como elegible para ProcessMonitorMode_Engineering
        self.mdProcessMonitorMode_Engineering.addSubMode(self.mdCurrentImgMode_Normal)
        # Marcamos CurrentImg_Range como elegible para CurrentImgMode_Normal
        self.mdCurrentImgMode_Normal.addValue(self.vlCurrentImg_Range)
        # Marcamos CurrentPctMode_Normal como elegible para ProcessMonitorMode_Normal
        self.mdProcessMonitorMode_Normal.addSubMode(self.mdCurrentPctMode_Normal)
        # Marcamos CurrentPctMode_Normal como elegible para ProcessMonitorMode_Engineering
        self.mdProcessMonitorMode_Engineering.addSubMode(self.mdCurrentPctMode_Normal)
        # Marcamos CurrentPct_Range como elegible para CurrentPctMode_Normal
        self.mdCurrentPctMode_Normal.addValue(self.vlCurrentPct_Range)
        # Marcamos OverallPctMode_Normal como elegible para ProcessMonitorMode_Normal
        self.mdProcessMonitorMode_Normal.addSubMode(self.mdOverallPctMode_Normal)
        # Marcamos OverallPctMode_Normal como elegible para ProcessMonitorMode_Engineering
        self.mdProcessMonitorMode_Engineering.addSubMode(self.mdOverallPctMode_Normal)
        # Marcamos OverallPct_Range como elegible para OverallPctMode_Normal
        self.mdOverallPctMode_Normal.addValue(self.vlOverallPct_Range)
        # Marcamos PreOpticsMode_NoDispersion como elegible para AcquisitionModesMode_aBBI
        self.mdAcquisitionModesMode_aBBI.addSubMode(self.mdPreOpticsMode_NoDispersion)
        # Marcamos PreOpticsMode_RTF como elegible para AcquisitionModesMode_aTFI
        self.mdAcquisitionModesMode_aTFI.addSubMode(self.mdPreOpticsMode_RTF)
        # Marcamos PreOpticsMode_RTF como elegible para AcquisitionModesMode_aTFI
        self.mdAcquisitionModesMode_aTFI.addSubMode(self.mdPreOpticsMode_RTF)
        # Marcamos PreOpticsMode_BTF como elegible para AcquisitionModesMode_aTFI
        self.mdAcquisitionModesMode_aTFI.addSubMode(self.mdPreOpticsMode_BTF)
        # Marcamos PreOpticsMode_GrismR como elegible para AcquisitionModesMode_aLSSpec
        self.mdAcquisitionModesMode_aLSSpec.addSubMode(self.mdPreOpticsMode_GrismR)
        # Marcamos PreOpticsMode_GrismB como elegible para AcquisitionModesMode_aLSSpec
        self.mdAcquisitionModesMode_aLSSpec.addSubMode(self.mdPreOpticsMode_GrismB)
        # Marcamos PreOpticsMode_GrismR como elegible para AcquisitionModesMode_aMOS
        self.mdAcquisitionModesMode_aMOS.addSubMode(self.mdPreOpticsMode_GrismR)
        # Marcamos PreOpticsMode_GrismBMOS como elegible para AcquisitionModesMode_aMOS
        self.mdAcquisitionModesMode_aMOS.addSubMode(self.mdPreOpticsMode_GrismBMOS)
        # Marcamos PreOpticsMode_NoDispersion como elegible para AcquisitionModesMode_aFastBBI
        self.mdAcquisitionModesMode_aFastBBI.addSubMode(self.mdPreOpticsMode_NoDispersion)
        # Marcamos PreOpticsMode_NoDispersion como elegible para AcquisitionModesMode_aFrTrBBI
        self.mdAcquisitionModesMode_aFrTrBBI.addSubMode(self.mdPreOpticsMode_NoDispersion)
        # Marcamos PreOpticsMode_GrismR como elegible para AcquisitionModesMode_aFastLSSpec
        self.mdAcquisitionModesMode_aFastLSSpec.addSubMode(self.mdPreOpticsMode_GrismR)
        # Marcamos PreOpticsMode_GrismB como elegible para AcquisitionModesMode_aFastLSSpec
        self.mdAcquisitionModesMode_aFastLSSpec.addSubMode(self.mdPreOpticsMode_GrismB)
        # Marcamos PreOpticsMode_RTF como elegible para AcquisitionModesMode_aFastTFImage
        self.mdAcquisitionModesMode_aFastTFImage.addSubMode(self.mdPreOpticsMode_RTF)
        # Marcamos PreOpticsMode_BTF como elegible para AcquisitionModesMode_aFastTFImage
        self.mdAcquisitionModesMode_aFastTFImage.addSubMode(self.mdPreOpticsMode_BTF)
        # Marcamos PreOpticsMode_RTF como elegible para AcquisitionModesMode_aFrTrTFI
        self.mdAcquisitionModesMode_aFrTrTFI.addSubMode(self.mdPreOpticsMode_RTF)
        # Marcamos PreOpticsMode_BTF como elegible para AcquisitionModesMode_aFrTrTFI
        self.mdAcquisitionModesMode_aFrTrTFI.addSubMode(self.mdPreOpticsMode_BTF)
        # Marcamos PreOpticsMode_RTFCalib como elegible para AcquisitionModesMode_aTFCalib
        self.mdAcquisitionModesMode_aTFCalib.addSubMode(self.mdPreOpticsMode_RTFCalib)
        # Marcamos PreOpticsMode_BTFCalib como elegible para AcquisitionModesMode_aTFCalib
        self.mdAcquisitionModesMode_aTFCalib.addSubMode(self.mdPreOpticsMode_BTFCalib)
        # Marcamos PreOpticsMode_NoDispersion como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_NoDispersion)
        # Marcamos PreOpticsMode_RTF como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_RTF)
        # Marcamos PreOpticsMode_GrismR como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_GrismR)
        # Marcamos PreOpticsMode_BTF como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_BTF)
        # Marcamos PreOpticsMode_GrismB como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_GrismB)
        # Marcamos PreOpticsMode_GrismBMOS como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_GrismBMOS)
        # Marcamos PreOpticsMode_RTFCalib como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_RTFCalib)
        # Marcamos PreOpticsMode_BTFCalib como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_BTFCalib)
        # Marcamos PreOpticsMode_Engineering como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_Engineering)
        # Marcamos GrismsMode_GrismsR como elegible para PreOpticsMode_GrismR
        self.mdPreOpticsMode_GrismR.addSubMode(self.mdGrismsMode_GrismsR)
        # Marcamos GrismsMode_GrismsB como elegible para PreOpticsMode_GrismB
        self.mdPreOpticsMode_GrismB.addSubMode(self.mdGrismsMode_GrismsB)
        # Marcamos GrismsMode_GrismsB como elegible para PreOpticsMode_GrismBMOS
        self.mdPreOpticsMode_GrismBMOS.addSubMode(self.mdGrismsMode_GrismsB)
        # Marcamos GrismsMode_GrismsB como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdGrismsMode_GrismsB)
        # Marcamos GrismsMode_GrismsR como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdGrismsMode_GrismsR)
        # Marcamos Grisms_R1000B como elegible para GrismsMode_GrismsB
        self.mdGrismsMode_GrismsB.addValue(self.vlGrisms_R1000B)
        # Marcamos Grisms_R300B como elegible para GrismsMode_GrismsB
        self.mdGrismsMode_GrismsB.addValue(self.vlGrisms_R300B)
        # Marcamos Grisms_R2500U como elegible para GrismsMode_GrismsB
        self.mdGrismsMode_GrismsB.addValue(self.vlGrisms_R2500U)
        # Marcamos Grisms_R500B como elegible para GrismsMode_GrismsB
        self.mdGrismsMode_GrismsB.addValue(self.vlGrisms_R500B)
        # Marcamos Grisms_R2000B como elegible para GrismsMode_GrismsB
        self.mdGrismsMode_GrismsB.addValue(self.vlGrisms_R2000B)
        # Marcamos Grisms_R2500V como elegible para GrismsMode_GrismsB
        self.mdGrismsMode_GrismsB.addValue(self.vlGrisms_R2500V)
        # Marcamos Grisms_R300R como elegible para GrismsMode_GrismsR
        self.mdGrismsMode_GrismsR.addValue(self.vlGrisms_R300R)
        # Marcamos Grisms_R2500R como elegible para GrismsMode_GrismsR
        self.mdGrismsMode_GrismsR.addValue(self.vlGrisms_R2500R)
        # Marcamos Grisms_R1000R como elegible para GrismsMode_GrismsR
        self.mdGrismsMode_GrismsR.addValue(self.vlGrisms_R1000R)
        # Marcamos Grisms_R2500I como elegible para GrismsMode_GrismsR
        self.mdGrismsMode_GrismsR.addValue(self.vlGrisms_R2500I)
        # Marcamos Grisms_R500R como elegible para GrismsMode_GrismsR
        self.mdGrismsMode_GrismsR.addValue(self.vlGrisms_R500R)
        # Marcamos RedTFMode_l651_799 como elegible para PreOpticsMode_RTF
        self.mdPreOpticsMode_RTF.addSubMode(self.mdRedTFMode_l651_799)
        # Marcamos RedTFMode_l800_819 como elegible para PreOpticsMode_RTF
        self.mdPreOpticsMode_RTF.addSubMode(self.mdRedTFMode_l800_819)
        # Marcamos RedTFMode_l820_839 como elegible para PreOpticsMode_RTF
        self.mdPreOpticsMode_RTF.addSubMode(self.mdRedTFMode_l820_839)
        # Marcamos RedTFMode_l840_879 como elegible para PreOpticsMode_RTF
        self.mdPreOpticsMode_RTF.addSubMode(self.mdRedTFMode_l840_879)
        # Marcamos RedTFMode_l880_909 como elegible para PreOpticsMode_RTF
        self.mdPreOpticsMode_RTF.addSubMode(self.mdRedTFMode_l880_909)
        # Marcamos RedTFMode_l910_934 como elegible para PreOpticsMode_RTF
        self.mdPreOpticsMode_RTF.addSubMode(self.mdRedTFMode_l910_934)
        # Marcamos RedTFMode_l651_799 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdRedTFMode_l651_799)
        # Marcamos RedTFMode_l800_819 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdRedTFMode_l800_819)
        # Marcamos RedTFMode_l820_839 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdRedTFMode_l820_839)
        # Marcamos RedTFMode_l840_879 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdRedTFMode_l840_879)
        # Marcamos RedTFMode_l880_909 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdRedTFMode_l880_909)
        # Marcamos RedTFMode_l910_934 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdRedTFMode_l910_934)
        # Marcamos RedTFMode_Engineering como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdRedTFMode_Engineering)
        # Marcamos RedFWHMMode_l2_0 como elegible para RedTFMode_l651_799
        self.mdRedTFMode_l651_799.addSubMode(self.mdRedFWHMMode_l2_0)
        # Marcamos RedFWHMMode_l1_5 como elegible para RedTFMode_l800_819
        self.mdRedTFMode_l800_819.addSubMode(self.mdRedFWHMMode_l1_5)
        # Marcamos RedFWHMMode_l1_4 como elegible para RedTFMode_l820_839
        self.mdRedTFMode_l820_839.addSubMode(self.mdRedFWHMMode_l1_4)
        # Marcamos RedFWHMMode_l1_3 como elegible para RedTFMode_l840_879
        self.mdRedTFMode_l840_879.addSubMode(self.mdRedFWHMMode_l1_3)
        # Marcamos RedFWHMMode_l1_2 como elegible para RedTFMode_l880_909
        self.mdRedTFMode_l880_909.addSubMode(self.mdRedFWHMMode_l1_2)
        # Marcamos RedFWHMMode_l1_2b como elegible para RedTFMode_l910_934
        self.mdRedTFMode_l910_934.addSubMode(self.mdRedFWHMMode_l1_2b)
        # Marcamos RedFWHMMode_l2_0 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedFWHMMode_l2_0)
        # Marcamos RedFWHMMode_l1_5 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedFWHMMode_l1_5)
        # Marcamos RedFWHMMode_l1_4 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedFWHMMode_l1_4)
        # Marcamos RedFWHMMode_l1_3 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedFWHMMode_l1_3)
        # Marcamos RedFWHMMode_l1_2 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedFWHMMode_l1_2)
        # Marcamos RedFWHMMode_l1_2b como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedFWHMMode_l1_2b)
        # Marcamos RedFWHM_Range2_0 como elegible para RedFWHMMode_l2_0
        self.mdRedFWHMMode_l2_0.addValue(self.vlRedFWHM_Range2_0)
        # Marcamos RedFWHM_Range1_5 como elegible para RedFWHMMode_l1_5
        self.mdRedFWHMMode_l1_5.addValue(self.vlRedFWHM_Range1_5)
        # Marcamos RedFWHM_Range1_4 como elegible para RedFWHMMode_l1_4
        self.mdRedFWHMMode_l1_4.addValue(self.vlRedFWHM_Range1_4)
        # Marcamos RedFWHM_Range1_3 como elegible para RedFWHMMode_l1_3
        self.mdRedFWHMMode_l1_3.addValue(self.vlRedFWHM_Range1_3)
        # Marcamos RedFWHM_Range1_2 como elegible para RedFWHMMode_l1_2
        self.mdRedFWHMMode_l1_2.addValue(self.vlRedFWHM_Range1_2)
        # Marcamos RedFWHM_Range1_2b como elegible para RedFWHMMode_l1_2b
        self.mdRedFWHMMode_l1_2b.addValue(self.vlRedFWHM_Range1_2b)
        # Marcamos RedLamdaMode_l651_799 como elegible para RedTFMode_l651_799
        self.mdRedTFMode_l651_799.addSubMode(self.mdRedLamdaMode_l651_799)
        # Marcamos RedLamdaMode_l800_819 como elegible para RedTFMode_l800_819
        self.mdRedTFMode_l800_819.addSubMode(self.mdRedLamdaMode_l800_819)
        # Marcamos RedLamdaMode_l820_839 como elegible para RedTFMode_l820_839
        self.mdRedTFMode_l820_839.addSubMode(self.mdRedLamdaMode_l820_839)
        # Marcamos RedLamdaMode_l840_879 como elegible para RedTFMode_l840_879
        self.mdRedTFMode_l840_879.addSubMode(self.mdRedLamdaMode_l840_879)
        # Marcamos RedLamdaMode_l880_909 como elegible para RedTFMode_l880_909
        self.mdRedTFMode_l880_909.addSubMode(self.mdRedLamdaMode_l880_909)
        # Marcamos RedLamdaMode_l910_934 como elegible para RedTFMode_l910_934
        self.mdRedTFMode_l910_934.addSubMode(self.mdRedLamdaMode_l910_934)
        # Marcamos RedLamdaMode_l651_799 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedLamdaMode_l651_799)
        # Marcamos RedLamdaMode_l800_819 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedLamdaMode_l800_819)
        # Marcamos RedLamdaMode_l820_839 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedLamdaMode_l820_839)
        # Marcamos RedLamdaMode_l840_879 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedLamdaMode_l840_879)
        # Marcamos RedLamdaMode_l880_909 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedLamdaMode_l880_909)
        # Marcamos RedLamdaMode_l910_934 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedLamdaMode_l910_934)
        # Marcamos RedLamda_Range651 como elegible para RedLamdaMode_l651_799
        self.mdRedLamdaMode_l651_799.addValue(self.vlRedLamda_Range651)
        # Marcamos RedLamda_Range800 como elegible para RedLamdaMode_l800_819
        self.mdRedLamdaMode_l800_819.addValue(self.vlRedLamda_Range800)
        # Marcamos RedLamda_Range820 como elegible para RedLamdaMode_l820_839
        self.mdRedLamdaMode_l820_839.addValue(self.vlRedLamda_Range820)
        # Marcamos RedLamda_Range840 como elegible para RedLamdaMode_l840_879
        self.mdRedLamdaMode_l840_879.addValue(self.vlRedLamda_Range840)
        # Marcamos RedLamda_Range880 como elegible para RedLamdaMode_l880_909
        self.mdRedLamdaMode_l880_909.addValue(self.vlRedLamda_Range880)
        # Marcamos RedLamda_Range910 como elegible para RedLamdaMode_l910_934
        self.mdRedLamdaMode_l910_934.addValue(self.vlRedLamda_Range910)
        # Marcamos BlueTFMode_l448_463 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l448_463)
        # Marcamos BlueTFMode_l464_480 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l464_480)
        # Marcamos BlueTFMode_l481_502 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l481_502)
        # Marcamos BlueTFMode_l503_521 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l503_521)
        # Marcamos BlueTFMode_l522_542 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l522_542)
        # Marcamos BlueTFMode_l543_583 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l543_583)
        # Marcamos BlueTFMode_l584_609 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l584_609)
        # Marcamos BlueTFMode_l610_637 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l610_637)
        # Marcamos BlueTFMode_l638_671 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l638_671)
        # Marcamos BlueTFMode_l448_463 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l448_463)
        # Marcamos BlueTFMode_l464_480 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l464_480)
        # Marcamos BlueTFMode_l481_502 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l481_502)
        # Marcamos BlueTFMode_l503_521 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l503_521)
        # Marcamos BlueTFMode_l522_542 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l522_542)
        # Marcamos BlueTFMode_l543_583 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l543_583)
        # Marcamos BlueTFMode_l584_609 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l584_609)
        # Marcamos BlueTFMode_l610_637 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l610_637)
        # Marcamos BlueTFMode_l638_671 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l638_671)
        # Marcamos BlueTFMode_Engineering como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_Engineering)
        # Marcamos BlueFWHMMode_l0_8 como elegible para BlueTFMode_l448_463
        self.mdBlueTFMode_l448_463.addSubMode(self.mdBlueFWHMMode_l0_8)
        # Marcamos BlueFWHMMode_l0_85 como elegible para BlueTFMode_l464_480
        self.mdBlueTFMode_l464_480.addSubMode(self.mdBlueFWHMMode_l0_85)
        # Marcamos BlueFWHMMode_l0_8 como elegible para BlueTFMode_l481_502
        self.mdBlueTFMode_l481_502.addSubMode(self.mdBlueFWHMMode_l0_8)
        # Marcamos BlueFWHMMode_l0_50 como elegible para BlueTFMode_l503_521
        self.mdBlueTFMode_l503_521.addSubMode(self.mdBlueFWHMMode_l0_50)
        # Marcamos BlueFWHMMode_l0_45 como elegible para BlueTFMode_l522_542
        self.mdBlueTFMode_l522_542.addSubMode(self.mdBlueFWHMMode_l0_45)
        # Marcamos BlueFWHMMode_l0_50 como elegible para BlueTFMode_l543_583
        self.mdBlueTFMode_l543_583.addSubMode(self.mdBlueFWHMMode_l0_50)
        # Marcamos BlueFWHMMode_l0_70 como elegible para BlueTFMode_l584_609
        self.mdBlueTFMode_l584_609.addSubMode(self.mdBlueFWHMMode_l0_70)
        # Marcamos BlueFWHMMode_l0_90 como elegible para BlueTFMode_l610_637
        self.mdBlueTFMode_l610_637.addSubMode(self.mdBlueFWHMMode_l0_90)
        # Marcamos BlueFWHMMode_l1_10 como elegible para BlueTFMode_l638_671
        self.mdBlueTFMode_l638_671.addSubMode(self.mdBlueFWHMMode_l1_10)
        # Marcamos BlueFWHMMode_l0_8 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueFWHMMode_l0_8)
        # Marcamos BlueFWHMMode_l0_85 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueFWHMMode_l0_85)
        # Marcamos BlueFWHMMode_l0_50 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueFWHMMode_l0_50)
        # Marcamos BlueFWHMMode_l0_45 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueFWHMMode_l0_45)
        # Marcamos BlueFWHMMode_l0_70 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueFWHMMode_l0_70)
        # Marcamos BlueFWHMMode_l0_90 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueFWHMMode_l0_90)
        # Marcamos BlueFWHMMode_l1_10 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueFWHMMode_l1_10)
        # Marcamos BlueFWHM_0_8 como elegible para BlueFWHMMode_l0_8
        self.mdBlueFWHMMode_l0_8.addValue(self.vlBlueFWHM_0_8)
        # Marcamos BlueFWHM_0_85 como elegible para BlueFWHMMode_l0_85
        self.mdBlueFWHMMode_l0_85.addValue(self.vlBlueFWHM_0_85)
        # Marcamos BlueFWHM_0_50 como elegible para BlueFWHMMode_l0_50
        self.mdBlueFWHMMode_l0_50.addValue(self.vlBlueFWHM_0_50)
        # Marcamos BlueFWHM_0_45 como elegible para BlueFWHMMode_l0_45
        self.mdBlueFWHMMode_l0_45.addValue(self.vlBlueFWHM_0_45)
        # Marcamos BlueFWHM_0_70 como elegible para BlueFWHMMode_l0_70
        self.mdBlueFWHMMode_l0_70.addValue(self.vlBlueFWHM_0_70)
        # Marcamos BlueFWHM_0_90 como elegible para BlueFWHMMode_l0_90
        self.mdBlueFWHMMode_l0_90.addValue(self.vlBlueFWHM_0_90)
        # Marcamos BlueFWHM_1_10 como elegible para BlueFWHMMode_l1_10
        self.mdBlueFWHMMode_l1_10.addValue(self.vlBlueFWHM_1_10)
        # Marcamos BlueLamdaMode_l448_463 como elegible para BlueTFMode_l448_463
        self.mdBlueTFMode_l448_463.addSubMode(self.mdBlueLamdaMode_l448_463)
        # Marcamos BlueLamdaMode_l464_480 como elegible para BlueTFMode_l464_480
        self.mdBlueTFMode_l464_480.addSubMode(self.mdBlueLamdaMode_l464_480)
        # Marcamos BlueLamdaMode_l481_502 como elegible para BlueTFMode_l481_502
        self.mdBlueTFMode_l481_502.addSubMode(self.mdBlueLamdaMode_l481_502)
        # Marcamos BlueLamdaMode_l503_521 como elegible para BlueTFMode_l503_521
        self.mdBlueTFMode_l503_521.addSubMode(self.mdBlueLamdaMode_l503_521)
        # Marcamos BlueLamdaMode_l522_542 como elegible para BlueTFMode_l522_542
        self.mdBlueTFMode_l522_542.addSubMode(self.mdBlueLamdaMode_l522_542)
        # Marcamos BlueLamdaMode_l543_583 como elegible para BlueTFMode_l543_583
        self.mdBlueTFMode_l543_583.addSubMode(self.mdBlueLamdaMode_l543_583)
        # Marcamos BlueLamdaMode_l584_609 como elegible para BlueTFMode_l584_609
        self.mdBlueTFMode_l584_609.addSubMode(self.mdBlueLamdaMode_l584_609)
        # Marcamos BlueLamdaMode_l610_637 como elegible para BlueTFMode_l610_637
        self.mdBlueTFMode_l610_637.addSubMode(self.mdBlueLamdaMode_l610_637)
        # Marcamos BlueLamdaMode_l638_671 como elegible para BlueTFMode_l638_671
        self.mdBlueTFMode_l638_671.addSubMode(self.mdBlueLamdaMode_l638_671)
        # Marcamos BlueLamdaMode_l448_463 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l448_463)
        # Marcamos BlueLamdaMode_l464_480 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l464_480)
        # Marcamos BlueLamdaMode_l481_502 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l481_502)
        # Marcamos BlueLamdaMode_l503_521 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l503_521)
        # Marcamos BlueLamdaMode_l522_542 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l522_542)
        # Marcamos BlueLamdaMode_l543_583 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l543_583)
        # Marcamos BlueLamdaMode_l584_609 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l584_609)
        # Marcamos BlueLamdaMode_l610_637 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l610_637)
        # Marcamos BlueLamdaMode_l638_671 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l638_671)
        # Marcamos BlueLamda_Range448 como elegible para BlueLamdaMode_l448_463
        self.mdBlueLamdaMode_l448_463.addValue(self.vlBlueLamda_Range448)
        # Marcamos BlueLamda_Range464 como elegible para BlueLamdaMode_l464_480
        self.mdBlueLamdaMode_l464_480.addValue(self.vlBlueLamda_Range464)
        # Marcamos BlueLamda_Range481 como elegible para BlueLamdaMode_l481_502
        self.mdBlueLamdaMode_l481_502.addValue(self.vlBlueLamda_Range481)
        # Marcamos BlueLamda_Range503 como elegible para BlueLamdaMode_l503_521
        self.mdBlueLamdaMode_l503_521.addValue(self.vlBlueLamda_Range503)
        # Marcamos BlueLamda_Range522 como elegible para BlueLamdaMode_l522_542
        self.mdBlueLamdaMode_l522_542.addValue(self.vlBlueLamda_Range522)
        # Marcamos BlueLamda_Range543 como elegible para BlueLamdaMode_l543_583
        self.mdBlueLamdaMode_l543_583.addValue(self.vlBlueLamda_Range543)
        # Marcamos BlueLamda_Range584 como elegible para BlueLamdaMode_l584_609
        self.mdBlueLamdaMode_l584_609.addValue(self.vlBlueLamda_Range584)
        # Marcamos BlueLamda_Range610 como elegible para BlueLamdaMode_l610_637
        self.mdBlueLamdaMode_l610_637.addValue(self.vlBlueLamda_Range610)
        # Marcamos BlueLamda_Range638 como elegible para BlueLamdaMode_l638_671
        self.mdBlueLamdaMode_l638_671.addValue(self.vlBlueLamda_Range638)
        # Marcamos zzeroMode_Normal como elegible para PreOpticsMode_RTFCalib
        self.mdPreOpticsMode_RTFCalib.addSubMode(self.mdzzeroMode_Normal)
        # Marcamos zzeroMode_Normal como elegible para PreOpticsMode_BTFCalib
        self.mdPreOpticsMode_BTFCalib.addSubMode(self.mdzzeroMode_Normal)
        # Marcamos zzeroMode_Normal como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdzzeroMode_Normal)
        # Marcamos zzero_NormalRange como elegible para zzeroMode_Normal
        self.mdzzeroMode_Normal.addValue(self.vlzzero_NormalRange)
        # Marcamos FiltersMode_Broad como elegible para PreOpticsMode_NoDispersion
        self.mdPreOpticsMode_NoDispersion.addSubMode(self.mdFiltersMode_Broad)
        # Marcamos FiltersMode_UFilter como elegible para PreOpticsMode_NoDispersion
        self.mdPreOpticsMode_NoDispersion.addSubMode(self.mdFiltersMode_UFilter)
        # Marcamos FiltersMode_NoFilter como elegible para PreOpticsMode_NoDispersion
        self.mdPreOpticsMode_NoDispersion.addSubMode(self.mdFiltersMode_NoFilter)
        # Marcamos FiltersMode_OS como elegible para PreOpticsMode_NoDispersion
        self.mdPreOpticsMode_NoDispersion.addSubMode(self.mdFiltersMode_OS)
        # Marcamos FiltersMode_OSCalc como elegible para PreOpticsMode_RTF
        self.mdPreOpticsMode_RTF.addSubMode(self.mdFiltersMode_OSCalc)
        # Marcamos FiltersMode_GR como elegible para PreOpticsMode_GrismR
        self.mdPreOpticsMode_GrismR.addSubMode(self.mdFiltersMode_GR)
        # Marcamos FiltersMode_OS como elegible para PreOpticsMode_GrismR
        self.mdPreOpticsMode_GrismR.addSubMode(self.mdFiltersMode_OS)
        # Marcamos FiltersMode_UFilter como elegible para PreOpticsMode_GrismR
        self.mdPreOpticsMode_GrismR.addSubMode(self.mdFiltersMode_UFilter)
        # Marcamos FiltersMode_Broad como elegible para PreOpticsMode_GrismR
        self.mdPreOpticsMode_GrismR.addSubMode(self.mdFiltersMode_Broad)
        # Marcamos FiltersMode_OSCalc como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdFiltersMode_OSCalc)
        # Marcamos FiltersMode_NoFilter como elegible para PreOpticsMode_GrismB
        self.mdPreOpticsMode_GrismB.addSubMode(self.mdFiltersMode_NoFilter)
        # Marcamos FiltersMode_NoFilter como elegible para PreOpticsMode_GrismBMOS
        self.mdPreOpticsMode_GrismBMOS.addSubMode(self.mdFiltersMode_NoFilter)
        # Marcamos FiltersMode_OS como elegible para PreOpticsMode_GrismBMOS
        self.mdPreOpticsMode_GrismBMOS.addSubMode(self.mdFiltersMode_OS)
        # Marcamos FiltersMode_Broad como elegible para PreOpticsMode_GrismBMOS
        self.mdPreOpticsMode_GrismBMOS.addSubMode(self.mdFiltersMode_Broad)
        # Marcamos FiltersMode_UFilter como elegible para PreOpticsMode_GrismBMOS
        self.mdPreOpticsMode_GrismBMOS.addSubMode(self.mdFiltersMode_UFilter)
        # Marcamos FiltersMode_OS como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdFiltersMode_OS)
        # Marcamos FiltersMode_UFilter como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdFiltersMode_UFilter)
        # Marcamos FiltersMode_NoFilter como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdFiltersMode_NoFilter)
        # Marcamos FiltersMode_GR como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdFiltersMode_GR)
        # Marcamos FiltersMode_Broad como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdFiltersMode_Broad)
        # Marcamos FiltersMode_OSCalc como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdFiltersMode_OSCalc)
        # Marcamos FiltersMode_Engineering como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdFiltersMode_Engineering)
        # Marcamos UFiltersMode_U9xx como elegible para FiltersMode_UFilter
        self.mdFiltersMode_UFilter.addSubMode(self.mdUFiltersMode_U9xx)
        # Marcamos UFiltersMode_U8xx como elegible para FiltersMode_UFilter
        self.mdFiltersMode_UFilter.addSubMode(self.mdUFiltersMode_U8xx)
        # Marcamos UFiltersMode_U7xx como elegible para FiltersMode_UFilter
        self.mdFiltersMode_UFilter.addSubMode(self.mdUFiltersMode_U7xx)
        # Marcamos UFiltersMode_U6xx como elegible para FiltersMode_UFilter
        self.mdFiltersMode_UFilter.addSubMode(self.mdUFiltersMode_U6xx)
        # Marcamos UFiltersMode_U5xx como elegible para FiltersMode_UFilter
        self.mdFiltersMode_UFilter.addSubMode(self.mdUFiltersMode_U5xx)
        # Marcamos UFiltersMode_U5xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdUFiltersMode_U5xx)
        # Marcamos UFiltersMode_U6xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdUFiltersMode_U6xx)
        # Marcamos UFiltersMode_U7xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdUFiltersMode_U7xx)
        # Marcamos UFiltersMode_U8xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdUFiltersMode_U8xx)
        # Marcamos UFiltersMode_U9xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdUFiltersMode_U9xx)
        # Marcamos UFilters_U551_17 como elegible para UFiltersMode_U5xx
        self.mdUFiltersMode_U5xx.addValue(self.vlUFilters_U551_17)
        # Marcamos UFilters_U568_17 como elegible para UFiltersMode_U5xx
        self.mdUFiltersMode_U5xx.addValue(self.vlUFilters_U568_17)
        # Marcamos UFilters_U534_17 como elegible para UFiltersMode_U5xx
        self.mdUFiltersMode_U5xx.addValue(self.vlUFilters_U534_17)
        # Marcamos UFilters_U500_17 como elegible para UFiltersMode_U5xx
        self.mdUFiltersMode_U5xx.addValue(self.vlUFilters_U500_17)
        # Marcamos UFilters_U517_17 como elegible para UFiltersMode_U5xx
        self.mdUFiltersMode_U5xx.addValue(self.vlUFilters_U517_17)
        # Marcamos UFilters_U585_17 como elegible para UFiltersMode_U5xx
        self.mdUFiltersMode_U5xx.addValue(self.vlUFilters_U585_17)
        # Marcamos UFilters_U653_17 como elegible para UFiltersMode_U6xx
        self.mdUFiltersMode_U6xx.addValue(self.vlUFilters_U653_17)
        # Marcamos UFilters_U670_17 como elegible para UFiltersMode_U6xx
        self.mdUFiltersMode_U6xx.addValue(self.vlUFilters_U670_17)
        # Marcamos UFilters_U687_17 como elegible para UFiltersMode_U6xx
        self.mdUFiltersMode_U6xx.addValue(self.vlUFilters_U687_17)
        # Marcamos UFilters_U602_17 como elegible para UFiltersMode_U6xx
        self.mdUFiltersMode_U6xx.addValue(self.vlUFilters_U602_17)
        # Marcamos UFilters_U636_17 como elegible para UFiltersMode_U6xx
        self.mdUFiltersMode_U6xx.addValue(self.vlUFilters_U636_17)
        # Marcamos UFilters_U619_17 como elegible para UFiltersMode_U6xx
        self.mdUFiltersMode_U6xx.addValue(self.vlUFilters_U619_17)
        # Marcamos UFilters_U772_17 como elegible para UFiltersMode_U7xx
        self.mdUFiltersMode_U7xx.addValue(self.vlUFilters_U772_17)
        # Marcamos UFilters_U721_17 como elegible para UFiltersMode_U7xx
        self.mdUFiltersMode_U7xx.addValue(self.vlUFilters_U721_17)
        # Marcamos UFilters_U755_17 como elegible para UFiltersMode_U7xx
        self.mdUFiltersMode_U7xx.addValue(self.vlUFilters_U755_17)
        # Marcamos UFilters_U704_17 como elegible para UFiltersMode_U7xx
        self.mdUFiltersMode_U7xx.addValue(self.vlUFilters_U704_17)
        # Marcamos UFilters_U738_17 como elegible para UFiltersMode_U7xx
        self.mdUFiltersMode_U7xx.addValue(self.vlUFilters_U738_17)
        # Marcamos UFilters_U789_17 como elegible para UFiltersMode_U7xx
        self.mdUFiltersMode_U7xx.addValue(self.vlUFilters_U789_17)
        # Marcamos UFilters_U806_17 como elegible para UFiltersMode_U8xx
        self.mdUFiltersMode_U8xx.addValue(self.vlUFilters_U806_17)
        # Marcamos UFilters_U840_17 como elegible para UFiltersMode_U8xx
        self.mdUFiltersMode_U8xx.addValue(self.vlUFilters_U840_17)
        # Marcamos UFilters_U857_17 como elegible para UFiltersMode_U8xx
        self.mdUFiltersMode_U8xx.addValue(self.vlUFilters_U857_17)
        # Marcamos UFilters_U823_17 como elegible para UFiltersMode_U8xx
        self.mdUFiltersMode_U8xx.addValue(self.vlUFilters_U823_17)
        # Marcamos UFilters_U883_35 como elegible para UFiltersMode_U8xx
        self.mdUFiltersMode_U8xx.addValue(self.vlUFilters_U883_35)
        # Marcamos UFilters_U941_33 como elegible para UFiltersMode_U9xx
        self.mdUFiltersMode_U9xx.addValue(self.vlUFilters_U941_33)
        # Marcamos UFilters_U913_25 como elegible para UFiltersMode_U9xx
        self.mdUFiltersMode_U9xx.addValue(self.vlUFilters_U913_25)
        # Marcamos OSMode_f8xx como elegible para FiltersMode_OS
        self.mdFiltersMode_OS.addSubMode(self.mdOSMode_f8xx)
        # Marcamos OSMode_f9xx como elegible para FiltersMode_OS
        self.mdFiltersMode_OS.addSubMode(self.mdOSMode_f9xx)
        # Marcamos OSMode_f7xx como elegible para FiltersMode_OS
        self.mdFiltersMode_OS.addSubMode(self.mdOSMode_f7xx)
        # Marcamos OSMode_f6xx como elegible para FiltersMode_OS
        self.mdFiltersMode_OS.addSubMode(self.mdOSMode_f6xx)
        # Marcamos OSMode_f4xx como elegible para FiltersMode_OS
        self.mdFiltersMode_OS.addSubMode(self.mdOSMode_f4xx)
        # Marcamos OSMode_f5xx como elegible para FiltersMode_OS
        self.mdFiltersMode_OS.addSubMode(self.mdOSMode_f5xx)
        # Marcamos OSMode_f5xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdOSMode_f5xx)
        # Marcamos OSMode_f4xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdOSMode_f4xx)
        # Marcamos OSMode_f6xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdOSMode_f6xx)
        # Marcamos OSMode_f7xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdOSMode_f7xx)
        # Marcamos OSMode_f9xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdOSMode_f9xx)
        # Marcamos OSMode_f8xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdOSMode_f8xx)
        # Marcamos OS_f504_16 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f504_16)
        # Marcamos OS_f509_16 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f509_16)
        # Marcamos OS_f514_16 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f514_16)
        # Marcamos OS_f519_16 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f519_16)
        # Marcamos OS_f525_17 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f525_17)
        # Marcamos OS_f530_17 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f530_17)
        # Marcamos OS_f536_17 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f536_17)
        # Marcamos OS_f542_18 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f542_18)
        # Marcamos OS_f548_18 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f548_18)
        # Marcamos OS_f554_18 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f554_18)
        # Marcamos OS_f561_19 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f561_19)
        # Marcamos OS_f568_19 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f568_19)
        # Marcamos OS_f575_19 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f575_19)
        # Marcamos OS_f583_20 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f583_20)
        # Marcamos OS_f591_21 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f591_21)
        # Marcamos OS_f599_22 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f599_22)
        # Marcamos OS_f451_13 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f451_13)
        # Marcamos OS_f477_14 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f477_14)
        # Marcamos OS_f454_13 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f454_13)
        # Marcamos OS_f481_14 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f481_14)
        # Marcamos OS_f458_13 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f458_13)
        # Marcamos OS_f486_14 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f486_14)
        # Marcamos OS_f461_13 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f461_13)
        # Marcamos OS_f490_15 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f490_15)
        # Marcamos OS_f495_15 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f495_15)
        # Marcamos OS_f465_13 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f465_13)
        # Marcamos OS_f499_15 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f499_15)
        # Marcamos OS_f469_14 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f469_14)
        # Marcamos OS_f473_14 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f473_14)
        # Marcamos OS_f608_22 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f608_22)
        # Marcamos OS_f617_23 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f617_23)
        # Marcamos OS_f627_24 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f627_24)
        # Marcamos OS_f638_25 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f638_25)
        # Marcamos OS_f649_25 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f649_25)
        # Marcamos OS_f657_35 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f657_35)
        # Marcamos OS_f661_27 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f661_27)
        # Marcamos OS_f666_36 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f666_36)
        # Marcamos OS_f680_43 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f680_43)
        # Marcamos OS_f694_44 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f694_44)
        # Marcamos OS_f709_45 como elegible para OSMode_f7xx
        self.mdOSMode_f7xx.addValue(self.vlOS_f709_45)
        # Marcamos OS_f754_50 como elegible para OSMode_f7xx
        self.mdOSMode_f7xx.addValue(self.vlOS_f754_50)
        # Marcamos OS_f770_50 como elegible para OSMode_f7xx
        self.mdOSMode_f7xx.addValue(self.vlOS_f770_50)
        # Marcamos OS_f723_45 como elegible para OSMode_f7xx
        self.mdOSMode_f7xx.addValue(self.vlOS_f723_45)
        # Marcamos OS_f738_49 como elegible para OSMode_f7xx
        self.mdOSMode_f7xx.addValue(self.vlOS_f738_49)
        # Marcamos OS_f785_48 como elegible para OSMode_f7xx
        self.mdOSMode_f7xx.addValue(self.vlOS_f785_48)
        # Marcamos OS_f902_44 como elegible para OSMode_f9xx
        self.mdOSMode_f9xx.addValue(self.vlOS_f902_44)
        # Marcamos OS_f910_40 como elegible para OSMode_f9xx
        self.mdOSMode_f9xx.addValue(self.vlOS_f910_40)
        # Marcamos OS_f919_41 como elegible para OSMode_f9xx
        self.mdOSMode_f9xx.addValue(self.vlOS_f919_41)
        # Marcamos OS_f923_34 como elegible para OSMode_f9xx
        self.mdOSMode_f9xx.addValue(self.vlOS_f923_34)
        # Marcamos OS_f927_34 como elegible para OSMode_f9xx
        self.mdOSMode_f9xx.addValue(self.vlOS_f927_34)
        # Marcamos OS_f932_34 como elegible para OSMode_f9xx
        self.mdOSMode_f9xx.addValue(self.vlOS_f932_34)
        # Marcamos OS_f802_51 como elegible para OSMode_f8xx
        self.mdOSMode_f8xx.addValue(self.vlOS_f802_51)
        # Marcamos OS_f819_52 como elegible para OSMode_f8xx
        self.mdOSMode_f8xx.addValue(self.vlOS_f819_52)
        # Marcamos OS_f838_58 como elegible para OSMode_f8xx
        self.mdOSMode_f8xx.addValue(self.vlOS_f838_58)
        # Marcamos OS_f858_58 como elegible para OSMode_f8xx
        self.mdOSMode_f8xx.addValue(self.vlOS_f858_58)
        # Marcamos OS_f878_59 como elegible para OSMode_f8xx
        self.mdOSMode_f8xx.addValue(self.vlOS_f878_59)
        # Marcamos OS_f893_50 como elegible para OSMode_f8xx
        self.mdOSMode_f8xx.addValue(self.vlOS_f893_50)
        # Marcamos BroadMode_All como elegible para FiltersMode_Broad
        self.mdFiltersMode_Broad.addSubMode(self.mdBroadMode_All)
        # Marcamos BroadMode_All como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdBroadMode_All)
        # Marcamos Broad_Sloan_z como elegible para BroadMode_All
        self.mdBroadMode_All.addValue(self.vlBroad_Sloan_z)
        # Marcamos Broad_Sloan_u como elegible para BroadMode_All
        self.mdBroadMode_All.addValue(self.vlBroad_Sloan_u)
        # Marcamos Broad_Sloan_r como elegible para BroadMode_All
        self.mdBroadMode_All.addValue(self.vlBroad_Sloan_r)
        # Marcamos Broad_Sloan_g como elegible para BroadMode_All
        self.mdBroadMode_All.addValue(self.vlBroad_Sloan_g)
        # Marcamos Broad_Sloan_i como elegible para BroadMode_All
        self.mdBroadMode_All.addValue(self.vlBroad_Sloan_i)
        # Marcamos DetectorMode_FullDetector como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdDetectorMode_FullDetector)
        # Marcamos DetectorMode_Window como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdDetectorMode_Window)
        # Marcamos DetectorMode_FT como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdDetectorMode_FT)
        # Marcamos DetectorMode_FullDetector como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdDetectorMode_FullDetector)
        # Marcamos DetectorMode_FT como elegible para AcquisitionMode_FTBias
        self.mdAcquisitionMode_FTBias.addSubMode(self.mdDetectorMode_FT)
        # Marcamos DetectorMode_FullDetector como elegible para AcquisitionMode_NormalBias
        self.mdAcquisitionMode_NormalBias.addSubMode(self.mdDetectorMode_FullDetector)
        # Marcamos DetectorMode_Window como elegible para AcquisitionMode_NormalBias
        self.mdAcquisitionMode_NormalBias.addSubMode(self.mdDetectorMode_Window)
        # Marcamos DetectorMode_FullDetector como elegible para AcquisitionMode_ShufflingBias
        self.mdAcquisitionMode_ShufflingBias.addSubMode(self.mdDetectorMode_FullDetector)
        # Marcamos DetectorMode_FullDetectorSq como elegible para AcquisitionMode_NormalSquare
        self.mdAcquisitionMode_NormalSquare.addSubMode(self.mdDetectorMode_FullDetectorSq)
        # Marcamos DetectorMode_WindowSq como elegible para AcquisitionMode_NormalSquare
        self.mdAcquisitionMode_NormalSquare.addSubMode(self.mdDetectorMode_WindowSq)
        # Marcamos DetectorMode_FullDetectorSq como elegible para AcquisitionMode_ShufflingSquare
        self.mdAcquisitionMode_ShufflingSquare.addSubMode(self.mdDetectorMode_FullDetectorSq)
        # Marcamos DetectorMode_FullDetector como elegible para AcquisitionMode_GainCalib
        self.mdAcquisitionMode_GainCalib.addSubMode(self.mdDetectorMode_FullDetector)
        # Marcamos DetectorMode_FT como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdDetectorMode_FT)
        # Marcamos DetectorMode_Window como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdDetectorMode_Window)
        # Marcamos DetectorMode_FullDetector como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdDetectorMode_FullDetector)
        # Marcamos DetectorMode_WindowSq como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdDetectorMode_WindowSq)
        # Marcamos DetectorMode_FullDetectorSq como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdDetectorMode_FullDetectorSq)
        # Marcamos DetectorMode_Engineering como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdDetectorMode_Engineering)
        # Marcamos OutputSourceMode_TWO como elegible para DetectorMode_FT
        self.mdDetectorMode_FT.addSubMode(self.mdOutputSourceMode_TWO)
        # Marcamos OutputSourceMode_0x0 como elegible para DetectorMode_FT
        self.mdDetectorMode_FT.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x0 como elegible para DetectorMode_Window
        self.mdDetectorMode_Window.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x0 como elegible para DetectorMode_FullDetector
        self.mdDetectorMode_FullDetector.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x1 como elegible para DetectorMode_FullDetector
        self.mdDetectorMode_FullDetector.addSubMode(self.mdOutputSourceMode_0x1)
        # Marcamos OutputSourceMode_0x2 como elegible para DetectorMode_FullDetector
        self.mdDetectorMode_FullDetector.addSubMode(self.mdOutputSourceMode_0x2)
        # Marcamos OutputSourceMode_0x3 como elegible para DetectorMode_FullDetector
        self.mdDetectorMode_FullDetector.addSubMode(self.mdOutputSourceMode_0x3)
        # Marcamos OutputSourceMode_ALL como elegible para DetectorMode_FullDetector
        self.mdDetectorMode_FullDetector.addSubMode(self.mdOutputSourceMode_ALL)
        # Marcamos OutputSourceMode_0x0 como elegible para DetectorMode_WindowSq
        self.mdDetectorMode_WindowSq.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x0 como elegible para DetectorMode_FullDetectorSq
        self.mdDetectorMode_FullDetectorSq.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x1 como elegible para DetectorMode_FullDetectorSq
        self.mdDetectorMode_FullDetectorSq.addSubMode(self.mdOutputSourceMode_0x1)
        # Marcamos OutputSourceMode_0x2 como elegible para DetectorMode_FullDetectorSq
        self.mdDetectorMode_FullDetectorSq.addSubMode(self.mdOutputSourceMode_0x2)
        # Marcamos OutputSourceMode_0x3 como elegible para DetectorMode_FullDetectorSq
        self.mdDetectorMode_FullDetectorSq.addSubMode(self.mdOutputSourceMode_0x3)
        # Marcamos OutputSourceMode_ALL como elegible para DetectorMode_FullDetectorSq
        self.mdDetectorMode_FullDetectorSq.addSubMode(self.mdOutputSourceMode_ALL)
        # Marcamos OutputSourceMode_0x0 como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x1 como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdOutputSourceMode_0x1)
        # Marcamos OutputSourceMode_0x2 como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdOutputSourceMode_0x2)
        # Marcamos OutputSourceMode_0x3 como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdOutputSourceMode_0x3)
        # Marcamos OutputSourceMode_ALL como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdOutputSourceMode_ALL)
        # Marcamos OutputSourceMode_TWO como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdOutputSourceMode_TWO)
        # Marcamos OutputSourceMode_Engineering como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdOutputSourceMode_Engineering)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_0x0
        self.mdOutputSourceMode_0x0.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_0x1
        self.mdOutputSourceMode_0x1.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_0x2
        self.mdOutputSourceMode_0x2.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_0x3
        self.mdOutputSourceMode_0x3.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_QuadCCD como elegible para OutputSourceMode_ALL
        self.mdOutputSourceMode_ALL.addSubMode(self.mdRecompositionMode_QuadCCD)
        # Marcamos RecompositionMode_Serial como elegible para OutputSourceMode_TWO
        self.mdOutputSourceMode_TWO.addSubMode(self.mdRecompositionMode_Serial)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_Serial como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_Serial)
        # Marcamos RecompositionMode_QuadCCD como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_QuadCCD)
        # Marcamos BinningMode_Square como elegible para DetectorMode_FT
        self.mdDetectorMode_FT.addSubMode(self.mdBinningMode_Square)
        # Marcamos BinningMode_All como elegible para DetectorMode_Window
        self.mdDetectorMode_Window.addSubMode(self.mdBinningMode_All)
        # Marcamos BinningMode_All como elegible para DetectorMode_FullDetector
        self.mdDetectorMode_FullDetector.addSubMode(self.mdBinningMode_All)
        # Marcamos BinningMode_Square como elegible para DetectorMode_WindowSq
        self.mdDetectorMode_WindowSq.addSubMode(self.mdBinningMode_Square)
        # Marcamos BinningMode_Square como elegible para DetectorMode_FullDetectorSq
        self.mdDetectorMode_FullDetectorSq.addSubMode(self.mdBinningMode_Square)
        # Marcamos BinningMode_All como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdBinningMode_All)
        # Marcamos BinningMode_Square como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdBinningMode_Square)
        # Marcamos BinningMode_Off como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdBinningMode_Off)
        # Marcamos Binning_1x1 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_1x1)
        # Marcamos Binning_1x2 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_1x2)
        # Marcamos Binning_2x1 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_2x1)
        # Marcamos Binning_2x2 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_2x2)
        # Marcamos Binning_1x1 como elegible para BinningMode_Square
        self.mdBinningMode_Square.addValue(self.vlBinning_1x1)
        # Marcamos Binning_2x2 como elegible para BinningMode_Square
        self.mdBinningMode_Square.addValue(self.vlBinning_2x2)
        # Marcamos Binning_1x1 como elegible para BinningMode_Off
        self.mdBinningMode_Off.addValue(self.vlBinning_1x1)
        # Marcamos WindowMode_Disabled como elegible para DetectorMode_FT
        self.mdDetectorMode_FT.addSubMode(self.mdWindowMode_Disabled)
        # Marcamos WindowMode_Enabled como elegible para DetectorMode_FT
        self.mdDetectorMode_FT.addSubMode(self.mdWindowMode_Enabled)
        # Marcamos WindowMode_Enabled como elegible para DetectorMode_Window
        self.mdDetectorMode_Window.addSubMode(self.mdWindowMode_Enabled)
        # Marcamos WindowMode_Disabled como elegible para DetectorMode_FullDetector
        self.mdDetectorMode_FullDetector.addSubMode(self.mdWindowMode_Disabled)
        # Marcamos WindowMode_Enabled como elegible para DetectorMode_WindowSq
        self.mdDetectorMode_WindowSq.addSubMode(self.mdWindowMode_Enabled)
        # Marcamos WindowMode_Disabled como elegible para DetectorMode_FullDetectorSq
        self.mdDetectorMode_FullDetectorSq.addSubMode(self.mdWindowMode_Disabled)
        # Marcamos WindowMode_Enabled como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdWindowMode_Enabled)
        # Marcamos WindowMode_Disabled como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdWindowMode_Disabled)
        # Marcamos WindowMode_Engineering como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdWindowMode_Engineering)
        # Marcamos RowsMode_Normal como elegible para WindowMode_Enabled
        self.mdWindowMode_Enabled.addSubMode(self.mdRowsMode_Normal)
        # Marcamos RowsMode_Normal como elegible para WindowMode_Engineering
        self.mdWindowMode_Engineering.addSubMode(self.mdRowsMode_Normal)
        # Marcamos Rows_FullRange como elegible para RowsMode_Normal
        self.mdRowsMode_Normal.addValue(self.vlRows_FullRange)
        # Marcamos ColsMode_Normal como elegible para WindowMode_Enabled
        self.mdWindowMode_Enabled.addSubMode(self.mdColsMode_Normal)
        # Marcamos ColsMode_Normal como elegible para WindowMode_Engineering
        self.mdWindowMode_Engineering.addSubMode(self.mdColsMode_Normal)
        # Marcamos Cols_FullRange como elegible para ColsMode_Normal
        self.mdColsMode_Normal.addValue(self.vlCols_FullRange)
        # Marcamos offsetRowMode_Normal como elegible para WindowMode_Enabled
        self.mdWindowMode_Enabled.addSubMode(self.mdoffsetRowMode_Normal)
        # Marcamos offsetRowMode_Normal como elegible para WindowMode_Engineering
        self.mdWindowMode_Engineering.addSubMode(self.mdoffsetRowMode_Normal)
        # Marcamos offsetRow_FullRange como elegible para offsetRowMode_Normal
        self.mdoffsetRowMode_Normal.addValue(self.vloffsetRow_FullRange)
        # Marcamos offsetColMode_Normal como elegible para WindowMode_Enabled
        self.mdWindowMode_Enabled.addSubMode(self.mdoffsetColMode_Normal)
        # Marcamos offsetColMode_Normal como elegible para WindowMode_Engineering
        self.mdWindowMode_Engineering.addSubMode(self.mdoffsetColMode_Normal)
        # Marcamos offsetCol_FullRange como elegible para offsetColMode_Normal
        self.mdoffsetColMode_Normal.addValue(self.vloffsetCol_FullRange)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## OsirisMode 
    def get_OsirisMode(self)-> PORISMode:
        return self.sysOsiris.getSelectedMode()

    def set_OsirisMode(self, mode: PORISMode)-> PORISMode :
        return self.sysOsiris.selectMode(mode)


    ## ObservingModesMode 
    def get_ObservingModesMode(self)-> PORISMode:
        return self.sysObservingModes.getSelectedMode()

    def set_ObservingModesMode(self, mode: PORISMode)-> PORISMode :
        return self.sysObservingModes.selectMode(mode)


    ## AcquisitionModesMode 
    def get_AcquisitionModesMode(self)-> PORISMode:
        return self.sysAcquisitionModes.getSelectedMode()

    def set_AcquisitionModesMode(self, mode: PORISMode)-> PORISMode :
        return self.sysAcquisitionModes.selectMode(mode)


    ## FPEMode 
    def get_FPEMode(self)-> PORISMode:
        return self.sysFPE.getSelectedMode()

    def set_FPEMode(self, mode: PORISMode)-> PORISMode :
        return self.sysFPE.selectMode(mode)


    ## prParam FocalPlaneElement 

    # FocalPlaneElement
    def get_FocalPlaneElement(self)-> PORISValue :
        return self.prFocalPlaneElement.getSelectedValue()

    def set_FocalPlaneElement(self, value: PORISValue)-> PORISValue :
        return self.prFocalPlaneElement.setValue(value)


    ## FocalPlaneElementMode 
    def get_FocalPlaneElementMode(self)-> PORISMode:
        return self.prFocalPlaneElement.getSelectedMode()

    def set_FocalPlaneElementMode(self, mode: PORISMode)-> PORISMode :
        return self.prFocalPlaneElement.selectMode(mode)


    ## DASMode 
    def get_DASMode(self)-> PORISMode:
        return self.sysDAS.getSelectedMode()

    def set_DASMode(self, mode: PORISMode)-> PORISMode :
        return self.sysDAS.selectMode(mode)


    ## AcquisitionMode 
    def get_AcquisitionMode(self)-> PORISMode:
        return self.sysAcquisition.getSelectedMode()

    def set_AcquisitionMode(self, mode: PORISMode)-> PORISMode :
        return self.sysAcquisition.selectMode(mode)


    ## prParam ShuffleLines 

    # ShuffleLines
    def get_ShuffleLines(self)-> PORISValue :
        return self.prShuffleLines.getSelectedValue()

    def set_ShuffleLines(self, value: PORISValue)-> PORISValue :
        return self.prShuffleLines.setValue(value)


    ## ShuffleLinesMode 
    def get_ShuffleLinesMode(self)-> PORISMode:
        return self.prShuffleLines.getSelectedMode()

    def set_ShuffleLinesMode(self, mode: PORISMode)-> PORISMode :
        return self.prShuffleLines.selectMode(mode)


    ## prParam Acquisition 

    # ShuffleLinesDouble  
    def get_ShuffleLinesDouble(self)-> float :
        v = self.prShuffleLines.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ShuffleLinesDouble(self, data: float)-> float :
        return self.prShuffleLines.getSelectedValue().setData(data)


    ## prParam ShiftNumber 

    # ShiftNumber
    def get_ShiftNumber(self)-> PORISValue :
        return self.prShiftNumber.getSelectedValue()

    def set_ShiftNumber(self, value: PORISValue)-> PORISValue :
        return self.prShiftNumber.setValue(value)


    ## ShiftNumberMode 
    def get_ShiftNumberMode(self)-> PORISMode:
        return self.prShiftNumber.getSelectedMode()

    def set_ShiftNumberMode(self, mode: PORISMode)-> PORISMode :
        return self.prShiftNumber.selectMode(mode)


    ## prParam Acquisition 

    # ShiftNumberDouble  
    def get_ShiftNumberDouble(self)-> float :
        v = self.prShiftNumber.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ShiftNumberDouble(self, data: float)-> float :
        return self.prShiftNumber.getSelectedValue().setData(data)


    ## prParam ExpTime 

    # ExpTime
    def get_ExpTime(self)-> PORISValue :
        return self.prExpTime.getSelectedValue()

    def set_ExpTime(self, value: PORISValue)-> PORISValue :
        return self.prExpTime.setValue(value)


    ## ExpTimeMode 
    def get_ExpTimeMode(self)-> PORISMode:
        return self.prExpTime.getSelectedMode()

    def set_ExpTimeMode(self, mode: PORISMode)-> PORISMode :
        return self.prExpTime.selectMode(mode)


    ## prParam Acquisition 

    # ExpTimeDouble  
    def get_ExpTimeDouble(self)-> float :
        v = self.prExpTime.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ExpTimeDouble(self, data: float)-> float :
        return self.prExpTime.getSelectedValue().setData(data)


    ## prParam Acquisition 

    # ExpTimeDouble  
    def get_ExpTimeDouble(self)-> float :
        v = self.prExpTime.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ExpTimeDouble(self, data: float)-> float :
        return self.prExpTime.getSelectedValue().setData(data)


    ## MultipleExposureMode 
    def get_MultipleExposureMode(self)-> PORISMode:
        return self.sysMultipleExposure.getSelectedMode()

    def set_MultipleExposureMode(self, mode: PORISMode)-> PORISMode :
        return self.sysMultipleExposure.selectMode(mode)


    ## prParam numOfFrames 

    # numOfFrames
    def get_numOfFrames(self)-> PORISValue :
        return self.prnumOfFrames.getSelectedValue()

    def set_numOfFrames(self, value: PORISValue)-> PORISValue :
        return self.prnumOfFrames.setValue(value)


    ## numOfFramesMode 
    def get_numOfFramesMode(self)-> PORISMode:
        return self.prnumOfFrames.getSelectedMode()

    def set_numOfFramesMode(self, mode: PORISMode)-> PORISMode :
        return self.prnumOfFrames.selectMode(mode)


    ## prParam MultipleExposure 

    # numOfFramesDouble  
    def get_numOfFramesDouble(self)-> float :
        v = self.prnumOfFrames.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_numOfFramesDouble(self, data: float)-> float :
        return self.prnumOfFrames.getSelectedValue().setData(data)


    ## prParam PixelSpeed 

    # PixelSpeed
    def get_PixelSpeed(self)-> PORISValue :
        return self.prPixelSpeed.getSelectedValue()

    def set_PixelSpeed(self, value: PORISValue)-> PORISValue :
        return self.prPixelSpeed.setValue(value)


    ## PixelSpeedMode 
    def get_PixelSpeedMode(self)-> PORISMode:
        return self.prPixelSpeed.getSelectedMode()

    def set_PixelSpeedMode(self, mode: PORISMode)-> PORISMode :
        return self.prPixelSpeed.selectMode(mode)


    ## prParam CalibGain 

    # CalibGain
    def get_CalibGain(self)-> PORISValue :
        return self.prCalibGain.getSelectedValue()

    def set_CalibGain(self, value: PORISValue)-> PORISValue :
        return self.prCalibGain.setValue(value)


    ## CalibGainMode 
    def get_CalibGainMode(self)-> PORISMode:
        return self.prCalibGain.getSelectedMode()

    def set_CalibGainMode(self, mode: PORISMode)-> PORISMode :
        return self.prCalibGain.selectMode(mode)


    ## prParam Acquisition 

    # CalibGainDouble  
    def get_CalibGainDouble(self)-> float :
        v = self.prCalibGain.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_CalibGainDouble(self, data: float)-> float :
        return self.prCalibGain.getSelectedValue().setData(data)


    ## OpenShutterMode 
    def get_OpenShutterMode(self)-> PORISMode:
        return self.sysOpenShutter.getSelectedMode()

    def set_OpenShutterMode(self, mode: PORISMode)-> PORISMode :
        return self.sysOpenShutter.selectMode(mode)


    ## ProcessMonitorMode 
    def get_ProcessMonitorMode(self)-> PORISMode:
        return self.sysProcessMonitor.getSelectedMode()

    def set_ProcessMonitorMode(self, mode: PORISMode)-> PORISMode :
        return self.sysProcessMonitor.selectMode(mode)


    ## prParam CurrentEllapsed 

    # CurrentEllapsed
    def get_CurrentEllapsed(self)-> PORISValue :
        return self.prCurrentEllapsed.getSelectedValue()

    def set_CurrentEllapsed(self, value: PORISValue)-> PORISValue :
        return self.prCurrentEllapsed.setValue(value)


    ## CurrentEllapsedMode 
    def get_CurrentEllapsedMode(self)-> PORISMode:
        return self.prCurrentEllapsed.getSelectedMode()

    def set_CurrentEllapsedMode(self, mode: PORISMode)-> PORISMode :
        return self.prCurrentEllapsed.selectMode(mode)


    ## prParam ProcessMonitor 

    # CurrentEllapsedDouble  
    def get_CurrentEllapsedDouble(self)-> float :
        v = self.prCurrentEllapsed.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_CurrentEllapsedDouble(self, data: float)-> float :
        return self.prCurrentEllapsed.getSelectedValue().setData(data)


    ## prParam CurrentImg 

    # CurrentImg
    def get_CurrentImg(self)-> PORISValue :
        return self.prCurrentImg.getSelectedValue()

    def set_CurrentImg(self, value: PORISValue)-> PORISValue :
        return self.prCurrentImg.setValue(value)


    ## CurrentImgMode 
    def get_CurrentImgMode(self)-> PORISMode:
        return self.prCurrentImg.getSelectedMode()

    def set_CurrentImgMode(self, mode: PORISMode)-> PORISMode :
        return self.prCurrentImg.selectMode(mode)


    ## prParam ProcessMonitor 

    # CurrentImgDouble  
    def get_CurrentImgDouble(self)-> float :
        v = self.prCurrentImg.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_CurrentImgDouble(self, data: float)-> float :
        return self.prCurrentImg.getSelectedValue().setData(data)


    ## prParam CurrentPct 

    # CurrentPct
    def get_CurrentPct(self)-> PORISValue :
        return self.prCurrentPct.getSelectedValue()

    def set_CurrentPct(self, value: PORISValue)-> PORISValue :
        return self.prCurrentPct.setValue(value)


    ## CurrentPctMode 
    def get_CurrentPctMode(self)-> PORISMode:
        return self.prCurrentPct.getSelectedMode()

    def set_CurrentPctMode(self, mode: PORISMode)-> PORISMode :
        return self.prCurrentPct.selectMode(mode)


    ## prParam ProcessMonitor 

    # CurrentPctDouble  
    def get_CurrentPctDouble(self)-> float :
        v = self.prCurrentPct.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_CurrentPctDouble(self, data: float)-> float :
        return self.prCurrentPct.getSelectedValue().setData(data)


    ## prParam OverallPct 

    # OverallPct
    def get_OverallPct(self)-> PORISValue :
        return self.prOverallPct.getSelectedValue()

    def set_OverallPct(self, value: PORISValue)-> PORISValue :
        return self.prOverallPct.setValue(value)


    ## OverallPctMode 
    def get_OverallPctMode(self)-> PORISMode:
        return self.prOverallPct.getSelectedMode()

    def set_OverallPctMode(self, mode: PORISMode)-> PORISMode :
        return self.prOverallPct.selectMode(mode)


    ## prParam ProcessMonitor 

    # OverallPctDouble  
    def get_OverallPctDouble(self)-> float :
        v = self.prOverallPct.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_OverallPctDouble(self, data: float)-> float :
        return self.prOverallPct.getSelectedValue().setData(data)


    ## PreOpticsMode 
    def get_PreOpticsMode(self)-> PORISMode:
        return self.sysPreOptics.getSelectedMode()

    def set_PreOpticsMode(self, mode: PORISMode)-> PORISMode :
        return self.sysPreOptics.selectMode(mode)


    ## prParam Grisms 

    # Grisms
    def get_Grisms(self)-> PORISValue :
        return self.prGrisms.getSelectedValue()

    def set_Grisms(self, value: PORISValue)-> PORISValue :
        return self.prGrisms.setValue(value)


    ## GrismsMode 
    def get_GrismsMode(self)-> PORISMode:
        return self.prGrisms.getSelectedMode()

    def set_GrismsMode(self, mode: PORISMode)-> PORISMode :
        return self.prGrisms.selectMode(mode)


    ## RedTFMode 
    def get_RedTFMode(self)-> PORISMode:
        return self.sysRedTF.getSelectedMode()

    def set_RedTFMode(self, mode: PORISMode)-> PORISMode :
        return self.sysRedTF.selectMode(mode)


    ## prParam RedFWHM 

    # RedFWHM
    def get_RedFWHM(self)-> PORISValue :
        return self.prRedFWHM.getSelectedValue()

    def set_RedFWHM(self, value: PORISValue)-> PORISValue :
        return self.prRedFWHM.setValue(value)


    ## RedFWHMMode 
    def get_RedFWHMMode(self)-> PORISMode:
        return self.prRedFWHM.getSelectedMode()

    def set_RedFWHMMode(self, mode: PORISMode)-> PORISMode :
        return self.prRedFWHM.selectMode(mode)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        v = self.prRedFWHM.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        v = self.prRedFWHM.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        v = self.prRedFWHM.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        v = self.prRedFWHM.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        v = self.prRedFWHM.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        v = self.prRedFWHM.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.getSelectedValue().setData(data)


    ## prParam RedLamda 

    # RedLamda
    def get_RedLamda(self)-> PORISValue :
        return self.prRedLamda.getSelectedValue()

    def set_RedLamda(self, value: PORISValue)-> PORISValue :
        return self.prRedLamda.setValue(value)


    ## RedLamdaMode 
    def get_RedLamdaMode(self)-> PORISMode:
        return self.prRedLamda.getSelectedMode()

    def set_RedLamdaMode(self, mode: PORISMode)-> PORISMode :
        return self.prRedLamda.selectMode(mode)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        v = self.prRedLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        v = self.prRedLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        v = self.prRedLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        v = self.prRedLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        v = self.prRedLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        v = self.prRedLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.getSelectedValue().setData(data)


    ## BlueTFMode 
    def get_BlueTFMode(self)-> PORISMode:
        return self.sysBlueTF.getSelectedMode()

    def set_BlueTFMode(self, mode: PORISMode)-> PORISMode :
        return self.sysBlueTF.selectMode(mode)


    ## prParam BlueFWHM 

    # BlueFWHM
    def get_BlueFWHM(self)-> PORISValue :
        return self.prBlueFWHM.getSelectedValue()

    def set_BlueFWHM(self, value: PORISValue)-> PORISValue :
        return self.prBlueFWHM.setValue(value)


    ## BlueFWHMMode 
    def get_BlueFWHMMode(self)-> PORISMode:
        return self.prBlueFWHM.getSelectedMode()

    def set_BlueFWHMMode(self, mode: PORISMode)-> PORISMode :
        return self.prBlueFWHM.selectMode(mode)


    ## prParam BlueLamda 

    # BlueLamda
    def get_BlueLamda(self)-> PORISValue :
        return self.prBlueLamda.getSelectedValue()

    def set_BlueLamda(self, value: PORISValue)-> PORISValue :
        return self.prBlueLamda.setValue(value)


    ## BlueLamdaMode 
    def get_BlueLamdaMode(self)-> PORISMode:
        return self.prBlueLamda.getSelectedMode()

    def set_BlueLamdaMode(self, mode: PORISMode)-> PORISMode :
        return self.prBlueLamda.selectMode(mode)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam zzero 

    # zzero
    def get_zzero(self)-> PORISValue :
        return self.przzero.getSelectedValue()

    def set_zzero(self, value: PORISValue)-> PORISValue :
        return self.przzero.setValue(value)


    ## zzeroMode 
    def get_zzeroMode(self)-> PORISMode:
        return self.przzero.getSelectedMode()

    def set_zzeroMode(self, mode: PORISMode)-> PORISMode :
        return self.przzero.selectMode(mode)


    ## prParam PreOptics 

    # zzeroDouble  
    def get_zzeroDouble(self)-> float :
        v = self.przzero.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_zzeroDouble(self, data: float)-> float :
        return self.przzero.getSelectedValue().setData(data)


    ## FiltersMode 
    def get_FiltersMode(self)-> PORISMode:
        return self.sysFilters.getSelectedMode()

    def set_FiltersMode(self, mode: PORISMode)-> PORISMode :
        return self.sysFilters.selectMode(mode)


    ## prParam UFilters 

    # UFilters
    def get_UFilters(self)-> PORISValue :
        return self.prUFilters.getSelectedValue()

    def set_UFilters(self, value: PORISValue)-> PORISValue :
        return self.prUFilters.setValue(value)


    ## UFiltersMode 
    def get_UFiltersMode(self)-> PORISMode:
        return self.prUFilters.getSelectedMode()

    def set_UFiltersMode(self, mode: PORISMode)-> PORISMode :
        return self.prUFilters.selectMode(mode)


    ## prParam OS 

    # OS
    def get_OS(self)-> PORISValue :
        return self.prOS.getSelectedValue()

    def set_OS(self, value: PORISValue)-> PORISValue :
        return self.prOS.setValue(value)


    ## OSMode 
    def get_OSMode(self)-> PORISMode:
        return self.prOS.getSelectedMode()

    def set_OSMode(self, mode: PORISMode)-> PORISMode :
        return self.prOS.selectMode(mode)


    ## prParam Broad 

    # Broad
    def get_Broad(self)-> PORISValue :
        return self.prBroad.getSelectedValue()

    def set_Broad(self, value: PORISValue)-> PORISValue :
        return self.prBroad.setValue(value)


    ## BroadMode 
    def get_BroadMode(self)-> PORISMode:
        return self.prBroad.getSelectedMode()

    def set_BroadMode(self, mode: PORISMode)-> PORISMode :
        return self.prBroad.selectMode(mode)


    ## DetectorMode 
    def get_DetectorMode(self)-> PORISMode:
        return self.sysDetector.getSelectedMode()

    def set_DetectorMode(self, mode: PORISMode)-> PORISMode :
        return self.sysDetector.selectMode(mode)


    ## OutputSourceMode 
    def get_OutputSourceMode(self)-> PORISMode:
        return self.sysOutputSource.getSelectedMode()

    def set_OutputSourceMode(self, mode: PORISMode)-> PORISMode :
        return self.sysOutputSource.selectMode(mode)


    ## RecompositionMode 
    def get_RecompositionMode(self)-> PORISMode:
        return self.sysRecomposition.getSelectedMode()

    def set_RecompositionMode(self, mode: PORISMode)-> PORISMode :
        return self.sysRecomposition.selectMode(mode)


    ## prParam Binning 

    # Binning
    def get_Binning(self)-> PORISValue :
        return self.prBinning.getSelectedValue()

    def set_Binning(self, value: PORISValue)-> PORISValue :
        return self.prBinning.setValue(value)


    ## BinningMode 
    def get_BinningMode(self)-> PORISMode:
        return self.prBinning.getSelectedMode()

    def set_BinningMode(self, mode: PORISMode)-> PORISMode :
        return self.prBinning.selectMode(mode)


    ## WindowMode 
    def get_WindowMode(self)-> PORISMode:
        return self.sysWindow.getSelectedMode()

    def set_WindowMode(self, mode: PORISMode)-> PORISMode :
        return self.sysWindow.selectMode(mode)


    ## prParam Rows 

    # Rows
    def get_Rows(self)-> PORISValue :
        return self.prRows.getSelectedValue()

    def set_Rows(self, value: PORISValue)-> PORISValue :
        return self.prRows.setValue(value)


    ## RowsMode 
    def get_RowsMode(self)-> PORISMode:
        return self.prRows.getSelectedMode()

    def set_RowsMode(self, mode: PORISMode)-> PORISMode :
        return self.prRows.selectMode(mode)


    ## prParam Window 

    # RowsDouble  
    def get_RowsDouble(self)-> float :
        v = self.prRows.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RowsDouble(self, data: float)-> float :
        return self.prRows.getSelectedValue().setData(data)


    ## prParam Cols 

    # Cols
    def get_Cols(self)-> PORISValue :
        return self.prCols.getSelectedValue()

    def set_Cols(self, value: PORISValue)-> PORISValue :
        return self.prCols.setValue(value)


    ## ColsMode 
    def get_ColsMode(self)-> PORISMode:
        return self.prCols.getSelectedMode()

    def set_ColsMode(self, mode: PORISMode)-> PORISMode :
        return self.prCols.selectMode(mode)


    ## prParam Window 

    # ColsDouble  
    def get_ColsDouble(self)-> float :
        v = self.prCols.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ColsDouble(self, data: float)-> float :
        return self.prCols.getSelectedValue().setData(data)


    ## prParam offsetRow 

    # offsetRow
    def get_offsetRow(self)-> PORISValue :
        return self.proffsetRow.getSelectedValue()

    def set_offsetRow(self, value: PORISValue)-> PORISValue :
        return self.proffsetRow.setValue(value)


    ## offsetRowMode 
    def get_offsetRowMode(self)-> PORISMode:
        return self.proffsetRow.getSelectedMode()

    def set_offsetRowMode(self, mode: PORISMode)-> PORISMode :
        return self.proffsetRow.selectMode(mode)


    ## prParam Window 

    # offsetRowDouble  
    def get_offsetRowDouble(self)-> float :
        v = self.proffsetRow.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_offsetRowDouble(self, data: float)-> float :
        return self.proffsetRow.getSelectedValue().setData(data)


    ## prParam offsetCol 

    # offsetCol
    def get_offsetCol(self)-> PORISValue :
        return self.proffsetCol.getSelectedValue()

    def set_offsetCol(self, value: PORISValue)-> PORISValue :
        return self.proffsetCol.setValue(value)


    ## offsetColMode 
    def get_offsetColMode(self)-> PORISMode:
        return self.proffsetCol.getSelectedMode()

    def set_offsetColMode(self, mode: PORISMode)-> PORISMode :
        return self.proffsetCol.selectMode(mode)


    ## prParam Window 

    # offsetColDouble  
    def get_offsetColDouble(self)-> float :
        v = self.proffsetCol.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_offsetColDouble(self, data: float)-> float :
        return self.proffsetCol.getSelectedValue().setData(data)


    ## Action trigger DAS_acquire ##
    def execDAS_acquire(self, value: bool) -> bool:
        # Override this
        return True


    ## Action trigger DAS_abort ##
    def execDAS_abort(self, value: bool) -> bool:
        # Override this
        return True

