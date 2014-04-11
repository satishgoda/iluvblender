import bpy


ccontext = bpy.context.copy()


for screen in bpy.data.screens:
    if screen.name == 'Default':
        continue
 
    ccontext['screen'] = screen
    bpy.ops.screen.delete(ccontext)
    
    print("Deleting screen {}".format(screen.name))

