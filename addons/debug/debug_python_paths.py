# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# Author: Satish Goda
# E-mail: satishgoda@gmail.com
# URL: http://learningblender3dsoftware.blogspot.in

import bpy


class DebugPythonPathsMenu(bpy.types.Menu):
    bl_idname = 'WM_MT_debug_python_paths'
    bl_label = 'Python Path'
    
    def draw(self, context):
        from mydebug import getPythonPaths
        area = context.area
        header = area.regions[0]
        paths = getPythonPaths()
        
        display_paths = reversed(paths) if area.y == header.y else paths
        
        layout = self.layout
        
        for index, path in enumerate(display_paths, start=1):
            if area.y == header.y:
                index = len(paths) - index + 1
            layout.label("{0:02} {1}".format(index, path))


def CONSOLE_HT_header_debug_paths_menu(self, context):
    layout = self.layout
    row = layout.row()
    row.scale_x = 1.1
    row.alert = True
    row.menu('WM_MT_debug_python_paths', icon='FILE_SCRIPT')


def register():
    bpy.utils.register_class(DebugPythonPathsMenu)
    bpy.types.CONSOLE_HT_header.append(CONSOLE_HT_header_debug_paths_menu)


def unregister():
    bpy.utils.unregister_class(DebugPythonPathsMenu)
    bpy.types.CONSOLE_HT_header.remove(CONSOLE_HT_header_debug_paths_menu)

