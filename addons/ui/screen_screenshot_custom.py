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
        overrides['window'] = bpy.context.window
        
        for area in context.screen.areas:
            overrides['area'] = area
            overrides['region'] = area.regions[1]
            bpy.ops.screen.screenshot(overrides, filepath="//{0}.png".format(area.type), full=False)
        
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
