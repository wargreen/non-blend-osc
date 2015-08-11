import bge
import mathutils

class Grab_env:
	debug = False

	def debug(self, message):
		if self.debug:
			print("DEBUG: \t{}".format(message))
	##### INIT #####
	def __init__(self, debug=None):
		if debug is not None:
			self.debug = debug
		
		self.width = bge.render.getWindowWidth()
		self.height = bge.render.getWindowHeight()
		self.ctrl = bge.logic.getCurrentController()
		self.object = bge.logic.getCurrentScene()
		self.camera = self.ctrl.owner
		
		self.mouse_pos = bge.logic.mouse.position
		self.obj_selected = None
		self.delta_color_sel = mathutils.Vector((0.2, 0.2, 0.2, 0))
		
	def mouse_hit_ray(self, property, distance=50.0):
		
		return_normal = 0
		x_ray = 1
		return_polygon = 0

		screen_vect = camera.getScreenVect(mouse_position[0],mouse_position[1])
		screen_vect.negate()
		target_position = camera.worldPosition + screen_vect                
		target_ray = camera.rayCast(target_position, camera, distance , property, return_normal, x_ray, return_polygon)
		#import pdb; pdb.set_trace()
		return target_ray

	def select_obj(self, grabbed):
		if obj_selected is not None :
			unsel_obj(grabbed)
		grabbed.color = grabbed.color + delta_color_sel
		obj_selected = grabbed
    
        #   selected = [object for object in objects if object.selected]

	def unsel_obj(self):
		object_selected.color = object_selected.color - delta_color_sel
		object_selected = None

	def calc_dest():
		...

	def grab_obj():
		hitten = mouse_hit_ray(self, "selectable")
		grabbed = hitten[0]
		print(hitten[0])
		if grabbed:
		#    import pdb; pdb.set_trace()
			if obj_selected is not grabbed:
			
				print(grabbed.color)
		#   grabbed.localPosition = grabbed.localPosition - hitten[1]
		#   print(dir(grabbed))    

def main():        

	grabing = Grab_env()
	print(grabing)
	grabing.grab_obj(self)
