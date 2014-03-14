bl_info = {
    'name': 'Development tools for Blender',
    'description': 'Registers operators, panels, menus etc to abet development and introspection',
    'category': 'Development',
}

"""Registers operators, panels, menus etc to abet development and introspection"""

import bpy

from rna_info import get_direct_properties


def isType(parent):
    types = []
    for typestr in dir(bpy.types):
        typ = eval('bpy.types.'+typestr)
        if (issubclass(typ, parent) and not (typ is parent)):
            types.append(typ)
    return types


class ContextProperties(bpy.types.Operator):
    bl_idname = 'debug.context'
    bl_label = 'Debug Context Properties'
    bl_description = 'View the properties of the current context'
    
    def execute(self, context):
        props = get_direct_properties(context.space_data.bl_rna)
        print(context.space_data.type)
        for prop in props:
            print("\t{}".format(prop.identifier))
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

    for header in isType(bpy.types.Header):
        print(header)
        header.append(ALL_HT_debug_context_draw)


def unregister():
    for operator in _operators:
        bpy.utils.unregister_class(operator)

    for header in isType(bpy.types.Header):
        header.remove(ALL_HT_debug_context_draw)


if __name__ == '__main__':
    register()
