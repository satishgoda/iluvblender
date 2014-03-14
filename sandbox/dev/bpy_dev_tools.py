bl_info = {
    'name': 'Development tools for Blender',
    'description': 'Registers operators, panels, menus etc to abet development and introspection',
    'category': 'Development',
}

"""Registers operators, panels, menus etc to abet development and introspection"""

import bpy

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


class ContextProperties(bpy.types.Operator):
    bl_idname = 'debug.context'
    bl_label = 'Debug Context Properties'
    bl_description = 'View the properties of the current context'
    bl_options = {'REGISTER'}

    def draw(self, context):
        layout = self.layout
        props = get_direct_properties(context.space_data.bl_rna)
        layout.label(context.space_data.type)
        flow = layout.column_flow()
        for prop in props:
            flow.prop(context.space_data, prop.identifier)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=500)
    
    def execute(self, context):
        return {'FINISHED'}


def ALL_HT_debug_context_draw(self, context):
    layout = self.layout
    row = layout.row()
    row.operator('debug.context')


_operators = (
    ContextProperties,
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
