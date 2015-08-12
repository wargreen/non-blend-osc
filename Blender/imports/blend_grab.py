import bge
import mathutils

######### Move objects in environnement ###########

class Grab_env():
	debug = True

	def debug(self, message):
		if self.debug:
			print("DEBUG Grab_env : \t{}".format(message))

	##### INIT #####
	def __init__(self, ctrl, debug=None):
		if debug is not None:
			self.debug = debug
		
		self.width = bge.render.getWindowWidth()
		self.height = bge.render.getWindowHeight()
		self.ctrl = ctrl #bge.logic.getCurrentController()
		self.object = bge.logic.getCurrentScene()
		self.camera = self.ctrl.owner
		
		self.mouse = bge.logic.mouse
		self.obj_selected = None
		self.delta_color_sel = mathutils.Vector((0.2, 0.2, 0.2, 0))
		self.debug("Instentiate Object")
	
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

	def select_obj(self, grabbed):
		self.debug("selecting")
		#if self.obj_selected is not None :
		#	self.unsel_obj(grabbed)
		grabbed.color = grabbed.color + self.delta_color_sel
		self.obj_selected = grabbed
    
        #   selected = [object for object in objects if object.selected]

	def unsel_obj(self):
		object_selected.color = object_selected.color - delta_color_sel
		object_selected = None

	def calc_dest():
		...
	
	def move_obj_to():
		...

	def grab_obj(self):
		if self.mouse.events[bge.events.LEFTMOUSE] is bge.logic.KX_INPUT_JUST_ACTIVATED :
			hitten = self.mouse_hit_ray("selectable")
			grabbed = hitten[0]
			self.debug(hitten[0])
			if grabbed:
			#    import pdb; pdb.set_trace()
				if self.obj_selected is not grabbed:
					self.debug(self.obj_selected)
					self.debug(grabbed)
					self.select_obj(grabbed)
			#   grabbed.localPosition = grabbed.localPosition - hitten[1]
			#   print(dir(grabbed))    
