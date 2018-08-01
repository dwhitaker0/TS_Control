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

running = 1

#####################
###Define Machines###
#####################

#twinscrew
ts = tt.twinscrew()
ts.remote_on()
#logger.info ("Twin Screw Connected")

#feeder
f = tt.feeder()
f.remote_on()
#logger.info ("Feeder Connected")

#syringepump
sp = fsp.sPump("COM4")
#logger.info ("Syringe Pump Connected")

###############
## Functions ##
###############

def set_point_set():
	#global ts_rpm
	#global feed_rate
	#global pump_speed
	ts.set_rate(ts_rpm)
	f.set_rate(feed_rate)
	sp.set_flow_rate(pump_speed)
	
def machines_start():
	ts.start()
	time.sleep(2)
	f.start()
	time.sleep(0.5)
	sp.start()
	
def machines_stop():
	sp.stop()
	f.stop()
	time.sleep(0.5)
	ts.stop()



def start_experimental_series():
	time.sleep(5)
	params = pd.read_csv("Parameters.csv")
	ts_rpm = int(params.iloc[0, 0])
	feed_rate = int(params.iloc[0, 1])
	pump_speed = int(params.iloc[0, 2])
	set_point_set()
	time.sleep(5)
	machines_start()
	#logger.info ("Initialised")
	time.sleep(5)


	try: 
		for i in range (0, params.shape[0]):
			ts_rpm = params.iloc[i, 0]
			feed_rate = params.iloc[i, 1]
			pump_speed = params.iloc[i, 2]
			set_point_set()
			#logger.info ("Set Points Changed", ts_rpm, feed_rate, pump_speed)
			time.sleep(params.loc[i,3])
			
	except KeyboardInterrupt: 
		machines_stop()
		collect_process_data.collect_data = 0
		#logger.info ("Keyboard Interrupt")
		running = 0
	
	running = 0
	