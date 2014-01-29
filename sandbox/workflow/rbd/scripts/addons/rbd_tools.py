import bpy


class RBDSelectMacro(bpy.types.Macro):
    """TODO"""
    bl_idname = "object.rbd_select"
    bl_label = "RBD Select"
    bl_options = {'REGISTER', 'UNDO'}
 

class RBDSelectAndHideMacro(bpy.types.Macro):
    """TODO"""
    bl_idname = "object.rbd_select_hide"
    bl_label = "RBD Select and Hide"
    bl_options = {'REGISTER', 'UNDO'}


def register():
    bpy.utils.register_class(RBDSelectMacro)
    op = RBDSelectMacro.define("OBJECT_OT_select_linked")
    op.properties.type = 'OBDATA'
    
    bpy.utils.register_class(RBDSelectAndHideMacro)
    op = RBDSelectAndHideMacro.define("OBJECT_OT_select_linked")
    op.properties.type = 'OBDATA'
    op = RBDSelectAndHideMacro.define("OBJECT_OT_hide_view_set")
    op.properties.unselected = False


def unregister():
    bpy.utils.unregister_class(RBDSelectAndHideMacro)
    bpy.utils.unregister_class(RBDSelectMacro)

if __name__ == '__main__':
    register()
