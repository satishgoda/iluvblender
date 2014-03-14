bl_info = {
    'name': 'Development tools for Blender',
    'description': 'Registers operators, panels, menus etc to abet development and introspection',
    'category': 'Development',
}

"""Registers operators, panels, menus etc to abet development and introspection"""

import bpy

import rna_info


class ContextProperties(bpy.types.Operator):
    bl_idname = 'debug.context'
    bl_label = 'Debug Context Properties'
    bl_description = 'View the properties of the current context'
    
    def execute(self, context):
        print(rna_info.get_direct_properties(context.bl_rna))
        return {'FINISHED'}


_operators = (
    ContextProperties,
)


def register():
    for operator in _operators:
        bpy.utils.register_class(operator)


def unregister():
    for operator in _operators:
        bpy.utils.unregister_class(operator)


if __name__ == '__main__':
    register()
