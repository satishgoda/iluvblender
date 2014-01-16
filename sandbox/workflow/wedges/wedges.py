import bpy

source = bpy.context.scene

resolutions = [100, 50, 25]

wedges = []

for i in range(0, 3):
     bpy.ops.scene.new(type='LINK_OBJECTS')
     scene = bpy.context.scene
     scene.name = '{0}.{1}'.format(source.name, i+1)
     scene.render.filepath = '//{0}.'.format(scene.name)
     scene.render.resolution_percentage = resolutions[i]
     wedges.append(scene)

bpy.context.screen.scene = source

for scene in wedges:
    bpy.ops.render.render(write_still=True, scene=scene.name)
    bpy.data.scenes.remove(scene)

del wedges

