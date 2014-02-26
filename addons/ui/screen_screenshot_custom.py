
bl_info = {
    "name": "Custom Screenshot Creator",
    "author": "Satish Goda (iluvblender on BA, satishgoda@gmail.com)",
    "version": (0, 1),
    "blender": (2, 7, 0),
    "location": "Save Screenshot Custom",
    "description": "Create screenshots of all the individual areas in the current screen (and the whole area also if you want)",
    "warning": "",
    "category": "Screen"
}


import bpy


def _screen(self, context):
    import screenshot
    screenshot = screenshot.Screenshot()

    bpy.ops.screen.screenshot(filepath=screenshot.filepath)

    context.window_manager.clipboard = screenshot.dirname


def _screen_all_areas(self, context):
    import screenshot
    screenshot = screenshot.Screenshot()

    overrides = {}

    overrides['window'] = context.window
    overrides['screen'] = context.screen
    overrides['scene'] = context.scene

    kwargs = { 'full': False }

    for area in context.screen.areas:
        overrides['area'] = area
        overrides['region'] = area.regions[1]
        overrides['space_data'] = area.spaces.active

        screenshot.filename_suffix = area.type

        kwargs['filepath'] = screenshot.filepath

        bpy.ops.screen.screenshot(overrides, **kwargs)

    context.window_manager.clipboard = screenshot.dirname


class ScreenshotsCustom(bpy.types.Operator):
    """Create and save screenshots of different areas"""
    bl_idname = "screen.screenshot_custom"
    bl_label = "Save Screenshot Custom"
    bl_options = {'REGISTER'}

    _items = [('SCREEN', 'Current Screen', 'Capture the current screen'),
              ('SCREEN_ALL_AREAS', 'All Screen Areas', 'Capture all the areas of the current screen'),
              ('SCREEN_AND_ALL_AREAS', 'Current Screen and all Areas', 'Capture screen and also all its areas')
              ]

    capture_mode = bpy.props.EnumProperty(items=_items, name="Capture mode", default='SCREEN_AND_ALL_AREAS')
    
    def __init__(self):
        print("Initializing " + self.bl_idname)        

    def invoke(self, context, event):
        print("Invoking " + self.bl_idname)
        if (event.oskey and event.type == 'C'):
            return self.execute(context)
        else:
            return context.window_manager.invoke_props_dialog(self)
    
    def execute(self, context):
        print("Executing " + self.bl_idname)

        if self.capture_mode == 'SCREEN':
            _screen(self, context)
        elif self.capture_mode == 'SCREEN_ALL_AREAS':
            _screen_all_areas(self, context)
        elif self.capture_mode == 'SCREEN_AND_ALL_AREAS':
            _screen_all_areas(self, context)
            _screen(self, context)
        else:
            self.report({'ERROR'}, "Save Screenshot Custom: No other capture modes supported")
            return {'CANCELLED'}

        self.report({'INFO'}, "Screenshot saved in {0}".format(context.window_manager.clipboard))

        file_browser_areas = filter(lambda area: area.type == 'FILE_BROWSER', context.screen.areas)

        overrides = context.copy()
        
        for file_browser in file_browser_areas:
            overrides['area'] = file_browser
            bpy.ops.file.refresh(overrides)
        
        return {'FINISHED'}
    
    def __del__(self):
        print("Destructing " + self.bl_idname)


def register():
    bpy.utils.register_class(ScreenshotsCustom)
    
    keyconfigs = bpy.context.window_manager.keyconfigs

    if 'Screen' not in keyconfigs.addon.keymaps:
        keyconfigs.addon.keymaps.new('Screen')

    keymap = keyconfigs.addon.keymaps['Screen']

    capture_mode_mapping = (('SCREEN', {}),
                            ('SCREEN_ALL_AREAS', {'shift': True}),
                            ('SCREEN_AND_ALL_AREAS', {'ctrl': True})
                            )

    for capture_mode, kwargs in capture_mode_mapping:
        kmi = keymap.keymap_items.new(ScreenshotsCustom.bl_idname, 'C', 'PRESS', oskey=True, **kwargs)
        setattr(kmi.properties, 'capture_mode', capture_mode)


def unregister():
    keyconfigs = bpy.context.window_manager.keyconfigs

    keymap = keyconfigs.addon.keymaps['Screen']

    for i in ScreenshotsCustom._items:
        kmi = keymap.keymap_items[ScreenshotsCustom.bl_idname]
        keymap.keymap_items.remove(kmi)

    bpy.utils.unregister_class(ScreenshotsCustom)


if __name__ == '__main__':
    register()
    #bpy.ops.screen.screenshot_custom()
