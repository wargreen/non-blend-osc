from imports.blend_grab import Grab_env
from imports.OSCpipe import OSCpipe
from imports.OSC import OSCClient, OSCMessage
import bge
import imports.config

def main(ctrl):
#	print("main")
	if ctrl.sensors["Always"].positive:
		
		globalDict = bge.logic.globalDict
		
		
		#### Initiate the grabbing environement
		if "grabing_env" not in globalDict:
			
			globalDict["grabing_env"] = Grab_env(ctrl)
			
			
		#### Initiate the osc pipe environement
		if "osc_pipes" not in globalDict:	
			globalDict["osc_pipes"] = dict()
			osc_pipes = globalDict["osc_pipes"]
			osc_pipes["client"] = OSCClient()
			osc_pipes["client"].connect( (conf["osc_client_addr"], conf["osc_client_port"]) )
		
		grabing_env = globalDict["grabing_env"]
		grabing_env.grab_obj()


#	while ctrl.sensors["Always"].positive:
		#print(grabing)
	#send infos
	#connect only once !
#	client = OSCClient()
#	client.connect( ("localhost", 7110) )

