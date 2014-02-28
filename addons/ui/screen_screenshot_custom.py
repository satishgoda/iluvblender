
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
import os


class Screenshot(object):
    filename_ext = 'png'
    filename_suffix = None
    filename_suffix_char = '_'
    filename = 'untitled'
    dirname = os.getcwd()

    def __init__(self):
        _filepath = bpy.data.filepath
        if _filepath:
            self.filename = bpy.path.display_name_from_filepath(_filepath)
            self.dirname = os.path.dirname(_filepath)

    @property
    def filepath(self):
        filename = self.filename
        if self.filename_suffix:
            filename += self.filename_suffix_char
            filename += self.filename_suffix
        filename += '.' + self.filename_ext
        return os.path.join(self.dirname, filename)


def _observer_file_browser(subject):
    from rna_info import get_direct_properties

    context = subject
    
    FILE_BROWSER = lambda area: area.spaces.active.type == 'FILE_BROWSER'
    SCREENSHOT_DIRECTORY = lambda params: context.window_manager.clipboard in params.directory
    to_update_filebrowser = lambda area: FILE_BROWSER(area) and SCREENSHOT_DIRECTORY(area.spaces.active.params)
    use_filter_props = lambda prop: prop.identifier.startswith('use_filter')

    overrides = context.copy()
    
    file_browser_areas = filter(to_update_filebrowser, context.screen.areas)

    for file_browser in file_browser_areas:
        params = file_browser.spaces.active.params

        for prop in filter(use_filter_props , get_direct_properties(params.bl_rna)):
            setattr(params, prop.identifier, False)

        params.use_filter = True
        params.use_filter_image = True
        params.display_type = 'FILE_IMGDISPLAY'

        overrides['area'] = file_browser
        overrides['space_data'] = file_browser.spaces.active

        bpy.ops.file.refresh(overrides)


def _observer_clipboard(context, subject):
    context.window_manager.clipboard = subject.dirname


def add_screenshot_observers(capture_mode):
    def capture(context, screenshot):
        capture_mode(context, screenshot)
        _observer_clipboard(context, screenshot)
        _observer_file_browser(context)
    return capture


def _capture_area(context, area, screenshot):
    overrides = context.copy()

    overrides.update((
                        ('area', area),
                        ('region', area.regions[1]),
                        ('space_data', area.spaces.active)
                    ))

    screenshot.filename_suffix = area.type

    kwargs = { 'full': False }
    kwargs['filepath'] = screenshot.filepath

    bpy.ops.screen.screenshot(overrides, **kwargs)


@add_screenshot_observers
def _screen(context, screenshot):
    bpy.ops.screen.screenshot(filepath=screenshot.filepath)


@add_screenshot_observers
def _screen_area(context, screenshot):
    area = context.area

    _capture_area(context, area, screenshot)


@add_screenshot_observers
def _screen_all_areas(context, screenshot):
    for area in context.screen.areas:
        _capture_area(context, area, screenshot)


class ScreenshotsCustom(bpy.types.Operator):
    """Create and save screenshots of different areas"""
    bl_idname = "screen.screenshot_custom"
    bl_label = "Save Screenshot Custom"
    bl_options = {'REGISTER'}

    _items = [('SCREEN', 'Current Screen', 'Capture the current screen'),
              ('SCREEN_ACTIVE_AREA', 'Active Screen Area', 'Capture the active screen area'),
              ('SCREEN_ALL_AREAS', 'All Screen Areas', 'Capture all the areas of the current screen'),
              ('SCREEN_AND_ALL_AREAS', 'Current Screen and all Areas', 'Capture screen and also all its areas'),
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

        screenshot = Screenshot()
        
        if self.capture_mode == 'SCREEN':
            _screen(context, screenshot)
        elif self.capture_mode == 'SCREEN_ACTIVE_AREA':
            _screen_area(context, screenshot)
        elif self.capture_mode == 'SCREEN_ALL_AREAS':
            _screen_all_areas(context, screenshot)
        elif self.capture_mode == 'SCREEN_AND_ALL_AREAS':
            _screen(context, screenshot)
            _screen_all_areas(context, screenshot)
        else:
            self.report({'ERROR'}, "Save Screenshot Custom: No other capture modes supported")
            return {'CANCELLED'}

        self.report({'INFO'}, "Screenshot saved in {0}".format(context.window_manager.clipboard))
        
        return {'FINISHED'}
    
    def __del__(self):
        print("Destructing " + self.bl_idname)


def register():
    bpy.utils.register_class(ScreenshotsCustom)
    
    addonKeyConfig = bpy.context.window_manager.keyconfigs.addon

    if 'Screen' not in addonKeyConfig.keymaps:
        addonKeyConfig.keymaps.new('Screen')

    keymap_items = addonKeyConfig.keymaps['Screen'].keymap_items
    
    capture_mode_mapping = (('SCREEN', {}),
                            ('SCREEN_ACTIVE_AREA', {'alt': True}),
                            ('SCREEN_ALL_AREAS', {'shift': True}),
                            ('SCREEN_AND_ALL_AREAS', {'ctrl': True}),
                            )

    for capture_mode, kwargs in capture_mode_mapping:
        kmi = keymap_items.new(ScreenshotsCustom.bl_idname, 'C', 'PRESS', oskey=True, **kwargs)
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
