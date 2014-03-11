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
import bpy
from bpy.types import Header


class PROPERTIES_HT_header(Header):
    bl_space_type = 'PROPERTIES'

    def draw(self, context):
        layout = self.layout
        view = ocntext.space_data
        row = layout.row(align=True)
        #row.template_header(menus=True)
        if not view.use_pin_id:
            row.prop_menu_enum(context.area, 'type', text='#', icon='TRIA_DOWN')
            #row.prop_menu_enum(context.area, 'type', text='#', icon=self.layout.icon(context.area))
            #row.props_enum(context.area, 'type')
        row.prop(view, "context", text='', expand=False, icon_only=False, emboss=True)
        if view.use_pin_id:
            row.prop(view, "context", text='', expand=True, icon_only=True, emboss=False)
        else:
            row.prop_enum(context.area, 'type', 'OUTLINER')


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
