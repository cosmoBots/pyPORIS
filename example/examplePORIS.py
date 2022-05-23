from PORIS import *

class examplePORIS:
	def __init__(self):
		identcounter = 1
		sysInstrument = PORISSys("Instrument")
		self.sysInstrument = sysInstrument
		mdInstrumentMode_UNKNOWN = PORISMode("InstrumentMode_UNKNOWN")
		self.mdInstrumentMode_UNKNOWN = mdInstrumentMode_UNKNOWN
		self.root = sysInstrument
		prMasks = PORISParam("Masks")
		mdMasksMode_UNKNOWN = PORISMode("MasksMode_UNKNOWN")
		vlMasks_UNKNOWN = PORISValue("Masks_UNKNOWN")
		prDispersion = PORISParam("Dispersion")
		mdDispersionMode_UNKNOWN = PORISMode("DispersionMode_UNKNOWN")
		vlDispersion_UNKNOWN = PORISValue("Dispersion_UNKNOWN")
		sysDetector = PORISSys("Detector")
		self.sysDetector = sysDetector
		mdDetectorMode_UNKNOWN = PORISMode("DetectorMode_UNKNOWN")
		self.mdDetectorMode_UNKNOWN = mdDetectorMode_UNKNOWN
		prexpTime = PORISParam("expTime")
		mdexpTimeMode_UNKNOWN = PORISMode("expTimeMode_UNKNOWN")
		vlexpTime_UNKNOWN = PORISValue("expTime_UNKNOWN")
		prBinning = PORISParam("Binning")
		mdBinningMode_UNKNOWN = PORISMode("BinningMode_UNKNOWN")
		vlBinning_UNKNOWN = PORISValue("Binning_UNKNOWN")
		sysFilter = PORISSys("Filter")
		self.sysFilter = sysFilter
		mdFilterMode_UNKNOWN = PORISMode("FilterMode_UNKNOWN")
		self.mdFilterMode_UNKNOWN = mdFilterMode_UNKNOWN
		prClassicFilters = PORISParam("ClassicFilters")
		mdClassicFiltersMode_UNKNOWN = PORISMode("ClassicFiltersMode_UNKNOWN")
		vlClassicFilters_UNKNOWN = PORISValue("ClassicFilters_UNKNOWN")
		vlMasks_0_6 = PORISValue("Masks_0_6")
		self.vlMasks_0_6 = vlMasks_0_6
		vlMasks_1_0 = PORISValue("Masks_1_0")
		self.vlMasks_1_0 = vlMasks_1_0
		vlMasks_2_0 = PORISValue("Masks_2_0")
		self.vlMasks_2_0 = vlMasks_2_0
		mdMasksMode_Spectroscopy = PORISMode("MasksMode_Spectroscopy")
		self.mdMasksMode_Spectroscopy = mdMasksMode_Spectroscopy
		vlMasks_Half_field = PORISValue("Masks_Half_field")
		self.vlMasks_Half_field = vlMasks_Half_field
		mdMasksMode_FastImg = PORISMode("MasksMode_FastImg")
		self.mdMasksMode_FastImg = mdMasksMode_FastImg
		vlDispersion_R500 = PORISValue("Dispersion_R500")
		self.vlDispersion_R500 = vlDispersion_R500
		vlDispersion_R1000 = PORISValue("Dispersion_R1000")
		self.vlDispersion_R1000 = vlDispersion_R1000
		vlDispersion_R2000 = PORISValue("Dispersion_R2000")
		self.vlDispersion_R2000 = vlDispersion_R2000
		mdDispersionMode_Normal = PORISMode("DispersionMode_Normal")
		self.mdDispersionMode_Normal = mdDispersionMode_Normal
		vlexpTime_NormalRange = PORISValueFloat("expTime_NormalRange")
		self.vlexpTime_NormalRange = vlexpTime_NormalRange
		mdexpTimeMode_Normal = PORISMode("expTimeMode_Normal")
		self.mdexpTimeMode_Normal = mdexpTimeMode_Normal
		mdexpTimeMode_Fast = PORISMode("expTimeMode_Fast")
		self.mdexpTimeMode_Fast = mdexpTimeMode_Fast
		vlexpTime_FastRange = PORISValueFloat("expTime_FastRange")
		self.vlexpTime_FastRange = vlexpTime_FastRange
		vlBinning_1x1 = PORISValue("Binning_1x1")
		self.vlBinning_1x1 = vlBinning_1x1
		vlBinning_2x1 = PORISValue("Binning_2x1")
		self.vlBinning_2x1 = vlBinning_2x1
		vlBinning_1x2 = PORISValue("Binning_1x2")
		self.vlBinning_1x2 = vlBinning_1x2
		vlBinning_2x2 = PORISValue("Binning_2x2")
		self.vlBinning_2x2 = vlBinning_2x2
		mdBinningMode_Normal = PORISMode("BinningMode_Normal")
		self.mdBinningMode_Normal = mdBinningMode_Normal
		mdBinningMode_Square = PORISMode("BinningMode_Square")
		self.mdBinningMode_Square = mdBinningMode_Square
		mdDetectorMode_Normal = PORISMode("DetectorMode_Normal")
		self.mdDetectorMode_Normal = mdDetectorMode_Normal
		mdDetectorMode_Image = PORISMode("DetectorMode_Image")
		self.mdDetectorMode_Image = mdDetectorMode_Image
		mdDetectorMode_FastImage = PORISMode("DetectorMode_FastImage")
		self.mdDetectorMode_FastImage = mdDetectorMode_FastImage
		mdInstrumentMode_Photometry = PORISMode("InstrumentMode_Photometry")
		self.mdInstrumentMode_Photometry = mdInstrumentMode_Photometry
		mdInstrumentMode_Spectroscopy = PORISMode("InstrumentMode_Spectroscopy")
		self.mdInstrumentMode_Spectroscopy = mdInstrumentMode_Spectroscopy
		mdInstrumentMode_FastPhotometry = PORISMode("InstrumentMode_FastPhotometry")
		self.mdInstrumentMode_FastPhotometry = mdInstrumentMode_FastPhotometry
		mdFilterMode_Classic = PORISMode("FilterMode_Classic")
		self.mdFilterMode_Classic = mdFilterMode_Classic
		mdFilterMode_TFBlue = PORISMode("FilterMode_TFBlue")
		self.mdFilterMode_TFBlue = mdFilterMode_TFBlue
		mdFilterMode_TFRed = PORISMode("FilterMode_TFRed")
		self.mdFilterMode_TFRed = mdFilterMode_TFRed
		vlClassicFilters_Red = PORISValue("ClassicFilters_Red")
		self.vlClassicFilters_Red = vlClassicFilters_Red
		vlClassicFilters_Blue = PORISValue("ClassicFilters_Blue")
		self.vlClassicFilters_Blue = vlClassicFilters_Blue
		mdClassicFiltersMode_Standard = PORISMode("ClassicFiltersMode_Standard")
		self.mdClassicFiltersMode_Standard = mdClassicFiltersMode_Standard
		mdClassicFiltersMode_Blue = PORISMode("ClassicFiltersMode_Blue")
		self.mdClassicFiltersMode_Blue = mdClassicFiltersMode_Blue
		mdClassicFiltersMode_Red = PORISMode("ClassicFiltersMode_Red")
		self.mdClassicFiltersMode_Red = mdClassicFiltersMode_Red
		vlClassicFilters_userFilter = PORISValueText("ClassicFilters_userFilter")
		self.vlClassicFilters_userFilter = vlClassicFilters_userFilter
		mdClassicFiltersMode_User = PORISMode("ClassicFiltersMode_User")
		self.mdClassicFiltersMode_User = mdClassicFiltersMode_User
		mdInstrumentMode_Engineering = PORISMode("InstrumentMode_Engineering")
		self.mdInstrumentMode_Engineering = mdInstrumentMode_Engineering
		mdDetectorMode_Engineering = PORISMode("DetectorMode_Engineering")
		self.mdDetectorMode_Engineering = mdDetectorMode_Engineering
		mdFilterMode_Engineering = PORISMode("FilterMode_Engineering")
		self.mdFilterMode_Engineering = mdFilterMode_Engineering

		sysInstrument.id = identcounter
		identcounter += 1
		sysInstrument.ident = "Instrument"
		sysInstrument.description = ""

		mdInstrumentMode_UNKNOWN.id = identcounter
		identcounter += 1
		mdInstrumentMode_UNKNOWN.ident = "InstrumentMode_UNKNOWN";
		mdInstrumentMode_UNKNOWN.description = "";
		sysInstrument.addMode(mdInstrumentMode_UNKNOWN);

		prMasks.id = identcounter
		identcounter += 1
		prMasks.ident = "Masks"
		prMasks.description = ""
		sysInstrument.addParam(prMasks)
		vlMasks_UNKNOWN.id = identcounter
		identcounter += 1
		vlMasks_UNKNOWN.ident = "Masks_UNKNOWN"
		vlMasks_UNKNOWN.description = "Unknown value for Masks"
		prMasks.addValue(vlMasks_UNKNOWN)

		mdMasksMode_UNKNOWN.id = identcounter
		identcounter += 1
		mdMasksMode_UNKNOWN.ident = "MasksMode_UNKNOWN"
		mdMasksMode_UNKNOWN.description = "Unknown mode for Masks"
		prMasks.addMode(mdMasksMode_UNKNOWN)
		mdMasksMode_UNKNOWN.addValue(vlMasks_UNKNOWN)
		mdInstrumentMode_UNKNOWN.addSubMode(mdMasksMode_UNKNOWN)

		prDispersion.id = identcounter
		identcounter += 1
		prDispersion.ident = "Dispersion"
		prDispersion.description = ""
		sysInstrument.addParam(prDispersion)
		vlDispersion_UNKNOWN.id = identcounter
		identcounter += 1
		vlDispersion_UNKNOWN.ident = "Dispersion_UNKNOWN"
		vlDispersion_UNKNOWN.description = "Unknown value for Dispersion"
		prDispersion.addValue(vlDispersion_UNKNOWN)

		mdDispersionMode_UNKNOWN.id = identcounter
		identcounter += 1
		mdDispersionMode_UNKNOWN.ident = "DispersionMode_UNKNOWN"
		mdDispersionMode_UNKNOWN.description = "Unknown mode for Dispersion"
		prDispersion.addMode(mdDispersionMode_UNKNOWN)
		mdDispersionMode_UNKNOWN.addValue(vlDispersion_UNKNOWN)
		mdInstrumentMode_UNKNOWN.addSubMode(mdDispersionMode_UNKNOWN)

		sysDetector.id = identcounter
		identcounter += 1
		sysDetector.ident = "Detector"
		sysDetector.description = ""
		sysInstrument.addSubsystem(sysDetector);

		mdDetectorMode_UNKNOWN.id = identcounter
		identcounter += 1
		mdDetectorMode_UNKNOWN.ident = "DetectorMode_UNKNOWN";
		mdDetectorMode_UNKNOWN.description = "";
		sysDetector.addMode(mdDetectorMode_UNKNOWN);

		prexpTime.id = identcounter
		identcounter += 1
		prexpTime.ident = "expTime"
		prexpTime.description = ""
		sysDetector.addParam(prexpTime)
		vlexpTime_UNKNOWN.id = identcounter
		identcounter += 1
		vlexpTime_UNKNOWN.ident = "expTime_UNKNOWN"
		vlexpTime_UNKNOWN.description = "Unknown value for expTime"
		prexpTime.addValue(vlexpTime_UNKNOWN)

		mdexpTimeMode_UNKNOWN.id = identcounter
		identcounter += 1
		mdexpTimeMode_UNKNOWN.ident = "expTimeMode_UNKNOWN"
		mdexpTimeMode_UNKNOWN.description = "Unknown mode for expTime"
		prexpTime.addMode(mdexpTimeMode_UNKNOWN)
		mdexpTimeMode_UNKNOWN.addValue(vlexpTime_UNKNOWN)
		mdDetectorMode_UNKNOWN.addSubMode(mdexpTimeMode_UNKNOWN)

		prBinning.id = identcounter
		identcounter += 1
		prBinning.ident = "Binning"
		prBinning.description = ""
		sysDetector.addParam(prBinning)
		vlBinning_UNKNOWN.id = identcounter
		identcounter += 1
		vlBinning_UNKNOWN.ident = "Binning_UNKNOWN"
		vlBinning_UNKNOWN.description = "Unknown value for Binning"
		prBinning.addValue(vlBinning_UNKNOWN)

		mdBinningMode_UNKNOWN.id = identcounter
		identcounter += 1
		mdBinningMode_UNKNOWN.ident = "BinningMode_UNKNOWN"
		mdBinningMode_UNKNOWN.description = "Unknown mode for Binning"
		prBinning.addMode(mdBinningMode_UNKNOWN)
		mdBinningMode_UNKNOWN.addValue(vlBinning_UNKNOWN)
		mdDetectorMode_UNKNOWN.addSubMode(mdBinningMode_UNKNOWN)

		sysFilter.id = identcounter
		identcounter += 1
		sysFilter.ident = "Filter"
		sysFilter.description = ""
		sysInstrument.addSubsystem(sysFilter);

		mdFilterMode_UNKNOWN.id = identcounter
		identcounter += 1
		mdFilterMode_UNKNOWN.ident = "FilterMode_UNKNOWN";
		mdFilterMode_UNKNOWN.description = "";
		sysFilter.addMode(mdFilterMode_UNKNOWN);

		prClassicFilters.id = identcounter
		identcounter += 1
		prClassicFilters.ident = "ClassicFilters"
		prClassicFilters.description = ""
		sysFilter.addParam(prClassicFilters)
		vlClassicFilters_UNKNOWN.id = identcounter
		identcounter += 1
		vlClassicFilters_UNKNOWN.ident = "ClassicFilters_UNKNOWN"
		vlClassicFilters_UNKNOWN.description = "Unknown value for ClassicFilters"
		prClassicFilters.addValue(vlClassicFilters_UNKNOWN)

		mdClassicFiltersMode_UNKNOWN.id = identcounter
		identcounter += 1
		mdClassicFiltersMode_UNKNOWN.ident = "ClassicFiltersMode_UNKNOWN"
		mdClassicFiltersMode_UNKNOWN.description = "Unknown mode for ClassicFilters"
		prClassicFilters.addMode(mdClassicFiltersMode_UNKNOWN)
		mdClassicFiltersMode_UNKNOWN.addValue(vlClassicFilters_UNKNOWN)
		mdFilterMode_UNKNOWN.addSubMode(mdClassicFiltersMode_UNKNOWN)

		vlMasks_0_6.id = identcounter
		identcounter += 1
		vlMasks_0_6.ident = "Masks_0_6"
		vlMasks_0_6.description = ""
		prMasks.addValue(vlMasks_0_6)

		vlMasks_1_0.id = identcounter
		identcounter += 1
		vlMasks_1_0.ident = "Masks_1_0"
		vlMasks_1_0.description = ""
		prMasks.addValue(vlMasks_1_0)

		vlMasks_2_0.id = identcounter
		identcounter += 1
		vlMasks_2_0.ident = "Masks_2_0"
		vlMasks_2_0.description = ""
		prMasks.addValue(vlMasks_2_0)

		mdMasksMode_Spectroscopy.id = identcounter
		identcounter += 1
		mdMasksMode_Spectroscopy.ident = "MasksMode_Spectroscopy"
		mdMasksMode_Spectroscopy.description = ""
		prMasks.addMode(mdMasksMode_Spectroscopy)

		vlMasks_Half_field.id = identcounter
		identcounter += 1
		vlMasks_Half_field.ident = "Masks_Half_field"
		vlMasks_Half_field.description = ""
		prMasks.addValue(vlMasks_Half_field)

		mdMasksMode_FastImg.id = identcounter
		identcounter += 1
		mdMasksMode_FastImg.ident = "MasksMode_FastImg"
		mdMasksMode_FastImg.description = ""
		prMasks.addMode(mdMasksMode_FastImg)

		vlDispersion_R500.id = identcounter
		identcounter += 1
		vlDispersion_R500.ident = "Dispersion_R500"
		vlDispersion_R500.description = ""
		prDispersion.addValue(vlDispersion_R500)

		vlDispersion_R1000.id = identcounter
		identcounter += 1
		vlDispersion_R1000.ident = "Dispersion_R1000"
		vlDispersion_R1000.description = ""
		prDispersion.addValue(vlDispersion_R1000)

		vlDispersion_R2000.id = identcounter
		identcounter += 1
		vlDispersion_R2000.ident = "Dispersion_R2000"
		vlDispersion_R2000.description = ""
		prDispersion.addValue(vlDispersion_R2000)

		mdDispersionMode_Normal.id = identcounter
		identcounter += 1
		mdDispersionMode_Normal.ident = "DispersionMode_Normal"
		mdDispersionMode_Normal.description = ""
		prDispersion.addMode(mdDispersionMode_Normal)

		vlexpTime_NormalRange.id = identcounter
		identcounter += 1
		vlexpTime_NormalRange.ident = "expTime_NormalRange";
		vlexpTime_NormalRange.description = "";
		vlexpTime_NormalRange.min = 0;
		vlexpTime_NormalRange.default_data = 1;
		vlexpTime_NormalRange.max = 3600;
		prexpTime.addValue(vlexpTime_NormalRange);

		mdexpTimeMode_Normal.id = identcounter
		identcounter += 1
		mdexpTimeMode_Normal.ident = "expTimeMode_Normal"
		mdexpTimeMode_Normal.description = ""
		prexpTime.addMode(mdexpTimeMode_Normal)

		mdexpTimeMode_Fast.id = identcounter
		identcounter += 1
		mdexpTimeMode_Fast.ident = "expTimeMode_Fast"
		mdexpTimeMode_Fast.description = ""
		prexpTime.addMode(mdexpTimeMode_Fast)

		vlexpTime_FastRange.id = identcounter
		identcounter += 1
		vlexpTime_FastRange.ident = "expTime_FastRange";
		vlexpTime_FastRange.description = "";
		vlexpTime_FastRange.min = 0;
		vlexpTime_FastRange.default_data = 0.01;
		vlexpTime_FastRange.max = 0.5;
		prexpTime.addValue(vlexpTime_FastRange);

		vlBinning_1x1.id = identcounter
		identcounter += 1
		vlBinning_1x1.ident = "Binning_1x1"
		vlBinning_1x1.description = ""
		prBinning.addValue(vlBinning_1x1)

		vlBinning_2x1.id = identcounter
		identcounter += 1
		vlBinning_2x1.ident = "Binning_2x1"
		vlBinning_2x1.description = ""
		prBinning.addValue(vlBinning_2x1)

		vlBinning_1x2.id = identcounter
		identcounter += 1
		vlBinning_1x2.ident = "Binning_1x2"
		vlBinning_1x2.description = ""
		prBinning.addValue(vlBinning_1x2)

		vlBinning_2x2.id = identcounter
		identcounter += 1
		vlBinning_2x2.ident = "Binning_2x2"
		vlBinning_2x2.description = ""
		prBinning.addValue(vlBinning_2x2)

		mdBinningMode_Normal.id = identcounter
		identcounter += 1
		mdBinningMode_Normal.ident = "BinningMode_Normal"
		mdBinningMode_Normal.description = ""
		prBinning.addMode(mdBinningMode_Normal)

		mdBinningMode_Square.id = identcounter
		identcounter += 1
		mdBinningMode_Square.ident = "BinningMode_Square"
		mdBinningMode_Square.description = ""
		prBinning.addMode(mdBinningMode_Square)

		mdDetectorMode_Normal.id = identcounter
		identcounter += 1
		mdDetectorMode_Normal.ident = "DetectorMode_Normal"
		mdDetectorMode_Normal.description = ""
		sysDetector.addMode(mdDetectorMode_Normal)

		mdDetectorMode_Image.id = identcounter
		identcounter += 1
		mdDetectorMode_Image.ident = "DetectorMode_Image"
		mdDetectorMode_Image.description = ""
		sysDetector.addMode(mdDetectorMode_Image)

		mdDetectorMode_FastImage.id = identcounter
		identcounter += 1
		mdDetectorMode_FastImage.ident = "DetectorMode_FastImage"
		mdDetectorMode_FastImage.description = ""
		sysDetector.addMode(mdDetectorMode_FastImage)

		mdInstrumentMode_Photometry.id = identcounter
		identcounter += 1
		mdInstrumentMode_Photometry.ident = "InstrumentMode_Photometry"
		mdInstrumentMode_Photometry.description = ""
		sysInstrument.addMode(mdInstrumentMode_Photometry)

		mdInstrumentMode_Spectroscopy.id = identcounter
		identcounter += 1
		mdInstrumentMode_Spectroscopy.ident = "InstrumentMode_Spectroscopy"
		mdInstrumentMode_Spectroscopy.description = ""
		sysInstrument.addMode(mdInstrumentMode_Spectroscopy)

		mdInstrumentMode_FastPhotometry.id = identcounter
		identcounter += 1
		mdInstrumentMode_FastPhotometry.ident = "InstrumentMode_FastPhotometry"
		mdInstrumentMode_FastPhotometry.description = ""
		sysInstrument.addMode(mdInstrumentMode_FastPhotometry)

		mdFilterMode_Classic.id = identcounter
		identcounter += 1
		mdFilterMode_Classic.ident = "FilterMode_Classic"
		mdFilterMode_Classic.description = ""
		sysFilter.addMode(mdFilterMode_Classic)

		mdFilterMode_TFBlue.id = identcounter
		identcounter += 1
		mdFilterMode_TFBlue.ident = "FilterMode_TFBlue"
		mdFilterMode_TFBlue.description = ""
		sysFilter.addMode(mdFilterMode_TFBlue)

		mdFilterMode_TFRed.id = identcounter
		identcounter += 1
		mdFilterMode_TFRed.ident = "FilterMode_TFRed"
		mdFilterMode_TFRed.description = ""
		sysFilter.addMode(mdFilterMode_TFRed)

		vlClassicFilters_Red.id = identcounter
		identcounter += 1
		vlClassicFilters_Red.ident = "ClassicFilters_Red"
		vlClassicFilters_Red.description = ""
		prClassicFilters.addValue(vlClassicFilters_Red)

		vlClassicFilters_Blue.id = identcounter
		identcounter += 1
		vlClassicFilters_Blue.ident = "ClassicFilters_Blue"
		vlClassicFilters_Blue.description = ""
		prClassicFilters.addValue(vlClassicFilters_Blue)

		mdClassicFiltersMode_Standard.id = identcounter
		identcounter += 1
		mdClassicFiltersMode_Standard.ident = "ClassicFiltersMode_Standard"
		mdClassicFiltersMode_Standard.description = ""
		prClassicFilters.addMode(mdClassicFiltersMode_Standard)

		mdClassicFiltersMode_Blue.id = identcounter
		identcounter += 1
		mdClassicFiltersMode_Blue.ident = "ClassicFiltersMode_Blue"
		mdClassicFiltersMode_Blue.description = ""
		prClassicFilters.addMode(mdClassicFiltersMode_Blue)

		mdClassicFiltersMode_Red.id = identcounter
		identcounter += 1
		mdClassicFiltersMode_Red.ident = "ClassicFiltersMode_Red"
		mdClassicFiltersMode_Red.description = ""
		prClassicFilters.addMode(mdClassicFiltersMode_Red)

		vlClassicFilters_userFilter.id = identcounter
		identcounter += 1
		vlClassicFilters_userFilter.ident = "ClassicFilters_userFilter";
		vlClassicFilters_userFilter.description = "";
		prClassicFilters.addValue(vlClassicFilters_userFilter);

		mdClassicFiltersMode_User.id = identcounter
		identcounter += 1
		mdClassicFiltersMode_User.ident = "ClassicFiltersMode_User"
		mdClassicFiltersMode_User.description = ""
		prClassicFilters.addMode(mdClassicFiltersMode_User)

		mdInstrumentMode_Engineering.id = identcounter
		identcounter += 1
		mdInstrumentMode_Engineering.ident = "InstrumentMode_Engineering"
		mdInstrumentMode_Engineering.description = "Instrument engineering mode"
		sysInstrument.addMode(mdInstrumentMode_Engineering)

		mdDetectorMode_Engineering.id = identcounter
		identcounter += 1
		mdDetectorMode_Engineering.ident = "DetectorMode_Engineering"
		mdDetectorMode_Engineering.description = "Detector engineering mode"
		sysDetector.addMode(mdDetectorMode_Engineering)

		mdFilterMode_Engineering.id = identcounter
		identcounter += 1
		mdFilterMode_Engineering.ident = "FilterMode_Engineering"
		mdFilterMode_Engineering.description = "Filter engineering mode"
		sysFilter.addMode(mdFilterMode_Engineering)
		# Marcamos MasksMode_Spectroscopy como elegible para InstrumentMode_Spectroscopy
		mdInstrumentMode_Spectroscopy.addSubMode(mdMasksMode_Spectroscopy)
		# Marcamos MasksMode_FastImg como elegible para InstrumentMode_FastPhotometry
		mdInstrumentMode_FastPhotometry.addSubMode(mdMasksMode_FastImg)
		# Marcamos MasksMode_Spectroscopy como elegible para InstrumentMode_Engineering
		mdInstrumentMode_Engineering.addSubMode(mdMasksMode_Spectroscopy)
		# Marcamos MasksMode_FastImg como elegible para InstrumentMode_Engineering
		mdInstrumentMode_Engineering.addSubMode(mdMasksMode_FastImg)
		# Marcamos Masks_0_6 como elegible para MasksMode_Spectroscopy
		mdMasksMode_Spectroscopy.addValue(vlMasks_0_6)
		# Marcamos Masks_2_0 como elegible para MasksMode_Spectroscopy
		mdMasksMode_Spectroscopy.addValue(vlMasks_2_0)
		# Marcamos Masks_1_0 como elegible para MasksMode_Spectroscopy
		mdMasksMode_Spectroscopy.addValue(vlMasks_1_0)
		# Marcamos Masks_Half_field como elegible para MasksMode_FastImg
		mdMasksMode_FastImg.addValue(vlMasks_Half_field)
		# Marcamos DispersionMode_Normal como elegible para InstrumentMode_Spectroscopy
		mdInstrumentMode_Spectroscopy.addSubMode(mdDispersionMode_Normal)
		# Marcamos DispersionMode_Normal como elegible para InstrumentMode_Engineering
		mdInstrumentMode_Engineering.addSubMode(mdDispersionMode_Normal)
		# Marcamos Dispersion_R500 como elegible para DispersionMode_Normal
		mdDispersionMode_Normal.addValue(vlDispersion_R500)
		# Marcamos Dispersion_R1000 como elegible para DispersionMode_Normal
		mdDispersionMode_Normal.addValue(vlDispersion_R1000)
		# Marcamos Dispersion_R2000 como elegible para DispersionMode_Normal
		mdDispersionMode_Normal.addValue(vlDispersion_R2000)
		# Marcamos DetectorMode_Image como elegible para InstrumentMode_Photometry
		mdInstrumentMode_Photometry.addSubMode(mdDetectorMode_Image)
		# Marcamos DetectorMode_Normal como elegible para InstrumentMode_Spectroscopy
		mdInstrumentMode_Spectroscopy.addSubMode(mdDetectorMode_Normal)
		# Marcamos DetectorMode_FastImage como elegible para InstrumentMode_FastPhotometry
		mdInstrumentMode_FastPhotometry.addSubMode(mdDetectorMode_FastImage)
		# Marcamos DetectorMode_Normal como elegible para InstrumentMode_Engineering
		mdInstrumentMode_Engineering.addSubMode(mdDetectorMode_Normal)
		# Marcamos DetectorMode_Image como elegible para InstrumentMode_Engineering
		mdInstrumentMode_Engineering.addSubMode(mdDetectorMode_Image)
		# Marcamos DetectorMode_FastImage como elegible para InstrumentMode_Engineering
		mdInstrumentMode_Engineering.addSubMode(mdDetectorMode_FastImage)
		# Marcamos DetectorMode_Engineering como elegible para InstrumentMode_Engineering
		mdInstrumentMode_Engineering.addSubMode(mdDetectorMode_Engineering)
		# Marcamos expTimeMode_Normal como elegible para DetectorMode_Normal
		mdDetectorMode_Normal.addSubMode(mdexpTimeMode_Normal)
		# Marcamos expTimeMode_Normal como elegible para DetectorMode_Image
		mdDetectorMode_Image.addSubMode(mdexpTimeMode_Normal)
		# Marcamos expTimeMode_Fast como elegible para DetectorMode_FastImage
		mdDetectorMode_FastImage.addSubMode(mdexpTimeMode_Fast)
		# Marcamos expTimeMode_Normal como elegible para DetectorMode_Engineering
		mdDetectorMode_Engineering.addSubMode(mdexpTimeMode_Normal)
		# Marcamos expTimeMode_Fast como elegible para DetectorMode_Engineering
		mdDetectorMode_Engineering.addSubMode(mdexpTimeMode_Fast)
		# Marcamos expTime_NormalRange como elegible para expTimeMode_Normal
		mdexpTimeMode_Normal.addValue(vlexpTime_NormalRange)
		# Marcamos expTime_FastRange como elegible para expTimeMode_Fast
		mdexpTimeMode_Fast.addValue(vlexpTime_FastRange)
		# Marcamos BinningMode_Normal como elegible para DetectorMode_Normal
		mdDetectorMode_Normal.addSubMode(mdBinningMode_Normal)
		# Marcamos BinningMode_Square como elegible para DetectorMode_Image
		mdDetectorMode_Image.addSubMode(mdBinningMode_Square)
		# Marcamos BinningMode_Square como elegible para DetectorMode_FastImage
		mdDetectorMode_FastImage.addSubMode(mdBinningMode_Square)
		# Marcamos BinningMode_Normal como elegible para DetectorMode_Engineering
		mdDetectorMode_Engineering.addSubMode(mdBinningMode_Normal)
		# Marcamos BinningMode_Square como elegible para DetectorMode_Engineering
		mdDetectorMode_Engineering.addSubMode(mdBinningMode_Square)
		# Marcamos Binning_1x1 como elegible para BinningMode_Normal
		mdBinningMode_Normal.addValue(vlBinning_1x1)
		# Marcamos Binning_2x1 como elegible para BinningMode_Normal
		mdBinningMode_Normal.addValue(vlBinning_2x1)
		# Marcamos Binning_1x2 como elegible para BinningMode_Normal
		mdBinningMode_Normal.addValue(vlBinning_1x2)
		# Marcamos Binning_2x2 como elegible para BinningMode_Normal
		mdBinningMode_Normal.addValue(vlBinning_2x2)
		# Marcamos Binning_1x1 como elegible para BinningMode_Square
		mdBinningMode_Square.addValue(vlBinning_1x1)
		# Marcamos Binning_2x2 como elegible para BinningMode_Square
		mdBinningMode_Square.addValue(vlBinning_2x2)
		# Marcamos FilterMode_TFRed como elegible para InstrumentMode_Photometry
		mdInstrumentMode_Photometry.addSubMode(mdFilterMode_TFRed)
		# Marcamos FilterMode_TFBlue como elegible para InstrumentMode_Photometry
		mdInstrumentMode_Photometry.addSubMode(mdFilterMode_TFBlue)
		# Marcamos FilterMode_Classic como elegible para InstrumentMode_Photometry
		mdInstrumentMode_Photometry.addSubMode(mdFilterMode_Classic)
		# Marcamos FilterMode_Classic como elegible para InstrumentMode_Spectroscopy
		mdInstrumentMode_Spectroscopy.addSubMode(mdFilterMode_Classic)
		# Marcamos FilterMode_TFRed como elegible para InstrumentMode_Spectroscopy
		mdInstrumentMode_Spectroscopy.addSubMode(mdFilterMode_TFRed)
		# Marcamos FilterMode_TFBlue como elegible para InstrumentMode_Spectroscopy
		mdInstrumentMode_Spectroscopy.addSubMode(mdFilterMode_TFBlue)
		# Marcamos FilterMode_Classic como elegible para InstrumentMode_FastPhotometry
		mdInstrumentMode_FastPhotometry.addSubMode(mdFilterMode_Classic)
		# Marcamos FilterMode_Classic como elegible para InstrumentMode_Engineering
		mdInstrumentMode_Engineering.addSubMode(mdFilterMode_Classic)
		# Marcamos FilterMode_TFBlue como elegible para InstrumentMode_Engineering
		mdInstrumentMode_Engineering.addSubMode(mdFilterMode_TFBlue)
		# Marcamos FilterMode_TFRed como elegible para InstrumentMode_Engineering
		mdInstrumentMode_Engineering.addSubMode(mdFilterMode_TFRed)
		# Marcamos FilterMode_Engineering como elegible para InstrumentMode_Engineering
		mdInstrumentMode_Engineering.addSubMode(mdFilterMode_Engineering)
		# Marcamos ClassicFiltersMode_Standard como elegible para FilterMode_Classic
		mdFilterMode_Classic.addSubMode(mdClassicFiltersMode_Standard)
		# Marcamos ClassicFiltersMode_User como elegible para FilterMode_Classic
		mdFilterMode_Classic.addSubMode(mdClassicFiltersMode_User)
		# Marcamos ClassicFiltersMode_Blue como elegible para FilterMode_TFBlue
		mdFilterMode_TFBlue.addSubMode(mdClassicFiltersMode_Blue)
		# Marcamos ClassicFiltersMode_Red como elegible para FilterMode_TFRed
		mdFilterMode_TFRed.addSubMode(mdClassicFiltersMode_Red)
		# Marcamos ClassicFiltersMode_Standard como elegible para FilterMode_Engineering
		mdFilterMode_Engineering.addSubMode(mdClassicFiltersMode_Standard)
		# Marcamos ClassicFiltersMode_Blue como elegible para FilterMode_Engineering
		mdFilterMode_Engineering.addSubMode(mdClassicFiltersMode_Blue)
		# Marcamos ClassicFiltersMode_Red como elegible para FilterMode_Engineering
		mdFilterMode_Engineering.addSubMode(mdClassicFiltersMode_Red)
		# Marcamos ClassicFiltersMode_User como elegible para FilterMode_Engineering
		mdFilterMode_Engineering.addSubMode(mdClassicFiltersMode_User)
		# Marcamos ClassicFilters_Red como elegible para ClassicFiltersMode_Standard
		mdClassicFiltersMode_Standard.addValue(vlClassicFilters_Red)
		# Marcamos ClassicFilters_Blue como elegible para ClassicFiltersMode_Standard
		mdClassicFiltersMode_Standard.addValue(vlClassicFilters_Blue)
		# Marcamos ClassicFilters_Blue como elegible para ClassicFiltersMode_Blue
		mdClassicFiltersMode_Blue.addValue(vlClassicFilters_Blue)
		# Marcamos ClassicFilters_Red como elegible para ClassicFiltersMode_Red
		mdClassicFiltersMode_Red.addValue(vlClassicFilters_Red)
		# Marcamos ClassicFilters_userFilter como elegible para ClassicFiltersMode_User
		mdClassicFiltersMode_User.addValue(vlClassicFilters_userFilter)

