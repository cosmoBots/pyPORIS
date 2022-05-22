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
prClassicFilters.values[vlClassicFiltersUnknown.name] = vlClassicFiltersUnknown
prClassicFilters.selectedValue = vlClassicFiltersUnknown
vlClassicFiltersUnknown.parent = prClassicFilters
prClassicFilters.modes[mdClassicFiltersUnknown.name] = mdClassicFiltersUnknown
prClassicFilters.selectedMode = mdClassicFiltersUnknown
mdClassicFiltersUnknown.parent = prClassicFilters

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
prBinning.values[vlBinningUnknown.name] = vlBinningUnknown
prBinning.selectedValue = vlBinningUnknown
vlBinningUnknown.parent = prBinning
prBinning.modes[mdBinningUnknown.name] = mdBinningUnknown
prBinning.selectedMode = mdBinningUnknown
mdBinningUnknown.parent = prBinning

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
prExpTime.values[vlExpTimeUnknown.name] = vlExpTimeUnknown
prExpTime.selectedValue = vlExpTimeUnknown
vlExpTimeUnknown.parent = prExpTime
prExpTime.modes[mdExpTimeUnknown.name] = mdExpTimeUnknown
prExpTime.selectedMode = mdExpTimeUnknown
mdExpTimeUnknown.parent = prExpTime

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
prDispersion.values[vlDispersionUnknown.name] = vlDispersionUnknown
prDispersion.selectedValue = vlDispersionUnknown
vlDispersionUnknown.parent = prDispersion
prDispersion.modes[mdDispersionUnknown.name] = mdDispersionUnknown
prDispersion.selectedMode = mdDispersionUnknown
mdDispersionUnknown.parent = prDispersion

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
prMasks.values[vlMasksUnknown.name] = vlMasksUnknown
prMasks.selectedValue = vlMasksUnknown
vlMasksUnknown.parent = prMasks
prMasks.modes[mdMasksUnknown.name] = mdMasksUnknown
prMasks.selectedMode = mdMasksUnknown
mdMasksUnknown.parent = prMasks

mdFilterUnknown = PORISMode("Filter_Unknown")
mdFilterUnknown.id = currentid
currentid += 1
sysFilter = PORISSys("Filter")
sysFilter.id = currentid
currentid += 1
sysFilter.modes[mdFilterUnknown.name] = mdFilterUnknown
sysFilter.selectedMode = mdFilterUnknown
mdFilterUnknown.parent = sysFilter

mdDetectorUnknown = PORISMode("Detector_Unknown")
mdDetectorUnknown.id = currentid
currentid += 1
sysDetector = PORISSys("Detector")
sysDetector.id = currentid
currentid += 1
sysDetector.modes[mdDetectorUnknown.name] = mdDetectorUnknown
sysDetector.selectedMode = mdDetectorUnknown
mdDetectorUnknown.parent = sysDetector

# Root level
mdInstrumentUnknown = PORISMode("Instrument_Unknown")
mdInstrumentUnknown.id = currentid
currentid += 1
sysInstrument = PORISSys("Instrument")
sysInstrument.id = currentid
currentid += 1
sysInstrument.modes[mdInstrumentUnknown.name] = mdInstrumentUnknown
sysInstrument.selectedMode = mdInstrumentUnknown
mdInstrumentUnknown.parent = sysInstrument

# Param values
vlClassicFiltersRed.parent = prClassicFilters
vlClassicFiltersBlue.parent = prClassicFilters
vlClassicFiltersuserFilter.parent = prClassicFilters
vlDispersionR500.parent = prDispersion
vlDispersionR1000.parent = prDispersion
vlDispersionR2000.parent = prDispersion
vlBinning1x1.parent = prBinning
vlBinning1x2.parent = prBinning
vlBinning2x1.parent = prBinning
vlBinning2x2.parent = prBinning
vlExpTimeNormalRange.parent = prExpTime
vlExpTimeFastRange.parent = prExpTime
vlMasks0_6.parent = prMasks
vlMasks1_0.parent = prMasks
vlMasks2_0.parent = prMasks
vlMasksHalf_field.parent = prMasks

prClassicFilters.values[vlClassicFiltersRed.name] = vlClassicFiltersRed
prClassicFilters.values[vlClassicFiltersBlue.name] = vlClassicFiltersBlue
prClassicFilters.values[vlClassicFiltersuserFilter.name] = vlClassicFiltersuserFilter
prDispersion.values[vlDispersionR500.name] = vlDispersionR500
prDispersion.values[vlDispersionR1000.name] = vlDispersionR1000
prDispersion.values[vlDispersionR2000.name] = vlDispersionR2000
prBinning.values[vlBinning1x1.name] = vlBinning1x1
prBinning.values[vlBinning1x2.name] = vlBinning1x2
prBinning.values[vlBinning2x1.name] = vlBinning2x1
prBinning.values[vlBinning2x2.name] = vlBinning2x2
prExpTime.values[vlExpTimeNormalRange.name] = vlExpTimeNormalRange
prExpTime.values[vlExpTimeFastRange.name] = vlExpTimeFastRange
prMasks.values[vlMasks0_6.name] = vlMasks0_6
prMasks.values[vlMasks1_0.name] = vlMasks1_0
prMasks.values[vlMasks2_0.name] = vlMasks2_0
prMasks.values[vlMasksHalf_field.name] = vlMasksHalf_field

# Param modes
prClassicFilters.modes[mdClassicFiltersRed.name] = mdClassicFiltersRed
mdClassicFiltersRed.parent = prClassicFilters
prClassicFilters.modes[mdClassicFiltersBlue.name] = mdClassicFiltersBlue
mdClassicFiltersBlue.parent = prClassicFilters
prClassicFilters.modes[mdClassicFiltersStandard.name] = mdClassicFiltersStandard
mdClassicFiltersStandard.parent = prClassicFilters
prClassicFilters.modes[mdClassicFiltersUser.name] = mdClassicFiltersUser
mdClassicFiltersUser.parent = prClassicFilters

prDispersion.modes[mdDispersionNormal.name] = mdDispersionNormal
mdDispersionNormal.parent = prDispersion
prBinning.modes[mdBinningNormal.name] = mdBinningNormal
mdBinningNormal.parent = prBinning
prBinning.modes[mdBinningSquare.name] = mdBinningSquare
mdBinningSquare.parent = prBinning
prExpTime.modes[mdExpTimeNormal.name] = mdExpTimeNormal
mdExpTimeNormal.parent = prExpTime
prExpTime.modes[mdExpTimeFast.name] = mdExpTimeFast
mdExpTimeFast.parent = prExpTime
prMasks.modes[mdMasksSpectroscopy.name] = mdMasksSpectroscopy
mdMasksSpectroscopy.parent = prMasks
prMasks.modes[mdMasksFastImg.name] = mdMasksFastImg
mdMasksFastImg.parent = prMasks

# Sys modes
sysFilter.modes[mdFilterTFRed.name] = mdFilterTFRed
mdFilterTFRed.parent = sysFilter
sysFilter.modes[mdFilterTFBlue.name] = mdFilterTFBlue
mdFilterTFBlue.parent = sysFilter
sysFilter.modes[mdFilterClassic.name] = mdFilterClassic
mdFilterClassic.parent = sysFilter

sysDetector.modes[mdDetectorNormal.name] = mdDetectorNormal
mdDetectorNormal.parent = sysDetector
sysDetector.modes[mdDetectorImage.name] = mdDetectorImage
mdDetectorImage.parent = sysDetector
sysDetector.modes[mdDetectorFastImage.name] = mdDetectorFastImage
mdDetectorFastImage.parent = sysDetector

sysInstrument.modes[mdInstrumentPhotometry.name] = mdInstrumentPhotometry
mdInstrumentPhotometry.parent = sysInstrument
sysInstrument.modes[mdInstrumentSpectroscopy.name] = mdInstrumentSpectroscopy
mdInstrumentSpectroscopy.parent = sysInstrument
sysInstrument.modes[mdInstrumentFastPhotometry.name] = mdInstrumentFastPhotometry
mdInstrumentFastPhotometry.parent = sysInstrument

# Architecture
sysFilter.params[prClassicFilters.name] = prClassicFilters
prClassicFilters.parent = sysFilter
sysDetector.params[prBinning.name] = prBinning
prBinning.parent = sysDetector
sysDetector.params[prExpTime.name] = prExpTime
prExpTime.parent = sysDetector
sysInstrument.params[prDispersion.name] = prDispersion
prDispersion.parent = sysInstrument
sysInstrument.params[prMasks.name] = prMasks
prMasks.parent = sysInstrument
sysInstrument.subsystems[sysFilter.name] = sysFilter
sysFilter.parent = sysInstrument
sysInstrument.subsystems[sysDetector.name] = sysDetector
sysDetector.parent = sysInstrument

# Relationships
mdClassicFiltersRed.values[vlClassicFiltersRed.name] = vlClassicFiltersRed
mdClassicFiltersBlue.values[vlClassicFiltersBlue.name] = vlClassicFiltersBlue
mdClassicFiltersStandard.values[vlClassicFiltersRed.name] = vlClassicFiltersRed
mdClassicFiltersStandard.values[vlClassicFiltersBlue.name] = vlClassicFiltersBlue
mdClassicFiltersUser.values[vlClassicFiltersuserFilter.name] = vlClassicFiltersuserFilter

mdDispersionNormal.values[vlDispersionR500.name] = vlDispersionR500
mdDispersionNormal.values[vlDispersionR2000.name] = vlDispersionR2000
mdDispersionNormal.values[vlDispersionR1000.name] = vlDispersionR1000

mdBinningNormal.values[vlBinning1x1.name] = vlBinning1x1
mdBinningNormal.values[vlBinning1x2.name] = vlBinning1x2
mdBinningNormal.values[vlBinning2x1.name] = vlBinning2x1
mdBinningNormal.values[vlBinning2x1.name] = vlBinning2x2

mdBinningSquare.values[vlBinning1x1.name] = vlBinning1x1
mdBinningSquare.values[vlBinning2x2.name] = vlBinning2x2

mdExpTimeNormal.values[vlExpTimeNormalRange.name] =  vlExpTimeNormalRange
mdExpTimeFast.values[vlExpTimeFastRange.name] =  vlExpTimeFastRange

mdMasksSpectroscopy.values[vlMasks0_6.name] = vlMasks0_6
mdMasksSpectroscopy.values[vlMasks1_0.name] = vlMasks1_0
mdMasksSpectroscopy.values[vlMasks2_0.name] = vlMasks2_0

mdMasksFastImg.values[vlMasksHalf_field.name] = vlMasksHalf_field

mdFilterTFRed.submodes[mdClassicFiltersRed.name] = mdClassicFiltersRed
mdFilterTFBlue.submodes[mdClassicFiltersBlue.name] = mdClassicFiltersBlue
mdFilterClassic.submodes[mdClassicFiltersStandard.name] = mdClassicFiltersStandard
mdFilterClassic.submodes[mdClassicFiltersUser.name] = mdClassicFiltersUser

mdDetectorNormal.submodes[mdBinningNormal.name] = mdBinningNormal
mdDetectorNormal.submodes[mdExpTimeNormal.name] = mdExpTimeNormal
mdDetectorImage.submodes[mdBinningSquare.name] = mdBinningSquare
mdDetectorImage.submodes[mdExpTimeNormal.name] = mdExpTimeNormal
mdDetectorFastImage.submodes[mdBinningSquare.name] = mdBinningSquare
mdDetectorFastImage.submodes[mdExpTimeFast.name] = mdExpTimeFast

mdInstrumentPhotometry.submodes[mdFilterTFRed.name] = mdFilterTFRed
mdInstrumentPhotometry.submodes[mdFilterTFBlue.name] = mdFilterTFBlue
mdInstrumentPhotometry.submodes[mdFilterClassic.name] = mdFilterClassic
mdInstrumentPhotometry.submodes[mdDetectorImage.name] = mdDetectorImage

mdInstrumentSpectroscopy.submodes[mdFilterTFRed.name] = mdFilterTFRed
mdInstrumentSpectroscopy.submodes[mdFilterTFBlue.name] = mdFilterTFBlue
mdInstrumentSpectroscopy.submodes[mdFilterClassic.name] = mdFilterClassic
mdInstrumentSpectroscopy.submodes[mdDetectorNormal.name] = mdDetectorNormal
mdInstrumentSpectroscopy.submodes[mdMasksSpectroscopy.name] = mdMasksSpectroscopy
mdInstrumentSpectroscopy.submodes[mdDispersionNormal.name] = mdDispersionNormal

mdInstrumentFastPhotometry.submodes[mdFilterClassic.name] = mdFilterClassic
mdInstrumentFastPhotometry.submodes[mdDetectorFastImage.name] = mdDetectorFastImage
mdInstrumentFastPhotometry.submodes[mdMasksFastImg.name] = mdMasksFastImg


print("\n\n\nSys:",sysInstrument.name)
print("\nmodes:",sysInstrument.modes)
print("\nselected:",sysInstrument.selectedMode)
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