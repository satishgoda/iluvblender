import bpy


bl_ui_headers_only = lambda header: header.__module__.startswith('bl_ui')
bl_ui_headers = tuple(filter(bl_ui_headers_only, bpy.types.Header.__subclasses__()))

header_map = {header.bl_space_type: header.draw for header in bl_ui_headers }


def ALL_HT_header_draw_override(self, context):
    layout = self.layout
    
    if bpy.app.debug_value == 1:
        area = context.area
        text = "{} ({})".format(area.type, layout.enum_item_description(area, 'type', area.type))
        icon = area.bl_rna.properties['type'].enum_items[area.type].icon
        row = layout.row()
        row.alert = True
        row.operator_context = 'EXEC_DEFAULT'
        row.operator('wm.debug_menu', text='', icon='LOOP_BACK').debug_value = 0
        row.operator_context = 'INVOKE_DEFAULT'
        row.label(text, icon=icon)
    else:
        header_map[context.area.type](self, context)


def register():
    for header in bl_ui_headers:
        header.draw = ALL_HT_header_draw_override


def unregister():
    for header in bl_ui_headers:
        header.draw = header_map[header.bl_space_type]
        

