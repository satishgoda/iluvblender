import bpy
import os

filepath = os.path.splitext(bpy.data.filepath)

if filepath[0].endswith('untitled'):
    print("ERROR: Cannot render. Filename is untitled.blend")
else:
    renderingContext = bpy.context.scene.render

    if renderingContext.filepath == '/tmp/':
        renderingContext.filepath = filepath[0]+'.'

    bpy.ops.render.render()

    imageFileName = renderingContext.filepath + renderingContext.file_format.lower()

    bpy.data.images['Render Result'].save_render(imageFileName)

    bpy.ops.wm.save_mainfile(filepath=bpy.data.filepath)
