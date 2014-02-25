import bpy

import os

_filepath = bpy.data.filepath

_screenshot = dict()
_screenshot['filename'] = bpy.path.display_name_from_filepath(_filepath) if _filepath else 'untitled'
_screenshot['filename_ext'] = 'png'
_screenshot['dirname'] = os.path.dirname(_filepath) if _filepath else os.getcwd()
_screenshot['filename_suffix_char'] = '_'
_screenshot['filename_suffix'] = None

def _get_filepath(screenshot):
    import os
    s = screenshot
    filename = s['filename']
    if s['filename_suffix']:
        filename += s['filename_suffix_char'] + s['filename_suffix']
    filename += '.' + s['filename_ext']
    filepath = os.path.join(s['dirname'], filename)
    return filepath

class ScreenshotsCustom(bpy.types.Operator):
    """Create and save screenshots of different areas"""
    bl_idname = "screen.screenshot_custom"
    bl_label = "Save Screenshot Custom"
    bl_options = {'REGISTER'}
    
    def __init__(self):
        print("Initializing " + self.bl_idname)        
    
    def execute(self, context):
        print("Executing " + self.bl_idname)
        
        overrides = {}
        overrides['window'] = bpy.context.window
        
        kwargs = { 'full': False }
        
        for area in context.screen.areas:
            overrides['area'] = area
            overrides['region'] = area.regions[1]
            
            screenshot = _screenshot.copy()
            screenshot['filename_suffix'] = area.type
            
            kwargs['filepath'] = _get_filepath(screenshot)

            bpy.ops.screen.screenshot(overrides, **kwargs)
        
        return {'FINISHED'}
    
    def __del__(self):
        print("Destructing " + self.bl_idname)


def register():
    bpy.utils.register_class(ScreenshotsCustom)

  
def unregister():
    bpy.utils.unregister_class(ScreenshotsCustom)

    
if __name__ == '__main__':
    register()
    bpy.ops.screen.screenshot_custom()
