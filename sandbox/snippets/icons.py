if isinstance(item, bpy.types.ID):
    box.prop(item, 'name', icon=bpy.types.EnumPropertyItem.bl_rna.properties['icon'].enum_items[layout.icon(item)].identifier)
else:
    box.label(str(item))
