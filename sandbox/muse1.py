import bpy
from bpy.app.handlers import persistent
import addon_utils
import bpy_types

import os
import sys

BLENDER_USER_SCRIPTS = os.getenv('BLENDER_USER_SCRIPTS')

if BLENDER_USER_SCRIPTS is None:
    print("BLENDER_USER_SCRIPTS env variable has not been set. Aborting launch of Blender\n\n")
    bpy.ops.wm.quit_blender()

print("Enabling custom addons located at {0}".format(BLENDER_USER_SCRIPTS))

ADDONS_PATH = os.path.join(BLENDER_USER_SCRIPTS, 'addons')

_ADDONS_FOR_PROJECT = tuple(map(lambda addon: addon[0], bpy.path.module_names(ADDONS_PATH)))

# We make this persistent so that when creating a new session the addons are still enabled
@persistent
def requiredAddons(self):
    bpy.types.RENDER_PT_render.bl_options = {'DEFAULT_CLOSED'}
    
    for addon in _ADDONS_FOR_PROJECT:
        addon_status = addon_utils.check(addon)
        if addon_status[0] == True:
            if bpy.app.debug:
                print("{0} is already loaded so disabling it".format(addon))
            bpy.ops.wm.addon_disable(module=addon)
            #continue
        
        try:
            bpy.ops.wm.addon_enable(module=addon)
        except AttributeError as e:
            print(e)
        else:
            if bpy.app.debug:
                print("Loaded {0}".format(addon))

if __name__ == '__main__':
    requiredAddons(None)
    bpy.app.handlers.load_post.append(requiredAddons)

