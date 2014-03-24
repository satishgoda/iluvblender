import bpy


bl_ui_headers_only = lambda header: header.__module__.startswith('bl_ui')
bl_ui_headers = filter(bl_ui_headers_only, bpy.types.Header.__subclasses__())
bl_ui_header_names = tuple(header.__name__ for header in bl_ui_headers)

header_map = {}
for header_name in bl_ui_header_names:
    header = getattr(bpy.types, header_name)
    header_map[header.bl_space_type] = header.draw


def ALL_HT_header_draw_override(self, context):
    if bpy.app.debug:
        print("Drawing custom header")
        self.layout.label(context.area.type)
    else:
        print("Drawing original header")
        header_map[context.area.type](self, context)


def register():
    for header_name in bl_ui_header_names:
        getattr(bpy.types, header_name).draw = ALL_HT_header_draw_override


def unregister():
    for header_name in bl_ui_header_names:
        getattr(bpy.types, header_name).draw = header_map[getattr(bpy.types, header_name).bl_space_type]
        

