>>> ccontext = bpy.context.copy()

>>> for screen in bpy.data.screens:
...     if screen.name in 'Default':
...         continue
...     ccontext['screen'] = screen
...     bpy.ops.screen.delete(ccontext)
...
>>>
