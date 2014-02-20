# -*- coding: utf-8 -*-
import bpy

bpy.app.debug = True
bpy.app.debug_python = True
bpy.app.debug_wm = True

render = bpy.context.scene.render

render.resolution_percentage = 100
render.filepath = '/tmp/MakeScreenCaseOperator.'
render.image_settings.file_format = 'H264'
render.ffmpeg.format = 'AVI'

bpy.ops.wm.window_fullscreen_toggle()
