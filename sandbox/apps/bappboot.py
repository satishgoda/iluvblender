import bpy

import bapp

bapp.Debug()("BOOTING UP")

bpy.app.handlers.load_post.insert(0, bapp.load_modules)

bpy.ops.wm.read_homefile()

bpy.context.user_preferences.view.show_splash = False
