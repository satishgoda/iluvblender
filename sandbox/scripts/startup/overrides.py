import bpy


bl_ui_headers_only = lambda header: header.__module__.startswith('bl_ui')
bl_ui_headers = tuple(filter(bl_ui_headers_only, bpy.types.Header.__subclasses__()))

header_map = {header.bl_space_type: header.draw for header in bl_ui_headers }


def ALL_HT_header_draw_override(self, context):  
    area = context.area
    area_type_enum_item = area.bl_rna.properties['type'].enum_items[area.type]
    icon = area_type_enum_item.icon
    text = "{} ({})".format(area.type, area_type_enum_item.description)
    
    layout = self.layout
    row = layout.row()
    
    if bpy.app.debug_value == 1:
        row.label(text, icon=icon)
    else:
        header_map[context.area.type](self, context)


def register():
    for header in bl_ui_headers:
        header.draw = ALL_HT_header_draw_override


def unregister():
    for header in bl_ui_headers:
        header.draw = header_map[header.bl_space_type]
        

