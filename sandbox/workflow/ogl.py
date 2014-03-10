import bpy

import os
bus = os.getenv('BLENDER_USER_SCRIPTS')
p = os.path.join(bus, 'presets')

for window in bpy.context.window_manager.windows:
    #screen = window.screen
    
    if 'VIEW_3D' not in map(lambda area: area.type, window.screen.areas):
        continue
    
    #scene = screen.scene

    path_to_restore = window.screen.scene.render.filepath
    
    window.screen.scene.render.filepath = '//{0}_{1}'.format('ogl_render_cmdline', window.screen.scene.name+window.screen.name)

    override = {
        'window': window,
    }

    bpy.ops.script.execute_preset(override, filepath=os.path.join(p, "render/stamp/ogl_render.py"), 
                                  menu_idname="RENDER_MT_stamp_presets")

    window.screen.scene.render.stamp_note_text = window.screen.scene.render.filepath

    override = {
        'window': window,
        'screen': window.screen,
        'scene': window.screen.scene,
    }

    bpy.ops.render.opengl(override, write_still=True)

    window.screen.scene.render.filepath = path_to_restore

    override = {
        'window': window,
    }

    bpy.ops.script.execute_preset(override, filepath=os.path.join(p, "render/stamp/defaults.py"), 
                                  menu_idname="RENDER_MT_stamp_presets")
