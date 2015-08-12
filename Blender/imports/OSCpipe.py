from imports.OSC import OSCClient, OSCMessage
import imports.config

############# Send position via OSC #############

class OSCpipe:
	debug = True

	def debug(self, message):
		if self.debug:
			print("DEBUG OSCpipe: \t{}".format(message))

	##### INIT #####
	def __init__(self, obj_to_pipe, debug=None):
		obj_linked = obj_to_pipe
		

	def get_obj_position(self):
		...
	
	def pos_to_polar(self):
		...
	
	def create_message(self):
		...
	
	def send_pos(self):
		...
