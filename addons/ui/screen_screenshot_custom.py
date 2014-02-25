import bpy

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
        overrides['window'] = context.window
        overrides['screen'] = context.screen
        overrides['scene'] = context.scene
        
        kwargs = { 'full': False }
        
        import screenshot
        screenshot = screenshot.Screenshot()
        
        for area in context.screen.areas:
            overrides['area'] = area
            overrides['region'] = area.regions[1]
            overrides['space_data'] = area.spaces.active
            
            screenshot.filename_suffix = area.type
            
            kwargs['filepath'] = screenshot.filepath

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
