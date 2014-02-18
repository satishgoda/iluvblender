import bpy
from bpy.app.handlers import persistent 

@persistent
def load_post_1(scene):
	print("{0} - {1}".format("load_post", bpy.context.scene.name))
	if bpy.data.filepath:
		print(bpy.data.filepath)
	
bpy.app.handlers.load_post.append(load_post_1)
