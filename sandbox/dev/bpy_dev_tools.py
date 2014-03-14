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
            typ = eval('bpy.types.'+typestr)
            if (issubclass(typ, bclass) and typ is not bclass):
                classes.append(typ)
        return classes
  
    @classmethod
    def headers(cls):
        base = bpy.types.Header
        return cls._get(base)


class ContextSpaceData(bpy.types.Operator):
    bl_idname = 'debug.context_space_data'
    bl_label = 'Debug Context Space Data Properties'
    bl_description = 'View the properties of the active space data'
    bl_options = {'REGISTER'}

    _items = (
        ('BOOLEAN', 'Boolean', ''),
        ('ENUM', 'Enumeration', ''),
        ('INT', 'Integer', ''),
        ('FLOAT', 'Real', ''),
        ('STRING', 'String', ''),
        ('POINTER', 'Group', ''),
        ('COLLECTION', 'Collection', ''),        
    )

    prop_type = bpy.props.EnumProperty(items= _items, default='BOOLEAN')

    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'prop_type')
        #props = get_direct_properties(context.space_data.bl_rna)
        props = context.space_data.bl_rna.properties
        #layout.label(context.space_data.type)
        flow = layout.column_flow()
        for prop in props:
            if prop.type == self.prop_type:
                flow.prop(context.space_data, prop.identifier)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=500)
    
    def check(self, context):
        self.prop_type = self.prop_type
    
    def execute(self, context):
        return {'FINISHED'}


def ALL_HT_debug_context_draw(self, context):
    space_data = context.space_data
    space_type = space_data.type
    space_icon = space_data.bl_rna.properties['type'].enum_items[space_type].icon
    
    layout = self.layout
    row = layout.row()
    row.operator('debug.context_space_data', text='Debug', icon=space_icon)


_operators = (
    ContextSpaceData,
)


def register():
    for operator in _operators:
        bpy.utils.register_class(operator)

    for header in BlenderTypes.headers():
        header.append(ALL_HT_debug_context_draw)


def unregister():
    for operator in _operators:
        bpy.utils.unregister_class(operator)

    for header in BlenderTypes.headers():
        header.remove(ALL_HT_debug_context_draw)


if __name__ == '__main__':
    register()
