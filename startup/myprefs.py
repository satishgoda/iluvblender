import bpy

userprefs = bpy.context.user_preferences

view = userprefs.view

view.show_splash = False

bpy.ops.wm.save_homefile()
bpy.ops.wm.save_userpref()
