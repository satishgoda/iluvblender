# -*- coding: utf-8 -*-
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

# <pep8 compliant>

bl_info = {
    "name": "Rename Object",
    "author": "Satish Goda (iluvblender on BA, satishgoda@gmail.com)",
    "version": (0, 1),
    "blender": (2, 6, 9),
    "location": "Bring up the Operator Search menu and type 'Rename Object' ",
    "description": "Rename Object by manually invoking the operator",
    "warning": "",
    "category": "Object"}

"""Rename Object quickly using an Operator"""

import bpy
from bpy.props import StringProperty

class RenameObject(bpy.types.Operator):
    bl_idname = 'object.rename'
    bl_label = "Rename Object"
    bl_options = {'REGISTER', 'UNDO'}
    
    new_name = StringProperty()
    
    @classmethod
    def poll(cls, context):
        return ( context.selected_objects and (len(context.selected_objects) == 1) )
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)
    
    def execute(self, context):
        if self.new_name.strip() == '':
            return {'CANCELLED'}
        else:
            context.selected_objects[0].name = self.new_name
            return {'FINISHED'}
    
def register():
    bpy.utils.register_class(RenameObject)
    
def unregister():
    bpy.utils.unregister_class(RenameObject)

if __name__ == '__main__':
    register()
