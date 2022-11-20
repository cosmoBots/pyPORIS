from PORIS import *

class examplePORIS:
	def __init__(self):
		idcounter = 1
		self.sysInstrument = PORISSys("Instrument")
		self.mdInstrumentUNKNOWN = PORISMode("UNKNOWN")
		self.root = self.sysInstrument
		self.prMasks = PORISParam("Masks")
		self.mdMasksUNKNOWN = PORISMode("UNKNOWN")
		self.vlMasks_UNKNOWN = PORISValue("UNKNOWN")
		self.prDispersion = PORISParam("Dispersion")
		self.mdDispersionUNKNOWN = PORISMode("UNKNOWN")
		self.vlDispersion_UNKNOWN = PORISValue("UNKNOWN")
		self.sysDetector = PORISSys("Detector")
		self.mdDetectorUNKNOWN = PORISMode("UNKNOWN")
		self.prexpTime = PORISParam("expTime")
		self.mdexpTimeUNKNOWN = PORISMode("UNKNOWN")
		self.vlexpTime_UNKNOWN = PORISValue("UNKNOWN")
		self.prBinning = PORISParam("Binning")
		self.mdBinningUNKNOWN = PORISMode("UNKNOWN")
		self.vlBinning_UNKNOWN = PORISValue("UNKNOWN")
		self.sysFilter = PORISSys("Filter")
		self.mdFilterUNKNOWN = PORISMode("UNKNOWN")
		self.prClassicFilters = PORISParam("ClassicFilters")
		self.mdClassicFiltersUNKNOWN = PORISMode("UNKNOWN")
		self.vlClassicFilters_UNKNOWN = PORISValue("UNKNOWN")
		self.vlMasks_0_6 = PORISValue("0_6")
		self.vlMasks_1_0 = PORISValue("1_0")
		self.vlMasks_2_0 = PORISValue("2_0")
		self.mdMasksSpectroscopy = PORISMode("Spectroscopy")
		self.vlMasks_Half_field = PORISValue("Half_field")
		self.mdMasksFastImg = PORISMode("FastImg")
		self.vlDispersion_R500 = PORISValue("R500")
		self.vlDispersion_R1000 = PORISValue("R1000")
		self.vlDispersion_R2000 = PORISValue("R2000")
		self.mdDispersionNormal = PORISMode("Normal")
		self.vlexpTime_NormalRange = PORISValueFloat("NormalRange")
		self.mdexpTimeNormal = PORISMode("Normal")
		self.mdexpTimeFast = PORISMode("Fast")
		self.vlexpTime_FastRange = PORISValueFloat("FastRange")
		self.vlBinning_1x1 = PORISValue("1x1")
		self.vlBinning_2x1 = PORISValue("2x1")
		self.vlBinning_1x2 = PORISValue("1x2")
		self.vlBinning_2x2 = PORISValue("2x2")
		self.mdBinningNormal = PORISMode("Normal")
		self.mdBinningSquare = PORISMode("Square")
		self.mdDetectorNormal = PORISMode("Normal")
		self.mdDetectorImage = PORISMode("Image")
		self.mdDetectorFastImage = PORISMode("FastImage")
		self.mdInstrumentPhotometry = PORISMode("Photometry")
		self.mdInstrumentSpectroscopy = PORISMode("Spectroscopy")
		self.mdInstrumentFastPhotometry = PORISMode("FastPhotometry")
		self.mdFilterClassic = PORISMode("Classic")
		self.mdFilterTFBlue = PORISMode("TFBlue")
		self.mdFilterTFRed = PORISMode("TFRed")
		self.vlClassicFilters_Red = PORISValue("Red")
		self.vlClassicFilters_Blue = PORISValue("Blue")
		self.mdClassicFiltersStandard = PORISMode("Standard")
		self.mdClassicFiltersBlue = PORISMode("Blue")
		self.mdClassicFiltersRed = PORISMode("Red")
		self.vlClassicFilters_userFilter = PORISValueText("userFilter")
		self.mdClassicFiltersUser = PORISMode("User")

		self.sysInstrument.id = idcounter
		idcounter += 1

		self.mdInstrumentUNKNOWN.id = idcounter
		idcounter += 1
		self.sysInstrument.addMode(self.mdInstrumentUNKNOWN)

		self.prMasks.id = idcounter
		idcounter += 1
		self.sysInstrument.addParam(self.prMasks)
		idcounter += 1
		self.prMasks.addValue(self.vlMasks_UNKNOWN)

		self.mdMasksUNKNOWN.id = idcounter
		idcounter += 1
		self.prMasks.addMode(self.mdMasksUNKNOWN)
		self.mdMasksUNKNOWN.addValue(self.vlMasks_UNKNOWN)
		self.mdInstrumentUNKNOWN.addSubMode(self.mdMasksUNKNOWN)

		self.prDispersion.id = idcounter
		idcounter += 1
		self.sysInstrument.addParam(self.prDispersion)
		idcounter += 1
		self.prDispersion.addValue(self.vlDispersion_UNKNOWN)

		self.mdDispersionUNKNOWN.id = idcounter
		idcounter += 1
		self.prDispersion.addMode(self.mdDispersionUNKNOWN)
		self.mdDispersionUNKNOWN.addValue(self.vlDispersion_UNKNOWN)
		self.mdInstrumentUNKNOWN.addSubMode(self.mdDispersionUNKNOWN)

		self.sysDetector.id = idcounter
		idcounter += 1
		self.sysInstrument.addSubsystem(self.sysDetector)

		self.mdDetectorUNKNOWN.id = idcounter
		idcounter += 1
		self.sysDetector.addMode(self.mdDetectorUNKNOWN)

		self.prexpTime.id = idcounter
		idcounter += 1
		self.sysDetector.addParam(self.prexpTime)
		idcounter += 1
		self.prexpTime.addValue(self.vlexpTime_UNKNOWN)

		self.mdexpTimeUNKNOWN.id = idcounter
		idcounter += 1
		self.prexpTime.addMode(self.mdexpTimeUNKNOWN)
		self.mdexpTimeUNKNOWN.addValue(self.vlexpTime_UNKNOWN)
		self.mdDetectorUNKNOWN.addSubMode(self.mdexpTimeUNKNOWN)

		self.prBinning.id = idcounter
		idcounter += 1
		self.sysDetector.addParam(self.prBinning)
		idcounter += 1
		self.prBinning.addValue(self.vlBinning_UNKNOWN)

		self.mdBinningUNKNOWN.id = idcounter
		idcounter += 1
		self.prBinning.addMode(self.mdBinningUNKNOWN)
		self.mdBinningUNKNOWN.addValue(self.vlBinning_UNKNOWN)
		self.mdDetectorUNKNOWN.addSubMode(self.mdBinningUNKNOWN)

		self.sysFilter.id = idcounter
		idcounter += 1
		self.sysInstrument.addSubsystem(self.sysFilter)

		self.mdFilterUNKNOWN.id = idcounter
		idcounter += 1
		self.sysFilter.addMode(self.mdFilterUNKNOWN)

		self.prClassicFilters.id = idcounter
		idcounter += 1
		self.sysFilter.addParam(self.prClassicFilters)
		idcounter += 1
		self.prClassicFilters.addValue(self.vlClassicFilters_UNKNOWN)

		self.mdClassicFiltersUNKNOWN.id = idcounter
		idcounter += 1
		self.prClassicFilters.addMode(self.mdClassicFiltersUNKNOWN)
		self.mdClassicFiltersUNKNOWN.addValue(self.vlClassicFilters_UNKNOWN)
		self.mdFilterUNKNOWN.addSubMode(self.mdClassicFiltersUNKNOWN)

		self.vlMasks_0_6.id = idcounter
		idcounter += 1
		self.prMasks.addValue(self.vlMasks_0_6)

		self.vlMasks_1_0.id = idcounter
		idcounter += 1
		self.prMasks.addValue(self.vlMasks_1_0)

		self.vlMasks_2_0.id = idcounter
		idcounter += 1
		self.prMasks.addValue(self.vlMasks_2_0)

		self.mdMasksSpectroscopy.id = idcounter
		idcounter += 1
		self.prMasks.addMode(self.mdMasksSpectroscopy)

		self.vlMasks_Half_field.id = idcounter
		idcounter += 1
		self.prMasks.addValue(self.vlMasks_Half_field)

		self.mdMasksFastImg.id = idcounter
		idcounter += 1
		self.prMasks.addMode(self.mdMasksFastImg)

		self.vlDispersion_R500.id = idcounter
		idcounter += 1
		self.prDispersion.addValue(self.vlDispersion_R500)

		self.vlDispersion_R1000.id = idcounter
		idcounter += 1
		self.prDispersion.addValue(self.vlDispersion_R1000)

		self.vlDispersion_R2000.id = idcounter
		idcounter += 1
		self.prDispersion.addValue(self.vlDispersion_R2000)

		self.mdDispersionNormal.id = idcounter
		idcounter += 1
		self.prDispersion.addMode(self.mdDispersionNormal)

		self.vlexpTime_NormalRange.id = idcounter
		idcounter += 1
		self.vlexpTime_NormalRange.min = 0
		self.vlexpTime_NormalRange.default_data = 1
		self.vlexpTime_NormalRange.max = 3600
		self.prexpTime.addValue(self.vlexpTime_NormalRange)

		self.mdexpTimeNormal.id = idcounter
		idcounter += 1
		self.prexpTime.addMode(self.mdexpTimeNormal)

		self.mdexpTimeFast.id = idcounter
		idcounter += 1
		self.prexpTime.addMode(self.mdexpTimeFast)

		self.vlexpTime_FastRange.id = idcounter
		idcounter += 1
		self.vlexpTime_FastRange.min = 0
		self.vlexpTime_FastRange.default_data = 0.01
		self.vlexpTime_FastRange.max = 0.5
		self.prexpTime.addValue(self.vlexpTime_FastRange)

		self.vlBinning_1x1.id = idcounter
		idcounter += 1
		self.prBinning.addValue(self.vlBinning_1x1)

		self.vlBinning_2x1.id = idcounter
		idcounter += 1
		self.prBinning.addValue(self.vlBinning_2x1)

		self.vlBinning_1x2.id = idcounter
		idcounter += 1
		self.prBinning.addValue(self.vlBinning_1x2)

		self.vlBinning_2x2.id = idcounter
		idcounter += 1
		self.prBinning.addValue(self.vlBinning_2x2)

		self.mdBinningNormal.id = idcounter
		idcounter += 1
		self.prBinning.addMode(self.mdBinningNormal)

		self.mdBinningSquare.id = idcounter
		idcounter += 1
		self.prBinning.addMode(self.mdBinningSquare)

		self.mdDetectorNormal.id = idcounter
		idcounter += 1
		self.sysDetector.addMode(self.mdDetectorNormal)

		self.mdDetectorImage.id = idcounter
		idcounter += 1
		self.sysDetector.addMode(self.mdDetectorImage)

		self.mdDetectorFastImage.id = idcounter
		idcounter += 1
		self.sysDetector.addMode(self.mdDetectorFastImage)

		self.mdInstrumentPhotometry.id = idcounter
		idcounter += 1
		self.sysInstrument.addMode(self.mdInstrumentPhotometry)

		self.mdInstrumentSpectroscopy.id = idcounter
		idcounter += 1
		self.sysInstrument.addMode(self.mdInstrumentSpectroscopy)

		self.mdInstrumentFastPhotometry.id = idcounter
		idcounter += 1
		self.sysInstrument.addMode(self.mdInstrumentFastPhotometry)

		self.mdFilterClassic.id = idcounter
		idcounter += 1
		self.sysFilter.addMode(self.mdFilterClassic)

		self.mdFilterTFBlue.id = idcounter
		idcounter += 1
		self.sysFilter.addMode(self.mdFilterTFBlue)

		self.mdFilterTFRed.id = idcounter
		idcounter += 1
		self.sysFilter.addMode(self.mdFilterTFRed)

		self.vlClassicFilters_Red.id = idcounter
		idcounter += 1
		self.prClassicFilters.addValue(self.vlClassicFilters_Red)

		self.vlClassicFilters_Blue.id = idcounter
		idcounter += 1
		self.prClassicFilters.addValue(self.vlClassicFilters_Blue)

		self.mdClassicFiltersStandard.id = idcounter
		idcounter += 1
		self.prClassicFilters.addMode(self.mdClassicFiltersStandard)

		self.mdClassicFiltersBlue.id = idcounter
		idcounter += 1
		self.prClassicFilters.addMode(self.mdClassicFiltersBlue)

		self.mdClassicFiltersRed.id = idcounter
		idcounter += 1
		self.prClassicFilters.addMode(self.mdClassicFiltersRed)

		self.vlClassicFilters_userFilter.id = idcounter
		idcounter += 1
		self.prClassicFilters.addValue(self.vlClassicFilters_userFilter)

		self.mdClassicFiltersUser.id = idcounter
		idcounter += 1
		self.prClassicFilters.addMode(self.mdClassicFiltersUser)
		self.mdInstrumentSpectroscopy.addSubMode(self.mdMasksSpectroscopy)
		self.mdInstrumentFastPhotometry.addSubMode(self.mdMasksFastImg)
		self.mdMasksSpectroscopy.addValue(self.vlMasks_0_6)
		self.mdMasksSpectroscopy.addValue(self.vlMasks_2_0)
		self.mdMasksSpectroscopy.addValue(self.vlMasks_1_0)
		self.mdMasksFastImg.addValue(self.vlMasks_Half_field)
		self.mdInstrumentSpectroscopy.addSubMode(self.mdDispersionNormal)
		self.mdDispersionNormal.addValue(self.vlDispersion_R500)
		self.mdDispersionNormal.addValue(self.vlDispersion_R1000)
		self.mdDispersionNormal.addValue(self.vlDispersion_R2000)
		self.mdInstrumentPhotometry.addSubMode(self.mdDetectorImage)
		self.mdInstrumentSpectroscopy.addSubMode(self.mdDetectorNormal)
		self.mdInstrumentFastPhotometry.addSubMode(self.mdDetectorFastImage)
		self.mdDetectorNormal.addSubMode(self.mdexpTimeNormal)
		self.mdDetectorImage.addSubMode(self.mdexpTimeNormal)
		self.mdDetectorFastImage.addSubMode(self.mdexpTimeFast)
		self.mdexpTimeNormal.addValue(self.vlexpTime_NormalRange)
		self.mdexpTimeFast.addValue(self.vlexpTime_FastRange)
		self.mdDetectorNormal.addSubMode(self.mdBinningNormal)
		self.mdDetectorImage.addSubMode(self.mdBinningSquare)
		self.mdDetectorFastImage.addSubMode(self.mdBinningSquare)
		self.mdBinningNormal.addValue(self.vlBinning_1x1)
		self.mdBinningNormal.addValue(self.vlBinning_2x1)
		self.mdBinningNormal.addValue(self.vlBinning_1x2)
		self.mdBinningNormal.addValue(self.vlBinning_2x2)
		self.mdBinningSquare.addValue(self.vlBinning_1x1)
		self.mdBinningSquare.addValue(self.vlBinning_2x2)
		self.mdInstrumentPhotometry.addSubMode(self.mdFilterTFRed)
		self.mdInstrumentPhotometry.addSubMode(self.mdFilterTFBlue)
		self.mdInstrumentPhotometry.addSubMode(self.mdFilterClassic)
		self.mdInstrumentSpectroscopy.addSubMode(self.mdFilterClassic)
		self.mdInstrumentSpectroscopy.addSubMode(self.mdFilterTFRed)
		self.mdInstrumentSpectroscopy.addSubMode(self.mdFilterTFBlue)
		self.mdInstrumentFastPhotometry.addSubMode(self.mdFilterClassic)
		self.mdFilterClassic.addSubMode(self.mdClassicFiltersStandard)
		self.mdFilterClassic.addSubMode(self.mdClassicFiltersUser)
		self.mdFilterTFBlue.addSubMode(self.mdClassicFiltersBlue)
		self.mdFilterTFRed.addSubMode(self.mdClassicFiltersRed)
		self.mdClassicFiltersStandard.addValue(self.vlClassicFilters_Red)
		self.mdClassicFiltersStandard.addValue(self.vlClassicFilters_Blue)
		self.mdClassicFiltersBlue.addValue(self.vlClassicFilters_Blue)
		self.mdClassicFiltersRed.addValue(self.vlClassicFilters_Red)
		self.mdClassicFiltersUser.addValue(self.vlClassicFilters_userFilter)

