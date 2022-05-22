from PORIS import *

# Values
currentid = 1
vlClassicFiltersRed = PORISValue("Red")
vlClassicFiltersRed.id = currentid
currentid += 1
vlClassicFiltersBlue = PORISValue("Blue")
vlClassicFiltersBlue.id = currentid
currentid += 1
vlClassicFiltersuserFilter = PORISValueText("userFilter")
vlClassicFiltersuserFilter.id = currentid
currentid += 1
vlDispersionR500 = PORISValue("R500")
vlDispersionR500.id = currentid
currentid += 1
vlDispersionR2000 = PORISValue("R2000")
vlDispersionR2000.id = currentid
currentid += 1
vlDispersionR1000 = PORISValue("R1000")
vlDispersionR1000.id = currentid
currentid += 1
vlBinning1x1 = PORISValue("1x1")
vlBinning1x1.id = currentid
currentid += 1
vlBinning1x2 = PORISValue("1x2")
vlBinning1x2.id = currentid
currentid += 1
vlBinning2x1 = PORISValue("2x1")
vlBinning2x1.id = currentid
currentid += 1
vlBinning2x2 = PORISValue("2x2")
vlBinning2x2.id = currentid
currentid += 1
vlExpTimeNormalRange = PORISValueFloat("NormalRange")
vlExpTimeNormalRange.id = currentid
currentid += 1
vlExpTimeFastRange = PORISValueFloat("FastRange")
vlExpTimeFastRange.id = currentid
currentid += 1
vlMasks0_6 = PORISValue("0_6")
vlMasks0_6.id = currentid
currentid += 1
vlMasks2_0 = PORISValue("2_0")
vlMasks2_0.id = currentid
currentid += 1
vlMasks1_0 = PORISValue("1_0")
vlMasks1_0.id = currentid
currentid += 1
vlMasksHalf_field = PORISValue("Half_field")
vlMasksHalf_field.id = currentid
currentid += 1

# Param modes
mdClassicFiltersRed = PORISMode("ClassicFilters_Red")
mdClassicFiltersRed.id = currentid
currentid += 1
mdClassicFiltersBlue = PORISMode("ClassicFilters_Blue")
mdClassicFiltersBlue.id = currentid
currentid += 1
mdClassicFiltersUser = PORISMode("ClassicFilters_User")
mdClassicFiltersUser.id = currentid
currentid += 1
mdClassicFiltersStandard = PORISMode("ClassicFilters_Standard")
mdClassicFiltersStandard.id = currentid
currentid += 1
mdDispersionNormal = PORISMode("Dispersion_Normal")
mdDispersionNormal.id = currentid
currentid += 1
mdBinningNormal = PORISMode("Binning_Normal")
mdBinningNormal.id = currentid
currentid += 1
mdBinningSquare = PORISMode("Binning_Square")
mdBinningSquare.id = currentid
currentid += 1
mdExpTimeNormal = PORISMode("ExpTime_Normal")
mdExpTimeNormal.id = currentid
currentid += 1
mdExpTimeFast = PORISMode("ExpTime_Fast")
mdExpTimeFast.id = currentid
currentid += 1
mdMasksSpectroscopy = PORISMode("Mask_Spectroscopy")
mdMasksSpectroscopy.id = currentid
currentid += 1
mdMasksFastImg = PORISMode("Masks_FastImg")
mdMasksFastImg.id = currentid
currentid += 1

# Sys modes
mdFilterTFRed = PORISMode("Filter_TFRed")
mdFilterTFRed.id = currentid
currentid += 1
mdFilterTFBlue = PORISMode("Filter_TFBlue")
mdFilterTFBlue.id = currentid
currentid += 1
mdFilterClassic = PORISMode("Filter_Classic")
mdFilterClassic.id = currentid
currentid += 1
mdDetectorNormal = PORISMode("Detector_Normal")
mdDetectorNormal.id = currentid
currentid += 1
mdDetectorImage = PORISMode("Detector_Image")
mdDetectorImage.id = currentid
currentid += 1
mdDetectorFastImage = PORISMode("Detector_FastImage")
mdDetectorFastImage.id = currentid
currentid += 1
mdInstrumentPhotometry = PORISMode("Instrument_Photometry")
mdInstrumentPhotometry.id = currentid
currentid += 1
mdInstrumentSpectroscopy = PORISMode("Instrument_Spectroscopy")
mdInstrumentSpectroscopy.id = currentid
currentid += 1
mdInstrumentFastPhotometry = PORISMode("Instrument_FastPhotometry")
mdInstrumentFastPhotometry.id = currentid
currentid += 1

# Second level

vlClassicFiltersUnknown = PORISValue("ClassicFilters_Unknown")
vlClassicFiltersUnknown.id = currentid
currentid += 1
mdClassicFiltersUnknown = PORISMode("ClassicFilters_Unknown")
mdClassicFiltersUnknown.id = currentid
currentid += 1
mdClassicFiltersUnknown.values[vlClassicFiltersUnknown.name] = vlClassicFiltersUnknown
prClassicFilters = PORISParam("ClassicFilters")
prClassicFilters.id = currentid
currentid += 1
prClassicFilters.addValue(vlClassicFiltersUnknown)
prClassicFilters.addMode(mdClassicFiltersUnknown)

vlBinningUnknown = PORISValue("Binning_Unknown")
vlBinningUnknown.id = currentid
currentid += 1
mdBinningUnknown = PORISMode("Binning_Unknown")
mdBinningUnknown.id = currentid
currentid += 1
mdBinningUnknown.values[vlBinningUnknown.name] = vlBinningUnknown
prBinning = PORISParam("Binning")
prBinning.id = currentid
currentid += 1
prBinning.addValue(vlBinningUnknown)
prBinning.addMode(mdBinningUnknown)

vlExpTimeUnknown = PORISValue("ExpTime_Unknown")
vlExpTimeUnknown.id = currentid
currentid += 1
mdExpTimeUnknown = PORISMode("ExpTime_Unknown")
mdExpTimeUnknown.id = currentid
currentid += 1
mdExpTimeUnknown.values[vlExpTimeUnknown.name] = vlExpTimeUnknown
prExpTime = PORISParam("ExpTime")
prExpTime.id = currentid
currentid += 1
prExpTime.addValue(vlExpTimeUnknown)
prExpTime.addMode(mdExpTimeUnknown)


# First level

vlDispersionUnknown = PORISValue("Dispersion_Unknown")
vlDispersionUnknown.id = currentid
currentid += 1
mdDispersionUnknown = PORISMode("Dispersion_Unknown")
mdDispersionUnknown.id = currentid
currentid += 1
mdDispersionUnknown.values[vlDispersionUnknown.name] = vlDispersionUnknown
prDispersion = PORISParam("Dispersion")
prDispersion.id = currentid
currentid += 1
prDispersion.addValue(vlDispersionUnknown)
prDispersion.addMode(mdDispersionUnknown)

vlMasksUnknown = PORISValue("Masks_Unknown")
vlMasksUnknown.id = currentid
currentid += 1
mdMasksUnknown = PORISMode("Masks_Unknown")
mdMasksUnknown.id = currentid
currentid += 1
mdMasksUnknown.values[vlMasksUnknown.name] = vlMasksUnknown
prMasks = PORISParam("Masks")
prMasks.id = currentid
currentid += 1
prMasks.addValue(vlMasksUnknown)
prMasks.addMode(mdMasksUnknown)


mdFilterUnknown = PORISMode("Filter_Unknown")
mdFilterUnknown.id = currentid
currentid += 1
sysFilter = PORISSys("Filter")
sysFilter.id = currentid
currentid += 1
sysFilter.addMode(mdFilterUnknown)

mdDetectorUnknown = PORISMode("Detector_Unknown")
mdDetectorUnknown.id = currentid
currentid += 1
sysDetector = PORISSys("Detector")
sysDetector.id = currentid
currentid += 1
sysDetector.addMode(mdDetectorUnknown)

# Root level
mdInstrumentUnknown = PORISMode("Instrument_Unknown")
mdInstrumentUnknown.id = currentid
currentid += 1
sysInstrument = PORISSys("Instrument")
sysInstrument.id = currentid
currentid += 1
sysInstrument.addMode(mdInstrumentUnknown)

# Param values
prClassicFilters.addValue(vlClassicFiltersRed)
prClassicFilters.addValue(vlClassicFiltersBlue)
prClassicFilters.addValue(vlClassicFiltersuserFilter)
prDispersion.addValue(vlDispersionR500)
prDispersion.addValue(vlDispersionR1000)
prDispersion.addValue(vlDispersionR2000)
prBinning.addValue(vlBinning1x1)
prBinning.addValue(vlBinning1x2)
prBinning.addValue(vlBinning2x1)
prBinning.addValue(vlBinning2x2)
prExpTime.addValue(vlExpTimeNormalRange)
prExpTime.addValue(vlExpTimeFastRange)
prMasks.addValue(vlMasks0_6)
prMasks.addValue(vlMasks1_0)
prMasks.addValue(vlMasks2_0)
prMasks.addValue(vlMasksHalf_field)

# Param modes
prClassicFilters.addMode(mdClassicFiltersRed)
prClassicFilters.addMode(mdClassicFiltersBlue)
prClassicFilters.addMode(mdClassicFiltersStandard)
prClassicFilters.addMode(mdClassicFiltersUser)

prDispersion.addMode(mdDispersionNormal)
prBinning.addMode(mdBinningNormal)
prBinning.addMode(mdBinningSquare)
prExpTime.addMode(mdExpTimeNormal)
prExpTime.addMode(mdExpTimeFast)
prMasks.addMode(mdMasksSpectroscopy)
prMasks.addMode(mdMasksFastImg)

# Sys modes
sysFilter.addMode(mdFilterTFRed)
sysFilter.addMode(mdFilterTFBlue)
sysFilter.addMode(mdFilterClassic)

sysDetector.addMode(mdDetectorNormal)
sysDetector.addMode(mdDetectorImage)
sysDetector.addMode(mdDetectorFastImage)

sysInstrument.addMode(mdInstrumentPhotometry)
sysInstrument.addMode(mdInstrumentSpectroscopy)
sysInstrument.addMode(mdInstrumentFastPhotometry)

# Architecture
sysFilter.addParam(prClassicFilters)
mdFilterUnknown.addSubMode(mdClassicFiltersUnknown)
sysDetector.addParam(prBinning)
mdDetectorUnknown.addSubMode(mdBinningUnknown)
sysDetector.addParam(prExpTime)
mdDetectorUnknown.addSubMode(mdExpTimeUnknown)
sysInstrument.addParam(prDispersion)
mdInstrumentUnknown.addSubMode(mdDispersionUnknown)
sysInstrument.addParam(prMasks)
mdInstrumentUnknown.addSubMode(mdMasksUnknown)
sysInstrument.addParam(sysFilter)
mdInstrumentUnknown.addSubMode(mdFilterUnknown)
sysInstrument.addParam(sysDetector)
mdInstrumentUnknown.addSubMode(mdDetectorUnknown)

# Relationships
mdClassicFiltersRed.addValue(vlClassicFiltersRed)
mdClassicFiltersBlue.addValue(vlClassicFiltersBlue)
mdClassicFiltersStandard.addValue(vlClassicFiltersRed)
mdClassicFiltersStandard.addValue(vlClassicFiltersBlue)
mdClassicFiltersUser.addValue(vlClassicFiltersuserFilter)

mdDispersionNormal.addValue(vlDispersionR500)
mdDispersionNormal.addValue(vlDispersionR2000)
mdDispersionNormal.addValue(vlDispersionR1000)

mdBinningNormal.addValue(vlBinning1x1)
mdBinningNormal.addValue(vlBinning1x2)
mdBinningNormal.addValue(vlBinning2x1)
mdBinningNormal.addValue(vlBinning2x2)

mdBinningSquare.addValue(vlBinning1x1)
mdBinningSquare.addValue(vlBinning2x2)

mdExpTimeNormal.addValue(vlExpTimeNormalRange)
mdExpTimeFast.addValue(vlExpTimeFastRange)

mdMasksSpectroscopy.addValue(vlMasks0_6)
mdMasksSpectroscopy.addValue(vlMasks1_0)
mdMasksSpectroscopy.addValue(vlMasks2_0)

mdMasksFastImg.addValue(vlMasksHalf_field)


mdFilterTFRed.addSubMode(mdClassicFiltersRed)
mdFilterTFBlue.addSubMode(mdClassicFiltersBlue)
mdFilterClassic.addSubMode(mdClassicFiltersStandard)
mdFilterClassic.addSubMode(mdClassicFiltersUser)

mdDetectorNormal.addSubMode(mdBinningNormal)
mdDetectorNormal.addSubMode(mdExpTimeNormal)
mdDetectorImage.addSubMode(mdBinningSquare)
mdDetectorImage.addSubMode(mdExpTimeNormal)
mdDetectorFastImage.addSubMode(mdBinningSquare)
mdDetectorFastImage.addSubMode(mdExpTimeFast)

mdInstrumentPhotometry.addSubMode(mdFilterTFRed)
mdInstrumentPhotometry.addSubMode(mdFilterTFBlue)
mdInstrumentPhotometry.addSubMode(mdFilterClassic)
mdInstrumentPhotometry.addSubMode(mdDetectorImage)

mdInstrumentSpectroscopy.addSubMode(mdFilterTFRed)
mdInstrumentSpectroscopy.addSubMode(mdFilterTFBlue)
mdInstrumentSpectroscopy.addSubMode(mdFilterClassic)
mdInstrumentSpectroscopy.addSubMode(mdDetectorNormal)
mdInstrumentSpectroscopy.addSubMode(mdMasksSpectroscopy)
mdInstrumentSpectroscopy.addSubMode(mdDispersionNormal)

mdInstrumentFastPhotometry.addSubMode(mdFilterClassic)
mdInstrumentFastPhotometry.addSubMode(mdDetectorFastImage)
mdInstrumentFastPhotometry.addSubMode(mdMasksFastImg)


print("\n\n\nSys:",sysInstrument.name)
print("\nmodes:",sysInstrument.modes)
print("\nselected:",sysInstrument.selectedMode.name)
print("\n\n\nPhotometry:",mdInstrumentPhotometry.name)
print("\nsubmodes:",mdInstrumentPhotometry.submodes)
print("\n\n\nSys:",sysFilter.name)
print("\nmodes:",sysFilter.modes)
print("\nselected:",sysFilter.selectedMode.name)
print("\n\n\nSys:",sysDetector.name)
print("\nmodes:",sysDetector.modes)
print("\nselected:",sysDetector.selectedMode.name)
print("\n\n\nParam:",prClassicFilters.name)
print("\nmodes:",prClassicFilters.modes)
print("\nselected:",prClassicFilters.selectedMode.name)
print("\nvalues:",prClassicFilters.values)
print("\nselected:",prClassicFilters.selectedValue.name)
print("\n\n\nParam:",prDispersion.name)
print("\nmodes:",prDispersion.modes)
print("\nselected:",prDispersion.selectedMode.name)
print("\nvalues:",prDispersion.values)
print("\nselected:",prDispersion.selectedValue.name)
print("\n\n\nParam:",prBinning.name)
print("\nmodes:",prBinning.modes)
print("\nselected:",prBinning.selectedMode.name)
print("\nvalues:",prBinning.values)
print("\nselected:",prBinning.selectedValue.name)
print("\n\n\nParam:",prExpTime.name)
print("\nmodes:",prExpTime.modes)
print("\nselected:",prExpTime.selectedMode.name)
print("\nvalues:",prExpTime.values)
print("\nselected:",prExpTime.selectedValue.name)
print("\n\n\nParam:",prMasks.name)
print("\nmodes:",prMasks.modes)
print("\nselected:",prMasks.selectedMode.name)
print("\nvalues:",prMasks.values)
print("\nselected:",prMasks.selectedValue.name)

print("\n\nSquare binning values:",mdBinningSquare.values)

sysInstrument.setMode(mdInstrumentPhotometry)
print("\n\n\nSelected filter:",prClassicFilters.selectedValue.name)
print("\n\n\nSelected dispersion:",prDispersion.selectedValue.name)
print("\n\n\nSelected detector mode:",sysDetector.selectedMode.name)
print("\n\n\nSelected binning mode:",prBinning.selectedMode.name)
print("\n\n\nSelected binning:",prBinning.selectedValue.name)
print("\n\n\nSelected expTime:",prExpTime.selectedValue.name)
print("\n\n\nSelected mask:",prMasks.selectedValue.name)

prBinning.setValue(vlBinning2x2)
print("\n\n\nSelected binning:",prBinning.selectedValue.name)
prBinning.setValue(vlBinning1x2)
print("\n\n\nSelected binning:",prBinning.selectedValue.name)
sysInstrument.setMode(mdInstrumentSpectroscopy)
print("\n\n\nSelected instrument mode:",sysInstrument.selectedMode.name)
print("\n\n\nSpectroscopy submodes:",mdInstrumentSpectroscopy.submodes)
print("\n\n\nSelected filter:",prClassicFilters.selectedValue.name)
print("\n\n\nSelected dispersion:",prDispersion.selectedValue.name)
print("\n\n\nSelected detector mode:",sysDetector.selectedMode.name)
print("\n\n\nSelected binning mode:",prBinning.selectedMode.name)
print("\n\n\nSelected binning:",prBinning.selectedValue.name)
print("\n\n\nSelected expTime:",prExpTime.selectedValue.name)
print("\n\n\nSelected masks mode:",prMasks.selectedMode.name)
print("\n\n\nSelected mask:",prMasks.selectedValue.name)
prBinning.setValue(vlBinning1x2)
print("\n\n\nSelected instrument mode:",sysInstrument.selectedMode.name)
print("\n\n\nSpectroscopy submodes:",mdInstrumentSpectroscopy.submodes)
print("\n\n\nSelected filter:",prClassicFilters.selectedValue.name)
print("\n\n\nSelected dispersion:",prDispersion.selectedValue.name)
print("\n\n\nSelected detector mode:",sysDetector.selectedMode.name)
print("\n\n\nSelected binning mode:",prBinning.selectedMode.name)
print("\n\n\nSelected binning:",prBinning.selectedValue.name)
print("\n\n\nSelected expTime:",prExpTime.selectedValue.name)
print("\n\n\nSelected masks mode:",prMasks.selectedMode.name)
print("\n\n\nSelected mask:",prMasks.selectedValue.name)