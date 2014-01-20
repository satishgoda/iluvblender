# <pep8 compliant>

bl_info = {
    "name": "Display Area Spaces in Header",
    "author": "Satish Goda (iluvblender on BA, satishgoda@gmail.com)",
    "version": (0, 1),
    "blender": (2, 7, 0),
    "location": "Most Editors -> Header",
    "description": "Displays spaces that were activated in all the areas so that you can \
                    conviniently switch between then",
    "warning": "",
    "category": "System"}

"""Display Area Spaces in Header"""

import bpy

def draw(self, context):
     row = self.layout.row(align=True)
     for space in filter(lambda space: space.type != context.area.type, context.area.spaces):
         op_props = row.operator('wm.context_set_enum', text=space.bl_rna.name.replace('Space', '').strip())
         op_props.data_path = "area.type"
         op_props.value = space.type

def register():
    bpy.types.VIEW3D_HT_header.append(draw)
    bpy.types.CONSOLE_HT_header.append(draw)
    bpy.types.NODE_HT_header.append(draw)
    bpy.types.IMAGE_HT_header.append(draw)
    bpy.types.OUTLINER_HT_header.append(draw)
    bpy.types.PROPERTIES_HT_header.append(draw)
    bpy.types.TEXT_HT_header.append(draw)

def unregister():
    bpy.types.VIEW3D_HT_header.remove(draw)
    bpy.types.CONSOLE_HT_header.remove(draw)
    bpy.types.NODE_HT_header.remove(draw)
    bpy.types.IMAGE_HT_header.remove(draw)
    bpy.types.OUTLINER_HT_header.remove(draw)
    bpy.types.PROPERTIES_HT_header.remove(draw)
    bpy.types.TEXT_HT_header.remove(draw)
    
if __name__ == '__main__':
    register()
