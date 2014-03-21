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
import os


class DebugPythonPathOperator(bpy.types.Operator):
    bl_idname = 'debug.python_path_open'
    bl_label = 'Open Python Path'
    bl_options = {'INTERNAL'}
    
    directory = bpy.props.StringProperty(
        name="Python directory path",
        description="Python directory path",
        maxlen=1024,
        subtype='DIR_PATH',
        )
    
    filepath = bpy.props.StringProperty(
        name="Python file in the directory path",
        description="Python file in directory path",
        maxlen=1024,
        subtype='FILE_PATH',
    )
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        if self.filepath == self.directory:
            self.report({'WARNING'}, "You have not chosen a filepath")
        else:
            filepath = self.filepath
            basename = os.path.basename(filepath)
            context.area.type = 'TEXT_EDITOR'
            if basename in context.blend_data.texts:
                self.report({'WARNING'}, "This file was already opened. Switched to it :)")
                bpy.ops.wm.context_set_id(data_path='space_data.text', value=basename)
            else:
                bpy.ops.text.open(filepath=filepath)
        
        return {'FINISHED'}

    def cancel(self, context):
        pass


class DebugPythonPathsMenu(bpy.types.Menu):
    bl_idname = 'WM_MT_debug_python_paths'
    bl_label = 'Python Path'
    
    def draw(self, context):
        from mydebug import getPythonPaths
        area = context.area
        header = area.regions[0]
        header_at_bottom = area.y == header.y
        
        paths = getPythonPaths()
        display_paths = reversed(paths) if header_at_bottom else paths
        
        layout = self.layout
        
        for index, path in enumerate(display_paths, start=1):
            index = (len(paths) - index + 1) if header_at_bottom else index
            text = "{0:02})   {1}".format(index, path)
            
            column = layout.column()
            column.scale_y = 1.1
            
            if os.path.exists(path):
                if os.path.isdir(path):
                    oper_props = column.operator('debug.python_path_open', text=text, icon='FILE_FOLDER')
                    oper_props.filepath = path+os.path.sep
                else:
                    column.label(text, icon='FILE_BLANK')
            else:
                column.label(text, icon='CANCEL')


def CONSOLE_HT_header_debug_paths_menu(self, context):
    layout = self.layout
    row = layout.row()
    row.scale_x = 1.1
    row.alert = True
    row.menu('WM_MT_debug_python_paths', icon='FILE_SCRIPT')


def register():
    bpy.utils.register_class(DebugPythonPathsMenu)
    bpy.utils.register_class(DebugPythonPathOperator)
    bpy.types.CONSOLE_HT_header.append(CONSOLE_HT_header_debug_paths_menu)


def unregister():
    bpy.utils.unregister_class(DebugPythonPathsMenu)
    bpy.utils.unregister_class(DebugPythonPathOperator)
    bpy.types.CONSOLE_HT_header.remove(CONSOLE_HT_header_debug_paths_menu)

