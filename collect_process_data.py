from Machines import Three_Tec as tt
from Machines import FusionSyringePump as fsp
import pandas as pd
import numpy as np
import time
import os



ts = tt.twinscrew()
f = tt.feeder()

collect_data = 1
path = "/"
interval = 1

def start_collection():


	results = pd.concat([ts.read_values(), f.read_values()], axis = 1)
	t = pd.Series(time.strftime("%H:%M:%S | %d-%m-%Y"))
	full_res = pd.concat([t, results], axis = 1)
	start_time = float(time.time())
	plot_t = np.array([(start_time - float(time.time()))])
	#print("######Recording Data. Push Ctrl+C to stop######")
	
	
	try:
		while (collect_data == 1):
			results = results.append(pd.concat([ts.read_values(), f.read_values()], axis = 1))
			t = t.append(pd.Series(time.strftime("%H:%M:%S | %d-%m-%Y")))		
			full_res = pd.concat([t, results], axis = 1)
			full_res.to_csv(os.path.join(experiment_name) +'/results.csv')
			#print ("Recorded at ", time.strftime("%H:%M:%S | %d-%m-%Y"))
			read_time = float(time.time())
			plot_t = np.append(plot_t, (read_time - start_time))
			#update_plot()
			time.sleep(interval)
			
			
	except KeyboardInterrupt: 
		print("Keyboard Interrupt - Stopping....")
		time.sleep(5)
		exit()