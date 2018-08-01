from Machines import Three_Tec as tt
from Machines import FusionSyringePump as fsp
import pandas as pd
import numpy as np
import time
import os
import datetime
import sys

####Graphing Modules####
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
########################


#### Connect ####
ts = tt.twinscrew()
print ("Connected: Twin Screw")
time.sleep(0.5)
f = tt.feeder()
print ("Connected: Feeder")
time.sleep(0.5)
##################

### User input ####
experiment_name = raw_input("Enter Experiment Name: ")
interval = raw_input("Enter Data Collection Interval: ")
interval = float(interval)
today = datetime.date.today()  
todaystr = today.isoformat() 
experiment_name = "./data/" + todaystr + "/" + experiment_name

if os.path.exists(experiment_name):
	print("Experiment already exists . . . . exiting")
	time.sleep (3)
	sys.exit()
else:
	os.makedirs(experiment_name)
#####################

### Set up Graphing ###
#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)

win = pg.GraphicsWindow(title="TwinScrew Experiment Data")
win.resize(1000,600)
win.setWindowTitle('TwinScrew Experiment Data')


p1 = win.addPlot(title="Extruder RPM")
p1_plot = p1.plot(pen='y')
p1_plot_sp = p1.plot(pen='b')
p2 = win.addPlot(title="Feed Rate")
p2_plot = p2.plot(pen='r')
p2_plot_sp = p1.plot(pen='b')
win.nextRow()

p3 = win.addPlot(title="Extruder Torque")
p3_plot = p3.plot(pen='y')
p4 = win.addPlot(title="Feeder Weight")
p4_plot = p4.plot(pen='r')

##########################

###########################

results = pd.concat([ts.read_values(), f.read_values()], axis = 1)
t = pd.Series(time.strftime("%H:%M:%S | %d-%m-%Y"))
full_res = pd.concat([t, results], axis = 1)
start_time = float(time.time())
plot_t = np.array([(start_time - float(time.time()))])
print("######Recording Data. Push Ctrl+C to stop######")

def update_plot():
	p1_plot.setData(plot_t, np.array(full_res.iloc[:,2]))
	p1_plot_sp.setData(plot_t, np.array(full_res.iloc[:,3]))
	p2_plot.setData(plot_t, np.array(full_res.iloc[:,35]))
	p2_plot_sp.setData(plot_t, np.array(full_res.iloc[:,33]))
	p3_plot.setData(plot_t, np.array(full_res.iloc[:,4]))
	p4_plot.setData(plot_t, np.array(full_res.iloc[:,29]))
	pg.QtGui.QApplication.processEvents()


	
try:
	while True:
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
	print("Keyboard Interrupt - Stopping....")
	time.sleep(5)
	sys.exit()