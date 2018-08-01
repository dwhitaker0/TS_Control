from Machines import Three_Tec as tt
from Machines import FusionSyringePump as fsp
import pandas as pd
import numpy as np
import time
import os
import threading
#import collect_process_data
import datetime
import logging
import serial

####Graphing Modules####
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
########################


#############
##define threads## :: The data collection is run as a seperate thread to allow the interpreter to continue
#############
experiment_thread = threading.Thread(name = "Experiments", target = Parameter_Loop.start_experimental_series)


#############
### Input ###
#############

global experiment_name
experiment_name = raw_input("Enter Experiment Name: ")
interval = raw_input("Enter Data Collection Interval: ")
collect_process_data.interval = float(interval)
start_time = float(time.time())
today = datetime.date.today()  
todaystr = today.isoformat() 
experiment_name = "./data/" + todaystr + "/" + experiment_name


if os.path.exists(experiment_name):
	print("Experiment already exists . . . . exiting")
	time.sleep (5)
	sys.exit()
else:
	os.makedirs(experiment_name)
	
	
	
	
##################	
##Set up logging##
##################

log_formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

#File to log to
logFile = os.path.join(experiment_name) + "/logfile.txt"

#Setup File handler
file_handler = logging.FileHandler(logFile)
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.INFO)

#Setup Stream Handler (console)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
stream_handler.setLevel(logging.INFO)

#Get logger
logger = logging.getLogger('root')
logger.setLevel(logging.INFO)

#Add both Handlers
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

#####################
###Define Machines###
#####################

#twinscrew
ts = tt.twinscrew()
ts.remote_on()
logger.info ("Twin Screw Connected")

#feeder
f = tt.feeder()
f.remote_on()
logger.info ("Feeder Connected")

#syringepump
sp = fsp.sPump("COM4")
logger.info ("Syringe Pump Connected")

### Set up Graphing ###
#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)

win = pg.GraphicsWindow(title="TwinScrew Experiment Data")
win.resize(1000,600)
win.setWindowTitle('TwinScrew Experiment Data ')


p1 = win.addPlot(title="Extruder RPM")
p1_plot = p1.plot(pen='y')
p2 = win.addPlot(title="Feed Rate")
p2_plot = p2.plot(pen='r')
win.nextRow()

p3 = win.addPlot(title="Extruder Torque")
p3_plot = p3.plot(pen='y')
p4 = win.addPlot(title="Feeder Weight")
p4_plot = p4.plot(pen='r')

##########################
	

###############
## Functions ##
###############

def update_plot():
	p1_plot.setData(plot_t, np.array(full_res.iloc[:,2]))
	p2_plot.setData(plot_t, np.array(full_res.iloc[:,35]))
	p3_plot.setData(plot_t, np.array(full_res.iloc[:,4]))
	p4_plot.setData(plot_t, np.array(full_res.iloc[:,29]))
	pg.QtGui.QApplication.processEvents()


### Run Experiments ####



experiment_thread.start()
logger.info("Experiment Started")

results = pd.concat([ts.read_values(), f.read_values()], axis = 1)
t = pd.Series(time.strftime("%H:%M:%S | %d-%m-%Y"))
full_res = pd.concat([t, results], axis = 1)
start_time = float(time.time())
plot_t = np.array([(start_time - float(time.time()))])
#print("######Recording Data. Push Ctrl+C to stop######")


try:
	while (Parameter_Loop.running == 1):
		results = results.append(pd.concat([ts.read_values(), f.read_values()], axis = 1))
		t = t.append(pd.Series(time.strftime("%H:%M:%S | %d-%m-%Y")))		
		full_res = pd.concat([t, results], axis = 1)
		full_res.to_csv(os.path.join(experiment_name) +'/results.csv')
		#print ("Recorded at ", time.strftime("%H:%M:%S | %d-%m-%Y"))
		read_time = float(time.time())
		plot_t = np.append(plot_t, (read_time - start_time))
		update_plot()
		time.sleep(interval)
		
except KeyboardInterrupt: 
		Parameter_Loop.machines_stop()
		logger.info ("Keyboard Interrupt")

		
##Shutdown function ##
Parameter_Loop.machines_stop()
		



