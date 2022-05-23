from PORIS import *

class ExamplePORIS(PORISSys):
    def __init__(self,name):
        super(ExamplePORIS, self).__init__(name)
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

        # Architecture
        sysFilter.addParam(prClassicFilters)
        mdFilterUnknown.addSubMode(mdClassicFiltersUnknown)
        sysDetector.addParam(prBinning)
        mdDetectorUnknown.addSubMode(mdBinningUnknown)
        sysDetector.addParam(prExpTime)
        mdDetectorUnknown.addSubMode(mdExpTimeUnknown)

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

        # Root level
        mdExampleUnknown = PORISMode("Example_Unknown")
        mdExampleUnknown.id = currentid
        currentid += 1

        mdExamplePhotometry = PORISMode("Example_Photometry")
        mdExamplePhotometry.id = currentid
        currentid += 1
        mdExampleSpectroscopy = PORISMode("Example_Spectroscopy")
        mdExampleSpectroscopy.id = currentid
        currentid += 1
        mdExampleFastPhotometry = PORISMode("Example_FastPhotometry")
        mdExampleFastPhotometry.id = currentid
        currentid += 1

        mdExampleUnknown.addSubMode(mdDispersionUnknown)
        mdExampleUnknown.addSubMode(mdMasksUnknown)
        mdExampleUnknown.addSubMode(mdFilterUnknown)
        mdExampleUnknown.addSubMode(mdDetectorUnknown)

        mdExamplePhotometry.addSubMode(mdFilterTFRed)
        mdExamplePhotometry.addSubMode(mdFilterTFBlue)
        mdExamplePhotometry.addSubMode(mdFilterClassic)
        mdExamplePhotometry.addSubMode(mdDetectorImage)

        mdExampleSpectroscopy.addSubMode(mdFilterTFRed)
        mdExampleSpectroscopy.addSubMode(mdFilterTFBlue)
        mdExampleSpectroscopy.addSubMode(mdFilterClassic)
        mdExampleSpectroscopy.addSubMode(mdDetectorNormal)
        mdExampleSpectroscopy.addSubMode(mdMasksSpectroscopy)
        mdExampleSpectroscopy.addSubMode(mdDispersionNormal)

        mdExampleFastPhotometry.addSubMode(mdFilterClassic)
        mdExampleFastPhotometry.addSubMode(mdDetectorFastImage)
        mdExampleFastPhotometry.addSubMode(mdMasksFastImg)

        
        # sysExample = PORISSys("Example")
        self.id = currentid
        currentid += 1
        self.addMode(mdExampleUnknown)
        self.addMode(mdExamplePhotometry)
        self.addMode(mdExampleSpectroscopy)
        self.addMode(mdExampleFastPhotometry)
        print(self.modes)
        print(self.params)
        self.addParam(prDispersion)
        self.addParam(prMasks)
        self.addSubsystem(sysFilter)
        self.addSubsystem(sysDetector)

        

sysExample = ExamplePORIS("example")


print("\n\n\nSys:",sysExample.name)
print("\nmodes:",sysExample.modes)
print("\nselected:",sysExample.selectedMode.name)
'''
print("\n\n\nPhotometry:",mdExamplePhotometry.name)
print("\nsubmodes:",mdExamplePhotometry.submodes)
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
'''
mdExamplePhotometry = sysExample.getModeFromName("Example_Photometry")
sysExample.setMode(mdExamplePhotometry)
'''
print("\n\n\nSelected filter:",prClassicFilters.selectedValue.name)
print("\n\n\nSelected dispersion:",prDispersion.selectedValue.name)
print("\n\n\nSelected detector mode:",sysDetector.selectedMode.name)
print("\n\n\nSelected binning mode:",prBinning.selectedMode.name)
'''
prBinning = sysExample.getDescendantParamFromName("Binning")
print("\n\n\nSelected binning:",prBinning.selectedValue.name)
prDispersion = sysExample.getDescendantParamFromName("Dispersion")
print("\n\n\nSelected dispersion:",prDispersion.selectedValue.name)

'''
print("\n\n\nSelected expTime:",prExpTime.selectedValue.name)
print("\n\n\nSelected mask:",prMasks.selectedValue.name)
'''
vlBinning2x2 = prBinning.getValueFromName("2x2")
prBinning.setValue(vlBinning2x2)
print("\n\n\nSelected binning:",prBinning.selectedValue.name)
print("\n\n\nSelected dispersion:",prDispersion.selectedValue.name)
vlBinning1x2 = prBinning.getValueFromName("1x2")
prBinning.setValue(vlBinning1x2)
print("\n\n\nSelected binning:",prBinning.selectedValue.name)
print("\n\n\nSelected dispersion:",prDispersion.selectedValue.name)
mdExampleSpectroscopy = sysExample.getModeFromName("Example_Spectroscopy")
sysExample.setMode(mdExampleSpectroscopy)
print("\n\n\nSelected binning:",prBinning.selectedValue.name)
print("\n\n\nSelected dispersion:",prDispersion.selectedValue.name)
prBinning.setValue(vlBinning1x2)
print("\n\n\nSelected binning:",prBinning.selectedValue.name)
print("\n\n\nSelected dispersion:",prDispersion.selectedValue.name)
sysExample.setMode(mdExamplePhotometry)
print("\n\n\nSelected binning:",prBinning.selectedValue.name)
print("\n\n\nSelected dispersion:",prDispersion.selectedValue.name)

'''
print("\n\n\nSelected Example mode:",sysExample.selectedMode.name)
print("\n\n\nSpectroscopy submodes:",mdExampleSpectroscopy.submodes)
print("\n\n\nSelected filter:",prClassicFilters.selectedValue.name)
print("\n\n\nSelected dispersion:",prDispersion.selectedValue.name)
print("\n\n\nSelected detector mode:",sysDetector.selectedMode.name)
print("\n\n\nSelected binning mode:",prBinning.selectedMode.name)
print("\n\n\nSelected binning:",prBinning.selectedValue.name)
print("\n\n\nSelected expTime:",prExpTime.selectedValue.name)
print("\n\n\nSelected masks mode:",prMasks.selectedMode.name)
print("\n\n\nSelected mask:",prMasks.selectedValue.name)
prBinning.setValue(vlBinning1x2)
print("\n\n\nSelected Example mode:",sysExample.selectedMode.name)
print("\n\n\nSpectroscopy submodes:",mdExampleSpectroscopy.submodes)
print("\n\n\nSelected filter:",prClassicFilters.selectedValue.name)
print("\n\n\nSelected dispersion:",prDispersion.selectedValue.name)
print("\n\n\nSelected detector mode:",sysDetector.selectedMode.name)
print("\n\n\nSelected binning mode:",prBinning.selectedMode.name)
print("\n\n\nSelected binning:",prBinning.selectedValue.name)
print("\n\n\nSelected expTime:",prExpTime.selectedValue.name)
print("\n\n\nSelected masks mode:",prMasks.selectedMode.name)
print("\n\n\nSelected mask:",prMasks.selectedValue.name)
'''    
