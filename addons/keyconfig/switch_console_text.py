bl_info = {
    'name': 'Switch Between Console and Text Editor Spaces',
    'description': 'Switch Between Console and Text Editor Spaces by using the SHIFT+ESC key',
    'category': 'System',
    "author": "Satish Goda (iluvblender on BA, satishgoda@gmail.com)",
    "version": (0, 1),
    "blender": (2, 7, 0),
}


import bpy

print (__name__)


def register():
    print(bpy.context, ' in {}.register'.format(__name__))


def unregister():
    print(bpy.context, ' in {}.register'.format(__name__))
