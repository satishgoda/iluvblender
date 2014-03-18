bl_info = {
    'name': 'Development tools for Blender',
    'description': 'Registers operators, panels, menus etc to abet development and introspection',
    'category': 'Development',
}

"""Registers operators, panels, menus etc to abet development and introspection"""

import bpy

import bpy.props

from rna_info import get_direct_properties


class BlenderTypes(object):
    base = bpy.types
    
    @classmethod
    def _get(cls, bclass):
        classes = []
        for typestr in dir(cls.base):
            typ = getattr(cls.base, typestr)
            if (issubclass(typ, bclass) and typ is not bclass):
                classes.append(typ)
        return classes
  
    @classmethod
    def headers(cls):
        base = bpy.types.Header
        return cls._get(base)

    @classmethod
    def panels(cls):
        base = bpy.types.Panel
        return cls._get(base)


class ContextSpaceData(bpy.types.Operator):
    bl_idname = 'debug.context_space_data'
    bl_label = 'Context Space Data Properties'
    bl_description = 'View the properties of the active space data'
    bl_options = {'REGISTER'}

    _items = (
        ('ALL', 'All', ''),
        ('BOOLEAN', 'Boolean', ''),
        ('ENUM', 'Enumeration', ''),
        ('INT', 'Integer', ''),
        ('FLOAT', 'Real', ''),
        ('STRING', 'String', ''),
        ('POINTER', 'Group', ''),
        ('COLLECTION', 'Collection', ''),        
    )

    prop_type = bpy.props.EnumProperty(items=_items, default='ALL')

    def draw(self, context):
        layout = self.layout
        props = filter(lambda prop: prop.identifier != 'rna_type', context.space_data.bl_rna.properties)
        
        if self.prop_type != 'ALL':
            props = filter(lambda prop: prop.type == self.prop_type, props)
        
        flow = layout.column_flow()
        flow.box().prop(context.space_data, 'rna_type')
        
        prop_map = {}
        criterion = lambda prop: prop.type
        
        import itertools
        for key, group in itertools.groupby(sorted(props, key=criterion), criterion):
            prop_map[key] = tuple(group)
        
        for key in prop_map:
            flow.box().label(key)
            if prop_map[key]:
                for prop in prop_map[key]:
                    flow.prop(context.space_data, prop.identifier)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=500)
      
    def execute(self, context):
        return {'FINISHED'}


def ALL_HT_debug_context_draw(self, context):
    space_data = context.space_data
    space_type = space_data.type
    space_icon = space_data.bl_rna.properties['type'].enum_items[space_type].icon
    
    layout = self.layout
    row = layout.row()
    row.operator_menu_enum('debug.context_space_data', 'prop_type', text="Properties", icon=space_icon)


def ALL_PT_debug_identifier_draw(self, context):
    layout = self.layout
    row = layout.row()
    row.label(self.__class__.__name__)


_operators = (
    ContextSpaceData,
)


def register():
    for operator in _operators:
        bpy.utils.register_class(operator)

    for header in BlenderTypes.headers():
        header.append(ALL_HT_debug_context_draw)
        
    for panel in BlenderTypes.panels():
        panel.append(ALL_PT_debug_identifier_draw)


def unregister():
    for operator in _operators:
        bpy.utils.unregister_class(operator)

    for header in BlenderTypes.headers():
        header.remove(ALL_HT_debug_context_draw)

    for panel in BlenderTypes.panels():
        panel.remove(ALL_PT_debug_identifier_draw)


if __name__ == '__main__':
    register()
