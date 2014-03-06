import bpy

from bl_operators import presets


class AddPresetOutput(presets.AddPresetBase, bpy.types.Operator):
    """Add or remove a Output Preset"""
    bl_idname = "render.preset_add"
    bl_label = "Add Render Preset"
    preset_menu = "RENDER_MT_output"

    preset_defines = [
        "scene = bpy.context.scene",
        "render = scene.render",
        "image_settings = render.image_settings"
    ]

    preset_values = [
        "render.filepath",
        "image_settings.file_format"
    ]

    preset_subdir = "output"


class RENDER_MT_output(bpy.types.Menu):
    bl_label = "Output Presets"
    preset_subdir = "output"
    preset_operator = "script.execute_preset"
    draw = bpy.types.Menu.draw_preset


def odraw(self, context):
    layout = self.layout

    scene = context.scene
    rd = scene.render

    row = layout.row(align=True)
    row.menu("RENDER_MT_output", text=bpy.types.RENDER_MT_output.bl_label)
    row.operator("render.preset_add", text="", icon='ZOOMIN')
    row.operator("render.preset_add", text="", icon='ZOOMOUT').remove_active = True

    
def register():
    bpy.utils.register_class(AddPresetOutput)
    bpy.utils.register_class(RENDER_MT_output)
    bpy.types.RENDER_PT_output.prepend(odraw)

    
def unregister():
    bpy.types.RENDER_PT_output.remove(odraw)
    bpy.utils.unregister_class(AddPresetOutput)
    bpy.utils.unregister_class(RENDER_MT_output)


if __name__ == '__main__':
    register()
