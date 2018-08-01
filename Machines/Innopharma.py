import OpenOPC
import pandas as pd


#############
##Define Names##
#############

server_name = 'Kepware.KEPServerEX.V5'
twin_screw_plc = 'TSWG.PLC.'
feeder_plc = 'Feeder.PLC.'


## Multieye Controls ##

Start	=	'Start'
Stop	=	'Stop'
Continuous	=	'Continuous'
StartWhiteRef	=	'StartWhiteRef'
NumberOfSpectra	=	'NumberOfSpectra'
NumberOfRepeats	=	'NumberOfRepeats'
MeasurementInterval	=	'MeasurementInterval'
StartWl	=	'StartWl'
EndWl	=	'EndWl'
StepWl	=	'StepWl'
SamplesPerWl	=	'SamplesPerWl'
DarkRefPeriod	=	'DarkRefPeriod'
ModelName	=	'ModelName'
SessionName	=	'SessionName'
BatchName	=	'BatchName'

## Multieye Values ##

SessionStatus	=	'SessionStatus'
ScanInProgress	=	'ScanInProgress'
ScanOnPause	=	'ScanOnPause'
WhiteRefStatus	=	'WhiteRefStatus'
ErrorStatus	=	'ErrorStatus'
ErrorString	=	'ErrorString'
ModelsNames	=	'ModelsNames'
ScanTime	=	'ScanTime'
DeviceTemperature	=	'DeviceTemperature'
SerialNumber	=	'SerialNumber'
SWVersion	=	'SWVersion'
NoOfChannels	=	'NoOfChannels'
NumOfPoints	=	'NumOfPoints'
Ch1_Intensity	=	'Ch1_Intensity'
Ch2_Intensity	=	'Ch2_Intensity'
Ch3_Intensity	=	'Ch3_Intensity'
Ch4_Intensity	=	'Ch4_Intensity'
Ch1_Reflectance	=	'Ch1_Reflectance'
Ch2_Reflectance	=	'Ch2_Reflectance'
Ch3_Reflectance	=	'Ch3_Reflectance'
Ch4_Reflectance	=	'Ch4_Reflectance'
Ch1_Absorbance	=	'Ch1_Absorbance'
Ch2_Absorbance	=	'Ch2_Absorbance'
Ch3_Absorbance	=	'Ch3_Absorbance'
Ch4_Absorbance	=	'Ch4_Absorbance'
Ch1_BlCorrAbsorbance	=	'Ch1_BlCorrAbsorbance'
Ch2_BlCorrAbsorbance	=	'Ch2_BlCorrAbsorbance'
Ch3_BlCorrAbsorbance	=	'Ch3_BlCorrAbsorbance'
Ch4_BlCorrAbsorbance	=	'Ch4_BlCorrAbsorbance'
Ch1_WhiteRef	=	'Ch1_WhiteRef'
Ch2_WhiteRef	=	'Ch2_WhiteRef'
Ch3_WhiteRef	=	'Ch3_WhiteRef'
Ch4_WhiteRef	=	'Ch4_WhiteRef'
Ch1_DarkRef	=	'Ch1_DarkRef'
Ch2_DarkRef	=	'Ch2_DarkRef'
Ch3_DarkRef	=	'Ch3_DarkRef'
Ch4_DarkRef	=	'Ch4_DarkRef'
AnalysisResults	=	'AnalysisResults'
AnalysisLabels	=	'AnalysisLabels'

## Eyecon Inputs ##
SessionID1	=	'SessionID1'
SessionID2	=	'SessionID2'
SessionID3	=	'SessionID3'
ConfigName	=	'ConfigName'
User	=	'User'
Password	=	'Password'
Start	=	'Start'
Stop	=	'Stop'
NewSessionComment	=	'NewSessionComment'

## Eyecon Outputs ##

Dn10	=	'Dn10'
Dn25	=	'Dn25'
Dn50	=	'Dn50'
Dn75	=	'Dn75'
Dn90	=	'Dn90'
Dv10	=	'Dv10'
Dv25	=	'Dv25'
Dv50	=	'Dv50'
Dv75	=	'Dv75'
Dv90	=	'Dv90'
VolumetricHistogramBinEdges	=	'VolumetricHistogramBinEdges'
VolumetricHistogramBinEdges	=	'VolumetricHistogramBinEdges'
NumericHistogramBinEdges	=	'NumericHistogramBinEdges'
NumericHistogram	=	'NumericHistogram'
Mean	=	'Mean'
Median	=	'Median'
Error	=	'Error'
ErrorMessage	=	'ErrorMessage'
Configurations	=	'Configurations'
SessionStatus	=	'SessionStatus'


## Classes ###

class multieye:
	def __init__(self):
		self.opc = OpenOPC.client()
		self.opc.connect(server_name)


## Define commands ##

    def setup_session(sessionname, batchname, self):
        self.opc.write(SessionName, sessionname)
        self.opc.write(BatchName, batchname)

    def setup_measurement(startwl, endwl, step, numspec, numrep, interval = 0, smpls = 500, drkreftime = 30, self):
        self.opc.write(StartWl, startwl)
        self.opc.write(EndWl, endwl)
        self.opc.write(StepWl, step)
        self.opc.write(NumberOfSpectra, numspec)
        self.opc.write(NumberOfRepeats, numrep)
        self.opc.write(MeasurementInterval, interval)
        self.opc.write(SamplesPerWl, smpls)
        self.opc.write(DarkRefPeriod, drkreftime)

    def start_ME(self):
        self.opc.write(Start, 1)

    def stop_ME(self):
        self.opc.write(Stop, 1)

## Define readable functions ##
