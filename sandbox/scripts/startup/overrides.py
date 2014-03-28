import bpy
from bpy_types import StructRNA as bpy_struct
import collections


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


class LabelOp(bpy.types.Operator):
    bl_idname = 'debug.label'
    bl_label = ''
    bl_description = ''
    bl_options = {'REGISTER', 'UNDO'}

    data_path = bpy.props.StringProperty()
    data_path_type = bpy.props.StringProperty()

    def draw(self, context):
        layout = self.layout
        path_type = self.data_path_type
        layout.box().label(self.data_path)
        layout.label(path_type)

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self)

    def execute(self, context):
        context.window_manager.clipboard = self.data_path
        return {'FINISHED'}


class ContextExplorer(bpy.types.Operator):
    bl_idname = 'debug.context_explorer'
    bl_label = 'Context Explorer'
    bl_description = 'Context Explorer'
    bl_options = {'REGISTER'}

    def draw(self, context):
        layout = self.layout

        header = layout.box().row()
        split = layout.split(percentage=0.65)
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
                args = (item, 'name')
                kwargs = {'text': ''}
                if isinstance(item, bpy.types.Object):
                    kwargs['icon'] = 'OBJECT_DATA'
                layout.prop(*args, **kwargs)
            elif isinstance(item, bpy.types.ObjectBase):
                layout.label(item.object.name)
            else:
                layout.label(str(item))

        def description(item):
            return "{}".format(item.rna_type.description)

        for name in sorted(attributes - ignored_attributes):
            value = getattr(context, name)
            if (not name.startswith('__')) and value:
                split_C_prop = column1.box().split(percentage=0.4)
                split_C_prop_name = split_C_prop.column()
                split_C_prop_description = split_C_prop.column()
                split_C_prop_name.alert = True
                column = column1.column_flow()
                oper_props = split_C_prop_name.operator('debug.label', text='context.'+name)
                oper_props.data_path = 'context.'+name
                if isinstance(value, collections.abc.Sequence):
                    oper_props.data_path_type = str(value[0].__class__)
                    split_C_prop_description.label(description(value[0]))
                    for item in value:
                        draw_item(column, item)
                else:
                    oper_props.data_path_type = str(value.__class__)
                    split_C_prop_description.label(description(value))
                    draw_item(column, value)

        for prop in sorted(rna_properties, key=lambda prop: prop.type):
            column2.prop(context, prop.identifier)

    def invoke(self, context, value):
        return context.window_manager.invoke_props_dialog(self, width=980)

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

        saved_operator_context = row.operator_context
        row.operator_context = 'EXEC_SCREEN'
        row.prop(context.window_manager, 'app_mode', text = '')
        row.operator_context = saved_operator_context

        row.label(text, icon=icon)
    else:
        header_map[context.area.type](self, context)


def switch_header_menu_item(self, context):
    layout = self.layout

    saved_operator_context = layout.operator_context
    layout.operator_context = 'EXEC_DEFAULT'

    args = ('wm.debug_menu',)
    kwargs = {'text': 'Draw Custom Headers', 'icon':'GHOST_ENABLED'}
    layout.operator(*args, **kwargs).debug_value = 1

    layout.operator_context = saved_operator_context
    layout.separator()


def handle_app_mode(self, context):
    app_mode = context.window_manager.app_mode
    if app_mode == 'BUILD':
        context.area.type = 'IMAGE_EDITOR'
    elif app_mode == 'CREATE':
        context.area.type = 'SEQUENCE_EDITOR'
    elif app_mode == 'VIEW':
        context.area.type = 'FILE_BROWSER'

    area = context.area
    if area.is_header_bottom():
        overrides = context.copy()
        overrides['region'] = area.regions[0]
        bpy.ops.screen.header_flip(overrides)


@bpy.app.handlers.persistent
def application_default_mode(incoming):
    bpy.data.screens['Default'].areas[4].type = 'IMAGE_EDITOR'


@bpy.app.handlers.persistent
def make_headers_consistent(incoming):
    window = bpy.context.window_manager.windows[0]

    for area in filter(bpy.types.Area.is_header_bottom, window.screen.areas):
        overrides = bpy.context.copy()

        overrides['window'] = window
        overrides['screen'] = window.screen
        overrides['area'] = area
        overrides['region'] = area.regions[0]

        bpy.ops.screen.header_flip(overrides)


def register():
    bpy.utils.register_class(ContextExplorer)
    bpy.utils.register_class(LabelOp)

    for header in bl_ui_headers:
        if hasattr(header.draw, '_draw_funcs'):
            for func in header.draw._draw_funcs:
                print(func.__module__, func.__name__)
        header.draw = ALL_HT_header_draw_override

    bpy.app.debug_value = 1

    bpy.types.INFO_MT_window.prepend(switch_header_menu_item)

    items = (('BUILD', 'Build', 'BUILD the storyboard'),
             ('CREATE', 'Create', 'Create the storyboard'),
             ('VIEW', 'View', 'View the storyboard'))

    bpy.types.WindowManager.app_mode = bpy.props.EnumProperty(items=items,
                                                            name="Application Mode",
                                                            description="application modes",
                                                            default='BUILD',
                                                            update=handle_app_mode)

    bpy.app.handlers.load_post.append(application_default_mode)
    bpy.app.handlers.load_post.append(make_headers_consistent)

    bpy.types.Area.is_header_bottom = lambda self: self.y == self.regions[0].y

    bpy.types.Screen.area_info = lambda self: tuple((area.type, area, (area.x, area.y), (area.width, area.height)) for area in self.areas)


def unregister():
    bpy.utils.unregister_class(ContextExplorer)
    bpy.utils.unregister_class(LabelOp)

    for header in bl_ui_headers:
        header.draw = header_map[header.bl_space_type]

    for area in bpy.context.screen.areas:
        area.tag_redraw()

    bpy.app.debug_value = 0

    bpy.types.INFO_MT_window.remove(switch_header_menu_item)

    bpy.app.handlers.load_post.remove(make_headers_consistent)
    bpy.app.handlers.load_post.remove(application_default_mode)


    del bpy.types.Area.is_header_bottom
    del bpy.types.Screen.area_info


if __name__ == '__main__':
    register()
