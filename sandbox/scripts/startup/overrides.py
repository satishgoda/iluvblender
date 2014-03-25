import bpy

bl_ui_headers_only = lambda header: header.__module__.startswith('bl_ui')
bl_ui_headers = tuple(filter(bl_ui_headers_only, bpy.types.Header.__subclasses__()))

header_map = { header.bl_space_type: header.draw for header in bl_ui_headers }


class Area(object):
    def __init__(self, context):
        area = context.area
        space = area.spaces.active
        self.name = bpy.types.UILayout.enum_item_name(space, 'type', area.type)
        self.description = bpy.types.UILayout.enum_item_description(area, 'type', area.type)
        self.icon = area.bl_rna.properties['type'].enum_items[area.type].icon
        self.type = area.type


class ContextExplorer(bpy.types.Operator):
    bl_idname = 'debug.context_explorer'
    bl_label = 'Context Explorer'
    bl_description = 'Context Explorer'
    bl_options = {'REGISTER'}
    
    def draw(self, context):
        layout = self.layout

        header = layout.box().row()
        split = layout.split(percentage=0.6)
        column1 = split.column()
        column2 = split.column()

        area = Area(context)

        header.label(area.type)
        header.label(area.name)
        header.label(area.description)

        rna_properties = context.bl_rna.properties
        rna_property_identifiers = set(map(lambda prop: prop.identifier, rna_properties))
        attributes = set(dir(context)) - rna_property_identifiers
        ignored_attributes = {'active_operator', 'bl_rna', 'copy'}

        def draw_item(layout, item):
            if isinstance(item, bpy.types.ID):
                box.prop(item, 'name')
            else:
                box.label(str(item))

        for name in sorted(attributes - ignored_attributes):
            if (not name.startswith('__')) and getattr(context, name):
                column1.row().label('context.'+name)
                box = column1.box()
                value = eval('context.'+name)
                if isinstance(value, list):
                    for item in value:
                        draw_item(box, item)
                else:
                    draw_item(box, value)

        for prop in sorted(rna_properties, key=lambda prop: prop.type):
            column2.prop(context, prop.identifier)
    
    def invoke(self, context, value):
        return context.window_manager.invoke_props_dialog(self, width=1280)

    def execute(self, context):
        return {'FINISHED'}


def ALL_HT_header_draw_override(self, context):
    if bpy.app.debug_value == 1:
        layout = self.layout
        
        row = layout.row(align=True)
        row.alert = True
        saved_operator_context = row.operator_context
        
        row.operator_context = 'EXEC_DEFAULT'
        row.operator('wm.debug_menu', text='', icon='LOOP_BACK').debug_value = 0
        row.operator_context = saved_operator_context
        row.operator('debug.context_explorer', text='', icon='QUESTION')
        
        area = Area(context)
        text = "[{}] - {}".format(area.name, area.description)
        icon = area.icon
        
        row.label(text, icon=icon)
        
    else:
        header_map[context.area.type](self, context)


def switch_header_menu_item(self, context):
    layout = self.layout
    
    saved_operator_context = layout.operator_context
    
    layout.operator_context = 'EXEC_DEFAULT'
    layout.operator('wm.debug_menu', text='Draw Custom Headers', icon='GHOST_ENABLED').debug_value = 1
    layout.operator_context = saved_operator_context
    
    layout.separator()


def register():
    bpy.utils.register_class(ContextExplorer)
    
    for header in bl_ui_headers:
        header.draw = ALL_HT_header_draw_override

    bpy.app.debug_value = 1
    
    bpy.types.INFO_MT_window.prepend(switch_header_menu_item)


def unregister():
    bpy.utils.unregister_class(ContextExplorer)
    
    for header in bl_ui_headers:
        header.draw = header_map[header.bl_space_type]

    for area in bpy.context.screen.areas:
        area.tag_redraw()
        
    bpy.app.debug_value = 0
    
    bpy.types.INFO_MT_window.remove(switch_header_menu_item)


if __name__ == '__main__':
    register()

