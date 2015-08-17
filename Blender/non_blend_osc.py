from imports.blend_grab import Grab_env
from imports.OSCpipe import OSCpipe
from imports.OSC import OSCClient, OSCMessage
from imports.config import conf
import bge

def main(ctrl):
	if ctrl.sensors["Always"].positive:

		globalDict = bge.logic.globalDict

		#### Load config from file ####
#		if "non_blend_osc_conf" not in globalDict:
#
#			globalDict["grabing_env"] = Grab_env(ctrl)
#
#		conf

		#### Initiate the grabbing environement ####
		if "grabing_env" not in globalDict:
			print("Init Grabing_env")

			globalDict["grabing_env"] = Grab_env(ctrl)

		grabing_env = globalDict["grabing_env"]
		

		#### Initiate the osc pipe environement ####
		if "osc_pipe" not in globalDict:
			print("Init OSCpipe")
			globalDict["osc_client"] = OSCClient()
			osc_client = globalDict["osc_client"]
			osc_client.connect( (conf["osc_client_addr"], conf["osc_client_port"]) )
			
			globalDict["osc_pipe"] = OSCpipe()
			print(osc_client)
		
		osc_client = globalDict["osc_client"]
		osc_pipe = globalDict["osc_pipe"]

		#### now, doing stuff ####
		grabing_env.grab_obj()
		osc_pipe.pipes_pool()


#	while ctrl.sensors["Always"].positive:
		#print(grabing)
	#send infos
	#connect only once !
#	client = OSCClient()
#	client.connect( ("localhost", 7110) )
