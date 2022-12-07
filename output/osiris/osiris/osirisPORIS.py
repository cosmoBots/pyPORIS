from PORIS import *

class osirisPORIS:
    def __init__(self):
        idcounter = 1
        self.sysOsiris = PORISSys("Osiris")
        self.mdOsirisMode_UNKNOWN = PORISMode("OsirisMode_UNKNOWN")
        self.root = self.sysOsiris
        self.sysObservingModes = PORISSys("ObservingModes")
        self.mdObservingModesMode_UNKNOWN = PORISMode("ObservingModesMode_UNKNOWN")
        self.sysAcquisitionModes = PORISSys("AcquisitionModes")
        self.mdAcquisitionModesMode_UNKNOWN = PORISMode("AcquisitionModesMode_UNKNOWN")
        self.sysDAS = PORISSys("DAS")
        self.mdDASMode_UNKNOWN = PORISMode("DASMode_UNKNOWN")
        self.sysAcquisition = PORISSys("Acquisition")
        self.mdAcquisitionMode_UNKNOWN = PORISMode("AcquisitionMode_UNKNOWN")
        self.prShuffleLines = PORISParam("ShuffleLines")
        self.mdShuffleLinesMode_UNKNOWN = PORISMode("ShuffleLinesMode_UNKNOWN")
        self.vlShuffleLines_UNKNOWN = PORISValue("ShuffleLines_UNKNOWN")
        self.prShiftNumber = PORISParam("ShiftNumber")
        self.mdShiftNumberMode_UNKNOWN = PORISMode("ShiftNumberMode_UNKNOWN")
        self.vlShiftNumber_UNKNOWN = PORISValue("ShiftNumber_UNKNOWN")
        self.prExpTime = PORISParam("ExpTime")
        self.mdExpTimeMode_UNKNOWN = PORISMode("ExpTimeMode_UNKNOWN")
        self.vlExpTime_UNKNOWN = PORISValue("ExpTime_UNKNOWN")
        self.sysMultipleExposure = PORISSys("MultipleExposure")
        self.mdMultipleExposureMode_UNKNOWN = PORISMode("MultipleExposureMode_UNKNOWN")
        self.prnumOfFrames = PORISParam("numOfFrames")
        self.mdnumOfFramesMode_UNKNOWN = PORISMode("numOfFramesMode_UNKNOWN")
        self.vlnumOfFrames_UNKNOWN = PORISValue("numOfFrames_UNKNOWN")
        self.prPixelSpeed = PORISParam("PixelSpeed")
        self.mdPixelSpeedMode_UNKNOWN = PORISMode("PixelSpeedMode_UNKNOWN")
        self.vlPixelSpeed_UNKNOWN = PORISValue("PixelSpeed_UNKNOWN")
        self.prCalibGain = PORISParam("CalibGain")
        self.mdCalibGainMode_UNKNOWN = PORISMode("CalibGainMode_UNKNOWN")
        self.vlCalibGain_UNKNOWN = PORISValue("CalibGain_UNKNOWN")
        self.sysOpenShutter = PORISSys("OpenShutter")
        self.mdOpenShutterMode_UNKNOWN = PORISMode("OpenShutterMode_UNKNOWN")
        self.sysProcessMonitor = PORISSys("ProcessMonitor")
        self.mdProcessMonitorMode_UNKNOWN = PORISMode("ProcessMonitorMode_UNKNOWN")
        self.prCurrentEllapsed = PORISParam("CurrentEllapsed")
        self.mdCurrentEllapsedMode_UNKNOWN = PORISMode("CurrentEllapsedMode_UNKNOWN")
        self.vlCurrentEllapsed_UNKNOWN = PORISValue("CurrentEllapsed_UNKNOWN")
        self.prCurrentImg = PORISParam("CurrentImg")
        self.mdCurrentImgMode_UNKNOWN = PORISMode("CurrentImgMode_UNKNOWN")
        self.vlCurrentImg_UNKNOWN = PORISValue("CurrentImg_UNKNOWN")
        self.prCurrentPct = PORISParam("CurrentPct")
        self.mdCurrentPctMode_UNKNOWN = PORISMode("CurrentPctMode_UNKNOWN")
        self.vlCurrentPct_UNKNOWN = PORISValue("CurrentPct_UNKNOWN")
        self.prOverallPct = PORISParam("OverallPct")
        self.mdOverallPctMode_UNKNOWN = PORISMode("OverallPctMode_UNKNOWN")
        self.vlOverallPct_UNKNOWN = PORISValue("OverallPct_UNKNOWN")
        self.sysFPE = PORISSys("FPE")
        self.mdFPEMode_UNKNOWN = PORISMode("FPEMode_UNKNOWN")
        self.prFocalPlaneElement = PORISParam("FocalPlaneElement")
        self.mdFocalPlaneElementMode_UNKNOWN = PORISMode("FocalPlaneElementMode_UNKNOWN")
        self.vlFocalPlaneElement_UNKNOWN = PORISValue("FocalPlaneElement_UNKNOWN")
        self.sysPreOptics = PORISSys("PreOptics")
        self.mdPreOpticsMode_UNKNOWN = PORISMode("PreOpticsMode_UNKNOWN")
        self.prGrisms = PORISParam("Grisms")
        self.mdGrismsMode_UNKNOWN = PORISMode("GrismsMode_UNKNOWN")
        self.vlGrisms_UNKNOWN = PORISValue("Grisms_UNKNOWN")
        self.sysRedTF = PORISSys("RedTF")
        self.mdRedTFMode_UNKNOWN = PORISMode("RedTFMode_UNKNOWN")
        self.prRedFWHM = PORISParam("RedFWHM")
        self.mdRedFWHMMode_UNKNOWN = PORISMode("RedFWHMMode_UNKNOWN")
        self.vlRedFWHM_UNKNOWN = PORISValue("RedFWHM_UNKNOWN")
        self.prRedLamda = PORISParam("RedLamda")
        self.mdRedLamdaMode_UNKNOWN = PORISMode("RedLamdaMode_UNKNOWN")
        self.vlRedLamda_UNKNOWN = PORISValue("RedLamda_UNKNOWN")
        self.sysBlueTF = PORISSys("BlueTF")
        self.mdBlueTFMode_UNKNOWN = PORISMode("BlueTFMode_UNKNOWN")
        self.prBlueFWHM = PORISParam("BlueFWHM")
        self.mdBlueFWHMMode_UNKNOWN = PORISMode("BlueFWHMMode_UNKNOWN")
        self.vlBlueFWHM_UNKNOWN = PORISValue("BlueFWHM_UNKNOWN")
        self.prBlueLamda = PORISParam("BlueLamda")
        self.mdBlueLamdaMode_UNKNOWN = PORISMode("BlueLamdaMode_UNKNOWN")
        self.vlBlueLamda_UNKNOWN = PORISValue("BlueLamda_UNKNOWN")
        self.przzero = PORISParam("zzero")
        self.mdzzeroMode_UNKNOWN = PORISMode("zzeroMode_UNKNOWN")
        self.vlzzero_UNKNOWN = PORISValue("zzero_UNKNOWN")
        self.sysDetector = PORISSys("Detector")
        self.mdDetectorMode_UNKNOWN = PORISMode("DetectorMode_UNKNOWN")
        self.sysOutputSource = PORISSys("OutputSource")
        self.mdOutputSourceMode_UNKNOWN = PORISMode("OutputSourceMode_UNKNOWN")
        self.sysRecomposition = PORISSys("Recomposition")
        self.mdRecompositionMode_UNKNOWN = PORISMode("RecompositionMode_UNKNOWN")
        self.prBinning = PORISParam("Binning")
        self.mdBinningMode_UNKNOWN = PORISMode("BinningMode_UNKNOWN")
        self.vlBinning_UNKNOWN = PORISValue("Binning_UNKNOWN")
        self.sysWindow = PORISSys("Window")
        self.mdWindowMode_UNKNOWN = PORISMode("WindowMode_UNKNOWN")
        self.prRows = PORISParam("Rows")
        self.mdRowsMode_UNKNOWN = PORISMode("RowsMode_UNKNOWN")
        self.vlRows_UNKNOWN = PORISValue("Rows_UNKNOWN")
        self.prCols = PORISParam("Cols")
        self.mdColsMode_UNKNOWN = PORISMode("ColsMode_UNKNOWN")
        self.vlCols_UNKNOWN = PORISValue("Cols_UNKNOWN")
        self.proffsetRow = PORISParam("offsetRow")
        self.mdoffsetRowMode_UNKNOWN = PORISMode("offsetRowMode_UNKNOWN")
        self.vloffsetRow_UNKNOWN = PORISValue("offsetRow_UNKNOWN")
        self.proffsetCol = PORISParam("offsetCol")
        self.mdoffsetColMode_UNKNOWN = PORISMode("offsetColMode_UNKNOWN")
        self.vloffsetCol_UNKNOWN = PORISValue("offsetCol_UNKNOWN")
        self.sysFilters = PORISSys("Filters")
        self.mdFiltersMode_UNKNOWN = PORISMode("FiltersMode_UNKNOWN")
        self.prUFilters = PORISParam("UFilters")
        self.mdUFiltersMode_UNKNOWN = PORISMode("UFiltersMode_UNKNOWN")
        self.vlUFilters_UNKNOWN = PORISValue("UFilters_UNKNOWN")
        self.prOS = PORISParam("OS")
        self.mdOSMode_UNKNOWN = PORISMode("OSMode_UNKNOWN")
        self.vlOS_UNKNOWN = PORISValue("OS_UNKNOWN")
        self.prBroad = PORISParam("Broad")
        self.mdBroadMode_UNKNOWN = PORISMode("BroadMode_UNKNOWN")
        self.vlBroad_UNKNOWN = PORISValue("Broad_UNKNOWN")
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
        self.mdAcquisitionMode_Normal = PORISMode("AcquisitionMode_Normal")
        self.mdAcquisitionMode_FrameTransfer = PORISMode("AcquisitionMode_FrameTransfer")
        self.mdAcquisitionMode_Shuffling = PORISMode("AcquisitionMode_Shuffling")
        self.vlShuffleLines_FullRange = PORISValueFloat("ShuffleLines_FullRange",0,200,1000)
        self.mdShuffleLinesMode_Normal = PORISMode("ShuffleLinesMode_Normal")
        self.vlShiftNumber_FullRange = PORISValueFloat("ShiftNumber_FullRange",0,5,1000)
        self.mdShiftNumberMode_Normal = PORISMode("ShiftNumberMode_Normal")
        self.vlExpTime_FullRange = PORISValueFloat("ExpTime_FullRange",0,1,10000)
        self.mdExpTimeMode_Normal = PORISMode("ExpTimeMode_Normal")
        self.mdExpTimeMode_Bias = PORISMode("ExpTimeMode_Bias")
        self.vlExpTime_0_0 = PORISValue("ExpTime_0_0")
        self.mdExpTimeMode_FT = PORISMode("ExpTimeMode_FT")
        self.vlExpTime_FTRange = PORISValueFloat("ExpTime_FTRange",0,0,360)
        self.mdnumOfFramesMode_Normal = PORISMode("numOfFramesMode_Normal")
        self.vlnumOfFrames_FullRange = PORISValueFloat("numOfFrames_FullRange",0,10,4294967295)
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
        self.vlCalibGain_FullRange = PORISValueFloat("CalibGain_FullRange",0,2,15)
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
        self.vlCurrentEllapsed_Range = PORISValueFloat("CurrentEllapsed_Range",0,0,10000)
        self.mdCurrentEllapsedMode_Normal = PORISMode("CurrentEllapsedMode_Normal")
        self.vlCurrentImg_Range = PORISValueFloat("CurrentImg_Range",0,0,10000)
        self.mdCurrentImgMode_Normal = PORISMode("CurrentImgMode_Normal")
        self.vlCurrentPct_Range = PORISValueFloat("CurrentPct_Range",0,0,100)
        self.mdCurrentPctMode_Normal = PORISMode("CurrentPctMode_Normal")
        self.vlOverallPct_Range = PORISValueFloat("OverallPct_Range",0,0,100)
        self.mdOverallPctMode_Normal = PORISMode("OverallPctMode_Normal")
        self.mdProcessMonitorMode_Normal = PORISMode("ProcessMonitorMode_Normal")
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
        self.vlRedFWHM_Range2_0 = PORISValueFloat("RedFWHM_Range2_0",1.2,1.6,2)
        self.mdRedFWHMMode_l2_0 = PORISMode("RedFWHMMode_l2_0")
        self.mdRedFWHMMode_l1_5 = PORISMode("RedFWHMMode_l1_5")
        self.mdRedFWHMMode_l1_4 = PORISMode("RedFWHMMode_l1_4")
        self.mdRedFWHMMode_l1_3 = PORISMode("RedFWHMMode_l1_3")
        self.mdRedFWHMMode_l1_2 = PORISMode("RedFWHMMode_l1_2")
        self.mdRedFWHMMode_l1_2b = PORISMode("RedFWHMMode_l1_2b")
        self.vlRedFWHM_Range1_5 = PORISValueFloat("RedFWHM_Range1_5",1,1.25,1.5)
        self.vlRedFWHM_Range1_4 = PORISValueFloat("RedFWHM_Range1_4",0.9,1.2,1.4)
        self.vlRedFWHM_Range1_3 = PORISValueFloat("RedFWHM_Range1_3",0.8,1.1,1.3)
        self.vlRedFWHM_Range1_2 = PORISValueFloat("RedFWHM_Range1_2",0.85,1,1.2)
        self.vlRedFWHM_Range1_2b = PORISValueFloat("RedFWHM_Range1_2b",0.9,1,1.2)
        self.mdRedTFMode_l651_799 = PORISMode("RedTFMode_l651_799")
        self.mdRedTFMode_l800_819 = PORISMode("RedTFMode_l800_819")
        self.mdRedTFMode_l820_839 = PORISMode("RedTFMode_l820_839")
        self.mdRedTFMode_l840_879 = PORISMode("RedTFMode_l840_879")
        self.mdRedTFMode_l880_909 = PORISMode("RedTFMode_l880_909")
        self.mdRedTFMode_l910_934 = PORISMode("RedTFMode_l910_934")
        self.vlRedLamda_Range651 = PORISValueFloat("RedLamda_Range651",651,700,799.9)
        self.mdRedLamdaMode_l651_799 = PORISMode("RedLamdaMode_l651_799")
        self.mdRedLamdaMode_l800_819 = PORISMode("RedLamdaMode_l800_819")
        self.mdRedLamdaMode_l820_839 = PORISMode("RedLamdaMode_l820_839")
        self.mdRedLamdaMode_l840_879 = PORISMode("RedLamdaMode_l840_879")
        self.mdRedLamdaMode_l880_909 = PORISMode("RedLamdaMode_l880_909")
        self.mdRedLamdaMode_l910_934 = PORISMode("RedLamdaMode_l910_934")
        self.vlRedLamda_Range800 = PORISValueFloat("RedLamda_Range800",800,810,819.9)
        self.vlRedLamda_Range820 = PORISValueFloat("RedLamda_Range820",820,830,839.9)
        self.vlRedLamda_Range840 = PORISValueFloat("RedLamda_Range840",840,860,879.9)
        self.vlRedLamda_Range880 = PORISValueFloat("RedLamda_Range880",880,895,909.9)
        self.vlRedLamda_Range910 = PORISValueFloat("RedLamda_Range910",910,920,934.5)
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
        self.vlBlueLamda_Range448 = PORISValueFloat("BlueLamda_Range448",448,454,463.9)
        self.mdBlueLamdaMode_l448_463 = PORISMode("BlueLamdaMode_l448_463")
        self.mdBlueLamdaMode_l464_480 = PORISMode("BlueLamdaMode_l464_480")
        self.mdBlueLamdaMode_l481_502 = PORISMode("BlueLamdaMode_l481_502")
        self.mdBlueLamdaMode_l503_521 = PORISMode("BlueLamdaMode_l503_521")
        self.mdBlueLamdaMode_l522_542 = PORISMode("BlueLamdaMode_l522_542")
        self.mdBlueLamdaMode_l543_583 = PORISMode("BlueLamdaMode_l543_583")
        self.vlBlueLamda_Range464 = PORISValueFloat("BlueLamda_Range464",464,472,480.9)
        self.vlBlueLamda_Range481 = PORISValueFloat("BlueLamda_Range481",481,492,502.9)
        self.vlBlueLamda_Range503 = PORISValueFloat("BlueLamda_Range503",503,514,521.9)
        self.vlBlueLamda_Range522 = PORISValueFloat("BlueLamda_Range522",522,536,542.9)
        self.vlBlueLamda_Range543 = PORISValueFloat("BlueLamda_Range543",543,565,583.9)
        self.mdBlueLamdaMode_l584_609 = PORISMode("BlueLamdaMode_l584_609")
        self.mdBlueLamdaMode_l610_637 = PORISMode("BlueLamdaMode_l610_637")
        self.mdBlueLamdaMode_l638_671 = PORISMode("BlueLamdaMode_l638_671")
        self.vlBlueLamda_Range584 = PORISValueFloat("BlueLamda_Range584",584,602,609.9)
        self.vlBlueLamda_Range610 = PORISValueFloat("BlueLamda_Range610",610,622,637.9)
        self.vlBlueLamda_Range638 = PORISValueFloat("BlueLamda_Range638",638,654,671)
        self.mdBlueTFMode_l584_609 = PORISMode("BlueTFMode_l584_609")
        self.mdBlueTFMode_l610_637 = PORISMode("BlueTFMode_l610_637")
        self.mdBlueTFMode_l638_671 = PORISMode("BlueTFMode_l638_671")
        self.mdPreOpticsMode_RTFCalib = PORISMode("PreOpticsMode_RTFCalib")
        self.mdPreOpticsMode_BTFCalib = PORISMode("PreOpticsMode_BTFCalib")
        self.vlzzero_NormalRange = PORISValueFloat("zzero_NormalRange",25000,29000,45000)
        self.mdzzeroMode_Normal = PORISMode("zzeroMode_Normal")
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
        self.vlRows_FullRange = PORISValueFloat("Rows_FullRange",0,2056,4112)
        self.mdColsMode_Normal = PORISMode("ColsMode_Normal")
        self.vlCols_FullRange = PORISValueFloat("Cols_FullRange",0,2048,4096)
        self.mdoffsetRowMode_Normal = PORISMode("offsetRowMode_Normal")
        self.vloffsetRow_FullRange = PORISValueFloat("offsetRow_FullRange",0,1028,4112)
        self.mdoffsetColMode_Normal = PORISMode("offsetColMode_Normal")
        self.vloffsetCol_FullRange = PORISValueFloat("offsetCol_FullRange",0,1024,4096)
        self.mdWindowMode_Disabled = PORISMode("WindowMode_Disabled")
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
        self.mdFiltersMode_Engineering = PORISMode("FiltersMode_Engineering")
        self.mdOsirisMode_Engineering = PORISMode("OsirisMode_Engineering")
        self.mdObservingModesMode_Engineering = PORISMode("ObservingModesMode_Engineering")
        self.mdAcquisitionModesMode_Engineering = PORISMode("AcquisitionModesMode_Engineering")
        self.mdDASMode_Engineering = PORISMode("DASMode_Engineering")
        self.mdAcquisitionMode_Engineering = PORISMode("AcquisitionMode_Engineering")
        self.mdMultipleExposureMode_Engineering = PORISMode("MultipleExposureMode_Engineering")
        self.mdProcessMonitorMode_Engineering = PORISMode("ProcessMonitorMode_Engineering")
        self.mdFPEMode_Engineering = PORISMode("FPEMode_Engineering")
        self.mdPreOpticsMode_Engineering = PORISMode("PreOpticsMode_Engineering")
        self.mdRedTFMode_Engineering = PORISMode("RedTFMode_Engineering")
        self.mdBlueTFMode_Engineering = PORISMode("BlueTFMode_Engineering")
        self.mdDetectorMode_Engineering = PORISMode("DetectorMode_Engineering")
        self.mdOutputSourceMode_Engineering = PORISMode("OutputSourceMode_Engineering")
        self.mdWindowMode_Engineering = PORISMode("WindowMode_Engineering")

        self.sysOsiris.id = idcounter
        idcounter += 1
        self.sysOsiris.ident = "Osiris"
        self.sysOsiris.description = ""

        self.mdOsirisMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdOsirisMode_UNKNOWN.ident = "OsirisMode_UNKNOWN"
        self.mdOsirisMode_UNKNOWN.description = ""
        self.sysOsiris.addMode(self.mdOsirisMode_UNKNOWN)

        self.sysObservingModes.id = idcounter
        idcounter += 1
        self.sysObservingModes.ident = "ObservingModes"
        self.sysObservingModes.description = ""
        self.sysOsiris.addSubsystem(self.sysObservingModes)

        self.mdObservingModesMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_UNKNOWN.ident = "ObservingModesMode_UNKNOWN"
        self.mdObservingModesMode_UNKNOWN.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_UNKNOWN)

        self.sysAcquisitionModes.id = idcounter
        idcounter += 1
        self.sysAcquisitionModes.ident = "AcquisitionModes"
        self.sysAcquisitionModes.description = ""
        self.sysObservingModes.addSubsystem(self.sysAcquisitionModes)

        self.mdAcquisitionModesMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_UNKNOWN.ident = "AcquisitionModesMode_UNKNOWN"
        self.mdAcquisitionModesMode_UNKNOWN.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_UNKNOWN)

        self.sysDAS.id = idcounter
        idcounter += 1
        self.sysDAS.ident = "DAS"
        self.sysDAS.description = ""
        self.sysAcquisitionModes.addSubsystem(self.sysDAS)

        self.mdDASMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdDASMode_UNKNOWN.ident = "DASMode_UNKNOWN"
        self.mdDASMode_UNKNOWN.description = ""
        self.sysDAS.addMode(self.mdDASMode_UNKNOWN)

        self.sysAcquisition.id = idcounter
        idcounter += 1
        self.sysAcquisition.ident = "Acquisition"
        self.sysAcquisition.description = ""
        self.sysDAS.addSubsystem(self.sysAcquisition)

        self.mdAcquisitionMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_UNKNOWN.ident = "AcquisitionMode_UNKNOWN"
        self.mdAcquisitionMode_UNKNOWN.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_UNKNOWN)

        self.prShuffleLines.id = idcounter
        idcounter += 1
        self.prShuffleLines.ident = "ShuffleLines"
        self.prShuffleLines.description = ""
        self.sysAcquisition.addParam(self.prShuffleLines)

        self.vlShuffleLines_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlShuffleLines_UNKNOWN.ident = "ShuffleLines_UNKNOWN"
        self.vlShuffleLines_UNKNOWN.description = "Unknown value for ShuffleLines"
        self.prShuffleLines.addValue(self.vlShuffleLines_UNKNOWN)

        self.mdShuffleLinesMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdShuffleLinesMode_UNKNOWN.ident = "ShuffleLinesMode_UNKNOWN"
        self.mdShuffleLinesMode_UNKNOWN.description = "Unknown mode for ShuffleLines"
        self.prShuffleLines.addMode(self.mdShuffleLinesMode_UNKNOWN)
        self.mdShuffleLinesMode_UNKNOWN.addValue(self.vlShuffleLines_UNKNOWN)
        self.mdAcquisitionMode_UNKNOWN.addSubMode(self.mdShuffleLinesMode_UNKNOWN)

        self.prShiftNumber.id = idcounter
        idcounter += 1
        self.prShiftNumber.ident = "ShiftNumber"
        self.prShiftNumber.description = ""
        self.sysAcquisition.addParam(self.prShiftNumber)

        self.vlShiftNumber_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlShiftNumber_UNKNOWN.ident = "ShiftNumber_UNKNOWN"
        self.vlShiftNumber_UNKNOWN.description = "Unknown value for ShiftNumber"
        self.prShiftNumber.addValue(self.vlShiftNumber_UNKNOWN)

        self.mdShiftNumberMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdShiftNumberMode_UNKNOWN.ident = "ShiftNumberMode_UNKNOWN"
        self.mdShiftNumberMode_UNKNOWN.description = "Unknown mode for ShiftNumber"
        self.prShiftNumber.addMode(self.mdShiftNumberMode_UNKNOWN)
        self.mdShiftNumberMode_UNKNOWN.addValue(self.vlShiftNumber_UNKNOWN)
        self.mdAcquisitionMode_UNKNOWN.addSubMode(self.mdShiftNumberMode_UNKNOWN)

        self.prExpTime.id = idcounter
        idcounter += 1
        self.prExpTime.ident = "ExpTime"
        self.prExpTime.description = ""
        self.sysAcquisition.addParam(self.prExpTime)

        self.vlExpTime_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlExpTime_UNKNOWN.ident = "ExpTime_UNKNOWN"
        self.vlExpTime_UNKNOWN.description = "Unknown value for ExpTime"
        self.prExpTime.addValue(self.vlExpTime_UNKNOWN)

        self.mdExpTimeMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdExpTimeMode_UNKNOWN.ident = "ExpTimeMode_UNKNOWN"
        self.mdExpTimeMode_UNKNOWN.description = "Unknown mode for ExpTime"
        self.prExpTime.addMode(self.mdExpTimeMode_UNKNOWN)
        self.mdExpTimeMode_UNKNOWN.addValue(self.vlExpTime_UNKNOWN)
        self.mdAcquisitionMode_UNKNOWN.addSubMode(self.mdExpTimeMode_UNKNOWN)

        self.sysMultipleExposure.id = idcounter
        idcounter += 1
        self.sysMultipleExposure.ident = "MultipleExposure"
        self.sysMultipleExposure.description = ""
        self.sysAcquisition.addSubsystem(self.sysMultipleExposure)

        self.mdMultipleExposureMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdMultipleExposureMode_UNKNOWN.ident = "MultipleExposureMode_UNKNOWN"
        self.mdMultipleExposureMode_UNKNOWN.description = ""
        self.sysMultipleExposure.addMode(self.mdMultipleExposureMode_UNKNOWN)

        self.prnumOfFrames.id = idcounter
        idcounter += 1
        self.prnumOfFrames.ident = "numOfFrames"
        self.prnumOfFrames.description = ""
        self.sysMultipleExposure.addParam(self.prnumOfFrames)

        self.vlnumOfFrames_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlnumOfFrames_UNKNOWN.ident = "numOfFrames_UNKNOWN"
        self.vlnumOfFrames_UNKNOWN.description = "Unknown value for numOfFrames"
        self.prnumOfFrames.addValue(self.vlnumOfFrames_UNKNOWN)

        self.mdnumOfFramesMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdnumOfFramesMode_UNKNOWN.ident = "numOfFramesMode_UNKNOWN"
        self.mdnumOfFramesMode_UNKNOWN.description = "Unknown mode for numOfFrames"
        self.prnumOfFrames.addMode(self.mdnumOfFramesMode_UNKNOWN)
        self.mdnumOfFramesMode_UNKNOWN.addValue(self.vlnumOfFrames_UNKNOWN)
        self.mdMultipleExposureMode_UNKNOWN.addSubMode(self.mdnumOfFramesMode_UNKNOWN)

        self.prPixelSpeed.id = idcounter
        idcounter += 1
        self.prPixelSpeed.ident = "PixelSpeed"
        self.prPixelSpeed.description = ""
        self.sysAcquisition.addParam(self.prPixelSpeed)

        self.vlPixelSpeed_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlPixelSpeed_UNKNOWN.ident = "PixelSpeed_UNKNOWN"
        self.vlPixelSpeed_UNKNOWN.description = "Unknown value for PixelSpeed"
        self.prPixelSpeed.addValue(self.vlPixelSpeed_UNKNOWN)

        self.mdPixelSpeedMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdPixelSpeedMode_UNKNOWN.ident = "PixelSpeedMode_UNKNOWN"
        self.mdPixelSpeedMode_UNKNOWN.description = "Unknown mode for PixelSpeed"
        self.prPixelSpeed.addMode(self.mdPixelSpeedMode_UNKNOWN)
        self.mdPixelSpeedMode_UNKNOWN.addValue(self.vlPixelSpeed_UNKNOWN)
        self.mdAcquisitionMode_UNKNOWN.addSubMode(self.mdPixelSpeedMode_UNKNOWN)

        self.prCalibGain.id = idcounter
        idcounter += 1
        self.prCalibGain.ident = "CalibGain"
        self.prCalibGain.description = ""
        self.sysAcquisition.addParam(self.prCalibGain)

        self.vlCalibGain_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlCalibGain_UNKNOWN.ident = "CalibGain_UNKNOWN"
        self.vlCalibGain_UNKNOWN.description = "Unknown value for CalibGain"
        self.prCalibGain.addValue(self.vlCalibGain_UNKNOWN)

        self.mdCalibGainMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdCalibGainMode_UNKNOWN.ident = "CalibGainMode_UNKNOWN"
        self.mdCalibGainMode_UNKNOWN.description = "Unknown mode for CalibGain"
        self.prCalibGain.addMode(self.mdCalibGainMode_UNKNOWN)
        self.mdCalibGainMode_UNKNOWN.addValue(self.vlCalibGain_UNKNOWN)
        self.mdAcquisitionMode_UNKNOWN.addSubMode(self.mdCalibGainMode_UNKNOWN)

        self.sysOpenShutter.id = idcounter
        idcounter += 1
        self.sysOpenShutter.ident = "OpenShutter"
        self.sysOpenShutter.description = ""
        self.sysDAS.addSubsystem(self.sysOpenShutter)

        self.mdOpenShutterMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdOpenShutterMode_UNKNOWN.ident = "OpenShutterMode_UNKNOWN"
        self.mdOpenShutterMode_UNKNOWN.description = ""
        self.sysOpenShutter.addMode(self.mdOpenShutterMode_UNKNOWN)

        self.sysProcessMonitor.id = idcounter
        idcounter += 1
        self.sysProcessMonitor.ident = "ProcessMonitor"
        self.sysProcessMonitor.description = ""
        self.sysDAS.addSubsystem(self.sysProcessMonitor)

        self.mdProcessMonitorMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdProcessMonitorMode_UNKNOWN.ident = "ProcessMonitorMode_UNKNOWN"
        self.mdProcessMonitorMode_UNKNOWN.description = ""
        self.sysProcessMonitor.addMode(self.mdProcessMonitorMode_UNKNOWN)

        self.prCurrentEllapsed.id = idcounter
        idcounter += 1
        self.prCurrentEllapsed.ident = "CurrentEllapsed"
        self.prCurrentEllapsed.description = ""
        self.sysProcessMonitor.addParam(self.prCurrentEllapsed)

        self.vlCurrentEllapsed_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlCurrentEllapsed_UNKNOWN.ident = "CurrentEllapsed_UNKNOWN"
        self.vlCurrentEllapsed_UNKNOWN.description = "Unknown value for CurrentEllapsed"
        self.prCurrentEllapsed.addValue(self.vlCurrentEllapsed_UNKNOWN)

        self.mdCurrentEllapsedMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdCurrentEllapsedMode_UNKNOWN.ident = "CurrentEllapsedMode_UNKNOWN"
        self.mdCurrentEllapsedMode_UNKNOWN.description = "Unknown mode for CurrentEllapsed"
        self.prCurrentEllapsed.addMode(self.mdCurrentEllapsedMode_UNKNOWN)
        self.mdCurrentEllapsedMode_UNKNOWN.addValue(self.vlCurrentEllapsed_UNKNOWN)
        self.mdProcessMonitorMode_UNKNOWN.addSubMode(self.mdCurrentEllapsedMode_UNKNOWN)

        self.prCurrentImg.id = idcounter
        idcounter += 1
        self.prCurrentImg.ident = "CurrentImg"
        self.prCurrentImg.description = ""
        self.sysProcessMonitor.addParam(self.prCurrentImg)

        self.vlCurrentImg_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlCurrentImg_UNKNOWN.ident = "CurrentImg_UNKNOWN"
        self.vlCurrentImg_UNKNOWN.description = "Unknown value for CurrentImg"
        self.prCurrentImg.addValue(self.vlCurrentImg_UNKNOWN)

        self.mdCurrentImgMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdCurrentImgMode_UNKNOWN.ident = "CurrentImgMode_UNKNOWN"
        self.mdCurrentImgMode_UNKNOWN.description = "Unknown mode for CurrentImg"
        self.prCurrentImg.addMode(self.mdCurrentImgMode_UNKNOWN)
        self.mdCurrentImgMode_UNKNOWN.addValue(self.vlCurrentImg_UNKNOWN)
        self.mdProcessMonitorMode_UNKNOWN.addSubMode(self.mdCurrentImgMode_UNKNOWN)

        self.prCurrentPct.id = idcounter
        idcounter += 1
        self.prCurrentPct.ident = "CurrentPct"
        self.prCurrentPct.description = ""
        self.sysProcessMonitor.addParam(self.prCurrentPct)

        self.vlCurrentPct_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlCurrentPct_UNKNOWN.ident = "CurrentPct_UNKNOWN"
        self.vlCurrentPct_UNKNOWN.description = "Unknown value for CurrentPct"
        self.prCurrentPct.addValue(self.vlCurrentPct_UNKNOWN)

        self.mdCurrentPctMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdCurrentPctMode_UNKNOWN.ident = "CurrentPctMode_UNKNOWN"
        self.mdCurrentPctMode_UNKNOWN.description = "Unknown mode for CurrentPct"
        self.prCurrentPct.addMode(self.mdCurrentPctMode_UNKNOWN)
        self.mdCurrentPctMode_UNKNOWN.addValue(self.vlCurrentPct_UNKNOWN)
        self.mdProcessMonitorMode_UNKNOWN.addSubMode(self.mdCurrentPctMode_UNKNOWN)

        self.prOverallPct.id = idcounter
        idcounter += 1
        self.prOverallPct.ident = "OverallPct"
        self.prOverallPct.description = ""
        self.sysProcessMonitor.addParam(self.prOverallPct)

        self.vlOverallPct_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlOverallPct_UNKNOWN.ident = "OverallPct_UNKNOWN"
        self.vlOverallPct_UNKNOWN.description = "Unknown value for OverallPct"
        self.prOverallPct.addValue(self.vlOverallPct_UNKNOWN)

        self.mdOverallPctMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdOverallPctMode_UNKNOWN.ident = "OverallPctMode_UNKNOWN"
        self.mdOverallPctMode_UNKNOWN.description = "Unknown mode for OverallPct"
        self.prOverallPct.addMode(self.mdOverallPctMode_UNKNOWN)
        self.mdOverallPctMode_UNKNOWN.addValue(self.vlOverallPct_UNKNOWN)
        self.mdProcessMonitorMode_UNKNOWN.addSubMode(self.mdOverallPctMode_UNKNOWN)

        self.sysFPE.id = idcounter
        idcounter += 1
        self.sysFPE.ident = "FPE"
        self.sysFPE.description = ""
        self.sysAcquisitionModes.addSubsystem(self.sysFPE)

        self.mdFPEMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdFPEMode_UNKNOWN.ident = "FPEMode_UNKNOWN"
        self.mdFPEMode_UNKNOWN.description = ""
        self.sysFPE.addMode(self.mdFPEMode_UNKNOWN)

        self.prFocalPlaneElement.id = idcounter
        idcounter += 1
        self.prFocalPlaneElement.ident = "FocalPlaneElement"
        self.prFocalPlaneElement.description = ""
        self.sysFPE.addParam(self.prFocalPlaneElement)

        self.vlFocalPlaneElement_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_UNKNOWN.ident = "FocalPlaneElement_UNKNOWN"
        self.vlFocalPlaneElement_UNKNOWN.description = "Unknown value for FocalPlaneElement"
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_UNKNOWN)

        self.mdFocalPlaneElementMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdFocalPlaneElementMode_UNKNOWN.ident = "FocalPlaneElementMode_UNKNOWN"
        self.mdFocalPlaneElementMode_UNKNOWN.description = "Unknown mode for FocalPlaneElement"
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_UNKNOWN)
        self.mdFocalPlaneElementMode_UNKNOWN.addValue(self.vlFocalPlaneElement_UNKNOWN)
        self.mdFPEMode_UNKNOWN.addSubMode(self.mdFocalPlaneElementMode_UNKNOWN)

        self.sysPreOptics.id = idcounter
        idcounter += 1
        self.sysPreOptics.ident = "PreOptics"
        self.sysPreOptics.description = ""
        self.sysAcquisitionModes.addSubsystem(self.sysPreOptics)

        self.mdPreOpticsMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdPreOpticsMode_UNKNOWN.ident = "PreOpticsMode_UNKNOWN"
        self.mdPreOpticsMode_UNKNOWN.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_UNKNOWN)

        self.prGrisms.id = idcounter
        idcounter += 1
        self.prGrisms.ident = "Grisms"
        self.prGrisms.description = ""
        self.sysPreOptics.addParam(self.prGrisms)

        self.vlGrisms_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlGrisms_UNKNOWN.ident = "Grisms_UNKNOWN"
        self.vlGrisms_UNKNOWN.description = "Unknown value for Grisms"
        self.prGrisms.addValue(self.vlGrisms_UNKNOWN)

        self.mdGrismsMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdGrismsMode_UNKNOWN.ident = "GrismsMode_UNKNOWN"
        self.mdGrismsMode_UNKNOWN.description = "Unknown mode for Grisms"
        self.prGrisms.addMode(self.mdGrismsMode_UNKNOWN)
        self.mdGrismsMode_UNKNOWN.addValue(self.vlGrisms_UNKNOWN)
        self.mdPreOpticsMode_UNKNOWN.addSubMode(self.mdGrismsMode_UNKNOWN)

        self.sysRedTF.id = idcounter
        idcounter += 1
        self.sysRedTF.ident = "RedTF"
        self.sysRedTF.description = ""
        self.sysPreOptics.addSubsystem(self.sysRedTF)

        self.mdRedTFMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdRedTFMode_UNKNOWN.ident = "RedTFMode_UNKNOWN"
        self.mdRedTFMode_UNKNOWN.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_UNKNOWN)

        self.prRedFWHM.id = idcounter
        idcounter += 1
        self.prRedFWHM.ident = "RedFWHM"
        self.prRedFWHM.description = ""
        self.sysRedTF.addParam(self.prRedFWHM)

        self.vlRedFWHM_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlRedFWHM_UNKNOWN.ident = "RedFWHM_UNKNOWN"
        self.vlRedFWHM_UNKNOWN.description = "Unknown value for RedFWHM"
        self.prRedFWHM.addValue(self.vlRedFWHM_UNKNOWN)

        self.mdRedFWHMMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdRedFWHMMode_UNKNOWN.ident = "RedFWHMMode_UNKNOWN"
        self.mdRedFWHMMode_UNKNOWN.description = "Unknown mode for RedFWHM"
        self.prRedFWHM.addMode(self.mdRedFWHMMode_UNKNOWN)
        self.mdRedFWHMMode_UNKNOWN.addValue(self.vlRedFWHM_UNKNOWN)
        self.mdRedTFMode_UNKNOWN.addSubMode(self.mdRedFWHMMode_UNKNOWN)

        self.prRedLamda.id = idcounter
        idcounter += 1
        self.prRedLamda.ident = "RedLamda"
        self.prRedLamda.description = ""
        self.sysRedTF.addParam(self.prRedLamda)

        self.vlRedLamda_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlRedLamda_UNKNOWN.ident = "RedLamda_UNKNOWN"
        self.vlRedLamda_UNKNOWN.description = "Unknown value for RedLamda"
        self.prRedLamda.addValue(self.vlRedLamda_UNKNOWN)

        self.mdRedLamdaMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdRedLamdaMode_UNKNOWN.ident = "RedLamdaMode_UNKNOWN"
        self.mdRedLamdaMode_UNKNOWN.description = "Unknown mode for RedLamda"
        self.prRedLamda.addMode(self.mdRedLamdaMode_UNKNOWN)
        self.mdRedLamdaMode_UNKNOWN.addValue(self.vlRedLamda_UNKNOWN)
        self.mdRedTFMode_UNKNOWN.addSubMode(self.mdRedLamdaMode_UNKNOWN)

        self.sysBlueTF.id = idcounter
        idcounter += 1
        self.sysBlueTF.ident = "BlueTF"
        self.sysBlueTF.description = ""
        self.sysPreOptics.addSubsystem(self.sysBlueTF)

        self.mdBlueTFMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdBlueTFMode_UNKNOWN.ident = "BlueTFMode_UNKNOWN"
        self.mdBlueTFMode_UNKNOWN.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_UNKNOWN)

        self.prBlueFWHM.id = idcounter
        idcounter += 1
        self.prBlueFWHM.ident = "BlueFWHM"
        self.prBlueFWHM.description = ""
        self.sysBlueTF.addParam(self.prBlueFWHM)

        self.vlBlueFWHM_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlBlueFWHM_UNKNOWN.ident = "BlueFWHM_UNKNOWN"
        self.vlBlueFWHM_UNKNOWN.description = "Unknown value for BlueFWHM"
        self.prBlueFWHM.addValue(self.vlBlueFWHM_UNKNOWN)

        self.mdBlueFWHMMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdBlueFWHMMode_UNKNOWN.ident = "BlueFWHMMode_UNKNOWN"
        self.mdBlueFWHMMode_UNKNOWN.description = "Unknown mode for BlueFWHM"
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_UNKNOWN)
        self.mdBlueFWHMMode_UNKNOWN.addValue(self.vlBlueFWHM_UNKNOWN)
        self.mdBlueTFMode_UNKNOWN.addSubMode(self.mdBlueFWHMMode_UNKNOWN)

        self.prBlueLamda.id = idcounter
        idcounter += 1
        self.prBlueLamda.ident = "BlueLamda"
        self.prBlueLamda.description = ""
        self.sysBlueTF.addParam(self.prBlueLamda)

        self.vlBlueLamda_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlBlueLamda_UNKNOWN.ident = "BlueLamda_UNKNOWN"
        self.vlBlueLamda_UNKNOWN.description = "Unknown value for BlueLamda"
        self.prBlueLamda.addValue(self.vlBlueLamda_UNKNOWN)

        self.mdBlueLamdaMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdBlueLamdaMode_UNKNOWN.ident = "BlueLamdaMode_UNKNOWN"
        self.mdBlueLamdaMode_UNKNOWN.description = "Unknown mode for BlueLamda"
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_UNKNOWN)
        self.mdBlueLamdaMode_UNKNOWN.addValue(self.vlBlueLamda_UNKNOWN)
        self.mdBlueTFMode_UNKNOWN.addSubMode(self.mdBlueLamdaMode_UNKNOWN)

        self.przzero.id = idcounter
        idcounter += 1
        self.przzero.ident = "zzero"
        self.przzero.description = ""
        self.sysPreOptics.addParam(self.przzero)

        self.vlzzero_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlzzero_UNKNOWN.ident = "zzero_UNKNOWN"
        self.vlzzero_UNKNOWN.description = "Unknown value for zzero"
        self.przzero.addValue(self.vlzzero_UNKNOWN)

        self.mdzzeroMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdzzeroMode_UNKNOWN.ident = "zzeroMode_UNKNOWN"
        self.mdzzeroMode_UNKNOWN.description = "Unknown mode for zzero"
        self.przzero.addMode(self.mdzzeroMode_UNKNOWN)
        self.mdzzeroMode_UNKNOWN.addValue(self.vlzzero_UNKNOWN)
        self.mdPreOpticsMode_UNKNOWN.addSubMode(self.mdzzeroMode_UNKNOWN)

        self.sysDetector.id = idcounter
        idcounter += 1
        self.sysDetector.ident = "Detector"
        self.sysDetector.description = ""
        self.sysAcquisition.addSubsystem(self.sysDetector)

        self.mdDetectorMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdDetectorMode_UNKNOWN.ident = "DetectorMode_UNKNOWN"
        self.mdDetectorMode_UNKNOWN.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_UNKNOWN)

        self.sysOutputSource.id = idcounter
        idcounter += 1
        self.sysOutputSource.ident = "OutputSource"
        self.sysOutputSource.description = ""
        self.sysDetector.addSubsystem(self.sysOutputSource)

        self.mdOutputSourceMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_UNKNOWN.ident = "OutputSourceMode_UNKNOWN"
        self.mdOutputSourceMode_UNKNOWN.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_UNKNOWN)

        self.sysRecomposition.id = idcounter
        idcounter += 1
        self.sysRecomposition.ident = "Recomposition"
        self.sysRecomposition.description = ""
        self.sysOutputSource.addSubsystem(self.sysRecomposition)

        self.mdRecompositionMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdRecompositionMode_UNKNOWN.ident = "RecompositionMode_UNKNOWN"
        self.mdRecompositionMode_UNKNOWN.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_UNKNOWN)

        self.prBinning.id = idcounter
        idcounter += 1
        self.prBinning.ident = "Binning"
        self.prBinning.description = ""
        self.sysDetector.addParam(self.prBinning)

        self.vlBinning_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlBinning_UNKNOWN.ident = "Binning_UNKNOWN"
        self.vlBinning_UNKNOWN.description = "Unknown value for Binning"
        self.prBinning.addValue(self.vlBinning_UNKNOWN)

        self.mdBinningMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdBinningMode_UNKNOWN.ident = "BinningMode_UNKNOWN"
        self.mdBinningMode_UNKNOWN.description = "Unknown mode for Binning"
        self.prBinning.addMode(self.mdBinningMode_UNKNOWN)
        self.mdBinningMode_UNKNOWN.addValue(self.vlBinning_UNKNOWN)
        self.mdDetectorMode_UNKNOWN.addSubMode(self.mdBinningMode_UNKNOWN)

        self.sysWindow.id = idcounter
        idcounter += 1
        self.sysWindow.ident = "Window"
        self.sysWindow.description = ""
        self.sysDetector.addSubsystem(self.sysWindow)

        self.mdWindowMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdWindowMode_UNKNOWN.ident = "WindowMode_UNKNOWN"
        self.mdWindowMode_UNKNOWN.description = ""
        self.sysWindow.addMode(self.mdWindowMode_UNKNOWN)

        self.prRows.id = idcounter
        idcounter += 1
        self.prRows.ident = "Rows"
        self.prRows.description = ""
        self.sysWindow.addParam(self.prRows)

        self.vlRows_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlRows_UNKNOWN.ident = "Rows_UNKNOWN"
        self.vlRows_UNKNOWN.description = "Unknown value for Rows"
        self.prRows.addValue(self.vlRows_UNKNOWN)

        self.mdRowsMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdRowsMode_UNKNOWN.ident = "RowsMode_UNKNOWN"
        self.mdRowsMode_UNKNOWN.description = "Unknown mode for Rows"
        self.prRows.addMode(self.mdRowsMode_UNKNOWN)
        self.mdRowsMode_UNKNOWN.addValue(self.vlRows_UNKNOWN)
        self.mdWindowMode_UNKNOWN.addSubMode(self.mdRowsMode_UNKNOWN)

        self.prCols.id = idcounter
        idcounter += 1
        self.prCols.ident = "Cols"
        self.prCols.description = ""
        self.sysWindow.addParam(self.prCols)

        self.vlCols_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlCols_UNKNOWN.ident = "Cols_UNKNOWN"
        self.vlCols_UNKNOWN.description = "Unknown value for Cols"
        self.prCols.addValue(self.vlCols_UNKNOWN)

        self.mdColsMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdColsMode_UNKNOWN.ident = "ColsMode_UNKNOWN"
        self.mdColsMode_UNKNOWN.description = "Unknown mode for Cols"
        self.prCols.addMode(self.mdColsMode_UNKNOWN)
        self.mdColsMode_UNKNOWN.addValue(self.vlCols_UNKNOWN)
        self.mdWindowMode_UNKNOWN.addSubMode(self.mdColsMode_UNKNOWN)

        self.proffsetRow.id = idcounter
        idcounter += 1
        self.proffsetRow.ident = "offsetRow"
        self.proffsetRow.description = ""
        self.sysWindow.addParam(self.proffsetRow)

        self.vloffsetRow_UNKNOWN.id = idcounter
        idcounter += 1
        self.vloffsetRow_UNKNOWN.ident = "offsetRow_UNKNOWN"
        self.vloffsetRow_UNKNOWN.description = "Unknown value for offsetRow"
        self.proffsetRow.addValue(self.vloffsetRow_UNKNOWN)

        self.mdoffsetRowMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdoffsetRowMode_UNKNOWN.ident = "offsetRowMode_UNKNOWN"
        self.mdoffsetRowMode_UNKNOWN.description = "Unknown mode for offsetRow"
        self.proffsetRow.addMode(self.mdoffsetRowMode_UNKNOWN)
        self.mdoffsetRowMode_UNKNOWN.addValue(self.vloffsetRow_UNKNOWN)
        self.mdWindowMode_UNKNOWN.addSubMode(self.mdoffsetRowMode_UNKNOWN)

        self.proffsetCol.id = idcounter
        idcounter += 1
        self.proffsetCol.ident = "offsetCol"
        self.proffsetCol.description = ""
        self.sysWindow.addParam(self.proffsetCol)

        self.vloffsetCol_UNKNOWN.id = idcounter
        idcounter += 1
        self.vloffsetCol_UNKNOWN.ident = "offsetCol_UNKNOWN"
        self.vloffsetCol_UNKNOWN.description = "Unknown value for offsetCol"
        self.proffsetCol.addValue(self.vloffsetCol_UNKNOWN)

        self.mdoffsetColMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdoffsetColMode_UNKNOWN.ident = "offsetColMode_UNKNOWN"
        self.mdoffsetColMode_UNKNOWN.description = "Unknown mode for offsetCol"
        self.proffsetCol.addMode(self.mdoffsetColMode_UNKNOWN)
        self.mdoffsetColMode_UNKNOWN.addValue(self.vloffsetCol_UNKNOWN)
        self.mdWindowMode_UNKNOWN.addSubMode(self.mdoffsetColMode_UNKNOWN)

        self.sysFilters.id = idcounter
        idcounter += 1
        self.sysFilters.ident = "Filters"
        self.sysFilters.description = ""
        self.sysPreOptics.addSubsystem(self.sysFilters)

        self.mdFiltersMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdFiltersMode_UNKNOWN.ident = "FiltersMode_UNKNOWN"
        self.mdFiltersMode_UNKNOWN.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_UNKNOWN)

        self.prUFilters.id = idcounter
        idcounter += 1
        self.prUFilters.ident = "UFilters"
        self.prUFilters.description = ""
        self.sysFilters.addParam(self.prUFilters)

        self.vlUFilters_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlUFilters_UNKNOWN.ident = "UFilters_UNKNOWN"
        self.vlUFilters_UNKNOWN.description = "Unknown value for UFilters"
        self.prUFilters.addValue(self.vlUFilters_UNKNOWN)

        self.mdUFiltersMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdUFiltersMode_UNKNOWN.ident = "UFiltersMode_UNKNOWN"
        self.mdUFiltersMode_UNKNOWN.description = "Unknown mode for UFilters"
        self.prUFilters.addMode(self.mdUFiltersMode_UNKNOWN)
        self.mdUFiltersMode_UNKNOWN.addValue(self.vlUFilters_UNKNOWN)
        self.mdFiltersMode_UNKNOWN.addSubMode(self.mdUFiltersMode_UNKNOWN)

        self.prOS.id = idcounter
        idcounter += 1
        self.prOS.ident = "OS"
        self.prOS.description = ""
        self.sysFilters.addParam(self.prOS)

        self.vlOS_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlOS_UNKNOWN.ident = "OS_UNKNOWN"
        self.vlOS_UNKNOWN.description = "Unknown value for OS"
        self.prOS.addValue(self.vlOS_UNKNOWN)

        self.mdOSMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdOSMode_UNKNOWN.ident = "OSMode_UNKNOWN"
        self.mdOSMode_UNKNOWN.description = "Unknown mode for OS"
        self.prOS.addMode(self.mdOSMode_UNKNOWN)
        self.mdOSMode_UNKNOWN.addValue(self.vlOS_UNKNOWN)
        self.mdFiltersMode_UNKNOWN.addSubMode(self.mdOSMode_UNKNOWN)

        self.prBroad.id = idcounter
        idcounter += 1
        self.prBroad.ident = "Broad"
        self.prBroad.description = ""
        self.sysFilters.addParam(self.prBroad)

        self.vlBroad_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlBroad_UNKNOWN.ident = "Broad_UNKNOWN"
        self.vlBroad_UNKNOWN.description = "Unknown value for Broad"
        self.prBroad.addValue(self.vlBroad_UNKNOWN)

        self.mdBroadMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdBroadMode_UNKNOWN.ident = "BroadMode_UNKNOWN"
        self.mdBroadMode_UNKNOWN.description = "Unknown mode for Broad"
        self.prBroad.addMode(self.mdBroadMode_UNKNOWN)
        self.mdBroadMode_UNKNOWN.addValue(self.vlBroad_UNKNOWN)
        self.mdFiltersMode_UNKNOWN.addSubMode(self.mdBroadMode_UNKNOWN)

        self.mdOsirisMode_Imaging.id = idcounter
        idcounter += 1
        self.mdOsirisMode_Imaging.ident = "OsirisMode_Imaging"
        self.mdOsirisMode_Imaging.description = ""
        self.sysOsiris.addMode(self.mdOsirisMode_Imaging)

        self.mdOsirisMode_Spectroscopy.id = idcounter
        idcounter += 1
        self.mdOsirisMode_Spectroscopy.ident = "OsirisMode_Spectroscopy"
        self.mdOsirisMode_Spectroscopy.description = ""
        self.sysOsiris.addMode(self.mdOsirisMode_Spectroscopy)

        self.mdOsirisMode_Calibration.id = idcounter
        idcounter += 1
        self.mdOsirisMode_Calibration.ident = "OsirisMode_Calibration"
        self.mdOsirisMode_Calibration.description = ""
        self.sysOsiris.addMode(self.mdOsirisMode_Calibration)

        self.mdAcquisitionModesMode_aBBI.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aBBI.ident = "AcquisitionModesMode_aBBI"
        self.mdAcquisitionModesMode_aBBI.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aBBI)

        self.mdAcquisitionModesMode_aTFI.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aTFI.ident = "AcquisitionModesMode_aTFI"
        self.mdAcquisitionModesMode_aTFI.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aTFI)

        self.mdAcquisitionModesMode_aLSSpec.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aLSSpec.ident = "AcquisitionModesMode_aLSSpec"
        self.mdAcquisitionModesMode_aLSSpec.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aLSSpec)

        self.mdAcquisitionModesMode_aMOS.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aMOS.ident = "AcquisitionModesMode_aMOS"
        self.mdAcquisitionModesMode_aMOS.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aMOS)

        self.mdAcquisitionModesMode_aFastBBI.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aFastBBI.ident = "AcquisitionModesMode_aFastBBI"
        self.mdAcquisitionModesMode_aFastBBI.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aFastBBI)

        self.mdAcquisitionModesMode_aFrTrBBI.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aFrTrBBI.ident = "AcquisitionModesMode_aFrTrBBI"
        self.mdAcquisitionModesMode_aFrTrBBI.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aFrTrBBI)

        self.mdAcquisitionModesMode_aFastLSSpec.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aFastLSSpec.ident = "AcquisitionModesMode_aFastLSSpec"
        self.mdAcquisitionModesMode_aFastLSSpec.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aFastLSSpec)

        self.mdAcquisitionModesMode_aFastTFImage.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aFastTFImage.ident = "AcquisitionModesMode_aFastTFImage"
        self.mdAcquisitionModesMode_aFastTFImage.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aFastTFImage)

        self.mdAcquisitionModesMode_aFrTrTFI.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aFrTrTFI.ident = "AcquisitionModesMode_aFrTrTFI"
        self.mdAcquisitionModesMode_aFrTrTFI.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aFrTrTFI)

        self.mdAcquisitionModesMode_aBias.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aBias.ident = "AcquisitionModesMode_aBias"
        self.mdAcquisitionModesMode_aBias.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aBias)

        self.mdAcquisitionModesMode_aDark.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aDark.ident = "AcquisitionModesMode_aDark"
        self.mdAcquisitionModesMode_aDark.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aDark)

        self.mdAcquisitionModesMode_aDomeFlat.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aDomeFlat.ident = "AcquisitionModesMode_aDomeFlat"
        self.mdAcquisitionModesMode_aDomeFlat.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aDomeFlat)

        self.mdAcquisitionModesMode_aSkyFlat.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aSkyFlat.ident = "AcquisitionModesMode_aSkyFlat"
        self.mdAcquisitionModesMode_aSkyFlat.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aSkyFlat)

        self.mdAcquisitionModesMode_aSpectralFlat.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aSpectralFlat.ident = "AcquisitionModesMode_aSpectralFlat"
        self.mdAcquisitionModesMode_aSpectralFlat.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aSpectralFlat)

        self.mdAcquisitionModesMode_aCalibLamp.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aCalibLamp.ident = "AcquisitionModesMode_aCalibLamp"
        self.mdAcquisitionModesMode_aCalibLamp.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aCalibLamp)

        self.mdAcquisitionModesMode_aTFCalib.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_aTFCalib.ident = "AcquisitionModesMode_aTFCalib"
        self.mdAcquisitionModesMode_aTFCalib.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aTFCalib)

        self.mdAcquisitionModesMode_Throughslit.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_Throughslit.ident = "AcquisitionModesMode_Throughslit"
        self.mdAcquisitionModesMode_Throughslit.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_Throughslit)

        self.mdObservingModesMode_BBI.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_BBI.ident = "ObservingModesMode_BBI"
        self.mdObservingModesMode_BBI.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_BBI)

        self.mdObservingModesMode_TFI.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_TFI.ident = "ObservingModesMode_TFI"
        self.mdObservingModesMode_TFI.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_TFI)

        self.mdObservingModesMode_LSSpec.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_LSSpec.ident = "ObservingModesMode_LSSpec"
        self.mdObservingModesMode_LSSpec.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_LSSpec)

        self.mdObservingModesMode_MOS.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_MOS.ident = "ObservingModesMode_MOS"
        self.mdObservingModesMode_MOS.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_MOS)

        self.mdObservingModesMode_FastBBI.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_FastBBI.ident = "ObservingModesMode_FastBBI"
        self.mdObservingModesMode_FastBBI.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_FastBBI)

        self.mdObservingModesMode_FrTrBBI.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_FrTrBBI.ident = "ObservingModesMode_FrTrBBI"
        self.mdObservingModesMode_FrTrBBI.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_FrTrBBI)

        self.mdObservingModesMode_FastLSSpec.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_FastLSSpec.ident = "ObservingModesMode_FastLSSpec"
        self.mdObservingModesMode_FastLSSpec.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_FastLSSpec)

        self.mdObservingModesMode_FastTFImage.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_FastTFImage.ident = "ObservingModesMode_FastTFImage"
        self.mdObservingModesMode_FastTFImage.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_FastTFImage)

        self.mdObservingModesMode_FrTrTFI.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_FrTrTFI.ident = "ObservingModesMode_FrTrTFI"
        self.mdObservingModesMode_FrTrTFI.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_FrTrTFI)

        self.mdObservingModesMode_Bias.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_Bias.ident = "ObservingModesMode_Bias"
        self.mdObservingModesMode_Bias.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_Bias)

        self.mdObservingModesMode_Dark.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_Dark.ident = "ObservingModesMode_Dark"
        self.mdObservingModesMode_Dark.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_Dark)

        self.mdObservingModesMode_DomeFlat.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_DomeFlat.ident = "ObservingModesMode_DomeFlat"
        self.mdObservingModesMode_DomeFlat.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_DomeFlat)

        self.mdObservingModesMode_SkyFlat.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_SkyFlat.ident = "ObservingModesMode_SkyFlat"
        self.mdObservingModesMode_SkyFlat.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_SkyFlat)

        self.mdObservingModesMode_SpectralFlat.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_SpectralFlat.ident = "ObservingModesMode_SpectralFlat"
        self.mdObservingModesMode_SpectralFlat.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_SpectralFlat)

        self.mdObservingModesMode_CalibLamp.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_CalibLamp.ident = "ObservingModesMode_CalibLamp"
        self.mdObservingModesMode_CalibLamp.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_CalibLamp)

        self.mdObservingModesMode_TFCalib.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_TFCalib.ident = "ObservingModesMode_TFCalib"
        self.mdObservingModesMode_TFCalib.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_TFCalib)

        self.mdAcquisitionMode_Normal.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_Normal.ident = "AcquisitionMode_Normal"
        self.mdAcquisitionMode_Normal.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Normal)

        self.mdAcquisitionMode_FrameTransfer.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_FrameTransfer.ident = "AcquisitionMode_FrameTransfer"
        self.mdAcquisitionMode_FrameTransfer.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_FrameTransfer)

        self.mdAcquisitionMode_Shuffling.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_Shuffling.ident = "AcquisitionMode_Shuffling"
        self.mdAcquisitionMode_Shuffling.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Shuffling)

        self.vlShuffleLines_FullRange.id = idcounter
        idcounter += 1
        self.vlShuffleLines_FullRange.ident = "ShuffleLines_FullRange"
        self.vlShuffleLines_FullRange.description = ""
        self.prShuffleLines.addValue(self.vlShuffleLines_FullRange)

        self.mdShuffleLinesMode_Normal.id = idcounter
        idcounter += 1
        self.mdShuffleLinesMode_Normal.ident = "ShuffleLinesMode_Normal"
        self.mdShuffleLinesMode_Normal.description = ""
        self.prShuffleLines.addMode(self.mdShuffleLinesMode_Normal)

        self.vlShiftNumber_FullRange.id = idcounter
        idcounter += 1
        self.vlShiftNumber_FullRange.ident = "ShiftNumber_FullRange"
        self.vlShiftNumber_FullRange.description = ""
        self.prShiftNumber.addValue(self.vlShiftNumber_FullRange)

        self.mdShiftNumberMode_Normal.id = idcounter
        idcounter += 1
        self.mdShiftNumberMode_Normal.ident = "ShiftNumberMode_Normal"
        self.mdShiftNumberMode_Normal.description = ""
        self.prShiftNumber.addMode(self.mdShiftNumberMode_Normal)

        self.vlExpTime_FullRange.id = idcounter
        idcounter += 1
        self.vlExpTime_FullRange.ident = "ExpTime_FullRange"
        self.vlExpTime_FullRange.description = ""
        self.prExpTime.addValue(self.vlExpTime_FullRange)

        self.mdExpTimeMode_Normal.id = idcounter
        idcounter += 1
        self.mdExpTimeMode_Normal.ident = "ExpTimeMode_Normal"
        self.mdExpTimeMode_Normal.description = ""
        self.prExpTime.addMode(self.mdExpTimeMode_Normal)

        self.mdExpTimeMode_Bias.id = idcounter
        idcounter += 1
        self.mdExpTimeMode_Bias.ident = "ExpTimeMode_Bias"
        self.mdExpTimeMode_Bias.description = ""
        self.prExpTime.addMode(self.mdExpTimeMode_Bias)

        self.vlExpTime_0_0.id = idcounter
        idcounter += 1
        self.vlExpTime_0_0.ident = "ExpTime_0_0"
        self.vlExpTime_0_0.description = ""
        self.prExpTime.addValue(self.vlExpTime_0_0)

        self.mdExpTimeMode_FT.id = idcounter
        idcounter += 1
        self.mdExpTimeMode_FT.ident = "ExpTimeMode_FT"
        self.mdExpTimeMode_FT.description = ""
        self.prExpTime.addMode(self.mdExpTimeMode_FT)

        self.vlExpTime_FTRange.id = idcounter
        idcounter += 1
        self.vlExpTime_FTRange.ident = "ExpTime_FTRange"
        self.vlExpTime_FTRange.description = ""
        self.prExpTime.addValue(self.vlExpTime_FTRange)

        self.mdnumOfFramesMode_Normal.id = idcounter
        idcounter += 1
        self.mdnumOfFramesMode_Normal.ident = "numOfFramesMode_Normal"
        self.mdnumOfFramesMode_Normal.description = ""
        self.prnumOfFrames.addMode(self.mdnumOfFramesMode_Normal)

        self.vlnumOfFrames_FullRange.id = idcounter
        idcounter += 1
        self.vlnumOfFrames_FullRange.ident = "numOfFrames_FullRange"
        self.vlnumOfFrames_FullRange.description = ""
        self.prnumOfFrames.addValue(self.vlnumOfFrames_FullRange)

        self.mdMultipleExposureMode_On.id = idcounter
        idcounter += 1
        self.mdMultipleExposureMode_On.ident = "MultipleExposureMode_On"
        self.mdMultipleExposureMode_On.description = ""
        self.sysMultipleExposure.addMode(self.mdMultipleExposureMode_On)

        self.mdMultipleExposureMode_Single.id = idcounter
        idcounter += 1
        self.mdMultipleExposureMode_Single.ident = "MultipleExposureMode_Single"
        self.mdMultipleExposureMode_Single.description = ""
        self.sysMultipleExposure.addMode(self.mdMultipleExposureMode_Single)

        self.vlPixelSpeed_SLW.id = idcounter
        idcounter += 1
        self.vlPixelSpeed_SLW.ident = "PixelSpeed_SLW"
        self.vlPixelSpeed_SLW.description = ""
        self.prPixelSpeed.addValue(self.vlPixelSpeed_SLW)

        self.vlPixelSpeed_MED.id = idcounter
        idcounter += 1
        self.vlPixelSpeed_MED.ident = "PixelSpeed_MED"
        self.vlPixelSpeed_MED.description = ""
        self.prPixelSpeed.addValue(self.vlPixelSpeed_MED)

        self.vlPixelSpeed_FST.id = idcounter
        idcounter += 1
        self.vlPixelSpeed_FST.ident = "PixelSpeed_FST"
        self.vlPixelSpeed_FST.description = ""
        self.prPixelSpeed.addValue(self.vlPixelSpeed_FST)

        self.mdPixelSpeedMode_All.id = idcounter
        idcounter += 1
        self.mdPixelSpeedMode_All.ident = "PixelSpeedMode_All"
        self.mdPixelSpeedMode_All.description = ""
        self.prPixelSpeed.addMode(self.mdPixelSpeedMode_All)

        self.mdAcquisitionMode_FTBias.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_FTBias.ident = "AcquisitionMode_FTBias"
        self.mdAcquisitionMode_FTBias.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_FTBias)

        self.mdAcquisitionMode_NormalBias.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_NormalBias.ident = "AcquisitionMode_NormalBias"
        self.mdAcquisitionMode_NormalBias.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_NormalBias)

        self.mdAcquisitionMode_ShufflingBias.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_ShufflingBias.ident = "AcquisitionMode_ShufflingBias"
        self.mdAcquisitionMode_ShufflingBias.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_ShufflingBias)

        self.mdAcquisitionMode_NormalSquare.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_NormalSquare.ident = "AcquisitionMode_NormalSquare"
        self.mdAcquisitionMode_NormalSquare.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_NormalSquare)

        self.mdAcquisitionMode_ShufflingSquare.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_ShufflingSquare.ident = "AcquisitionMode_ShufflingSquare"
        self.mdAcquisitionMode_ShufflingSquare.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_ShufflingSquare)

        self.mdAcquisitionMode_GainCalib.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_GainCalib.ident = "AcquisitionMode_GainCalib"
        self.mdAcquisitionMode_GainCalib.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_GainCalib)

        self.vlCalibGain_FullRange.id = idcounter
        idcounter += 1
        self.vlCalibGain_FullRange.ident = "CalibGain_FullRange"
        self.vlCalibGain_FullRange.description = ""
        self.prCalibGain.addValue(self.vlCalibGain_FullRange)

        self.mdCalibGainMode_Normal.id = idcounter
        idcounter += 1
        self.mdCalibGainMode_Normal.ident = "CalibGainMode_Normal"
        self.mdCalibGainMode_Normal.description = ""
        self.prCalibGain.addMode(self.mdCalibGainMode_Normal)

        self.mdDASMode_SimpleImg.id = idcounter
        idcounter += 1
        self.mdDASMode_SimpleImg.ident = "DASMode_SimpleImg"
        self.mdDASMode_SimpleImg.description = ""
        self.sysDAS.addMode(self.mdDASMode_SimpleImg)

        self.mdDASMode_SimpleSpec.id = idcounter
        idcounter += 1
        self.mdDASMode_SimpleSpec.ident = "DASMode_SimpleSpec"
        self.mdDASMode_SimpleSpec.description = ""
        self.sysDAS.addMode(self.mdDASMode_SimpleSpec)

        self.mdDASMode_ShufffingSpec.id = idcounter
        idcounter += 1
        self.mdDASMode_ShufffingSpec.ident = "DASMode_ShufffingSpec"
        self.mdDASMode_ShufffingSpec.description = ""
        self.sysDAS.addMode(self.mdDASMode_ShufffingSpec)

        self.mdOpenShutterMode_On.id = idcounter
        idcounter += 1
        self.mdOpenShutterMode_On.ident = "OpenShutterMode_On"
        self.mdOpenShutterMode_On.description = ""
        self.sysOpenShutter.addMode(self.mdOpenShutterMode_On)

        self.mdOpenShutterMode_Off.id = idcounter
        idcounter += 1
        self.mdOpenShutterMode_Off.ident = "OpenShutterMode_Off"
        self.mdOpenShutterMode_Off.description = ""
        self.sysOpenShutter.addMode(self.mdOpenShutterMode_Off)

        self.mdDASMode_FTImg.id = idcounter
        idcounter += 1
        self.mdDASMode_FTImg.ident = "DASMode_FTImg"
        self.mdDASMode_FTImg.description = ""
        self.sysDAS.addMode(self.mdDASMode_FTImg)

        self.mdDASMode_FTDark.id = idcounter
        idcounter += 1
        self.mdDASMode_FTDark.ident = "DASMode_FTDark"
        self.mdDASMode_FTDark.description = ""
        self.sysDAS.addMode(self.mdDASMode_FTDark)

        self.mdDASMode_FTBias.id = idcounter
        idcounter += 1
        self.mdDASMode_FTBias.ident = "DASMode_FTBias"
        self.mdDASMode_FTBias.description = ""
        self.sysDAS.addMode(self.mdDASMode_FTBias)

        self.mdDASMode_SimpleBias.id = idcounter
        idcounter += 1
        self.mdDASMode_SimpleBias.ident = "DASMode_SimpleBias"
        self.mdDASMode_SimpleBias.description = ""
        self.sysDAS.addMode(self.mdDASMode_SimpleBias)

        self.mdDASMode_SimpleDark.id = idcounter
        idcounter += 1
        self.mdDASMode_SimpleDark.ident = "DASMode_SimpleDark"
        self.mdDASMode_SimpleDark.description = ""
        self.sysDAS.addMode(self.mdDASMode_SimpleDark)

        self.mdDASMode_ShufffingDark.id = idcounter
        idcounter += 1
        self.mdDASMode_ShufffingDark.ident = "DASMode_ShufffingDark"
        self.mdDASMode_ShufffingDark.description = ""
        self.sysDAS.addMode(self.mdDASMode_ShufffingDark)

        self.mdDASMode_ShufffingBias.id = idcounter
        idcounter += 1
        self.mdDASMode_ShufffingBias.ident = "DASMode_ShufffingBias"
        self.mdDASMode_ShufffingBias.description = ""
        self.sysDAS.addMode(self.mdDASMode_ShufffingBias)

        self.mdDASMode_ShufffingImage.id = idcounter
        idcounter += 1
        self.mdDASMode_ShufffingImage.ident = "DASMode_ShufffingImage"
        self.mdDASMode_ShufffingImage.description = ""
        self.sysDAS.addMode(self.mdDASMode_ShufffingImage)

        self.mdDASMode_SimpleCalib.id = idcounter
        idcounter += 1
        self.mdDASMode_SimpleCalib.ident = "DASMode_SimpleCalib"
        self.mdDASMode_SimpleCalib.description = ""
        self.sysDAS.addMode(self.mdDASMode_SimpleCalib)

        self.mdDASMode_GainCalib.id = idcounter
        idcounter += 1
        self.mdDASMode_GainCalib.ident = "DASMode_GainCalib"
        self.mdDASMode_GainCalib.description = ""
        self.sysDAS.addMode(self.mdDASMode_GainCalib)

        self.vlCurrentEllapsed_Range.id = idcounter
        idcounter += 1
        self.vlCurrentEllapsed_Range.ident = "CurrentEllapsed_Range"
        self.vlCurrentEllapsed_Range.description = ""
        self.prCurrentEllapsed.addValue(self.vlCurrentEllapsed_Range)

        self.mdCurrentEllapsedMode_Normal.id = idcounter
        idcounter += 1
        self.mdCurrentEllapsedMode_Normal.ident = "CurrentEllapsedMode_Normal"
        self.mdCurrentEllapsedMode_Normal.description = ""
        self.prCurrentEllapsed.addMode(self.mdCurrentEllapsedMode_Normal)

        self.vlCurrentImg_Range.id = idcounter
        idcounter += 1
        self.vlCurrentImg_Range.ident = "CurrentImg_Range"
        self.vlCurrentImg_Range.description = ""
        self.prCurrentImg.addValue(self.vlCurrentImg_Range)

        self.mdCurrentImgMode_Normal.id = idcounter
        idcounter += 1
        self.mdCurrentImgMode_Normal.ident = "CurrentImgMode_Normal"
        self.mdCurrentImgMode_Normal.description = ""
        self.prCurrentImg.addMode(self.mdCurrentImgMode_Normal)

        self.vlCurrentPct_Range.id = idcounter
        idcounter += 1
        self.vlCurrentPct_Range.ident = "CurrentPct_Range"
        self.vlCurrentPct_Range.description = ""
        self.prCurrentPct.addValue(self.vlCurrentPct_Range)

        self.mdCurrentPctMode_Normal.id = idcounter
        idcounter += 1
        self.mdCurrentPctMode_Normal.ident = "CurrentPctMode_Normal"
        self.mdCurrentPctMode_Normal.description = ""
        self.prCurrentPct.addMode(self.mdCurrentPctMode_Normal)

        self.vlOverallPct_Range.id = idcounter
        idcounter += 1
        self.vlOverallPct_Range.ident = "OverallPct_Range"
        self.vlOverallPct_Range.description = ""
        self.prOverallPct.addValue(self.vlOverallPct_Range)

        self.mdOverallPctMode_Normal.id = idcounter
        idcounter += 1
        self.mdOverallPctMode_Normal.ident = "OverallPctMode_Normal"
        self.mdOverallPctMode_Normal.description = ""
        self.prOverallPct.addMode(self.mdOverallPctMode_Normal)

        self.mdProcessMonitorMode_Normal.id = idcounter
        idcounter += 1
        self.mdProcessMonitorMode_Normal.ident = "ProcessMonitorMode_Normal"
        self.mdProcessMonitorMode_Normal.description = ""
        self.sysProcessMonitor.addMode(self.mdProcessMonitorMode_Normal)

        self.mdFocalPlaneElementMode_Disabled.id = idcounter
        idcounter += 1
        self.mdFocalPlaneElementMode_Disabled.ident = "FocalPlaneElementMode_Disabled"
        self.mdFocalPlaneElementMode_Disabled.description = ""
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_Disabled)

        self.vlFocalPlaneElement_LS0_4.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_LS0_4.ident = "FocalPlaneElement_LS0_4"
        self.vlFocalPlaneElement_LS0_4.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS0_4)

        self.vlFocalPlaneElement_LS0_6.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_LS0_6.ident = "FocalPlaneElement_LS0_6"
        self.vlFocalPlaneElement_LS0_6.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS0_6)

        self.vlFocalPlaneElement_LS0_8.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_LS0_8.ident = "FocalPlaneElement_LS0_8"
        self.vlFocalPlaneElement_LS0_8.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS0_8)

        self.vlFocalPlaneElement_LS1_0.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_LS1_0.ident = "FocalPlaneElement_LS1_0"
        self.vlFocalPlaneElement_LS1_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS1_0)

        self.vlFocalPlaneElement_LS1_2.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_LS1_2.ident = "FocalPlaneElement_LS1_2"
        self.vlFocalPlaneElement_LS1_2.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS1_2)

        self.vlFocalPlaneElement_LS1_5.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_LS1_5.ident = "FocalPlaneElement_LS1_5"
        self.vlFocalPlaneElement_LS1_5.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS1_5)

        self.vlFocalPlaneElement_LS1_8.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_LS1_8.ident = "FocalPlaneElement_LS1_8"
        self.vlFocalPlaneElement_LS1_8.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS1_8)

        self.vlFocalPlaneElement_LS2_5.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_LS2_5.ident = "FocalPlaneElement_LS2_5"
        self.vlFocalPlaneElement_LS2_5.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS2_5)

        self.vlFocalPlaneElement_LS3_0.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_LS3_0.ident = "FocalPlaneElement_LS3_0"
        self.vlFocalPlaneElement_LS3_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS3_0)

        self.vlFocalPlaneElement_LS5_0.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_LS5_0.ident = "FocalPlaneElement_LS5_0"
        self.vlFocalPlaneElement_LS5_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS5_0)

        self.vlFocalPlaneElement_LS10_0.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_LS10_0.ident = "FocalPlaneElement_LS10_0"
        self.vlFocalPlaneElement_LS10_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS10_0)

        self.vlFocalPlaneElement_LS12_0.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_LS12_0.ident = "FocalPlaneElement_LS12_0"
        self.vlFocalPlaneElement_LS12_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS12_0)

        self.vlFocalPlaneElement_LS40_0.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_LS40_0.ident = "FocalPlaneElement_LS40_0"
        self.vlFocalPlaneElement_LS40_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS40_0)

        self.mdFocalPlaneElementMode_MOS.id = idcounter
        idcounter += 1
        self.mdFocalPlaneElementMode_MOS.ident = "FocalPlaneElementMode_MOS"
        self.mdFocalPlaneElementMode_MOS.description = ""
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_MOS)

        self.mdFocalPlaneElementMode_FastPhotometry.id = idcounter
        idcounter += 1
        self.mdFocalPlaneElementMode_FastPhotometry.ident = "FocalPlaneElementMode_FastPhotometry"
        self.mdFocalPlaneElementMode_FastPhotometry.description = ""
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_FastPhotometry)

        self.mdFocalPlaneElementMode_FrameTransfer.id = idcounter
        idcounter += 1
        self.mdFocalPlaneElementMode_FrameTransfer.ident = "FocalPlaneElementMode_FrameTransfer"
        self.mdFocalPlaneElementMode_FrameTransfer.description = ""
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_FrameTransfer)

        self.mdFocalPlaneElementMode_LS.id = idcounter
        idcounter += 1
        self.mdFocalPlaneElementMode_LS.ident = "FocalPlaneElementMode_LS"
        self.mdFocalPlaneElementMode_LS.description = ""
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_LS)

        self.vlFocalPlaneElement_FrameTransferMask.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_FrameTransferMask.ident = "FocalPlaneElement_FrameTransferMask"
        self.vlFocalPlaneElement_FrameTransferMask.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_FrameTransferMask)

        self.vlFocalPlaneElement_FastPhotometryMask.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_FastPhotometryMask.ident = "FocalPlaneElement_FastPhotometryMask"
        self.vlFocalPlaneElement_FastPhotometryMask.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_FastPhotometryMask)

        self.vlFocalPlaneElement_MOSmask.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_MOSmask.ident = "FocalPlaneElement_MOSmask"
        self.vlFocalPlaneElement_MOSmask.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_MOSmask)

        self.vlFocalPlaneElement_NoFPE.id = idcounter
        idcounter += 1
        self.vlFocalPlaneElement_NoFPE.ident = "FocalPlaneElement_NoFPE"
        self.vlFocalPlaneElement_NoFPE.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_NoFPE)

        self.mdFPEMode_NoFPE.id = idcounter
        idcounter += 1
        self.mdFPEMode_NoFPE.ident = "FPEMode_NoFPE"
        self.mdFPEMode_NoFPE.description = ""
        self.sysFPE.addMode(self.mdFPEMode_NoFPE)

        self.mdFPEMode_MOSmask.id = idcounter
        idcounter += 1
        self.mdFPEMode_MOSmask.ident = "FPEMode_MOSmask"
        self.mdFPEMode_MOSmask.description = ""
        self.sysFPE.addMode(self.mdFPEMode_MOSmask)

        self.mdFPEMode_FastPhotometryMask.id = idcounter
        idcounter += 1
        self.mdFPEMode_FastPhotometryMask.ident = "FPEMode_FastPhotometryMask"
        self.mdFPEMode_FastPhotometryMask.description = ""
        self.sysFPE.addMode(self.mdFPEMode_FastPhotometryMask)

        self.mdFPEMode_FrameTransferMask.id = idcounter
        idcounter += 1
        self.mdFPEMode_FrameTransferMask.ident = "FPEMode_FrameTransferMask"
        self.mdFPEMode_FrameTransferMask.description = ""
        self.sysFPE.addMode(self.mdFPEMode_FrameTransferMask)

        self.mdFPEMode_LSMask.id = idcounter
        idcounter += 1
        self.mdFPEMode_LSMask.ident = "FPEMode_LSMask"
        self.mdFPEMode_LSMask.description = ""
        self.sysFPE.addMode(self.mdFPEMode_LSMask)

        self.mdPreOpticsMode_NoDispersion.id = idcounter
        idcounter += 1
        self.mdPreOpticsMode_NoDispersion.ident = "PreOpticsMode_NoDispersion"
        self.mdPreOpticsMode_NoDispersion.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_NoDispersion)

        self.mdPreOpticsMode_RTF.id = idcounter
        idcounter += 1
        self.mdPreOpticsMode_RTF.ident = "PreOpticsMode_RTF"
        self.mdPreOpticsMode_RTF.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_RTF)

        self.mdPreOpticsMode_GrismR.id = idcounter
        idcounter += 1
        self.mdPreOpticsMode_GrismR.ident = "PreOpticsMode_GrismR"
        self.mdPreOpticsMode_GrismR.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_GrismR)

        self.mdPreOpticsMode_BTF.id = idcounter
        idcounter += 1
        self.mdPreOpticsMode_BTF.ident = "PreOpticsMode_BTF"
        self.mdPreOpticsMode_BTF.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_BTF)

        self.vlGrisms_R300B.id = idcounter
        idcounter += 1
        self.vlGrisms_R300B.ident = "Grisms_R300B"
        self.vlGrisms_R300B.description = ""
        self.prGrisms.addValue(self.vlGrisms_R300B)

        self.vlGrisms_R300R.id = idcounter
        idcounter += 1
        self.vlGrisms_R300R.ident = "Grisms_R300R"
        self.vlGrisms_R300R.description = ""
        self.prGrisms.addValue(self.vlGrisms_R300R)

        self.vlGrisms_R500B.id = idcounter
        idcounter += 1
        self.vlGrisms_R500B.ident = "Grisms_R500B"
        self.vlGrisms_R500B.description = ""
        self.prGrisms.addValue(self.vlGrisms_R500B)

        self.vlGrisms_R500R.id = idcounter
        idcounter += 1
        self.vlGrisms_R500R.ident = "Grisms_R500R"
        self.vlGrisms_R500R.description = ""
        self.prGrisms.addValue(self.vlGrisms_R500R)

        self.vlGrisms_R1000B.id = idcounter
        idcounter += 1
        self.vlGrisms_R1000B.ident = "Grisms_R1000B"
        self.vlGrisms_R1000B.description = ""
        self.prGrisms.addValue(self.vlGrisms_R1000B)

        self.vlGrisms_R1000R.id = idcounter
        idcounter += 1
        self.vlGrisms_R1000R.ident = "Grisms_R1000R"
        self.vlGrisms_R1000R.description = ""
        self.prGrisms.addValue(self.vlGrisms_R1000R)

        self.vlGrisms_R2000B.id = idcounter
        idcounter += 1
        self.vlGrisms_R2000B.ident = "Grisms_R2000B"
        self.vlGrisms_R2000B.description = ""
        self.prGrisms.addValue(self.vlGrisms_R2000B)

        self.vlGrisms_R2500U.id = idcounter
        idcounter += 1
        self.vlGrisms_R2500U.ident = "Grisms_R2500U"
        self.vlGrisms_R2500U.description = ""
        self.prGrisms.addValue(self.vlGrisms_R2500U)

        self.vlGrisms_R2500V.id = idcounter
        idcounter += 1
        self.vlGrisms_R2500V.ident = "Grisms_R2500V"
        self.vlGrisms_R2500V.description = ""
        self.prGrisms.addValue(self.vlGrisms_R2500V)

        self.vlGrisms_R2500R.id = idcounter
        idcounter += 1
        self.vlGrisms_R2500R.ident = "Grisms_R2500R"
        self.vlGrisms_R2500R.description = ""
        self.prGrisms.addValue(self.vlGrisms_R2500R)

        self.vlGrisms_R2500I.id = idcounter
        idcounter += 1
        self.vlGrisms_R2500I.ident = "Grisms_R2500I"
        self.vlGrisms_R2500I.description = ""
        self.prGrisms.addValue(self.vlGrisms_R2500I)

        self.mdGrismsMode_GrismsB.id = idcounter
        idcounter += 1
        self.mdGrismsMode_GrismsB.ident = "GrismsMode_GrismsB"
        self.mdGrismsMode_GrismsB.description = ""
        self.prGrisms.addMode(self.mdGrismsMode_GrismsB)

        self.mdGrismsMode_GrismsR.id = idcounter
        idcounter += 1
        self.mdGrismsMode_GrismsR.ident = "GrismsMode_GrismsR"
        self.mdGrismsMode_GrismsR.description = ""
        self.prGrisms.addMode(self.mdGrismsMode_GrismsR)

        self.mdPreOpticsMode_GrismB.id = idcounter
        idcounter += 1
        self.mdPreOpticsMode_GrismB.ident = "PreOpticsMode_GrismB"
        self.mdPreOpticsMode_GrismB.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_GrismB)

        self.mdPreOpticsMode_GrismBMOS.id = idcounter
        idcounter += 1
        self.mdPreOpticsMode_GrismBMOS.ident = "PreOpticsMode_GrismBMOS"
        self.mdPreOpticsMode_GrismBMOS.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_GrismBMOS)

        self.vlRedFWHM_Range2_0.id = idcounter
        idcounter += 1
        self.vlRedFWHM_Range2_0.ident = "RedFWHM_Range2_0"
        self.vlRedFWHM_Range2_0.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range2_0)

        self.mdRedFWHMMode_l2_0.id = idcounter
        idcounter += 1
        self.mdRedFWHMMode_l2_0.ident = "RedFWHMMode_l2_0"
        self.mdRedFWHMMode_l2_0.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l2_0)

        self.mdRedFWHMMode_l1_5.id = idcounter
        idcounter += 1
        self.mdRedFWHMMode_l1_5.ident = "RedFWHMMode_l1_5"
        self.mdRedFWHMMode_l1_5.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l1_5)

        self.mdRedFWHMMode_l1_4.id = idcounter
        idcounter += 1
        self.mdRedFWHMMode_l1_4.ident = "RedFWHMMode_l1_4"
        self.mdRedFWHMMode_l1_4.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l1_4)

        self.mdRedFWHMMode_l1_3.id = idcounter
        idcounter += 1
        self.mdRedFWHMMode_l1_3.ident = "RedFWHMMode_l1_3"
        self.mdRedFWHMMode_l1_3.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l1_3)

        self.mdRedFWHMMode_l1_2.id = idcounter
        idcounter += 1
        self.mdRedFWHMMode_l1_2.ident = "RedFWHMMode_l1_2"
        self.mdRedFWHMMode_l1_2.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l1_2)

        self.mdRedFWHMMode_l1_2b.id = idcounter
        idcounter += 1
        self.mdRedFWHMMode_l1_2b.ident = "RedFWHMMode_l1_2b"
        self.mdRedFWHMMode_l1_2b.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l1_2b)

        self.vlRedFWHM_Range1_5.id = idcounter
        idcounter += 1
        self.vlRedFWHM_Range1_5.ident = "RedFWHM_Range1_5"
        self.vlRedFWHM_Range1_5.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range1_5)

        self.vlRedFWHM_Range1_4.id = idcounter
        idcounter += 1
        self.vlRedFWHM_Range1_4.ident = "RedFWHM_Range1_4"
        self.vlRedFWHM_Range1_4.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range1_4)

        self.vlRedFWHM_Range1_3.id = idcounter
        idcounter += 1
        self.vlRedFWHM_Range1_3.ident = "RedFWHM_Range1_3"
        self.vlRedFWHM_Range1_3.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range1_3)

        self.vlRedFWHM_Range1_2.id = idcounter
        idcounter += 1
        self.vlRedFWHM_Range1_2.ident = "RedFWHM_Range1_2"
        self.vlRedFWHM_Range1_2.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range1_2)

        self.vlRedFWHM_Range1_2b.id = idcounter
        idcounter += 1
        self.vlRedFWHM_Range1_2b.ident = "RedFWHM_Range1_2b"
        self.vlRedFWHM_Range1_2b.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range1_2b)

        self.mdRedTFMode_l651_799.id = idcounter
        idcounter += 1
        self.mdRedTFMode_l651_799.ident = "RedTFMode_l651_799"
        self.mdRedTFMode_l651_799.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l651_799)

        self.mdRedTFMode_l800_819.id = idcounter
        idcounter += 1
        self.mdRedTFMode_l800_819.ident = "RedTFMode_l800_819"
        self.mdRedTFMode_l800_819.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l800_819)

        self.mdRedTFMode_l820_839.id = idcounter
        idcounter += 1
        self.mdRedTFMode_l820_839.ident = "RedTFMode_l820_839"
        self.mdRedTFMode_l820_839.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l820_839)

        self.mdRedTFMode_l840_879.id = idcounter
        idcounter += 1
        self.mdRedTFMode_l840_879.ident = "RedTFMode_l840_879"
        self.mdRedTFMode_l840_879.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l840_879)

        self.mdRedTFMode_l880_909.id = idcounter
        idcounter += 1
        self.mdRedTFMode_l880_909.ident = "RedTFMode_l880_909"
        self.mdRedTFMode_l880_909.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l880_909)

        self.mdRedTFMode_l910_934.id = idcounter
        idcounter += 1
        self.mdRedTFMode_l910_934.ident = "RedTFMode_l910_934"
        self.mdRedTFMode_l910_934.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l910_934)

        self.vlRedLamda_Range651.id = idcounter
        idcounter += 1
        self.vlRedLamda_Range651.ident = "RedLamda_Range651"
        self.vlRedLamda_Range651.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range651)

        self.mdRedLamdaMode_l651_799.id = idcounter
        idcounter += 1
        self.mdRedLamdaMode_l651_799.ident = "RedLamdaMode_l651_799"
        self.mdRedLamdaMode_l651_799.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l651_799)

        self.mdRedLamdaMode_l800_819.id = idcounter
        idcounter += 1
        self.mdRedLamdaMode_l800_819.ident = "RedLamdaMode_l800_819"
        self.mdRedLamdaMode_l800_819.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l800_819)

        self.mdRedLamdaMode_l820_839.id = idcounter
        idcounter += 1
        self.mdRedLamdaMode_l820_839.ident = "RedLamdaMode_l820_839"
        self.mdRedLamdaMode_l820_839.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l820_839)

        self.mdRedLamdaMode_l840_879.id = idcounter
        idcounter += 1
        self.mdRedLamdaMode_l840_879.ident = "RedLamdaMode_l840_879"
        self.mdRedLamdaMode_l840_879.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l840_879)

        self.mdRedLamdaMode_l880_909.id = idcounter
        idcounter += 1
        self.mdRedLamdaMode_l880_909.ident = "RedLamdaMode_l880_909"
        self.mdRedLamdaMode_l880_909.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l880_909)

        self.mdRedLamdaMode_l910_934.id = idcounter
        idcounter += 1
        self.mdRedLamdaMode_l910_934.ident = "RedLamdaMode_l910_934"
        self.mdRedLamdaMode_l910_934.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l910_934)

        self.vlRedLamda_Range800.id = idcounter
        idcounter += 1
        self.vlRedLamda_Range800.ident = "RedLamda_Range800"
        self.vlRedLamda_Range800.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range800)

        self.vlRedLamda_Range820.id = idcounter
        idcounter += 1
        self.vlRedLamda_Range820.ident = "RedLamda_Range820"
        self.vlRedLamda_Range820.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range820)

        self.vlRedLamda_Range840.id = idcounter
        idcounter += 1
        self.vlRedLamda_Range840.ident = "RedLamda_Range840"
        self.vlRedLamda_Range840.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range840)

        self.vlRedLamda_Range880.id = idcounter
        idcounter += 1
        self.vlRedLamda_Range880.ident = "RedLamda_Range880"
        self.vlRedLamda_Range880.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range880)

        self.vlRedLamda_Range910.id = idcounter
        idcounter += 1
        self.vlRedLamda_Range910.ident = "RedLamda_Range910"
        self.vlRedLamda_Range910.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range910)

        self.vlBlueFWHM_0_8.id = idcounter
        idcounter += 1
        self.vlBlueFWHM_0_8.ident = "BlueFWHM_0_8"
        self.vlBlueFWHM_0_8.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_8)

        self.mdBlueFWHMMode_l0_8.id = idcounter
        idcounter += 1
        self.mdBlueFWHMMode_l0_8.ident = "BlueFWHMMode_l0_8"
        self.mdBlueFWHMMode_l0_8.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_8)

        self.mdBlueFWHMMode_l0_85.id = idcounter
        idcounter += 1
        self.mdBlueFWHMMode_l0_85.ident = "BlueFWHMMode_l0_85"
        self.mdBlueFWHMMode_l0_85.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_85)

        self.mdBlueFWHMMode_l0_50.id = idcounter
        idcounter += 1
        self.mdBlueFWHMMode_l0_50.ident = "BlueFWHMMode_l0_50"
        self.mdBlueFWHMMode_l0_50.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_50)

        self.mdBlueFWHMMode_l0_45.id = idcounter
        idcounter += 1
        self.mdBlueFWHMMode_l0_45.ident = "BlueFWHMMode_l0_45"
        self.mdBlueFWHMMode_l0_45.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_45)

        self.vlBlueFWHM_0_85.id = idcounter
        idcounter += 1
        self.vlBlueFWHM_0_85.ident = "BlueFWHM_0_85"
        self.vlBlueFWHM_0_85.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_85)

        self.vlBlueFWHM_0_50.id = idcounter
        idcounter += 1
        self.vlBlueFWHM_0_50.ident = "BlueFWHM_0_50"
        self.vlBlueFWHM_0_50.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_50)

        self.vlBlueFWHM_0_45.id = idcounter
        idcounter += 1
        self.vlBlueFWHM_0_45.ident = "BlueFWHM_0_45"
        self.vlBlueFWHM_0_45.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_45)

        self.vlBlueFWHM_0_70.id = idcounter
        idcounter += 1
        self.vlBlueFWHM_0_70.ident = "BlueFWHM_0_70"
        self.vlBlueFWHM_0_70.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_70)

        self.mdBlueFWHMMode_l0_70.id = idcounter
        idcounter += 1
        self.mdBlueFWHMMode_l0_70.ident = "BlueFWHMMode_l0_70"
        self.mdBlueFWHMMode_l0_70.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_70)

        self.mdBlueFWHMMode_l0_90.id = idcounter
        idcounter += 1
        self.mdBlueFWHMMode_l0_90.ident = "BlueFWHMMode_l0_90"
        self.mdBlueFWHMMode_l0_90.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_90)

        self.mdBlueFWHMMode_l1_10.id = idcounter
        idcounter += 1
        self.mdBlueFWHMMode_l1_10.ident = "BlueFWHMMode_l1_10"
        self.mdBlueFWHMMode_l1_10.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l1_10)

        self.vlBlueFWHM_0_90.id = idcounter
        idcounter += 1
        self.vlBlueFWHM_0_90.ident = "BlueFWHM_0_90"
        self.vlBlueFWHM_0_90.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_90)

        self.vlBlueFWHM_1_10.id = idcounter
        idcounter += 1
        self.vlBlueFWHM_1_10.ident = "BlueFWHM_1_10"
        self.vlBlueFWHM_1_10.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_1_10)

        self.mdBlueTFMode_l448_463.id = idcounter
        idcounter += 1
        self.mdBlueTFMode_l448_463.ident = "BlueTFMode_l448_463"
        self.mdBlueTFMode_l448_463.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l448_463)

        self.mdBlueTFMode_l464_480.id = idcounter
        idcounter += 1
        self.mdBlueTFMode_l464_480.ident = "BlueTFMode_l464_480"
        self.mdBlueTFMode_l464_480.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l464_480)

        self.mdBlueTFMode_l481_502.id = idcounter
        idcounter += 1
        self.mdBlueTFMode_l481_502.ident = "BlueTFMode_l481_502"
        self.mdBlueTFMode_l481_502.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l481_502)

        self.mdBlueTFMode_l503_521.id = idcounter
        idcounter += 1
        self.mdBlueTFMode_l503_521.ident = "BlueTFMode_l503_521"
        self.mdBlueTFMode_l503_521.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l503_521)

        self.mdBlueTFMode_l522_542.id = idcounter
        idcounter += 1
        self.mdBlueTFMode_l522_542.ident = "BlueTFMode_l522_542"
        self.mdBlueTFMode_l522_542.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l522_542)

        self.mdBlueTFMode_l543_583.id = idcounter
        idcounter += 1
        self.mdBlueTFMode_l543_583.ident = "BlueTFMode_l543_583"
        self.mdBlueTFMode_l543_583.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l543_583)

        self.vlBlueLamda_Range448.id = idcounter
        idcounter += 1
        self.vlBlueLamda_Range448.ident = "BlueLamda_Range448"
        self.vlBlueLamda_Range448.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range448)

        self.mdBlueLamdaMode_l448_463.id = idcounter
        idcounter += 1
        self.mdBlueLamdaMode_l448_463.ident = "BlueLamdaMode_l448_463"
        self.mdBlueLamdaMode_l448_463.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l448_463)

        self.mdBlueLamdaMode_l464_480.id = idcounter
        idcounter += 1
        self.mdBlueLamdaMode_l464_480.ident = "BlueLamdaMode_l464_480"
        self.mdBlueLamdaMode_l464_480.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l464_480)

        self.mdBlueLamdaMode_l481_502.id = idcounter
        idcounter += 1
        self.mdBlueLamdaMode_l481_502.ident = "BlueLamdaMode_l481_502"
        self.mdBlueLamdaMode_l481_502.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l481_502)

        self.mdBlueLamdaMode_l503_521.id = idcounter
        idcounter += 1
        self.mdBlueLamdaMode_l503_521.ident = "BlueLamdaMode_l503_521"
        self.mdBlueLamdaMode_l503_521.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l503_521)

        self.mdBlueLamdaMode_l522_542.id = idcounter
        idcounter += 1
        self.mdBlueLamdaMode_l522_542.ident = "BlueLamdaMode_l522_542"
        self.mdBlueLamdaMode_l522_542.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l522_542)

        self.mdBlueLamdaMode_l543_583.id = idcounter
        idcounter += 1
        self.mdBlueLamdaMode_l543_583.ident = "BlueLamdaMode_l543_583"
        self.mdBlueLamdaMode_l543_583.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l543_583)

        self.vlBlueLamda_Range464.id = idcounter
        idcounter += 1
        self.vlBlueLamda_Range464.ident = "BlueLamda_Range464"
        self.vlBlueLamda_Range464.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range464)

        self.vlBlueLamda_Range481.id = idcounter
        idcounter += 1
        self.vlBlueLamda_Range481.ident = "BlueLamda_Range481"
        self.vlBlueLamda_Range481.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range481)

        self.vlBlueLamda_Range503.id = idcounter
        idcounter += 1
        self.vlBlueLamda_Range503.ident = "BlueLamda_Range503"
        self.vlBlueLamda_Range503.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range503)

        self.vlBlueLamda_Range522.id = idcounter
        idcounter += 1
        self.vlBlueLamda_Range522.ident = "BlueLamda_Range522"
        self.vlBlueLamda_Range522.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range522)

        self.vlBlueLamda_Range543.id = idcounter
        idcounter += 1
        self.vlBlueLamda_Range543.ident = "BlueLamda_Range543"
        self.vlBlueLamda_Range543.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range543)

        self.mdBlueLamdaMode_l584_609.id = idcounter
        idcounter += 1
        self.mdBlueLamdaMode_l584_609.ident = "BlueLamdaMode_l584_609"
        self.mdBlueLamdaMode_l584_609.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l584_609)

        self.mdBlueLamdaMode_l610_637.id = idcounter
        idcounter += 1
        self.mdBlueLamdaMode_l610_637.ident = "BlueLamdaMode_l610_637"
        self.mdBlueLamdaMode_l610_637.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l610_637)

        self.mdBlueLamdaMode_l638_671.id = idcounter
        idcounter += 1
        self.mdBlueLamdaMode_l638_671.ident = "BlueLamdaMode_l638_671"
        self.mdBlueLamdaMode_l638_671.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l638_671)

        self.vlBlueLamda_Range584.id = idcounter
        idcounter += 1
        self.vlBlueLamda_Range584.ident = "BlueLamda_Range584"
        self.vlBlueLamda_Range584.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range584)

        self.vlBlueLamda_Range610.id = idcounter
        idcounter += 1
        self.vlBlueLamda_Range610.ident = "BlueLamda_Range610"
        self.vlBlueLamda_Range610.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range610)

        self.vlBlueLamda_Range638.id = idcounter
        idcounter += 1
        self.vlBlueLamda_Range638.ident = "BlueLamda_Range638"
        self.vlBlueLamda_Range638.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range638)

        self.mdBlueTFMode_l584_609.id = idcounter
        idcounter += 1
        self.mdBlueTFMode_l584_609.ident = "BlueTFMode_l584_609"
        self.mdBlueTFMode_l584_609.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l584_609)

        self.mdBlueTFMode_l610_637.id = idcounter
        idcounter += 1
        self.mdBlueTFMode_l610_637.ident = "BlueTFMode_l610_637"
        self.mdBlueTFMode_l610_637.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l610_637)

        self.mdBlueTFMode_l638_671.id = idcounter
        idcounter += 1
        self.mdBlueTFMode_l638_671.ident = "BlueTFMode_l638_671"
        self.mdBlueTFMode_l638_671.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l638_671)

        self.mdPreOpticsMode_RTFCalib.id = idcounter
        idcounter += 1
        self.mdPreOpticsMode_RTFCalib.ident = "PreOpticsMode_RTFCalib"
        self.mdPreOpticsMode_RTFCalib.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_RTFCalib)

        self.mdPreOpticsMode_BTFCalib.id = idcounter
        idcounter += 1
        self.mdPreOpticsMode_BTFCalib.ident = "PreOpticsMode_BTFCalib"
        self.mdPreOpticsMode_BTFCalib.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_BTFCalib)

        self.vlzzero_NormalRange.id = idcounter
        idcounter += 1
        self.vlzzero_NormalRange.ident = "zzero_NormalRange"
        self.vlzzero_NormalRange.description = ""
        self.przzero.addValue(self.vlzzero_NormalRange)

        self.mdzzeroMode_Normal.id = idcounter
        idcounter += 1
        self.mdzzeroMode_Normal.ident = "zzeroMode_Normal"
        self.mdzzeroMode_Normal.description = ""
        self.przzero.addMode(self.mdzzeroMode_Normal)

        self.mdDetectorMode_FT.id = idcounter
        idcounter += 1
        self.mdDetectorMode_FT.ident = "DetectorMode_FT"
        self.mdDetectorMode_FT.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_FT)

        self.mdDetectorMode_Window.id = idcounter
        idcounter += 1
        self.mdDetectorMode_Window.ident = "DetectorMode_Window"
        self.mdDetectorMode_Window.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_Window)

        self.mdOutputSourceMode_0x0.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_0x0.ident = "OutputSourceMode_0x0"
        self.mdOutputSourceMode_0x0.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x0)

        self.mdOutputSourceMode_0x1.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_0x1.ident = "OutputSourceMode_0x1"
        self.mdOutputSourceMode_0x1.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x1)

        self.mdOutputSourceMode_0x2.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_0x2.ident = "OutputSourceMode_0x2"
        self.mdOutputSourceMode_0x2.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x2)

        self.mdOutputSourceMode_0x3.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_0x3.ident = "OutputSourceMode_0x3"
        self.mdOutputSourceMode_0x3.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x3)

        self.mdOutputSourceMode_ALL.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_ALL.ident = "OutputSourceMode_ALL"
        self.mdOutputSourceMode_ALL.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_ALL)

        self.mdOutputSourceMode_TWO.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_TWO.ident = "OutputSourceMode_TWO"
        self.mdOutputSourceMode_TWO.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_TWO)

        self.mdRecompositionMode_None.id = idcounter
        idcounter += 1
        self.mdRecompositionMode_None.ident = "RecompositionMode_None"
        self.mdRecompositionMode_None.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_None)

        self.mdRecompositionMode_Serial.id = idcounter
        idcounter += 1
        self.mdRecompositionMode_Serial.ident = "RecompositionMode_Serial"
        self.mdRecompositionMode_Serial.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_Serial)

        self.mdRecompositionMode_QuadCCD.id = idcounter
        idcounter += 1
        self.mdRecompositionMode_QuadCCD.ident = "RecompositionMode_QuadCCD"
        self.mdRecompositionMode_QuadCCD.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_QuadCCD)

        self.mdDetectorMode_FullDetector.id = idcounter
        idcounter += 1
        self.mdDetectorMode_FullDetector.ident = "DetectorMode_FullDetector"
        self.mdDetectorMode_FullDetector.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_FullDetector)

        self.mdDetectorMode_WindowSq.id = idcounter
        idcounter += 1
        self.mdDetectorMode_WindowSq.ident = "DetectorMode_WindowSq"
        self.mdDetectorMode_WindowSq.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_WindowSq)

        self.mdDetectorMode_FullDetectorSq.id = idcounter
        idcounter += 1
        self.mdDetectorMode_FullDetectorSq.ident = "DetectorMode_FullDetectorSq"
        self.mdDetectorMode_FullDetectorSq.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_FullDetectorSq)

        self.vlBinning_1x1.id = idcounter
        idcounter += 1
        self.vlBinning_1x1.ident = "Binning_1x1"
        self.vlBinning_1x1.description = ""
        self.prBinning.addValue(self.vlBinning_1x1)

        self.vlBinning_1x2.id = idcounter
        idcounter += 1
        self.vlBinning_1x2.ident = "Binning_1x2"
        self.vlBinning_1x2.description = ""
        self.prBinning.addValue(self.vlBinning_1x2)

        self.vlBinning_2x1.id = idcounter
        idcounter += 1
        self.vlBinning_2x1.ident = "Binning_2x1"
        self.vlBinning_2x1.description = ""
        self.prBinning.addValue(self.vlBinning_2x1)

        self.vlBinning_2x2.id = idcounter
        idcounter += 1
        self.vlBinning_2x2.ident = "Binning_2x2"
        self.vlBinning_2x2.description = ""
        self.prBinning.addValue(self.vlBinning_2x2)

        self.mdBinningMode_All.id = idcounter
        idcounter += 1
        self.mdBinningMode_All.ident = "BinningMode_All"
        self.mdBinningMode_All.description = ""
        self.prBinning.addMode(self.mdBinningMode_All)

        self.mdBinningMode_Square.id = idcounter
        idcounter += 1
        self.mdBinningMode_Square.ident = "BinningMode_Square"
        self.mdBinningMode_Square.description = ""
        self.prBinning.addMode(self.mdBinningMode_Square)

        self.mdBinningMode_Off.id = idcounter
        idcounter += 1
        self.mdBinningMode_Off.ident = "BinningMode_Off"
        self.mdBinningMode_Off.description = ""
        self.prBinning.addMode(self.mdBinningMode_Off)

        self.mdWindowMode_Enabled.id = idcounter
        idcounter += 1
        self.mdWindowMode_Enabled.ident = "WindowMode_Enabled"
        self.mdWindowMode_Enabled.description = ""
        self.sysWindow.addMode(self.mdWindowMode_Enabled)

        self.mdRowsMode_Normal.id = idcounter
        idcounter += 1
        self.mdRowsMode_Normal.ident = "RowsMode_Normal"
        self.mdRowsMode_Normal.description = ""
        self.prRows.addMode(self.mdRowsMode_Normal)

        self.vlRows_FullRange.id = idcounter
        idcounter += 1
        self.vlRows_FullRange.ident = "Rows_FullRange"
        self.vlRows_FullRange.description = ""
        self.prRows.addValue(self.vlRows_FullRange)

        self.mdColsMode_Normal.id = idcounter
        idcounter += 1
        self.mdColsMode_Normal.ident = "ColsMode_Normal"
        self.mdColsMode_Normal.description = ""
        self.prCols.addMode(self.mdColsMode_Normal)

        self.vlCols_FullRange.id = idcounter
        idcounter += 1
        self.vlCols_FullRange.ident = "Cols_FullRange"
        self.vlCols_FullRange.description = ""
        self.prCols.addValue(self.vlCols_FullRange)

        self.mdoffsetRowMode_Normal.id = idcounter
        idcounter += 1
        self.mdoffsetRowMode_Normal.ident = "offsetRowMode_Normal"
        self.mdoffsetRowMode_Normal.description = ""
        self.proffsetRow.addMode(self.mdoffsetRowMode_Normal)

        self.vloffsetRow_FullRange.id = idcounter
        idcounter += 1
        self.vloffsetRow_FullRange.ident = "offsetRow_FullRange"
        self.vloffsetRow_FullRange.description = ""
        self.proffsetRow.addValue(self.vloffsetRow_FullRange)

        self.mdoffsetColMode_Normal.id = idcounter
        idcounter += 1
        self.mdoffsetColMode_Normal.ident = "offsetColMode_Normal"
        self.mdoffsetColMode_Normal.description = ""
        self.proffsetCol.addMode(self.mdoffsetColMode_Normal)

        self.vloffsetCol_FullRange.id = idcounter
        idcounter += 1
        self.vloffsetCol_FullRange.ident = "offsetCol_FullRange"
        self.vloffsetCol_FullRange.description = ""
        self.proffsetCol.addValue(self.vloffsetCol_FullRange)

        self.mdWindowMode_Disabled.id = idcounter
        idcounter += 1
        self.mdWindowMode_Disabled.ident = "WindowMode_Disabled"
        self.mdWindowMode_Disabled.description = ""
        self.sysWindow.addMode(self.mdWindowMode_Disabled)

        self.mdFiltersMode_OS.id = idcounter
        idcounter += 1
        self.mdFiltersMode_OS.ident = "FiltersMode_OS"
        self.mdFiltersMode_OS.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_OS)

        self.mdFiltersMode_UFilter.id = idcounter
        idcounter += 1
        self.mdFiltersMode_UFilter.ident = "FiltersMode_UFilter"
        self.mdFiltersMode_UFilter.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_UFilter)

        self.vlUFilters_U500_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U500_17.ident = "UFilters_U500_17"
        self.vlUFilters_U500_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U500_17)

        self.vlUFilters_U517_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U517_17.ident = "UFilters_U517_17"
        self.vlUFilters_U517_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U517_17)

        self.vlUFilters_U534_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U534_17.ident = "UFilters_U534_17"
        self.vlUFilters_U534_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U534_17)

        self.vlUFilters_U551_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U551_17.ident = "UFilters_U551_17"
        self.vlUFilters_U551_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U551_17)

        self.vlUFilters_U568_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U568_17.ident = "UFilters_U568_17"
        self.vlUFilters_U568_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U568_17)

        self.vlUFilters_U585_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U585_17.ident = "UFilters_U585_17"
        self.vlUFilters_U585_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U585_17)

        self.vlUFilters_U602_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U602_17.ident = "UFilters_U602_17"
        self.vlUFilters_U602_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U602_17)

        self.vlUFilters_U619_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U619_17.ident = "UFilters_U619_17"
        self.vlUFilters_U619_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U619_17)

        self.vlUFilters_U636_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U636_17.ident = "UFilters_U636_17"
        self.vlUFilters_U636_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U636_17)

        self.vlUFilters_U653_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U653_17.ident = "UFilters_U653_17"
        self.vlUFilters_U653_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U653_17)

        self.vlUFilters_U670_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U670_17.ident = "UFilters_U670_17"
        self.vlUFilters_U670_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U670_17)

        self.vlUFilters_U687_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U687_17.ident = "UFilters_U687_17"
        self.vlUFilters_U687_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U687_17)

        self.vlUFilters_U704_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U704_17.ident = "UFilters_U704_17"
        self.vlUFilters_U704_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U704_17)

        self.vlUFilters_U721_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U721_17.ident = "UFilters_U721_17"
        self.vlUFilters_U721_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U721_17)

        self.vlUFilters_U738_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U738_17.ident = "UFilters_U738_17"
        self.vlUFilters_U738_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U738_17)

        self.vlUFilters_U755_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U755_17.ident = "UFilters_U755_17"
        self.vlUFilters_U755_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U755_17)

        self.vlUFilters_U772_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U772_17.ident = "UFilters_U772_17"
        self.vlUFilters_U772_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U772_17)

        self.vlUFilters_U789_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U789_17.ident = "UFilters_U789_17"
        self.vlUFilters_U789_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U789_17)

        self.vlUFilters_U806_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U806_17.ident = "UFilters_U806_17"
        self.vlUFilters_U806_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U806_17)

        self.vlUFilters_U823_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U823_17.ident = "UFilters_U823_17"
        self.vlUFilters_U823_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U823_17)

        self.vlUFilters_U840_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U840_17.ident = "UFilters_U840_17"
        self.vlUFilters_U840_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U840_17)

        self.vlUFilters_U857_17.id = idcounter
        idcounter += 1
        self.vlUFilters_U857_17.ident = "UFilters_U857_17"
        self.vlUFilters_U857_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U857_17)

        self.vlUFilters_U883_35.id = idcounter
        idcounter += 1
        self.vlUFilters_U883_35.ident = "UFilters_U883_35"
        self.vlUFilters_U883_35.description = ""
        self.prUFilters.addValue(self.vlUFilters_U883_35)

        self.vlUFilters_U913_25.id = idcounter
        idcounter += 1
        self.vlUFilters_U913_25.ident = "UFilters_U913_25"
        self.vlUFilters_U913_25.description = ""
        self.prUFilters.addValue(self.vlUFilters_U913_25)

        self.vlUFilters_U941_33.id = idcounter
        idcounter += 1
        self.vlUFilters_U941_33.ident = "UFilters_U941_33"
        self.vlUFilters_U941_33.description = ""
        self.prUFilters.addValue(self.vlUFilters_U941_33)

        self.mdUFiltersMode_U5xx.id = idcounter
        idcounter += 1
        self.mdUFiltersMode_U5xx.ident = "UFiltersMode_U5xx"
        self.mdUFiltersMode_U5xx.description = ""
        self.prUFilters.addMode(self.mdUFiltersMode_U5xx)

        self.mdUFiltersMode_U6xx.id = idcounter
        idcounter += 1
        self.mdUFiltersMode_U6xx.ident = "UFiltersMode_U6xx"
        self.mdUFiltersMode_U6xx.description = ""
        self.prUFilters.addMode(self.mdUFiltersMode_U6xx)

        self.mdUFiltersMode_U7xx.id = idcounter
        idcounter += 1
        self.mdUFiltersMode_U7xx.ident = "UFiltersMode_U7xx"
        self.mdUFiltersMode_U7xx.description = ""
        self.prUFilters.addMode(self.mdUFiltersMode_U7xx)

        self.mdUFiltersMode_U8xx.id = idcounter
        idcounter += 1
        self.mdUFiltersMode_U8xx.ident = "UFiltersMode_U8xx"
        self.mdUFiltersMode_U8xx.description = ""
        self.prUFilters.addMode(self.mdUFiltersMode_U8xx)

        self.mdUFiltersMode_U9xx.id = idcounter
        idcounter += 1
        self.mdUFiltersMode_U9xx.ident = "UFiltersMode_U9xx"
        self.mdUFiltersMode_U9xx.description = ""
        self.prUFilters.addMode(self.mdUFiltersMode_U9xx)

        self.vlOS_f504_16.id = idcounter
        idcounter += 1
        self.vlOS_f504_16.ident = "OS_f504_16"
        self.vlOS_f504_16.description = ""
        self.prOS.addValue(self.vlOS_f504_16)

        self.vlOS_f509_16.id = idcounter
        idcounter += 1
        self.vlOS_f509_16.ident = "OS_f509_16"
        self.vlOS_f509_16.description = ""
        self.prOS.addValue(self.vlOS_f509_16)

        self.vlOS_f514_16.id = idcounter
        idcounter += 1
        self.vlOS_f514_16.ident = "OS_f514_16"
        self.vlOS_f514_16.description = ""
        self.prOS.addValue(self.vlOS_f514_16)

        self.vlOS_f519_16.id = idcounter
        idcounter += 1
        self.vlOS_f519_16.ident = "OS_f519_16"
        self.vlOS_f519_16.description = ""
        self.prOS.addValue(self.vlOS_f519_16)

        self.vlOS_f525_17.id = idcounter
        idcounter += 1
        self.vlOS_f525_17.ident = "OS_f525_17"
        self.vlOS_f525_17.description = ""
        self.prOS.addValue(self.vlOS_f525_17)

        self.vlOS_f530_17.id = idcounter
        idcounter += 1
        self.vlOS_f530_17.ident = "OS_f530_17"
        self.vlOS_f530_17.description = ""
        self.prOS.addValue(self.vlOS_f530_17)

        self.vlOS_f536_17.id = idcounter
        idcounter += 1
        self.vlOS_f536_17.ident = "OS_f536_17"
        self.vlOS_f536_17.description = ""
        self.prOS.addValue(self.vlOS_f536_17)

        self.vlOS_f542_18.id = idcounter
        idcounter += 1
        self.vlOS_f542_18.ident = "OS_f542_18"
        self.vlOS_f542_18.description = ""
        self.prOS.addValue(self.vlOS_f542_18)

        self.vlOS_f548_18.id = idcounter
        idcounter += 1
        self.vlOS_f548_18.ident = "OS_f548_18"
        self.vlOS_f548_18.description = ""
        self.prOS.addValue(self.vlOS_f548_18)

        self.vlOS_f554_18.id = idcounter
        idcounter += 1
        self.vlOS_f554_18.ident = "OS_f554_18"
        self.vlOS_f554_18.description = ""
        self.prOS.addValue(self.vlOS_f554_18)

        self.vlOS_f561_19.id = idcounter
        idcounter += 1
        self.vlOS_f561_19.ident = "OS_f561_19"
        self.vlOS_f561_19.description = ""
        self.prOS.addValue(self.vlOS_f561_19)

        self.vlOS_f568_19.id = idcounter
        idcounter += 1
        self.vlOS_f568_19.ident = "OS_f568_19"
        self.vlOS_f568_19.description = ""
        self.prOS.addValue(self.vlOS_f568_19)

        self.vlOS_f575_19.id = idcounter
        idcounter += 1
        self.vlOS_f575_19.ident = "OS_f575_19"
        self.vlOS_f575_19.description = ""
        self.prOS.addValue(self.vlOS_f575_19)

        self.vlOS_f583_20.id = idcounter
        idcounter += 1
        self.vlOS_f583_20.ident = "OS_f583_20"
        self.vlOS_f583_20.description = ""
        self.prOS.addValue(self.vlOS_f583_20)

        self.vlOS_f591_21.id = idcounter
        idcounter += 1
        self.vlOS_f591_21.ident = "OS_f591_21"
        self.vlOS_f591_21.description = ""
        self.prOS.addValue(self.vlOS_f591_21)

        self.vlOS_f599_22.id = idcounter
        idcounter += 1
        self.vlOS_f599_22.ident = "OS_f599_22"
        self.vlOS_f599_22.description = ""
        self.prOS.addValue(self.vlOS_f599_22)

        self.mdOSMode_f5xx.id = idcounter
        idcounter += 1
        self.mdOSMode_f5xx.ident = "OSMode_f5xx"
        self.mdOSMode_f5xx.description = ""
        self.prOS.addMode(self.mdOSMode_f5xx)

        self.vlOS_f477_14.id = idcounter
        idcounter += 1
        self.vlOS_f477_14.ident = "OS_f477_14"
        self.vlOS_f477_14.description = ""
        self.prOS.addValue(self.vlOS_f477_14)

        self.vlOS_f481_14.id = idcounter
        idcounter += 1
        self.vlOS_f481_14.ident = "OS_f481_14"
        self.vlOS_f481_14.description = ""
        self.prOS.addValue(self.vlOS_f481_14)

        self.mdOSMode_f4xx.id = idcounter
        idcounter += 1
        self.mdOSMode_f4xx.ident = "OSMode_f4xx"
        self.mdOSMode_f4xx.description = ""
        self.prOS.addMode(self.mdOSMode_f4xx)

        self.vlOS_f486_14.id = idcounter
        idcounter += 1
        self.vlOS_f486_14.ident = "OS_f486_14"
        self.vlOS_f486_14.description = ""
        self.prOS.addValue(self.vlOS_f486_14)

        self.vlOS_f469_14.id = idcounter
        idcounter += 1
        self.vlOS_f469_14.ident = "OS_f469_14"
        self.vlOS_f469_14.description = ""
        self.prOS.addValue(self.vlOS_f469_14)

        self.vlOS_f461_13.id = idcounter
        idcounter += 1
        self.vlOS_f461_13.ident = "OS_f461_13"
        self.vlOS_f461_13.description = ""
        self.prOS.addValue(self.vlOS_f461_13)

        self.vlOS_f499_15.id = idcounter
        idcounter += 1
        self.vlOS_f499_15.ident = "OS_f499_15"
        self.vlOS_f499_15.description = ""
        self.prOS.addValue(self.vlOS_f499_15)

        self.vlOS_f454_13.id = idcounter
        idcounter += 1
        self.vlOS_f454_13.ident = "OS_f454_13"
        self.vlOS_f454_13.description = ""
        self.prOS.addValue(self.vlOS_f454_13)

        self.vlOS_f451_13.id = idcounter
        idcounter += 1
        self.vlOS_f451_13.ident = "OS_f451_13"
        self.vlOS_f451_13.description = ""
        self.prOS.addValue(self.vlOS_f451_13)

        self.vlOS_f495_15.id = idcounter
        idcounter += 1
        self.vlOS_f495_15.ident = "OS_f495_15"
        self.vlOS_f495_15.description = ""
        self.prOS.addValue(self.vlOS_f495_15)

        self.vlOS_f465_13.id = idcounter
        idcounter += 1
        self.vlOS_f465_13.ident = "OS_f465_13"
        self.vlOS_f465_13.description = ""
        self.prOS.addValue(self.vlOS_f465_13)

        self.vlOS_f490_15.id = idcounter
        idcounter += 1
        self.vlOS_f490_15.ident = "OS_f490_15"
        self.vlOS_f490_15.description = ""
        self.prOS.addValue(self.vlOS_f490_15)

        self.vlOS_f458_13.id = idcounter
        idcounter += 1
        self.vlOS_f458_13.ident = "OS_f458_13"
        self.vlOS_f458_13.description = ""
        self.prOS.addValue(self.vlOS_f458_13)

        self.vlOS_f473_14.id = idcounter
        idcounter += 1
        self.vlOS_f473_14.ident = "OS_f473_14"
        self.vlOS_f473_14.description = ""
        self.prOS.addValue(self.vlOS_f473_14)

        self.vlOS_f638_25.id = idcounter
        idcounter += 1
        self.vlOS_f638_25.ident = "OS_f638_25"
        self.vlOS_f638_25.description = ""
        self.prOS.addValue(self.vlOS_f638_25)

        self.vlOS_f680_43.id = idcounter
        idcounter += 1
        self.vlOS_f680_43.ident = "OS_f680_43"
        self.vlOS_f680_43.description = ""
        self.prOS.addValue(self.vlOS_f680_43)

        self.vlOS_f608_22.id = idcounter
        idcounter += 1
        self.vlOS_f608_22.ident = "OS_f608_22"
        self.vlOS_f608_22.description = ""
        self.prOS.addValue(self.vlOS_f608_22)

        self.vlOS_f627_24.id = idcounter
        idcounter += 1
        self.vlOS_f627_24.ident = "OS_f627_24"
        self.vlOS_f627_24.description = ""
        self.prOS.addValue(self.vlOS_f627_24)

        self.vlOS_f694_44.id = idcounter
        idcounter += 1
        self.vlOS_f694_44.ident = "OS_f694_44"
        self.vlOS_f694_44.description = ""
        self.prOS.addValue(self.vlOS_f694_44)

        self.vlOS_f617_23.id = idcounter
        idcounter += 1
        self.vlOS_f617_23.ident = "OS_f617_23"
        self.vlOS_f617_23.description = ""
        self.prOS.addValue(self.vlOS_f617_23)

        self.vlOS_f666_36.id = idcounter
        idcounter += 1
        self.vlOS_f666_36.ident = "OS_f666_36"
        self.vlOS_f666_36.description = ""
        self.prOS.addValue(self.vlOS_f666_36)

        self.vlOS_f649_25.id = idcounter
        idcounter += 1
        self.vlOS_f649_25.ident = "OS_f649_25"
        self.vlOS_f649_25.description = ""
        self.prOS.addValue(self.vlOS_f649_25)

        self.vlOS_f657_35.id = idcounter
        idcounter += 1
        self.vlOS_f657_35.ident = "OS_f657_35"
        self.vlOS_f657_35.description = ""
        self.prOS.addValue(self.vlOS_f657_35)

        self.mdOSMode_f6xx.id = idcounter
        idcounter += 1
        self.mdOSMode_f6xx.ident = "OSMode_f6xx"
        self.mdOSMode_f6xx.description = ""
        self.prOS.addMode(self.mdOSMode_f6xx)

        self.vlOS_f661_27.id = idcounter
        idcounter += 1
        self.vlOS_f661_27.ident = "OS_f661_27"
        self.vlOS_f661_27.description = ""
        self.prOS.addValue(self.vlOS_f661_27)

        self.vlOS_f723_45.id = idcounter
        idcounter += 1
        self.vlOS_f723_45.ident = "OS_f723_45"
        self.vlOS_f723_45.description = ""
        self.prOS.addValue(self.vlOS_f723_45)

        self.mdOSMode_f7xx.id = idcounter
        idcounter += 1
        self.mdOSMode_f7xx.ident = "OSMode_f7xx"
        self.mdOSMode_f7xx.description = ""
        self.prOS.addMode(self.mdOSMode_f7xx)

        self.vlOS_f770_50.id = idcounter
        idcounter += 1
        self.vlOS_f770_50.ident = "OS_f770_50"
        self.vlOS_f770_50.description = ""
        self.prOS.addValue(self.vlOS_f770_50)

        self.vlOS_f738_49.id = idcounter
        idcounter += 1
        self.vlOS_f738_49.ident = "OS_f738_49"
        self.vlOS_f738_49.description = ""
        self.prOS.addValue(self.vlOS_f738_49)

        self.vlOS_f709_45.id = idcounter
        idcounter += 1
        self.vlOS_f709_45.ident = "OS_f709_45"
        self.vlOS_f709_45.description = ""
        self.prOS.addValue(self.vlOS_f709_45)

        self.vlOS_f754_50.id = idcounter
        idcounter += 1
        self.vlOS_f754_50.ident = "OS_f754_50"
        self.vlOS_f754_50.description = ""
        self.prOS.addValue(self.vlOS_f754_50)

        self.vlOS_f785_48.id = idcounter
        idcounter += 1
        self.vlOS_f785_48.ident = "OS_f785_48"
        self.vlOS_f785_48.description = ""
        self.prOS.addValue(self.vlOS_f785_48)

        self.vlOS_f923_34.id = idcounter
        idcounter += 1
        self.vlOS_f923_34.ident = "OS_f923_34"
        self.vlOS_f923_34.description = ""
        self.prOS.addValue(self.vlOS_f923_34)

        self.mdOSMode_f9xx.id = idcounter
        idcounter += 1
        self.mdOSMode_f9xx.ident = "OSMode_f9xx"
        self.mdOSMode_f9xx.description = ""
        self.prOS.addMode(self.mdOSMode_f9xx)

        self.vlOS_f932_34.id = idcounter
        idcounter += 1
        self.vlOS_f932_34.ident = "OS_f932_34"
        self.vlOS_f932_34.description = ""
        self.prOS.addValue(self.vlOS_f932_34)

        self.vlOS_f927_34.id = idcounter
        idcounter += 1
        self.vlOS_f927_34.ident = "OS_f927_34"
        self.vlOS_f927_34.description = ""
        self.prOS.addValue(self.vlOS_f927_34)

        self.vlOS_f902_44.id = idcounter
        idcounter += 1
        self.vlOS_f902_44.ident = "OS_f902_44"
        self.vlOS_f902_44.description = ""
        self.prOS.addValue(self.vlOS_f902_44)

        self.vlOS_f919_41.id = idcounter
        idcounter += 1
        self.vlOS_f919_41.ident = "OS_f919_41"
        self.vlOS_f919_41.description = ""
        self.prOS.addValue(self.vlOS_f919_41)

        self.vlOS_f910_40.id = idcounter
        idcounter += 1
        self.vlOS_f910_40.ident = "OS_f910_40"
        self.vlOS_f910_40.description = ""
        self.prOS.addValue(self.vlOS_f910_40)

        self.vlOS_f802_51.id = idcounter
        idcounter += 1
        self.vlOS_f802_51.ident = "OS_f802_51"
        self.vlOS_f802_51.description = ""
        self.prOS.addValue(self.vlOS_f802_51)

        self.vlOS_f878_59.id = idcounter
        idcounter += 1
        self.vlOS_f878_59.ident = "OS_f878_59"
        self.vlOS_f878_59.description = ""
        self.prOS.addValue(self.vlOS_f878_59)

        self.vlOS_f858_58.id = idcounter
        idcounter += 1
        self.vlOS_f858_58.ident = "OS_f858_58"
        self.vlOS_f858_58.description = ""
        self.prOS.addValue(self.vlOS_f858_58)

        self.vlOS_f893_50.id = idcounter
        idcounter += 1
        self.vlOS_f893_50.ident = "OS_f893_50"
        self.vlOS_f893_50.description = ""
        self.prOS.addValue(self.vlOS_f893_50)

        self.vlOS_f838_58.id = idcounter
        idcounter += 1
        self.vlOS_f838_58.ident = "OS_f838_58"
        self.vlOS_f838_58.description = ""
        self.prOS.addValue(self.vlOS_f838_58)

        self.vlOS_f819_52.id = idcounter
        idcounter += 1
        self.vlOS_f819_52.ident = "OS_f819_52"
        self.vlOS_f819_52.description = ""
        self.prOS.addValue(self.vlOS_f819_52)

        self.mdOSMode_f8xx.id = idcounter
        idcounter += 1
        self.mdOSMode_f8xx.ident = "OSMode_f8xx"
        self.mdOSMode_f8xx.description = ""
        self.prOS.addMode(self.mdOSMode_f8xx)

        self.mdFiltersMode_NoFilter.id = idcounter
        idcounter += 1
        self.mdFiltersMode_NoFilter.ident = "FiltersMode_NoFilter"
        self.mdFiltersMode_NoFilter.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_NoFilter)

        self.mdFiltersMode_GR.id = idcounter
        idcounter += 1
        self.mdFiltersMode_GR.ident = "FiltersMode_GR"
        self.mdFiltersMode_GR.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_GR)

        self.vlBroad_Sloan_u.id = idcounter
        idcounter += 1
        self.vlBroad_Sloan_u.ident = "Broad_Sloan_u"
        self.vlBroad_Sloan_u.description = ""
        self.prBroad.addValue(self.vlBroad_Sloan_u)

        self.vlBroad_Sloan_g.id = idcounter
        idcounter += 1
        self.vlBroad_Sloan_g.ident = "Broad_Sloan_g"
        self.vlBroad_Sloan_g.description = ""
        self.prBroad.addValue(self.vlBroad_Sloan_g)

        self.vlBroad_Sloan_r.id = idcounter
        idcounter += 1
        self.vlBroad_Sloan_r.ident = "Broad_Sloan_r"
        self.vlBroad_Sloan_r.description = ""
        self.prBroad.addValue(self.vlBroad_Sloan_r)

        self.vlBroad_Sloan_i.id = idcounter
        idcounter += 1
        self.vlBroad_Sloan_i.ident = "Broad_Sloan_i"
        self.vlBroad_Sloan_i.description = ""
        self.prBroad.addValue(self.vlBroad_Sloan_i)

        self.vlBroad_Sloan_z.id = idcounter
        idcounter += 1
        self.vlBroad_Sloan_z.ident = "Broad_Sloan_z"
        self.vlBroad_Sloan_z.description = ""
        self.prBroad.addValue(self.vlBroad_Sloan_z)

        self.mdBroadMode_All.id = idcounter
        idcounter += 1
        self.mdBroadMode_All.ident = "BroadMode_All"
        self.mdBroadMode_All.description = ""
        self.prBroad.addMode(self.mdBroadMode_All)

        self.mdFiltersMode_Broad.id = idcounter
        idcounter += 1
        self.mdFiltersMode_Broad.ident = "FiltersMode_Broad"
        self.mdFiltersMode_Broad.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_Broad)

        self.mdFiltersMode_OSCalc.id = idcounter
        idcounter += 1
        self.mdFiltersMode_OSCalc.ident = "FiltersMode_OSCalc"
        self.mdFiltersMode_OSCalc.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_OSCalc)

        self.mdFiltersMode_Engineering.id = idcounter
        idcounter += 1
        self.mdFiltersMode_Engineering.ident = "FiltersMode_Engineering"
        self.mdFiltersMode_Engineering.description = "Filters engineering mode"
        self.sysFilters.addMode(self.mdFiltersMode_Engineering)

        self.mdOsirisMode_Engineering.id = idcounter
        idcounter += 1
        self.mdOsirisMode_Engineering.ident = "OsirisMode_Engineering"
        self.mdOsirisMode_Engineering.description = "Osiris engineering mode"
        self.sysOsiris.addMode(self.mdOsirisMode_Engineering)

        self.mdObservingModesMode_Engineering.id = idcounter
        idcounter += 1
        self.mdObservingModesMode_Engineering.ident = "ObservingModesMode_Engineering"
        self.mdObservingModesMode_Engineering.description = "ObservingModes engineering mode"
        self.sysObservingModes.addMode(self.mdObservingModesMode_Engineering)

        self.mdAcquisitionModesMode_Engineering.id = idcounter
        idcounter += 1
        self.mdAcquisitionModesMode_Engineering.ident = "AcquisitionModesMode_Engineering"
        self.mdAcquisitionModesMode_Engineering.description = "AcquisitionModes engineering mode"
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_Engineering)

        self.mdDASMode_Engineering.id = idcounter
        idcounter += 1
        self.mdDASMode_Engineering.ident = "DASMode_Engineering"
        self.mdDASMode_Engineering.description = "DAS engineering mode"
        self.sysDAS.addMode(self.mdDASMode_Engineering)

        self.mdAcquisitionMode_Engineering.id = idcounter
        idcounter += 1
        self.mdAcquisitionMode_Engineering.ident = "AcquisitionMode_Engineering"
        self.mdAcquisitionMode_Engineering.description = "Acquisition engineering mode"
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Engineering)

        self.mdMultipleExposureMode_Engineering.id = idcounter
        idcounter += 1
        self.mdMultipleExposureMode_Engineering.ident = "MultipleExposureMode_Engineering"
        self.mdMultipleExposureMode_Engineering.description = "MultipleExposure engineering mode"
        self.sysMultipleExposure.addMode(self.mdMultipleExposureMode_Engineering)

        self.mdProcessMonitorMode_Engineering.id = idcounter
        idcounter += 1
        self.mdProcessMonitorMode_Engineering.ident = "ProcessMonitorMode_Engineering"
        self.mdProcessMonitorMode_Engineering.description = "ProcessMonitor engineering mode"
        self.sysProcessMonitor.addMode(self.mdProcessMonitorMode_Engineering)

        self.mdFPEMode_Engineering.id = idcounter
        idcounter += 1
        self.mdFPEMode_Engineering.ident = "FPEMode_Engineering"
        self.mdFPEMode_Engineering.description = "FPE engineering mode"
        self.sysFPE.addMode(self.mdFPEMode_Engineering)

        self.mdPreOpticsMode_Engineering.id = idcounter
        idcounter += 1
        self.mdPreOpticsMode_Engineering.ident = "PreOpticsMode_Engineering"
        self.mdPreOpticsMode_Engineering.description = "PreOptics engineering mode"
        self.sysPreOptics.addMode(self.mdPreOpticsMode_Engineering)

        self.mdRedTFMode_Engineering.id = idcounter
        idcounter += 1
        self.mdRedTFMode_Engineering.ident = "RedTFMode_Engineering"
        self.mdRedTFMode_Engineering.description = "RedTF engineering mode"
        self.sysRedTF.addMode(self.mdRedTFMode_Engineering)

        self.mdBlueTFMode_Engineering.id = idcounter
        idcounter += 1
        self.mdBlueTFMode_Engineering.ident = "BlueTFMode_Engineering"
        self.mdBlueTFMode_Engineering.description = "BlueTF engineering mode"
        self.sysBlueTF.addMode(self.mdBlueTFMode_Engineering)

        self.mdDetectorMode_Engineering.id = idcounter
        idcounter += 1
        self.mdDetectorMode_Engineering.ident = "DetectorMode_Engineering"
        self.mdDetectorMode_Engineering.description = "Detector engineering mode"
        self.sysDetector.addMode(self.mdDetectorMode_Engineering)

        self.mdOutputSourceMode_Engineering.id = idcounter
        idcounter += 1
        self.mdOutputSourceMode_Engineering.ident = "OutputSourceMode_Engineering"
        self.mdOutputSourceMode_Engineering.description = "OutputSource engineering mode"
        self.sysOutputSource.addMode(self.mdOutputSourceMode_Engineering)

        self.mdWindowMode_Engineering.id = idcounter
        idcounter += 1
        self.mdWindowMode_Engineering.ident = "WindowMode_Engineering"
        self.mdWindowMode_Engineering.description = "Window engineering mode"
        self.sysWindow.addMode(self.mdWindowMode_Engineering)
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
        # Marcamos RecompositionMode_QuadCCD como elegible para OutputSourceMode_TWO
        self.mdOutputSourceMode_TWO.addSubMode(self.mdRecompositionMode_QuadCCD)
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
        return self.prShuffleLines.selectedValue

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
        return self.prShuffleLines.selectedValue.getData()

    def set_ShuffleLinesDouble(self, data: float)-> float :
        return self.prShuffleLines.selectedValue.setData(data)


    ## prParam ShiftNumber 

    # ShiftNumber
    def get_ShiftNumber(self)-> PORISValue :
        return self.prShiftNumber.selectedValue

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
        return self.prShiftNumber.selectedValue.getData()

    def set_ShiftNumberDouble(self, data: float)-> float :
        return self.prShiftNumber.selectedValue.setData(data)


    ## prParam ExpTime 

    # ExpTime
    def get_ExpTime(self)-> PORISValue :
        return self.prExpTime.selectedValue

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
        return self.prExpTime.selectedValue.getData()

    def set_ExpTimeDouble(self, data: float)-> float :
        return self.prExpTime.selectedValue.setData(data)


    ## prParam Acquisition 

    # ExpTimeDouble  
    def get_ExpTimeDouble(self)-> float :
        v = self.prExpTime.selectedValue
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ExpTimeDouble(self, data: float)-> float :
        return self.prExpTime.selectedValue.setData(data)


    ## MultipleExposureMode 
    def get_MultipleExposureMode(self)-> PORISMode:
        return self.sysMultipleExposure.getSelectedMode()

    def set_MultipleExposureMode(self, mode: PORISMode)-> PORISMode :
        return self.sysMultipleExposure.selectMode(mode)


    ## prParam numOfFrames 

    # numOfFrames
    def get_numOfFrames(self)-> PORISValue :
        return self.prnumOfFrames.selectedValue

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
        return self.prnumOfFrames.selectedValue.getData()

    def set_numOfFramesDouble(self, data: float)-> float :
        return self.prnumOfFrames.selectedValue.setData(data)


    ## prParam PixelSpeed 

    # PixelSpeed
    def get_PixelSpeed(self)-> PORISValue :
        return self.prPixelSpeed.selectedValue

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
        return self.prCalibGain.selectedValue

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
        return self.prCalibGain.selectedValue.getData()

    def set_CalibGainDouble(self, data: float)-> float :
        return self.prCalibGain.selectedValue.setData(data)


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
        return self.prCurrentEllapsed.selectedValue

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
        return self.prCurrentEllapsed.selectedValue.getData()

    def set_CurrentEllapsedDouble(self, data: float)-> float :
        return self.prCurrentEllapsed.selectedValue.setData(data)


    ## prParam CurrentImg 

    # CurrentImg
    def get_CurrentImg(self)-> PORISValue :
        return self.prCurrentImg.selectedValue

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
        return self.prCurrentImg.selectedValue.getData()

    def set_CurrentImgDouble(self, data: float)-> float :
        return self.prCurrentImg.selectedValue.setData(data)


    ## prParam CurrentPct 

    # CurrentPct
    def get_CurrentPct(self)-> PORISValue :
        return self.prCurrentPct.selectedValue

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
        return self.prCurrentPct.selectedValue.getData()

    def set_CurrentPctDouble(self, data: float)-> float :
        return self.prCurrentPct.selectedValue.setData(data)


    ## prParam OverallPct 

    # OverallPct
    def get_OverallPct(self)-> PORISValue :
        return self.prOverallPct.selectedValue

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
        return self.prOverallPct.selectedValue.getData()

    def set_OverallPctDouble(self, data: float)-> float :
        return self.prOverallPct.selectedValue.setData(data)


    ## FPEMode 
    def get_FPEMode(self)-> PORISMode:
        return self.sysFPE.getSelectedMode()

    def set_FPEMode(self, mode: PORISMode)-> PORISMode :
        return self.sysFPE.selectMode(mode)


    ## prParam FocalPlaneElement 

    # FocalPlaneElement
    def get_FocalPlaneElement(self)-> PORISValue :
        return self.prFocalPlaneElement.selectedValue

    def set_FocalPlaneElement(self, value: PORISValue)-> PORISValue :
        return self.prFocalPlaneElement.setValue(value)


    ## FocalPlaneElementMode 
    def get_FocalPlaneElementMode(self)-> PORISMode:
        return self.prFocalPlaneElement.getSelectedMode()

    def set_FocalPlaneElementMode(self, mode: PORISMode)-> PORISMode :
        return self.prFocalPlaneElement.selectMode(mode)


    ## PreOpticsMode 
    def get_PreOpticsMode(self)-> PORISMode:
        return self.sysPreOptics.getSelectedMode()

    def set_PreOpticsMode(self, mode: PORISMode)-> PORISMode :
        return self.sysPreOptics.selectMode(mode)


    ## prParam Grisms 

    # Grisms
    def get_Grisms(self)-> PORISValue :
        return self.prGrisms.selectedValue

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
        return self.prRedFWHM.selectedValue

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
        return self.prRedFWHM.selectedValue.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.selectedValue.setData(data)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        return self.prRedFWHM.selectedValue.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.selectedValue.setData(data)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        return self.prRedFWHM.selectedValue.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.selectedValue.setData(data)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        return self.prRedFWHM.selectedValue.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.selectedValue.setData(data)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        return self.prRedFWHM.selectedValue.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.selectedValue.setData(data)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        return self.prRedFWHM.selectedValue.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.selectedValue.setData(data)


    ## prParam RedLamda 

    # RedLamda
    def get_RedLamda(self)-> PORISValue :
        return self.prRedLamda.selectedValue

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
        return self.prRedLamda.selectedValue.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.selectedValue.setData(data)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        return self.prRedLamda.selectedValue.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.selectedValue.setData(data)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        return self.prRedLamda.selectedValue.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.selectedValue.setData(data)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        return self.prRedLamda.selectedValue.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.selectedValue.setData(data)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        return self.prRedLamda.selectedValue.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.selectedValue.setData(data)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        return self.prRedLamda.selectedValue.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.selectedValue.setData(data)


    ## BlueTFMode 
    def get_BlueTFMode(self)-> PORISMode:
        return self.sysBlueTF.getSelectedMode()

    def set_BlueTFMode(self, mode: PORISMode)-> PORISMode :
        return self.sysBlueTF.selectMode(mode)


    ## prParam BlueFWHM 

    # BlueFWHM
    def get_BlueFWHM(self)-> PORISValue :
        return self.prBlueFWHM.selectedValue

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
        return self.prBlueLamda.selectedValue

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
        return self.prBlueLamda.selectedValue.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.selectedValue.setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        return self.prBlueLamda.selectedValue.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.selectedValue.setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        return self.prBlueLamda.selectedValue.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.selectedValue.setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        return self.prBlueLamda.selectedValue.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.selectedValue.setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        return self.prBlueLamda.selectedValue.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.selectedValue.setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        return self.prBlueLamda.selectedValue.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.selectedValue.setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        return self.prBlueLamda.selectedValue.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.selectedValue.setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        return self.prBlueLamda.selectedValue.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.selectedValue.setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        return self.prBlueLamda.selectedValue.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.selectedValue.setData(data)


    ## prParam zzero 

    # zzero
    def get_zzero(self)-> PORISValue :
        return self.przzero.selectedValue

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
        return self.przzero.selectedValue.getData()

    def set_zzeroDouble(self, data: float)-> float :
        return self.przzero.selectedValue.setData(data)


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
        return self.prBinning.selectedValue

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
        return self.prRows.selectedValue

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
        return self.prRows.selectedValue.getData()

    def set_RowsDouble(self, data: float)-> float :
        return self.prRows.selectedValue.setData(data)


    ## prParam Cols 

    # Cols
    def get_Cols(self)-> PORISValue :
        return self.prCols.selectedValue

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
        return self.prCols.selectedValue.getData()

    def set_ColsDouble(self, data: float)-> float :
        return self.prCols.selectedValue.setData(data)


    ## prParam offsetRow 

    # offsetRow
    def get_offsetRow(self)-> PORISValue :
        return self.proffsetRow.selectedValue

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
        return self.proffsetRow.selectedValue.getData()

    def set_offsetRowDouble(self, data: float)-> float :
        return self.proffsetRow.selectedValue.setData(data)


    ## prParam offsetCol 

    # offsetCol
    def get_offsetCol(self)-> PORISValue :
        return self.proffsetCol.selectedValue

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
        return self.proffsetCol.selectedValue.getData()

    def set_offsetColDouble(self, data: float)-> float :
        return self.proffsetCol.selectedValue.setData(data)


    ## FiltersMode 
    def get_FiltersMode(self)-> PORISMode:
        return self.sysFilters.getSelectedMode()

    def set_FiltersMode(self, mode: PORISMode)-> PORISMode :
        return self.sysFilters.selectMode(mode)


    ## prParam UFilters 

    # UFilters
    def get_UFilters(self)-> PORISValue :
        return self.prUFilters.selectedValue

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
        return self.prOS.selectedValue

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
        return self.prBroad.selectedValue

    def set_Broad(self, value: PORISValue)-> PORISValue :
        return self.prBroad.setValue(value)


    ## BroadMode 
    def get_BroadMode(self)-> PORISMode:
        return self.prBroad.getSelectedMode()

    def set_BroadMode(self, mode: PORISMode)-> PORISMode :
        return self.prBroad.selectMode(mode)


    ## Action trigger DAS_acquire ##
    def execDAS_acquire(self, value: bool) -> bool:
        # Override this
        return True


    ## Action trigger DAS_abort ##
    def execDAS_abort(self, value: bool) -> bool:
        # Override this
        return True

