import bpy


INFO_HT_header_draw_original = bpy.types.INFO_HT_header.draw


def INFO_HT_header_draw_override(self, context):
    if bpy.app.debug:
        print("Drawing custom header")
        self.layout.label(context.area.type)
    else:
        print("Drawing original header")
        INFO_HT_header_draw_original(self, context)


def register():
    bpy.types.INFO_HT_header.draw = INFO_HT_header_draw_override


def unregister():
    bpy.types.INFO_HT_header.draw = INFO_HT_header_draw_original

