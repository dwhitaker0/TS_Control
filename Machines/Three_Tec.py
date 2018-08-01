import OpenOPC
import pandas as pd

#############
##Define Names##
#############

server_name = 'Kepware.KEPServerEX.V5'
twin_screw_plc = 'TSWG.PLC.'
feeder_plc = 'Feeder.PLC.'


##Tiwn_Screw Controls##
ts_start_stop = 'Granulator_Z12_StartStop'
ts_remote_mode = 'Granulator_ControlMode'
ts_Z12_speed_set = 'Granulator_Z12_Speed_SP'
ts_zone_1_startstop = 'Zone_1_StartStop'
ts_zone_2_startstop = 'Zone_2_StartStop'
ts_zone_3_startstop = 'Zone_3_StartStop'
ts_zone_4_startstop = 'Zone_4_StartStop'
ts_zone_5_startstop = 'Zone_5_StartStop'
ts_zone_6_startstop = 'Zone_6_StartStop'
ts_zone_1_temp_set = 'Zone_1_Temp_SP'
ts_zone_2_temp_set = 'Zone_2_Temp_SP'
ts_zone_3_temp_set = 'Zone_3_Temp_SP'
ts_zone_4_temp_set = 'Zone_4_Temp_SP'
ts_zone_5_temp_set = 'Zone_5_Temp_SP'
ts_zone_6_temp_set = 'Zone_6_Temp_SP'

##Feeder Controls##
f_start_stop = 'Feeder_Gravimetric_StartStop'
f_remote_mode = 'Feeder_ControlMode'
f_flow_set = 'FlowRate_SP'


##Twin_Screw Process Values##
ts_current_speed_Z12 = 'Granulator_Z12_Speed_PV'
ts_Z12_speed_sp = 'Granulator_Z12_Speed_SP'
ts_current_running = 'Granulator_Z12_Running'
ts_current_speed_rpm = 'Granulator_Z12_Speed_PV'
ts_current_torque_Z12 ='Torque_Z12_PV'
ts_die_Presuure = 'Die_Pressure_PV'
ts_error_reset = 'Error_Reset'
ts_current_Z_inuse = 'Granulator_Current_Z'
ts_current_error = 'Granulator_Error'
ts_is_the_TSWG_remote_on = 'Granulator_Remote_ON'
ts_current_Z12_power = 'Granulator_Z12_Power_PV'
ts_is_zone_1_connected = 'Zone_1_Connected'
ts_is_zone_2_connected = 'Zone_2_Connected'
ts_is_zone_3_connected = 'Zone_3_Connected'
ts_is_zone_4_connected = 'Zone_4_Connected'
ts_is_zone_5_connected = 'Zone_5_Connected'
ts_is_zone_6_connected = 'Zone_6_Connected'
ts_is_zone_1_running = 'Zone_1_Running'
ts_is_zone_2_running = 'Zone_2_Running'
ts_is_zone_3_running = 'Zone_3_Running'
ts_is_zone_4_running = 'Zone_4_Running'
ts_is_zone_5_running = 'Zone_5_Running'
ts_is_zone_6_running = 'Zone_6_Running'
ts_current_zone_1_temp = 'Zone_1_Temp_PV'
ts_current_zone_2_temp = 'Zone_2_Temp_PV'
ts_current_zone_3_temp = 'Zone_3_Temp_PV'
ts_current_zone_4_temp = 'Zone_4_Temp_PV'
ts_current_zone_5_temp = 'Zone_5_Temp_PV'
ts_current_zone_6_temp = 'Zone_6_Temp_PV'

##Feeder Process Values##
f_current_weight = 'Weight_PV'
f_current_speed_rpm = 'Speed_RPM_PV'
f_current_speed_percent = 'Speed_%_PV'
f_hopper_level = 'HopperLevel_PV'
f_flow_rate_SP_read = 'FlowRate_SP_Readback'
f_raw_flow_PV = 'FlowRate_RAW_PV' 						####################
f_controller_flow_PV= 'FlowRate_PIController_PV'			##Various Levels of Filtering##
f_HMI_flow_PV = 'FlowRate_HMI_PV'							####################
f_max_flow = 'FlowRate_Maximum'
f_deviation = 'FlowRate_Controller_Deviation'
f_volumetic_running = 'Feeder_Volumetric_Running'
f_gravimetric_running = 'Feeder_Gravimetric_Running'
f_stable = 'Feeder_Stable'
f_running = 'Feeder_Running'
f_error = 'Feeder_Error'
f_remote_mode_OnOff = 'Feeder_Remote_ON'

##Watchdog##

ts_WD_in = 'Granulator_Watchdog_In'
ts_WD_out = 'Granulator_Watchdog_Out'

f_WD_in = 'Feeder_Watchdog_In'
f_WD_out = 'Feeder_Watchdog_Out'


####################
##Initialise OPC Connection with Twin Screw Class##
####################

class twinscrew: 
	def __init__(self): 
		self.opc = OpenOPC.client()
		self.opc.connect(server_name)

####################
##Define Control Functions##
###################

	def remote_on(self):
		self.opc.write((twin_screw_plc+ts_remote_mode, 1))

	def remote_off(self):
		self.opc.write((twin_screw_plc+ts_remote_mode, 0))

	def start(self):
		self.opc.write((twin_screw_plc+ts_start_stop, 1))

	def stop(self):
		self.opc.write((twin_screw_plc+ts_start_stop, 0))

	def set_rate(self, rate):
		self.opc.write((twin_screw_plc+ts_Z12_speed_set, rate))

	def zone_1_on(self):
		self.opc.write((twin_screw_plc+ts_zone_1_startstop, 1))

	def zone_2_on(self):
		self.opc.write((twin_screw_plc+ts_zone_2_startstop, 1))

	def zone_3_on(self):
		self.opc.write((twin_screw_plc+ts_zone_3_startstop, 1))

	def zone_4_on(self):
		self.opc.write((twin_screw_plc+ts_zone_4_startstop, 1))

	def zone_5_on(self):
		self.opc.write((twin_screw_plc+ts_zone_5_startstop, 1))

	def zone_6_on(self):
		self.opc.write((twin_screw_plc+ts_zone_6_startstop, 1))

	def zone_1_off(self):
		self.opc.write((twin_screw_plc+ts_zone_1_startstop, 0))

	def zone_2_off(self):
		self.opc.write((twin_screw_plc+ts_zone_2_startstop, 0))

	def zone_3_off(self):
		self.opc.write((twin_screw_plc+ts_zone_3_startstop, 0))

	def zone_4_off(self):
		self.opc.write((twin_screw_plc+ts_zone_4_startstop, 0))

	def zone_5_off(self):
		self.opc.write((twin_screw_plc+ts_zone_5_startstop, 0))

	def zone_6_off(self):
		self.opc.write((twin_screw_plc+ts_zone_6_startstop, 0))

	def zone_1_set_temp(self, temp):
		self.opc.write((twin_screw_plc+ts_zone_1_temp_set, temp))

	def zone_2_set_temp(self, temp):
		self.opc.write((twin_screw_plc+ts_zone_2_temp_set, temp))

	def zone_3_set_temp(self, temp):
		self.opc.write((twin_screw_plc+ts_zone_3_temp_set, temp))

	def zone_4_set_temp(self, temp):
		self.opc.write((twin_screw_plc+ts_zone_4_temp_set, temp))

	def zone_5_set_temp(self, temp):
		self.opc.write((twin_screw_plc+ts_zone_5_temp_set, temp))

	def zone_6_set_temp(self, temp):
		self.opc.write((twin_screw_plc+ts_zone_6_temp_set, temp))
	##################
	##Define Read Functions##
	##################

	global ts_process_tags
	ts_process_tags = [twin_screw_plc+ts_current_speed_Z12, 
	twin_screw_plc+ts_current_running, 
	twin_screw_plc+ts_current_speed_rpm,
	twin_screw_plc+ts_Z12_speed_sp,	
	twin_screw_plc+ts_current_torque_Z12,
	twin_screw_plc+ts_die_Presuure,
	twin_screw_plc+ts_error_reset,
	twin_screw_plc+ts_current_Z_inuse,
	twin_screw_plc+ts_current_error,
	twin_screw_plc+ts_is_the_TSWG_remote_on,
	twin_screw_plc+ts_current_Z12_power,
	twin_screw_plc+ts_is_zone_1_connected,
	twin_screw_plc+ts_is_zone_2_connected,
	twin_screw_plc+ts_is_zone_3_connected,
	twin_screw_plc+ts_is_zone_4_connected,
	twin_screw_plc+ts_is_zone_5_connected,
	twin_screw_plc+ts_is_zone_6_connected,
	twin_screw_plc+ts_is_zone_1_running,
	twin_screw_plc+ts_is_zone_2_running,
	twin_screw_plc+ts_is_zone_3_running,
	twin_screw_plc+ts_is_zone_4_running,
	twin_screw_plc+ts_is_zone_5_running,
	twin_screw_plc+ts_is_zone_6_running,
	twin_screw_plc+ts_current_zone_1_temp,
	twin_screw_plc+ts_current_zone_2_temp,
	twin_screw_plc+ts_current_zone_3_temp,
	twin_screw_plc+ts_current_zone_4_temp,
	twin_screw_plc+ts_current_zone_5_temp,
	twin_screw_plc+ts_current_zone_6_temp]

	def read_values_initial(self):
		return  pd.DataFrame(self.opc.read(ts_process_tags))
		
		def read_values(self):
		return  pd.DataFrame(self.opc(ts_process_tags))
	
	
	
####################
##Initialise OPC Connection with Feeder Class##
####################

class feeder: 
	def __init__(self): 
		self.opc = OpenOPC.client()
		self.opc.connect(server_name)

####################
##Define Control Functions##
###################

	def remote_on(self):
		self.opc.write((feeder_plc+f_remote_mode, 1))

	def remote_off(self):
		self.opc.write((feeder_plc+f_remote_mode, 0))

	def start(self):
		self.opc.write((feeder_plc+f_start_stop, 1))
		
	def stop(self):
		self.opc.write((feeder_plc+f_start_stop, 0))
		
	def set_rate(self, rate):
		self.opc.write((feeder_plc+f_flow_set, rate))
	
	
	##################
	##Define Read Functions##
	##################

	global f_process_tags
	f_process_tags = [feeder_plc+f_current_weight, 
	feeder_plc+f_current_speed_rpm, 
	feeder_plc+f_current_speed_percent, 
	feeder_plc+f_hopper_level, 
	feeder_plc+f_flow_rate_SP_read, 
	feeder_plc+f_raw_flow_PV,
	feeder_plc+f_HMI_flow_PV, 
	feeder_plc+f_controller_flow_PV, 
	feeder_plc+f_deviation, 
	feeder_plc+f_stable]

	def read_values_initial(self):
		return  pd.DataFrame(self.opc.read(f_process_tags))
		
		def read_values(self):
		return  pd.DataFrame(self.opc(f_process_tags))

















