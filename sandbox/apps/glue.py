bl_info = {
    'name':'Glue app with Blender',
    'description': 'This addon glues the custom application and factory blender together',
    'category': 'System',
}


import bpy


def register():
    print(__name__, type(bpy.context))
    pass


def unregister():
    print(__name__, type(bpy.context))
    pass


if __name__ ==  '__main__':
    register()

