from PORIS import *

class examplePORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysInstrument = PORISSys("Instrument")
        self.mdInstrumentMode_UNKNOWN = PORISMode("InstrumentMode_UNKNOWN")
        self.setRoot(self.sysInstrument)
        self.prMasks = PORISParam("Masks")
        self.mdMasksMode_UNKNOWN = PORISMode("MasksMode_UNKNOWN")
        self.vlMasks_UNKNOWN = PORISValue("Masks_UNKNOWN")
        self.prDispersion = PORISParam("Dispersion")
        self.mdDispersionMode_UNKNOWN = PORISMode("DispersionMode_UNKNOWN")
        self.vlDispersion_UNKNOWN = PORISValue("Dispersion_UNKNOWN")
        self.sysDetector = PORISSys("Detector")
        self.mdDetectorMode_UNKNOWN = PORISMode("DetectorMode_UNKNOWN")
        self.prexpTime = PORISParam("expTime")
        self.mdexpTimeMode_UNKNOWN = PORISMode("expTimeMode_UNKNOWN")
        self.vlexpTime_UNKNOWN = PORISValue("expTime_UNKNOWN")
        self.prBinning = PORISParam("Binning")
        self.mdBinningMode_UNKNOWN = PORISMode("BinningMode_UNKNOWN")
        self.vlBinning_UNKNOWN = PORISValue("Binning_UNKNOWN")
        self.sysFilter = PORISSys("Filter")
        self.mdFilterMode_UNKNOWN = PORISMode("FilterMode_UNKNOWN")
        self.prClassicFilters = PORISParam("ClassicFilters")
        self.mdClassicFiltersMode_UNKNOWN = PORISMode("ClassicFiltersMode_UNKNOWN")
        self.vlClassicFilters_UNKNOWN = PORISValue("ClassicFilters_UNKNOWN")
        self.vlMasks_0_6 = PORISValue("Masks_0_6")
        self.vlMasks_1_0 = PORISValue("Masks_1_0")
        self.vlMasks_2_0 = PORISValue("Masks_2_0")
        self.mdMasksMode_Spectroscopy = PORISMode("MasksMode_Spectroscopy")
        self.vlMasks_Half_field = PORISValue("Masks_Half_field")
        self.mdMasksMode_FastImg = PORISMode("MasksMode_FastImg")
        self.vlDispersion_R500 = PORISValue("Dispersion_R500")
        self.vlDispersion_R1000 = PORISValue("Dispersion_R1000")
        self.vlDispersion_R2000 = PORISValue("Dispersion_R2000")
        self.mdDispersionMode_Normal = PORISMode("DispersionMode_Normal")
        self.vlexpTime_NormalRange = PORISValueFloat("expTime_NormalRange",0,1,3600)
        self.mdexpTimeMode_Normal = PORISMode("expTimeMode_Normal")
        self.mdexpTimeMode_Fast = PORISMode("expTimeMode_Fast")
        self.vlexpTime_FastRange = PORISValueFloat("expTime_FastRange",0,0.01,0.5)
        self.vlBinning_1x1 = PORISValue("Binning_1x1")
        self.vlBinning_2x1 = PORISValue("Binning_2x1")
        self.vlBinning_1x2 = PORISValue("Binning_1x2")
        self.vlBinning_2x2 = PORISValue("Binning_2x2")
        self.mdBinningMode_Normal = PORISMode("BinningMode_Normal")
        self.mdBinningMode_Square = PORISMode("BinningMode_Square")
        self.mdDetectorMode_Normal = PORISMode("DetectorMode_Normal")
        self.mdDetectorMode_Image = PORISMode("DetectorMode_Image")
        self.mdDetectorMode_FastImage = PORISMode("DetectorMode_FastImage")
        self.mdInstrumentMode_Photometry = PORISMode("InstrumentMode_Photometry")
        self.mdInstrumentMode_Spectroscopy = PORISMode("InstrumentMode_Spectroscopy")
        self.mdInstrumentMode_FastPhotometry = PORISMode("InstrumentMode_FastPhotometry")
        self.mdFilterMode_Classic = PORISMode("FilterMode_Classic")
        self.mdFilterMode_TFBlue = PORISMode("FilterMode_TFBlue")
        self.mdFilterMode_TFRed = PORISMode("FilterMode_TFRed")
        self.vlClassicFilters_Red = PORISValue("ClassicFilters_Red")
        self.vlClassicFilters_Blue = PORISValue("ClassicFilters_Blue")
        self.mdClassicFiltersMode_Standard = PORISMode("ClassicFiltersMode_Standard")
        self.mdClassicFiltersMode_Blue = PORISMode("ClassicFiltersMode_Blue")
        self.mdClassicFiltersMode_Red = PORISMode("ClassicFiltersMode_Red")
        self.vlClassicFilters_userFilter = PORISValueString("ClassicFilters_userFilter",'mycustomfilter')
        self.mdClassicFiltersMode_User = PORISMode("ClassicFiltersMode_User")
        self.mdInstrumentMode_Engineering = PORISMode("InstrumentMode_Engineering")
        self.mdDetectorMode_Engineering = PORISMode("DetectorMode_Engineering")
        self.mdFilterMode_Engineering = PORISMode("FilterMode_Engineering")
        self.addItem(self.sysInstrument)
        self.sysInstrument.ident = "EX-1862"
        self.sysInstrument.description = ""
        self.addItem(self.mdInstrumentMode_UNKNOWN)
        self.mdInstrumentMode_UNKNOWN.ident = "InstrumentMode_UNKNOWN"
        self.mdInstrumentMode_UNKNOWN.description = ""
        self.sysInstrument.addMode(self.mdInstrumentMode_UNKNOWN)
        self.addItem(self.prMasks)
        self.prMasks.ident = "EX-1863"
        self.prMasks.description = ""
        self.sysInstrument.addParam(self.prMasks)
        self.addItem(self.vlMasks_UNKNOWN)
        self.vlMasks_UNKNOWN.ident = "Masks_UNKNOWN"
        self.vlMasks_UNKNOWN.description = "Unknown value for Masks"
        self.prMasks.addValue(self.vlMasks_UNKNOWN)
        self.addItem(self.mdMasksMode_UNKNOWN)
        self.mdMasksMode_UNKNOWN.ident = "MasksMode_UNKNOWN"
        self.mdMasksMode_UNKNOWN.description = "Unknown mode for Masks"
        self.prMasks.addMode(self.mdMasksMode_UNKNOWN)
        self.mdMasksMode_UNKNOWN.addValue(self.vlMasks_UNKNOWN)
        self.mdInstrumentMode_UNKNOWN.addSubMode(self.mdMasksMode_UNKNOWN)
        self.addItem(self.prDispersion)
        self.prDispersion.ident = "EX-1864"
        self.prDispersion.description = ""
        self.sysInstrument.addParam(self.prDispersion)
        self.addItem(self.vlDispersion_UNKNOWN)
        self.vlDispersion_UNKNOWN.ident = "Dispersion_UNKNOWN"
        self.vlDispersion_UNKNOWN.description = "Unknown value for Dispersion"
        self.prDispersion.addValue(self.vlDispersion_UNKNOWN)
        self.addItem(self.mdDispersionMode_UNKNOWN)
        self.mdDispersionMode_UNKNOWN.ident = "DispersionMode_UNKNOWN"
        self.mdDispersionMode_UNKNOWN.description = "Unknown mode for Dispersion"
        self.prDispersion.addMode(self.mdDispersionMode_UNKNOWN)
        self.mdDispersionMode_UNKNOWN.addValue(self.vlDispersion_UNKNOWN)
        self.mdInstrumentMode_UNKNOWN.addSubMode(self.mdDispersionMode_UNKNOWN)
        self.addItem(self.sysDetector)
        self.sysDetector.ident = "EX-1865"
        self.sysDetector.description = ""
        self.sysInstrument.addSubsystem(self.sysDetector)
        self.addItem(self.mdDetectorMode_UNKNOWN)
        self.mdDetectorMode_UNKNOWN.ident = "DetectorMode_UNKNOWN"
        self.mdDetectorMode_UNKNOWN.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_UNKNOWN)
        self.addItem(self.prexpTime)
        self.prexpTime.ident = "EX-1866"
        self.prexpTime.description = ""
        self.sysDetector.addParam(self.prexpTime)
        self.addItem(self.vlexpTime_UNKNOWN)
        self.vlexpTime_UNKNOWN.ident = "expTime_UNKNOWN"
        self.vlexpTime_UNKNOWN.description = "Unknown value for expTime"
        self.prexpTime.addValue(self.vlexpTime_UNKNOWN)
        self.addItem(self.mdexpTimeMode_UNKNOWN)
        self.mdexpTimeMode_UNKNOWN.ident = "expTimeMode_UNKNOWN"
        self.mdexpTimeMode_UNKNOWN.description = "Unknown mode for expTime"
        self.prexpTime.addMode(self.mdexpTimeMode_UNKNOWN)
        self.mdexpTimeMode_UNKNOWN.addValue(self.vlexpTime_UNKNOWN)
        self.mdDetectorMode_UNKNOWN.addSubMode(self.mdexpTimeMode_UNKNOWN)
        self.addItem(self.prBinning)
        self.prBinning.ident = "EX-1867"
        self.prBinning.description = ""
        self.sysDetector.addParam(self.prBinning)
        self.addItem(self.vlBinning_UNKNOWN)
        self.vlBinning_UNKNOWN.ident = "Binning_UNKNOWN"
        self.vlBinning_UNKNOWN.description = "Unknown value for Binning"
        self.prBinning.addValue(self.vlBinning_UNKNOWN)
        self.addItem(self.mdBinningMode_UNKNOWN)
        self.mdBinningMode_UNKNOWN.ident = "BinningMode_UNKNOWN"
        self.mdBinningMode_UNKNOWN.description = "Unknown mode for Binning"
        self.prBinning.addMode(self.mdBinningMode_UNKNOWN)
        self.mdBinningMode_UNKNOWN.addValue(self.vlBinning_UNKNOWN)
        self.mdDetectorMode_UNKNOWN.addSubMode(self.mdBinningMode_UNKNOWN)
        self.addItem(self.sysFilter)
        self.sysFilter.ident = "EX-1868"
        self.sysFilter.description = ""
        self.sysInstrument.addSubsystem(self.sysFilter)
        self.addItem(self.mdFilterMode_UNKNOWN)
        self.mdFilterMode_UNKNOWN.ident = "FilterMode_UNKNOWN"
        self.mdFilterMode_UNKNOWN.description = ""
        self.sysFilter.addMode(self.mdFilterMode_UNKNOWN)
        self.addItem(self.prClassicFilters)
        self.prClassicFilters.ident = "EX-1869"
        self.prClassicFilters.description = ""
        self.sysFilter.addParam(self.prClassicFilters)
        self.addItem(self.vlClassicFilters_UNKNOWN)
        self.vlClassicFilters_UNKNOWN.ident = "ClassicFilters_UNKNOWN"
        self.vlClassicFilters_UNKNOWN.description = "Unknown value for ClassicFilters"
        self.prClassicFilters.addValue(self.vlClassicFilters_UNKNOWN)
        self.addItem(self.mdClassicFiltersMode_UNKNOWN)
        self.mdClassicFiltersMode_UNKNOWN.ident = "ClassicFiltersMode_UNKNOWN"
        self.mdClassicFiltersMode_UNKNOWN.description = "Unknown mode for ClassicFilters"
        self.prClassicFilters.addMode(self.mdClassicFiltersMode_UNKNOWN)
        self.mdClassicFiltersMode_UNKNOWN.addValue(self.vlClassicFilters_UNKNOWN)
        self.mdFilterMode_UNKNOWN.addSubMode(self.mdClassicFiltersMode_UNKNOWN)
        self.addItem(self.vlMasks_0_6)
        self.vlMasks_0_6.ident = "EX-1826"
        self.vlMasks_0_6.description = ""
        self.prMasks.addValue(self.vlMasks_0_6)
        self.addItem(self.vlMasks_1_0)
        self.vlMasks_1_0.ident = "EX-1827"
        self.vlMasks_1_0.description = ""
        self.prMasks.addValue(self.vlMasks_1_0)
        self.addItem(self.vlMasks_2_0)
        self.vlMasks_2_0.ident = "EX-1828"
        self.vlMasks_2_0.description = ""
        self.prMasks.addValue(self.vlMasks_2_0)
        self.addItem(self.mdMasksMode_Spectroscopy)
        self.mdMasksMode_Spectroscopy.ident = "EX-1829"
        self.mdMasksMode_Spectroscopy.description = ""
        self.prMasks.addMode(self.mdMasksMode_Spectroscopy)
        self.addItem(self.vlMasks_Half_field)
        self.vlMasks_Half_field.ident = "EX-1830"
        self.vlMasks_Half_field.description = ""
        self.prMasks.addValue(self.vlMasks_Half_field)
        self.addItem(self.mdMasksMode_FastImg)
        self.mdMasksMode_FastImg.ident = "EX-1831"
        self.mdMasksMode_FastImg.description = ""
        self.prMasks.addMode(self.mdMasksMode_FastImg)
        self.addItem(self.vlDispersion_R500)
        self.vlDispersion_R500.ident = "EX-1832"
        self.vlDispersion_R500.description = ""
        self.prDispersion.addValue(self.vlDispersion_R500)
        self.addItem(self.vlDispersion_R1000)
        self.vlDispersion_R1000.ident = "EX-1833"
        self.vlDispersion_R1000.description = ""
        self.prDispersion.addValue(self.vlDispersion_R1000)
        self.addItem(self.vlDispersion_R2000)
        self.vlDispersion_R2000.ident = "EX-1834"
        self.vlDispersion_R2000.description = ""
        self.prDispersion.addValue(self.vlDispersion_R2000)
        self.addItem(self.mdDispersionMode_Normal)
        self.mdDispersionMode_Normal.ident = "EX-1835"
        self.mdDispersionMode_Normal.description = ""
        self.prDispersion.addMode(self.mdDispersionMode_Normal)
        self.addItem(self.vlexpTime_NormalRange)
        self.vlexpTime_NormalRange.ident = "EX-1836"
        self.vlexpTime_NormalRange.description = ""
        self.prexpTime.addValue(self.vlexpTime_NormalRange)
        self.addItem(self.mdexpTimeMode_Normal)
        self.mdexpTimeMode_Normal.ident = "EX-1837"
        self.mdexpTimeMode_Normal.description = ""
        self.prexpTime.addMode(self.mdexpTimeMode_Normal)
        self.addItem(self.mdexpTimeMode_Fast)
        self.mdexpTimeMode_Fast.ident = "EX-1838"
        self.mdexpTimeMode_Fast.description = ""
        self.prexpTime.addMode(self.mdexpTimeMode_Fast)
        self.addItem(self.vlexpTime_FastRange)
        self.vlexpTime_FastRange.ident = "EX-1839"
        self.vlexpTime_FastRange.description = ""
        self.prexpTime.addValue(self.vlexpTime_FastRange)
        self.addItem(self.vlBinning_1x1)
        self.vlBinning_1x1.ident = "EX-1840"
        self.vlBinning_1x1.description = ""
        self.prBinning.addValue(self.vlBinning_1x1)
        self.addItem(self.vlBinning_2x1)
        self.vlBinning_2x1.ident = "EX-1841"
        self.vlBinning_2x1.description = ""
        self.prBinning.addValue(self.vlBinning_2x1)
        self.addItem(self.vlBinning_1x2)
        self.vlBinning_1x2.ident = "EX-1842"
        self.vlBinning_1x2.description = ""
        self.prBinning.addValue(self.vlBinning_1x2)
        self.addItem(self.vlBinning_2x2)
        self.vlBinning_2x2.ident = "EX-1843"
        self.vlBinning_2x2.description = ""
        self.prBinning.addValue(self.vlBinning_2x2)
        self.addItem(self.mdBinningMode_Normal)
        self.mdBinningMode_Normal.ident = "EX-1844"
        self.mdBinningMode_Normal.description = ""
        self.prBinning.addMode(self.mdBinningMode_Normal)
        self.addItem(self.mdBinningMode_Square)
        self.mdBinningMode_Square.ident = "EX-1845"
        self.mdBinningMode_Square.description = ""
        self.prBinning.addMode(self.mdBinningMode_Square)
        self.addItem(self.mdDetectorMode_Normal)
        self.mdDetectorMode_Normal.ident = "EX-1846"
        self.mdDetectorMode_Normal.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_Normal)
        self.addItem(self.mdDetectorMode_Image)
        self.mdDetectorMode_Image.ident = "EX-1847"
        self.mdDetectorMode_Image.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_Image)
        self.addItem(self.mdDetectorMode_FastImage)
        self.mdDetectorMode_FastImage.ident = "EX-1848"
        self.mdDetectorMode_FastImage.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_FastImage)
        self.addItem(self.mdInstrumentMode_Photometry)
        self.mdInstrumentMode_Photometry.ident = "EX-1849"
        self.mdInstrumentMode_Photometry.description = ""
        self.sysInstrument.addMode(self.mdInstrumentMode_Photometry)
        self.addItem(self.mdInstrumentMode_Spectroscopy)
        self.mdInstrumentMode_Spectroscopy.ident = "EX-1850"
        self.mdInstrumentMode_Spectroscopy.description = ""
        self.sysInstrument.addMode(self.mdInstrumentMode_Spectroscopy)
        self.addItem(self.mdInstrumentMode_FastPhotometry)
        self.mdInstrumentMode_FastPhotometry.ident = "EX-1851"
        self.mdInstrumentMode_FastPhotometry.description = ""
        self.sysInstrument.addMode(self.mdInstrumentMode_FastPhotometry)
        self.addItem(self.mdFilterMode_Classic)
        self.mdFilterMode_Classic.ident = "EX-1852"
        self.mdFilterMode_Classic.description = ""
        self.sysFilter.addMode(self.mdFilterMode_Classic)
        self.addItem(self.mdFilterMode_TFBlue)
        self.mdFilterMode_TFBlue.ident = "EX-1853"
        self.mdFilterMode_TFBlue.description = ""
        self.sysFilter.addMode(self.mdFilterMode_TFBlue)
        self.addItem(self.mdFilterMode_TFRed)
        self.mdFilterMode_TFRed.ident = "EX-1854"
        self.mdFilterMode_TFRed.description = ""
        self.sysFilter.addMode(self.mdFilterMode_TFRed)
        self.addItem(self.vlClassicFilters_Red)
        self.vlClassicFilters_Red.ident = "EX-1855"
        self.vlClassicFilters_Red.description = ""
        self.prClassicFilters.addValue(self.vlClassicFilters_Red)
        self.addItem(self.vlClassicFilters_Blue)
        self.vlClassicFilters_Blue.ident = "EX-1856"
        self.vlClassicFilters_Blue.description = ""
        self.prClassicFilters.addValue(self.vlClassicFilters_Blue)
        self.addItem(self.mdClassicFiltersMode_Standard)
        self.mdClassicFiltersMode_Standard.ident = "EX-1857"
        self.mdClassicFiltersMode_Standard.description = ""
        self.prClassicFilters.addMode(self.mdClassicFiltersMode_Standard)
        self.addItem(self.mdClassicFiltersMode_Blue)
        self.mdClassicFiltersMode_Blue.ident = "EX-1858"
        self.mdClassicFiltersMode_Blue.description = ""
        self.prClassicFilters.addMode(self.mdClassicFiltersMode_Blue)
        self.addItem(self.mdClassicFiltersMode_Red)
        self.mdClassicFiltersMode_Red.ident = "EX-1859"
        self.mdClassicFiltersMode_Red.description = ""
        self.prClassicFilters.addMode(self.mdClassicFiltersMode_Red)
        self.addItem(self.vlClassicFilters_userFilter)
        self.vlClassicFilters_userFilter.ident = "EX-1860"
        self.vlClassicFilters_userFilter.description = ""
        self.prClassicFilters.addValue(self.vlClassicFilters_userFilter)
        self.addItem(self.mdClassicFiltersMode_User)
        self.mdClassicFiltersMode_User.ident = "EX-1861"
        self.mdClassicFiltersMode_User.description = ""
        self.prClassicFilters.addMode(self.mdClassicFiltersMode_User)
        self.addItem(self.mdInstrumentMode_Engineering)
        self.mdInstrumentMode_Engineering.ident = "ENG-1"
        self.mdInstrumentMode_Engineering.description = "Instrument engineering mode"
        self.sysInstrument.addMode(self.mdInstrumentMode_Engineering)
        self.addItem(self.mdDetectorMode_Engineering)
        self.mdDetectorMode_Engineering.ident = "ENG-2"
        self.mdDetectorMode_Engineering.description = "Detector engineering mode"
        self.sysDetector.addMode(self.mdDetectorMode_Engineering)
        self.addItem(self.mdFilterMode_Engineering)
        self.mdFilterMode_Engineering.ident = "ENG-3"
        self.mdFilterMode_Engineering.description = "Filter engineering mode"
        self.sysFilter.addMode(self.mdFilterMode_Engineering)
        # Marcamos MasksMode_Spectroscopy como elegible para InstrumentMode_Spectroscopy
        self.mdInstrumentMode_Spectroscopy.addSubMode(self.mdMasksMode_Spectroscopy)
        # Marcamos MasksMode_FastImg como elegible para InstrumentMode_FastPhotometry
        self.mdInstrumentMode_FastPhotometry.addSubMode(self.mdMasksMode_FastImg)
        # Marcamos MasksMode_Spectroscopy como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdMasksMode_Spectroscopy)
        # Marcamos MasksMode_FastImg como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdMasksMode_FastImg)
        # Marcamos Masks_0_6 como elegible para MasksMode_Spectroscopy
        self.mdMasksMode_Spectroscopy.addValue(self.vlMasks_0_6)
        # Marcamos Masks_2_0 como elegible para MasksMode_Spectroscopy
        self.mdMasksMode_Spectroscopy.addValue(self.vlMasks_2_0)
        # Marcamos Masks_1_0 como elegible para MasksMode_Spectroscopy
        self.mdMasksMode_Spectroscopy.addValue(self.vlMasks_1_0)
        # Marcamos Masks_Half_field como elegible para MasksMode_FastImg
        self.mdMasksMode_FastImg.addValue(self.vlMasks_Half_field)
        # Marcamos DispersionMode_Normal como elegible para InstrumentMode_Spectroscopy
        self.mdInstrumentMode_Spectroscopy.addSubMode(self.mdDispersionMode_Normal)
        # Marcamos DispersionMode_Normal como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdDispersionMode_Normal)
        # Marcamos Dispersion_R500 como elegible para DispersionMode_Normal
        self.mdDispersionMode_Normal.addValue(self.vlDispersion_R500)
        # Marcamos Dispersion_R1000 como elegible para DispersionMode_Normal
        self.mdDispersionMode_Normal.addValue(self.vlDispersion_R1000)
        # Marcamos Dispersion_R2000 como elegible para DispersionMode_Normal
        self.mdDispersionMode_Normal.addValue(self.vlDispersion_R2000)
        # Marcamos DetectorMode_Image como elegible para InstrumentMode_Photometry
        self.mdInstrumentMode_Photometry.addSubMode(self.mdDetectorMode_Image)
        # Marcamos DetectorMode_Normal como elegible para InstrumentMode_Spectroscopy
        self.mdInstrumentMode_Spectroscopy.addSubMode(self.mdDetectorMode_Normal)
        # Marcamos DetectorMode_FastImage como elegible para InstrumentMode_FastPhotometry
        self.mdInstrumentMode_FastPhotometry.addSubMode(self.mdDetectorMode_FastImage)
        # Marcamos DetectorMode_Normal como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdDetectorMode_Normal)
        # Marcamos DetectorMode_Image como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdDetectorMode_Image)
        # Marcamos DetectorMode_FastImage como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdDetectorMode_FastImage)
        # Marcamos DetectorMode_Engineering como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdDetectorMode_Engineering)
        # Marcamos expTimeMode_Normal como elegible para DetectorMode_Normal
        self.mdDetectorMode_Normal.addSubMode(self.mdexpTimeMode_Normal)
        # Marcamos expTimeMode_Normal como elegible para DetectorMode_Image
        self.mdDetectorMode_Image.addSubMode(self.mdexpTimeMode_Normal)
        # Marcamos expTimeMode_Fast como elegible para DetectorMode_FastImage
        self.mdDetectorMode_FastImage.addSubMode(self.mdexpTimeMode_Fast)
        # Marcamos expTimeMode_Normal como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdexpTimeMode_Normal)
        # Marcamos expTimeMode_Fast como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdexpTimeMode_Fast)
        # Marcamos expTime_NormalRange como elegible para expTimeMode_Normal
        self.mdexpTimeMode_Normal.addValue(self.vlexpTime_NormalRange)
        # Marcamos expTime_FastRange como elegible para expTimeMode_Fast
        self.mdexpTimeMode_Fast.addValue(self.vlexpTime_FastRange)
        # Marcamos BinningMode_Normal como elegible para DetectorMode_Normal
        self.mdDetectorMode_Normal.addSubMode(self.mdBinningMode_Normal)
        # Marcamos BinningMode_Square como elegible para DetectorMode_Image
        self.mdDetectorMode_Image.addSubMode(self.mdBinningMode_Square)
        # Marcamos BinningMode_Square como elegible para DetectorMode_FastImage
        self.mdDetectorMode_FastImage.addSubMode(self.mdBinningMode_Square)
        # Marcamos BinningMode_Normal como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdBinningMode_Normal)
        # Marcamos BinningMode_Square como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdBinningMode_Square)
        # Marcamos Binning_1x1 como elegible para BinningMode_Normal
        self.mdBinningMode_Normal.addValue(self.vlBinning_1x1)
        # Marcamos Binning_2x1 como elegible para BinningMode_Normal
        self.mdBinningMode_Normal.addValue(self.vlBinning_2x1)
        # Marcamos Binning_1x2 como elegible para BinningMode_Normal
        self.mdBinningMode_Normal.addValue(self.vlBinning_1x2)
        # Marcamos Binning_2x2 como elegible para BinningMode_Normal
        self.mdBinningMode_Normal.addValue(self.vlBinning_2x2)
        # Marcamos Binning_1x1 como elegible para BinningMode_Square
        self.mdBinningMode_Square.addValue(self.vlBinning_1x1)
        # Marcamos Binning_2x2 como elegible para BinningMode_Square
        self.mdBinningMode_Square.addValue(self.vlBinning_2x2)
        # Marcamos FilterMode_TFRed como elegible para InstrumentMode_Photometry
        self.mdInstrumentMode_Photometry.addSubMode(self.mdFilterMode_TFRed)
        # Marcamos FilterMode_TFBlue como elegible para InstrumentMode_Photometry
        self.mdInstrumentMode_Photometry.addSubMode(self.mdFilterMode_TFBlue)
        # Marcamos FilterMode_Classic como elegible para InstrumentMode_Photometry
        self.mdInstrumentMode_Photometry.addSubMode(self.mdFilterMode_Classic)
        # Marcamos FilterMode_Classic como elegible para InstrumentMode_Spectroscopy
        self.mdInstrumentMode_Spectroscopy.addSubMode(self.mdFilterMode_Classic)
        # Marcamos FilterMode_TFRed como elegible para InstrumentMode_Spectroscopy
        self.mdInstrumentMode_Spectroscopy.addSubMode(self.mdFilterMode_TFRed)
        # Marcamos FilterMode_TFBlue como elegible para InstrumentMode_Spectroscopy
        self.mdInstrumentMode_Spectroscopy.addSubMode(self.mdFilterMode_TFBlue)
        # Marcamos FilterMode_Classic como elegible para InstrumentMode_FastPhotometry
        self.mdInstrumentMode_FastPhotometry.addSubMode(self.mdFilterMode_Classic)
        # Marcamos FilterMode_Classic como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdFilterMode_Classic)
        # Marcamos FilterMode_TFBlue como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdFilterMode_TFBlue)
        # Marcamos FilterMode_TFRed como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdFilterMode_TFRed)
        # Marcamos FilterMode_Engineering como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdFilterMode_Engineering)
        # Marcamos ClassicFiltersMode_Standard como elegible para FilterMode_Classic
        self.mdFilterMode_Classic.addSubMode(self.mdClassicFiltersMode_Standard)
        # Marcamos ClassicFiltersMode_User como elegible para FilterMode_Classic
        self.mdFilterMode_Classic.addSubMode(self.mdClassicFiltersMode_User)
        # Marcamos ClassicFiltersMode_Blue como elegible para FilterMode_TFBlue
        self.mdFilterMode_TFBlue.addSubMode(self.mdClassicFiltersMode_Blue)
        # Marcamos ClassicFiltersMode_Red como elegible para FilterMode_TFRed
        self.mdFilterMode_TFRed.addSubMode(self.mdClassicFiltersMode_Red)
        # Marcamos ClassicFiltersMode_Standard como elegible para FilterMode_Engineering
        self.mdFilterMode_Engineering.addSubMode(self.mdClassicFiltersMode_Standard)
        # Marcamos ClassicFiltersMode_Blue como elegible para FilterMode_Engineering
        self.mdFilterMode_Engineering.addSubMode(self.mdClassicFiltersMode_Blue)
        # Marcamos ClassicFiltersMode_Red como elegible para FilterMode_Engineering
        self.mdFilterMode_Engineering.addSubMode(self.mdClassicFiltersMode_Red)
        # Marcamos ClassicFiltersMode_User como elegible para FilterMode_Engineering
        self.mdFilterMode_Engineering.addSubMode(self.mdClassicFiltersMode_User)
        # Marcamos ClassicFilters_Red como elegible para ClassicFiltersMode_Standard
        self.mdClassicFiltersMode_Standard.addValue(self.vlClassicFilters_Red)
        # Marcamos ClassicFilters_Blue como elegible para ClassicFiltersMode_Standard
        self.mdClassicFiltersMode_Standard.addValue(self.vlClassicFilters_Blue)
        # Marcamos ClassicFilters_Blue como elegible para ClassicFiltersMode_Blue
        self.mdClassicFiltersMode_Blue.addValue(self.vlClassicFilters_Blue)
        # Marcamos ClassicFilters_Red como elegible para ClassicFiltersMode_Red
        self.mdClassicFiltersMode_Red.addValue(self.vlClassicFilters_Red)
        # Marcamos ClassicFilters_userFilter como elegible para ClassicFiltersMode_User
        self.mdClassicFiltersMode_User.addValue(self.vlClassicFilters_userFilter)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## InstrumentMode 
    def get_InstrumentMode(self)-> PORISMode:
        return self.sysInstrument.getSelectedMode()

    def set_InstrumentMode(self, mode: PORISMode)-> PORISMode :
        return self.sysInstrument.selectMode(mode)


    ## prParam Masks 

    # Masks
    def get_Masks(self)-> PORISValue :
        return self.prMasks.getSelectedValue()

    def set_Masks(self, value: PORISValue)-> PORISValue :
        return self.prMasks.setValue(value)


    ## MasksMode 
    def get_MasksMode(self)-> PORISMode:
        return self.prMasks.getSelectedMode()

    def set_MasksMode(self, mode: PORISMode)-> PORISMode :
        return self.prMasks.selectMode(mode)


    ## prParam Dispersion 

    # Dispersion
    def get_Dispersion(self)-> PORISValue :
        return self.prDispersion.getSelectedValue()

    def set_Dispersion(self, value: PORISValue)-> PORISValue :
        return self.prDispersion.setValue(value)


    ## DispersionMode 
    def get_DispersionMode(self)-> PORISMode:
        return self.prDispersion.getSelectedMode()

    def set_DispersionMode(self, mode: PORISMode)-> PORISMode :
        return self.prDispersion.selectMode(mode)


    ## DetectorMode 
    def get_DetectorMode(self)-> PORISMode:
        return self.sysDetector.getSelectedMode()

    def set_DetectorMode(self, mode: PORISMode)-> PORISMode :
        return self.sysDetector.selectMode(mode)


    ## prParam expTime 

    # expTime
    def get_expTime(self)-> PORISValue :
        return self.prexpTime.getSelectedValue()

    def set_expTime(self, value: PORISValue)-> PORISValue :
        return self.prexpTime.setValue(value)


    ## expTimeMode 
    def get_expTimeMode(self)-> PORISMode:
        return self.prexpTime.getSelectedMode()

    def set_expTimeMode(self, mode: PORISMode)-> PORISMode :
        return self.prexpTime.selectMode(mode)


    ## prParam Detector 

    # expTimeDouble  
    def get_expTimeDouble(self)-> float :
        v = self.prexpTime.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_expTimeDouble(self, data: float)-> float :
        return self.prexpTime.getSelectedValue().setData(data)


    ## prParam Detector 

    # expTimeDouble  
    def get_expTimeDouble(self)-> float :
        v = self.prexpTime.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_expTimeDouble(self, data: float)-> float :
        return self.prexpTime.getSelectedValue().setData(data)


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


    ## FilterMode 
    def get_FilterMode(self)-> PORISMode:
        return self.sysFilter.getSelectedMode()

    def set_FilterMode(self, mode: PORISMode)-> PORISMode :
        return self.sysFilter.selectMode(mode)


    ## prParam ClassicFilters 

    # ClassicFilters
    def get_ClassicFilters(self)-> PORISValue :
        return self.prClassicFilters.getSelectedValue()

    def set_ClassicFilters(self, value: PORISValue)-> PORISValue :
        return self.prClassicFilters.setValue(value)


    ## ClassicFiltersMode 
    def get_ClassicFiltersMode(self)-> PORISMode:
        return self.prClassicFilters.getSelectedMode()

    def set_ClassicFiltersMode(self, mode: PORISMode)-> PORISMode :
        return self.prClassicFilters.selectMode(mode)


    ## prParam Filter 

    # ClassicFiltersString #
    def get_ClassicFiltersString(self)-> str :
        v = self.prClassicFilters.getSelectedValue()
        v.__class__ = PORISValueString
        return v.getData()

    def set_ClassicFiltersString(self, data: str)-> str :
        return self.prClassicFilters.getSelectedValue().setData(data)

