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


def _doIt(process):
    only_headers = lambda typestr: typestr.find('HT_header') != -1
    processstr = ('remove', 'append')
    for headerstr in filter(only_headers, dir(bpy.types)):
        headertype = eval('bpy.types.' + headerstr)
        getattr(headertype, processstr[process])(draw)


def register():
    _doIt(1)


def unregister():
    _doIt(0)
   
    
if __name__ == '__main__':
    register()
