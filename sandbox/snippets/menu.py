import bpy


class VIEW3D_MT_quick_tools(bpy.types.Menu):
    bl_label = 'Quick Tools'
    
    def draw(self, context):
        layout = self.layout
        column = layout.column()
        column.prop_menu_enum(context.area, 'type')
        column.prop_menu_enum(context.scene.render, 'engine')

  
def register():
    bpy.utils.register_class(VIEW3D_MT_quick_tools)


def unregister():
    bpy.utils.unregister_class(VIEW3D_MT_quick_tools)


if __name__ == '__main__':
    register()
    bpy.ops.wm.call_menu(name='VIEW3D_MT_quick_tools')
    print (bpy.types.VIEW3D_MT_quick_tools)
    print (type(bpy.types.VIEW3D_MT_quick_tools))
    print (bpy.types.VIEW3D_MT_quick_tools.__bases__)
    
