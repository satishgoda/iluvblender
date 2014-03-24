import bpy


bl_ui_headers_only = lambda header: header.__module__.startswith('bl_ui')
bl_ui_headers = tuple(filter(bl_ui_headers_only, bpy.types.Header.__subclasses__()))

header_map = { header.bl_space_type: header.draw for header in bl_ui_headers }


class ContextExplorer(bpy.types.Operator):
    bl_idname = 'debug.context_explorer'
    bl_label = 'Context Explorer'
    bl_description = 'Context Explorer'
    bl_options = {'REGISTER'}
    
    def draw(self, context):
        layout = self.layout

        header = layout.box()

        row = header.row()
        row.label(context.area.type)
        row.label(layout.enum_item_name(context.area, 'type', context.area.type))
        row.label(layout.enum_item_description(context.area, 'type', context.area.type))

        split = layout.split(percentage=0.6)

        column1 = split.column()
        column2 = split.column()

        rna_properties = context.bl_rna.properties
        rna_property_identifiers = set(map(lambda prop: prop.identifier, rna_properties))
        attributes = set(dir(context)) - rna_property_identifiers
        ignored_attributes = {'active_operator', 'bl_rna', 'copy'}
        
        for name in sorted(attributes - ignored_attributes):
            if (not name.startswith('__')) and getattr(context, name):
                column1.row().label('context.'+name)
                box = column1.box()
                value = eval('context.'+name)
                if isinstance(value, list):
                    for item in value:
                        box.label(str(item))
                else:
                    box.label(str(value))

        for prop in sorted(rna_properties, key=lambda prop: prop.type):
            column2.prop(context, prop.identifier)
    
    def invoke(self, context, value):
        return context.window_manager.invoke_props_dialog(self, width=1280)

    def execute(self, context):
        return {'FINISHED'}


def ALL_HT_header_draw_override(self, context):
    layout = self.layout
    
    if bpy.app.debug_value == 1:
        area = context.area
        space = context.space_data
        space_name = layout.enum_item_name(space, 'type', area.type)
        space_description = layout.enum_item_description(area, 'type', area.type)
        text = "[{}] - {}".format(space_name, space_description)
        icon = area.bl_rna.properties['type'].enum_items[area.type].icon
        row = layout.row()
        row.alert = True
        row.operator_context = 'EXEC_DEFAULT'
        row.operator('wm.debug_menu', text='', icon='LOOP_BACK').debug_value = 0
        row.operator_context = 'INVOKE_DEFAULT'
        row.operator('debug.context_explorer', text='', icon='QUESTION')
        row.label(text, icon=icon)
        
    else:
        header_map[context.area.type](self, context)


def register():
    bpy.utils.register_class(ContextExplorer)
    
    for header in bl_ui_headers:
        header.draw = ALL_HT_header_draw_override

    bpy.app.debug_value = 1


def unregister():
    bpy.utils.unregister_class(ContextExplorer)
    
    for header in bl_ui_headers:
        header.draw = header_map[header.bl_space_type]

    for area in bpy.context.screen.areas:
        area.tag_redraw()
        
    bpy.app.debug_value = 0

