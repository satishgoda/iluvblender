import bpy


bl_ui_headers_only = lambda header: header.__module__.startswith('bl_ui')
bl_ui_headers = filter(bl_ui_headers_only, bpy.types.Header.__subclasses__())

header_map = { header.__name__: header.draw for header in bl_ui_headers }


def ALL_HT_header_draw_override(self, context):
    if bpy.app.debug:
        print("Drawing custom header")
        self.layout.label(context.area.type)
    else:
        print("Drawing original header")
        header_map[header.__name__](self, context)


def register():
    for header in bl_ui_headers:
        header.draw = ALL_HT_header_draw_override


def unregister():
    for header in bl_ui_headers:
        header.draw = header_map[header.__name__]

