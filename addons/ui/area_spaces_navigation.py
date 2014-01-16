import bpy

def draw(self, context):
     row = self.layout.row(align=True)
     for space in filter(lambda space: space.type != context.area.type, context.area.spaces):
         op_props = row.operator('wm.context_set_enum', text=space.bl_rna.name.replace('Space', '').strip())
         op_props.data_path = "area.type"
         op_props.value = space.type
         
bpy.types.VIEW3D_HT_header.append(draw)
bpy.types.CONSOLE_HT_header.append(draw)
bpy.types.NODE_HT_header.append(draw)
bpy.types.IMAGE_HT_header.append(draw)
bpy.types.OUTLINER_HT_header.append(draw)
bpy.types.PROPERTIES_HT_header.append(draw)
bpy.types.TEXT_HT_header.append(draw)

