
bl_info = {
    "name": "Custom Screenshot Creator",
    "author": "Satish Goda (iluvblender on BA, satishgoda@gmail.com)",
    "version": (0, 1),
    "blender": (2, 7, 0),
    "location": "Save Screenshot Custom",
    "description": "Create screenshots of all the individual areas in the current screen (and the whole area also if you want)",
    "warning": "",
    "category": "Screen"
}

import bpy

class ScreenshotsCustom(bpy.types.Operator):
    """Create and save screenshots of different areas"""
    bl_idname = "screen.screenshot_custom"
    bl_label = "Save Screenshot Custom"
    bl_options = {'REGISTER'}

    _items = [('SCREEN', 'Current Screen', 'Capture the current screen'),
              ('SCREEN_ALL_AREAS', 'All Screen Areas', 'Capture all the areas of the current screen'),
              ('SCREEN_AND_ALL_AREAS', 'Current Screen and all Areas', 'Capture screen and also all its areas')
              ]

    capture_mode = bpy.props.EnumProperty(items=_items, name="Capture mode", default='SCREEN_AND_ALL_AREAS')
    
    def __init__(self):
        print("Initializing " + self.bl_idname)        

    def invoke(self, context, event):
        print("Invoking " + self.bl_idname)
        if (event.oskey and event.type == 'C'):
            return self.execute(context)
        else:
            return context.window_manager.invoke_props_dialog(self)
    
    def execute(self, context):
        print("Executing " + self.bl_idname)
        
        overrides = {}
        overrides['window'] = context.window
        overrides['screen'] = context.screen
        overrides['scene'] = context.scene
        
        import screenshot
        screenshot = screenshot.Screenshot()

        if self.capture_mode == 'SCREEN':
            bpy.ops.screen.screenshot(filepath=screenshot.filepath)
        elif self.capture_mode == 'SCREEN_ALL_AREAS':
            kwargs = { 'full': False }

            for area in context.screen.areas:
                overrides['area'] = area
                overrides['region'] = area.regions[1]
                overrides['space_data'] = area.spaces.active

                screenshot.filename_suffix = area.type

                kwargs['filepath'] = screenshot.filepath

                bpy.ops.screen.screenshot(overrides, **kwargs)
        else:
            self.report({'INFO'}, self.capture_mode)

        self.report({'INFO'}, "Screenshot saved in {0}".format(screenshot.dirname))
        context.window_manager.clipboard = screenshot.dirname
        
        return {'FINISHED'}
    
    def __del__(self):
        print("Destructing " + self.bl_idname)


def register():
    bpy.utils.register_class(ScreenshotsCustom)
    
    keyconfigs = bpy.context.window_manager.keyconfigs

    if 'Screen' not in keyconfigs.addon.keymaps:
        keyconfigs.addon.keymaps.new('Screen')

    keymap = keyconfigs.addon.keymaps['Screen']
    
    kmi = keymap.keymap_items.new('screen.screenshot_custom', 'C', 'PRESS', oskey=True)
    
    setattr(kmi.properties, 'capture_mode', 'SCREEN')

    kmi = keymap.keymap_items.new('screen.screenshot_custom', 'C', 'PRESS', shift=True, oskey=True)

    setattr(kmi.properties, 'capture_mode', 'SCREEN_ALL_AREAS')

  
def unregister():
    keyconfigs = bpy.context.window_manager.keyconfigs

    keymap = keyconfigs.addon.keymaps['Screen']

    kmi = keymap.keymap_items[ScreenshotsCustom.bl_idname]
    keymap.keymap_items.remove(kmi)
    del kmi

    kmi = keymap.keymap_items[ScreenshotsCustom.bl_idname]
    keymap.keymap_items.remove(kmi)
    del kmi
    
    bpy.utils.unregister_class(ScreenshotsCustom)
    
if __name__ == '__main__':
    register()
    #bpy.ops.screen.screenshot_custom()
