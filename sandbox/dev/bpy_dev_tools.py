bl_info = {
    'name': 'Development tools for Blender',
    'description': 'Registers operators, panels, menus etc to abet development and introspection',
    'category': 'Development',
}

"""Registers operators, panels, menus etc to abet development and introspection"""

import bpy

import rna_info

HEADER_TYPES = filter(lambda identifier: identifier.endswith('_HT_header'), dir(bpy.types))


class ContextProperties(bpy.types.Operator):
    bl_idname = 'debug.context'
    bl_label = 'Debug Context Properties'
    bl_description = 'View the properties of the current context'
    
    def execute(self, context):
        print(rna_info.get_direct_properties(context.space_data.bl_rna))
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

    for header_identifier in HEADER_TYPES:
        eval('.'.join(('bpy.types', header_identifier))).append(ALL_HT_debug_context_draw)


def unregister():
    for operator in _operators:
        bpy.utils.unregister_class(operator)

    for header_identifier in HEADER_TYPES:
        eval('.'.join(('bpy.types', header_identifier))).remove(ALL_HT_debug_context_draw)

if __name__ == '__main__':
    register()
