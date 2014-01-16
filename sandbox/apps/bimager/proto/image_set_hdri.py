# -*- coding: utf-8 -*-
import bpy
import os
    

def getImageEditor(context):
    areas = context.screen.areas
    for area in areas:
        if area.type == 'IMAGE_EDITOR':
        return area
    return None


def setImageEditorImage(editor, image):
    editor.spaces.active.image = image


def updateRenderSettings(context):
    render = context.scene.render
    render.resolution_x = image.size[0]
    render.resolution_y = image.size[1]
    render.resolution_percentage = 100


def imageLoad(context):
    params = context.space_data.params
    directory, filename = params.directory, params.filename
    filepath = os.path.join(directory, filename)
    blend_data = context.blend_data

    if filename not in blend_data.images:
      blend_data.images.load(filepath)

    return blend_data.images[filename]


def main(context):


class SetHDRIForEdit(bpy.types.Operator):
    """Set the selected HDRI for Editing"""
    bl_idname = "image.set_hdri"
    bl_label = "Set HDRI Image"

    @classmethod
    def poll(cls, context):
        return (context.space_data.params.filename)

    def execute(self, context):
        image = imageLoad(context)
        editor = getImageEditor(context)
        if editor:
            setImageEditorImage(image)
            updateRenderSettings(image)
        return {'FINISHED'}


def FILEBROWSER_HT_header_draw1(self, context):
    layout = self.layout
    layout.operator('image.set_hdri')


def register():
    bpy.utils.register_class(SetHDRIForEdit)
    bpy.types.FILEBROWSER_HT_header.append(FILEBROWSER_HT_header_draw1)


def unregister():
    bpy.utils.unregister_class(SetHDRIForEdit)    
    bpy.types.FILEBROWSER_HT_header.remove(FILEBROWSER_HT_header_draw1)


if __name__ == "__main__":
    register()


