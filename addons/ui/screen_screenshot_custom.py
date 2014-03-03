
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


class OutputFilename(object):
    filename = 'untitled'
    ext = 'blend'
    suffix = None
    suffix_char = '_'
    dirname = os.getcwd()
    
    def __init__(self, filepath, ext=''):
        import bpy
        import os
        
        self.filename = bpy.path.display_name_from_filepath(filepath)
        self.dirname = os.path.dirname(filepath)
        
        if self.ext:
            self.ext = ext

    def getSuffix(self):
        return self.suffix_char + self.suffix
    
    @property
    def filepath(self):
        import os
        filename = self.filename
        if self.suffix:
            filename += self.getSuffix()
        filename += '.' + self.ext
        return os.path.join(self.dirname, filename)


class OutputImageFilename(OutputFilename):
    ext = 'png'
    suffix_index = 0
    
    def __init__(self, filepath, suffix='', suffix_index=0):
        super(OutputImageFilename, self).__init__(filepath)
        if suffix:
            self.suffix=suffix
        if suffix_index:
            self.suffix_index = suffix_index
    
    def getSuffix(self):
        suffix_base = super(OutputImageFilename, self).getSuffix()
        return '.'.join([suffix_base, "{0:02}".format(self.suffix_index)])
        

class Screenshot(object):
    full = False    

    def __init__(self, context, full=False):
        self.context = context

        if full:
            self.full = True

    @property
    def kwargs(self):
        return {'full': self.full, 'filepath': self.output.filepath}


def _observer_file_browser(subject):
    from rna_info import get_direct_properties

    window_manager = subject.context['window_manager']
    screen = subject.context['screen']
    
    FILE_BROWSER = lambda area: area.spaces.active.type == 'FILE_BROWSER'
    SCREENSHOT_DIRECTORY = lambda params: window_manager.clipboard in params.directory
    to_update_filebrowser = lambda area: FILE_BROWSER(area) and SCREENSHOT_DIRECTORY(area.spaces.active.params)
    use_filter_props = lambda prop: prop.identifier.startswith('use_filter')

    overrides = subject.context.copy()
    
    file_browser_areas = filter(to_update_filebrowser, screen.areas)

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


def _observer_clipboard(subject):
    window_manager = subject.context['window_manager']
    window_manager.clipboard = subject.output.dirname


def _capture(screenshot):
    print(screenshot.kwargs)
    bpy.ops.screen.screenshot(screenshot.context, **screenshot.kwargs)
    
    _observer_clipboard(screenshot)
    _observer_file_browser(screenshot)


def _prepare_context(context, area=None):
    overrides = context.copy()

    if area:
        overrides.update((
                            ('area', area),
                            ('region', area.regions[1]),
                            ('space_data', area.spaces.active)
                        ))
    
    return overrides


def _screen(context):
    context = _prepare_context(context)

    screenshot = Screenshot(context, True)
    screenshot.output = OutputFilename(context['blend_data'].filepath, 'png')

    _capture(screenshot)


def _handle_area(context, area, index=0):
    context = _prepare_context(context, area)
    
    screenshot = Screenshot(context, False)
    screenshot.output = OutputImageFilename(context['blend_data'].filepath, area.type, index)
    
    _capture(screenshot)   


def _screen_area(context):
    area = context.area
    _handle_area(context, area)


def _screen_all_areas(context):
    from itertools import groupby

    area_map = {}

    criterion = lambda area: area.type
    
    for key, group in groupby(sorted(context.screen.areas, key=criterion), criterion):
        area_map[key] = tuple(group)
    
    for area_type, areas in area_map.items():
        for index, area in enumerate(areas):
            _handle_area(context, area, index)


def _screen_and_all_areas(context):
    _screen(context)
    _screen_all_areas(context)


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
        
        if self.capture_mode == 'SCREEN':
            _screen(context)
        elif self.capture_mode == 'SCREEN_ACTIVE_AREA':
            _screen_area(context)
        elif self.capture_mode == 'SCREEN_ALL_AREAS':
            _screen_all_areas(context)
        elif self.capture_mode == 'SCREEN_AND_ALL_AREAS':
            _screen_and_all_areas(context)
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
