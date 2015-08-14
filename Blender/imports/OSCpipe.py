from imports.OSC import OSCClient, OSCMessage
import imports.config
import imports.coord_transform
import bge

############# Send position via OSC #############

class OSCpipe:
	debug = False

	def debug(self, message):
		if self.debug:
			print("DEBUG OSCpipe: \t{}".format(message))

	##### INIT #####
	def __init__(self, obj_to_pipe, debug=None):
		self.scene = bge.logic.getCurrentScene()
		self.head = self.scene.objects["Listener"]
		self.obj_to_pipe = obj_to_pipe
		self.obj_cart_pos = obj_linked.worldPosition
		self.obj_cart_pos_from_head = obj_linked.getVectTo(self.head)
	
	def create_message(self):
		...
	
	def send_pos(self):
		...
	

def pipes_pool():
	scene = bge.logic.getCurrentScene()
#	debug(scene.objects["Sphere"]["selectable"])
	obj_to_pool = [object for object in scene.objects if object.get("selectable", False)]
#	debug(obj_to_pool)
