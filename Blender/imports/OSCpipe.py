from sys import stderr
from functools import partial

from imports.OSC import OSCClient, OSCMessage
from imports.config import conf
import imports.coord_transform
import bge

############# Send position via OSC #############

print_stderr = partial(print, file=stderr)

class OSCpipe():
	debug = False

	def debug(self, message):
		if self.debug:
			print_stderr("DEBUG OSCpipe: \t{}".format(message))

	##### INIT #####
	def __init__(self, debug=None):
		self.scene = bge.logic.getCurrentScene()
		self.head = self.scene.objects["Listener"]
		self.debug("Instantiate Object OSCpipe")
				
	def get_value(self, obj, just_look=False):
		obj_cart_pos_from_head = obj.getVectTo(self.head)
		if just_look:
			return obj_cart_pos_from_head
		#obj_sphe_pos_from_head = cartesian_to_spherical(obj_cart_pos_from_head)
		
		
	def create_message(self, obj):
		mesg_x = conf["osc_base_path"] + str(obj)
		#self.debug("create message")
		
	
	def send_osc(self, obj):
		has_changed = self.test_change(obj)
		#self.debug(has_changed)
		if not has_changed:
			self.create_message(obj)
		
	
	def test_change(self, obj_pool):
		self.debug(obj_pool)
		#self.debug(obj_pool.get("prev_Vect", False))
		if obj_pool.get("prev_Vect", False):
			obj_pool["new_Vect"] = self.get_value(obj_pool, True)
			
			
			if obj_pool["prev_Vect"] != obj_pool["new_Vect"]:
				self.debug(obj_pool["prev_Vect"])
				self.debug(obj_pool["new_Vect"])
				has_changed = obj_pool["new_Vect"]
			else:
				has_changed = False
			#if obj_pool["prev_worldOri"] != obj_pool.worldOrientation.copy():
			#	has_changed = has_changes, obj_pool.worldOrientation
			obj_pool["prev_Vect"] = obj_pool["new_Vect"]
			
			return has_changed
		
		else:
			obj_pool["prev_Vect"] = self.get_value(obj_pool, True)
			self.debug("adding prev_vect")
			#self.debug(obj_pool["prev_Vect"])
			return False

	def pipes_pool(self):
	#	debug(scene.objects["Sphere"]["selectable"])
		for obj_pool in self.scene.objects:
			if obj_pool.get("selectable", False):
				self.send_osc(obj_pool)
