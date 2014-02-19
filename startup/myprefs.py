# -*- coding: utf-8 -*-
import bpy

context = bpy.context

# Scene Settings
scene = context.scene

# Scene Units
unit_settings = scene.unit_settings

unit_settings.system = 'METRIC'

# Scene Render Settings
render = scene.render

render.engine = 'CYCLES'


# User Preferences
userprefs = context.user_preferences


# View (Interface)
view = userprefs.view

view.show_splash = False


# File Paths
filepaths = userprefs.filepaths

filepaths.use_file_compression = True
filepaths.show_thumbnails = True


# System
system = userprefs.system

system.use_vertex_buffer_objects = True
system.use_region_overlap = True
system.use_scripts_auto_execute = True
system.author = "First Last(emailid@domain)- learningblender3dsoftware.blogspot.in"


for area in context.window_manager.windows[0].screen.areas:
    area.show_menus = False
    area.tag_redraw()

# Addons to Disable (Factory addons)
for addon in userprefs.addons:
    print("{0} - {1}".format("Disabling", addon))
    bpy.ops.wm.addon_disable(module=addon.module)


# Addons to auto-register
myaddonpath = bpy.utils.user_resource('SCRIPTS', path='addons')
if myaddonpath:
    myaddonmodules = bpy.utils.modules_from_path(myaddonpath, set())
    for module in myaddonmodules:
        print("{0} - {1}".format("Enabling", module))
        bpy.ops.wm.addon_enable(module=module.__name__)


# Window Manager
wm = context.window_manager

wm.addon_filter = 'Enabled'
wm.addon_support = {'COMMUNITY', 'OFFICIAL'}

userprefs.active_section = 'ADDONS'

# Save 'em
bpy.ops.wm.save_homefile()
bpy.ops.wm.save_userpref()
