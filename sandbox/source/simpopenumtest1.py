import bpy


def main(context):
    for ob in context.scene.objects:
        print(ob)

def _modes(self, context):
    modes = []
    for mode in ("one", "two", "three"):
        i = mode.upper()
        n = mode.capitalize()
        d = "Mode " + n
        modes.append(tuple((i, n, d)))
    return modes

class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"
    bl_options = {'REGISTER'}

    modes = bpy.props.EnumProperty(items=_modes, name="Operator Modes")

    @classmethod
    def poll(cls, context):
        return context.area.spaces.active.type == 'VIEW_3D'

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        self.report({'INFO'}, self.modes)
        #main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SimpleOperator)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.object.simple_operator(modes='THREE')
