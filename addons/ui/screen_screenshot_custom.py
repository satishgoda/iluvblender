import bpy


class ScreenshotsCustom(bpy.types.Operator):
    """Create and save screenshots of different areas"""
    bl_idname = "screen.screenshot_custom"
    bl_label = "Save Screenshot Custom"
    bl_options = {'REGISTER'}
    
    def __init__(self):
        print("Initializing")        
    
    def execute(self, context):
        print("Executing")
        return {'FINISHED'}
    
    def __del__(self):
        print("Destructing")


def register():
    bpy.utils.register_class(ScreenshotsCustom)
  

def unregister():
    bpy.utils.unregister_class(ScreenshotsCustom)
    

if __name__ == '__main__':
    register()
    bpy.ops.screen.screenshot_custom()
