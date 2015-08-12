from imports.blend_grab import Grab_env
#from imports.OSCpipe import OSCpipe
import bge

def main(ctrl):
#	print("main")
	
	
	#### Initiate the grabbing environement
	if "grabing_env" not in bge.logic.globalDict:
		
		bge.logic.globalDict["grabing_env"] = Grab_env(ctrl)
		
		
	#### Initiate the osc pipe environement
	if "osc_pipes" not in bge.logic.globalDict:	
		bge.logic.globalDict["osc_pipes"] = dict()
#		client = OSCClient()
#		client.connect( ("localhost", 7110) )
	
	grabing_env = bge.logic.globalDict["grabing_env"]
	grabing_env.grab_obj()


#	while ctrl.sensors["Always"].positive:
		#print(grabing)
	#send infos
	#connect only once !
#	client = OSCClient()
#	client.connect( ("localhost", 7110) )

