# -*- coding: utf-8 -*-
import bpy


if False:
    bpy.app.debug = True
    bpy.app.debug_python = True
    bpy.app.debug_wm = True


context = bpy.context

userprefs = context.user_preferences

loaded_modules = set(map(lambda addon: addon.module, userprefs.addons))

myaddonpath = bpy.utils.user_resource('SCRIPTS', path='addons')

new_modules = bpy.utils.modules_from_path(myaddonpath, loaded_modules)

if new_modules:
    for module in new_modules:
        print("{0} - {1}".format("Enabling", module))
        bpy.ops.wm.addon_enable(module=module.__name__)
    # Save 'em
    bpy.ops.wm.save_homefile()
    bpy.ops.wm.save_userpref()
else:
    print("No new modules to load")
