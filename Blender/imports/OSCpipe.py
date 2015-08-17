from imports.OSC import OSCClient, OSCMessage
import imports.config
import imports.coord_transform
import bge

############# Send position via OSC #############

class OSCpipe:
	debug = True

	def debug(self, message):
		if self.debug:
			print("DEBUG OSCpipe: \t{}".format(message))

	##### INIT #####
	def __init__(self, debug=None):
		self.scene = bge.logic.getCurrentScene()
		self.head = self.scene.objects["Listener"]
		self.debug("Instentiate Object OSCpipe")
				
	def get_value(self, obj, just_look=False):
		obj_cart_pos_from_head = obj.getVectTo(self.head)
		if just_look:
			return obj_cart_pos_from_head
		#obj_sphe_pos_from_head = cartesian_to_spherical(obj_cart_pos_from_head)
		
		
	def create_message(self, obj):
		mesg_x = ""
		#self.debug("create message")
		
	
	def send_osc(self, obj):
		has_changed = self.test_change(obj)
		self.debug(has_changed)
		if has_changed is not False or None:
			self.create_message(obj)
			
	
	
	
	def test_change(self, obj_pool):
		self.debug(obj_pool)
		#self.debug(obj_pool.get("prev_Vect", False))
		if obj_pool.get("prev_Vect", False):
			obj_pool["new_Vect"] = self.get_value(obj_pool, True)
			
			# FIXME : Comparaison entre les vecteurs foire
			if obj_pool["prev_Vect"][1] != obj_pool["new_Vect"][1]:
				has_changed = obj_pool["new_Vect"]
			else:
				has_changed = False
			#if obj_pool["prev_worldOri"] != obj_pool.worldOrientation.copy():
			#	has_changed = has_changes, obj_pool.worldOrientation
			
			return has_changed
		
		else:
			obj_pool["prev_Vect"] = self.get_value(obj_pool, True)
			self.debug("adding prev_vect")
			#self.debug(obj_pool["prev_Vect"])
			return False

	def pipes_pool(self):
	#	debug(scene.objects["Sphere"]["selectable"])
		obj_to_pool = [object for object in self.scene.objects if object.get("selectable", False)]
		for obj_pool in obj_to_pool:
			self.send_osc(obj_pool)
