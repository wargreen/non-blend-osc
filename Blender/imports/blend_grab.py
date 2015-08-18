from sys import stderr
from functools import partial
import time
import mathutils

import bge
import imports.config
######### Move objects in environnement ###########
print_stderr = partial(print, file=stderr)

class Grab_env():
	debug = False

	def debug(self, message):
		if self.debug:
			print_stderr("DEBUG Grab_env : \t{}".format(message))

	##### INIT #####
	def __init__(self, ctrl, debug=None):
		if debug is not None:
			self.debug = debug
		
		self.width = bge.render.getWindowWidth()
		self.height = bge.render.getWindowHeight()
		self.ctrl = ctrl #bge.logic.getCurrentController()
		self.scene = bge.logic.getCurrentScene()
		self.camera = self.scene.active_camera
		
		self.mouse = bge.logic.mouse
		self.last_obj_selected = None
		self.delta_color_sel = mathutils.Vector((0.2, 0.2, 0.2, 0))
		self.debug("Instentiate Object Grab_env")
	
	def mouse_hit_ray(self, property, distance=50.0):
		return_normal = 0
		x_ray = 1
		return_polygon = 0

		screen_vect = self.camera.getScreenVect(self.mouse.position[0],self.mouse.position[1])
		screen_vect.negate()
		target_position = self.camera.worldPosition + screen_vect
		target_ray = self.camera.rayCast(target_position, self.camera, distance , property, return_normal, x_ray, return_polygon)
		#import pdb; pdb.set_trace()
		return target_ray

	def toggle_select_obj(self, grabbed):
		if grabbed is not None:
			self.debug(grabbed.get("selected"))
			if grabbed.get("selected", False):
				##unselect
				self.debug("unselect")
				grabbed["selected"] = False
				grabbed["selected_time"] = 0
				#grabbed.color = grabbed.color - self.delta_color_sel
				grabbed.debug = False
				#self.debug(grabbed.color)
				#self.debug(grabbed["color_orig"])
				grabbed.color = grabbed["color_orig"]
				
			else:
				##select
				self.debug("select")
				grabbed["selected"] = True
				grabbed["selected_time"] = time.time()
				# FIXME 
				grabbed["color_orig"] = grabbed.color.copy()
				grabbed.color = grabbed.color + self.delta_color_sel
				grabbed.debug = True
				#self.debug(grabbed.color)
				#self.debug(grabbed["color_orig"])
		else:
			self.debug("Rien de grabbed!")
	
	def toggle_active_cam():
		self.scene.active_camera
		self.scene.cameras
		

	def calc_dest():
		...
	
	def move_obj_to():
		...
		
	def move_selected(self):
		obj_to_move =  [object for object in self.scene.objects if object.get("selected", False)]
		self.debug(obj_to_move)
		
	def grab_obj(self):
		if self.mouse.events[bge.events.LEFTMOUSE] is bge.logic.KX_INPUT_JUST_ACTIVATED :
			hitten = self.mouse_hit_ray("selectable")
			grabbed = hitten[0]
			self.debug(hitten[0])
			if grabbed:
				delta_select_time = time.time() - grabbed.get("selected_time", 0)
				if delta_select_time > 0.8:
					self.debug("toggle select")
					self.toggle_select_obj(grabbed)
				else:
					self.debug("move selected")
					self.move_selected()
				
				
			#    import pdb; pdb.set_trace()
			#	if self.obj_selected is not grabbed:
			#		self.debug(self.obj_selected)
			#		self.debug(grabbed)
			#		self.select_obj(grabbed)
			#   grabbed.localPosition = grabbed.localPosition - hitten[1]
			#   print(dir(grabbed))    
