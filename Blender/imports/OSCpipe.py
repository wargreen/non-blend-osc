from imports.OSC import OSCClient, OSCMessage

############# Send position via OSC #############

class OSCpipe:
	debug = True

	def debug(self, message):
		if self.debug:
			print("DEBUG OSCpipe: \t{}".format(message))

	##### INIT #####
	def __init__(self, object, debug=None):
		...
