bl_info = {
    "name": "Modify frame range for the RBD simulation and scene as well",
    "author": "Satish Goda (iluvblender on BA, satishgoda@gmail.com)",
    "version": (0, 1),
    "blender": (2, 6, 9),
    "location": "Operator Search Menu",
    "description": "Modify the scene frame range and rbd point cache frame range from one place",
    "warning": "",
    "category": "System"}

"""Modify frame range globally"""

import bpy
from bpy.props import IntProperty

class RBDChangeFrangeOperator(bpy.types.Operator):
    """Modify the frame range for the RBD simulation"""
    bl_idname = "object.rbd_change_frange"
    bl_label = "RBD Change Frange"

    frame_start = IntProperty(name="Start Frame")
    frame_end = IntProperty(name="End Frame")

    @classmethod
    def poll(cls, context):
        rbdworld = context.scene.rigidbody_world
        return rbdworld and \
               (not rbdworld.point_cache.is_baking) and \
               (not rbdworld.point_cache.is_baked)

    def invoke(self, context, event):
        wm = context.window_manager
        scene = context.scene
        self.frame_start = scene.frame_start
        self.frame_end = scene.frame_end
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        scene = context.scene
        rbdworld = scene.rigidbody_world
        scene.frame_start = self.frame_start
        scene.frame_end = self.frame_end
        rbdworld.point_cache.frame_start = self.frame_start
        rbdworld.point_cache.frame_end = self.frame_end
        return {'FINISHED'}


def register():
    bpy.utils.register_class(RBDChangeFrangeOperator)


def unregister():
    bpy.utils.unregister_class(RBDChangeFrangeOperator)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.rbd_change_frange('INVOKE_DEFAULT')

