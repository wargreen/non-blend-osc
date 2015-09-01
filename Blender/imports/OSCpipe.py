from imports.logs import Logged, logger
logger = logger.getChild(__name__)


from sys import stderr
from functools import partial

from imports.OSC import OSCClient, OSCMessage
from imports.config import conf

import bge
import mathutils
from math import acos, atan, sqrt, cos, sin, tan, pi, degrees

############# Send position via OSC #############

print_stderr = partial(print, file=stderr)

	
class OSCpipe(Logged):
	##### INIT #####
	def __init__(self):
		super().__init__(logger)
		
		self.scene = bge.logic.getCurrentScene()
		self.head = self.scene.objects["Listener"]
		self.debug("Instantiate Object OSCpipe")
		
		
	###### Cartesian to polar, thx to agoose77 ! ######
	def vect_to_polar(self, vect):
		x, y, z = vect
		
		r = vect.length
		#theta = degrees(sin(acos(z / r))-1) #elevation
		#phi = degrees(sin(atan(y / x))-1) #azimuth
		theta = degrees(acos(z / r)-1) #elevation
		phi = degrees(atan(y / -x)) #azimuth
		
		if (x < 0.0):
			phi = phi + 180
		#elif (x < 0.0) & (y < 0.0):
		#	phi = phi + 360
		
		return r, phi, theta


	def polar_to_vect(self, polar):
		r, phi, theta = polar
		
		x = r * cos(theta) * sin(phi)
		y = r * sin(theta) * sin(phi)
		z = r * cos(phi)
		
		return Vector((x, y, z))
		
		

	def get_value(self, obj, just_look=False):
		obj_cart_pos_from_head = obj.getVectTo(self.head)
		if just_look:
			return obj_cart_pos_from_head
		#obj_sphe_pos_from_head = cartesian_to_spherical(obj_cart_pos_from_head)
		
		
	def create_message(self, obj):
		pos = obj["new_Vect"][1] * obj["new_Vect"][0]
		
		
		self.debug(obj)
		#self.debug(obj["new_Vect"])
		#self.debug(pos.length)
		self.debug(pos)
		
		pos = self.vect_to_polar(pos)
		
		self.debug(pos)
		
		mesg_azi = OSCMessage("{}{}{}".format(conf["osc_base_path"], str(obj), conf["osc_azimuth_path"]))
		mesg_rad = OSCMessage("{}{}{}".format(conf["osc_base_path"], str(obj), conf["osc_radius_path"]))
		mesg_ele = OSCMessage("{}{}{}".format(conf["osc_base_path"], str(obj), conf["osc_elevation_path"]))
		
		mesg_azi.append(pos[1])
		mesg_rad.append(pos[0])
		mesg_ele.append(pos[2])
		
		#print("--------")
		#self.debug(obj["new_Vect"][1][0])
		
		#self.debug(mesg_azi)
		#self.debug(mesg_rad)
		#self.debug(mesg_ele)
		
		return mesg_azi, mesg_rad, mesg_ele
	
	
	def test_change(self, obj_pool):
		#self.debug(obj_pool)
		#self.debug(obj_pool.get("prev_Vect", False))
		if obj_pool.get("prev_Vect", False):
			obj_pool["new_Vect"] = self.get_value(obj_pool, True)
			
			
			if obj_pool["prev_Vect"] != obj_pool["new_Vect"]:
				#self.debug(obj_pool["prev_Vect"])
				#self.debug(obj_pool["new_Vect"])
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

	
	#### Main pipes Processssss: Pool objects ####
	def pipes_pool(self):
	#	debug(scene.objects["Sphere"]["selectable"])
		tosend = []
		for obj_pool in self.scene.objects:
			if obj_pool.get("selectable", False):
				has_changed = self.test_change(obj_pool)
				#self.debug(has_changed)
				if has_changed:
					tosend.extend(self.create_message(obj_pool))
		return tosend
