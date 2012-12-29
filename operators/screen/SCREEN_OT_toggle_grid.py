import bpy

def main(context):
    screen = context.screen
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            active_space = area.spaces[0]
            attrs = ['show_floor', 'show_axis_x', 'show_axis_y', 'show_axis_z']
            for attr, toggle in map(lambda attr: (attr, getattr(active_space, attr)), attrs):
                setattr(active_space, attr, not toggle)
    
class SCREEN_OT_toggle_grid(bpy.types.Operator):
    """Toggles the Grid display in all 3D Views for the current screen"""
    bl_idname = "screen.toggle_grid"
    bl_label = "Screen Toggle Grid"
    bl_options = {'REGISTER'}

    def execute(self, context):
        main(context)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SCREEN_OT_toggle_grid)

def unregister():
    bpy.utils.unregister_class(SCREEN_OT_toggle_grid)

if __name__ == "__main__":
    register()

    # test call
    bpy.ops.screen.toggle_grid()
