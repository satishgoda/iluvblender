import bpy


def main(context):
    window = context.window
    screen = window.screen

    is_header_bottom = lambda area: area.y == area.regions[0].y

    for area in screen.areas:
        if is_header_bottom(area):
            print("Flipping header for {0}".format(area.spaces.active.type))

            overrides = {
                'window':window,
                'screen':screen,
                'area': area,
                'region':area.regions[0]
            }

            bpy.ops.screen.header_flip(overrides)


class AreaHeadersConsistentOperator(bpy.types.Operator):
    """Position the Area Headers consistently"""
    bl_idname = "screen.area_headers_consistent"
    bl_label = "Make Area Headers Consistent"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(AreaHeadersConsistentOperator)


def unregister():
    bpy.utils.unregister_class(AreaHeadersConsistentOperator)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.screen.area_headers_consistent()
