import bpy

class Debug(object):
    def __call__(self, message):
        if bpy.app.debug:
            print("{0}: {1}".format(__name__, message))


class AppAddonModule(object):
    def __init__(self, data):
        self._data = data

    @property
    def name(self):
        return self._data[0]

    @property
    def path(self):
        return self._data[1]

    def enable(self):
        bpy.ops.wm.addon_enable(module=self.name)

    def disable(self):
        bpy.ops.wm.addon_disable(module=self.name)


class AppAddonModules(object):
    def __init__(self):
        location = bpy.utils.user_resource('SCRIPTS', path='addons')
        self._data = [AppAddonModule(data) for data in bpy.path.module_names(location)]

    def enable(self):
        for module in self._data:
            module.enable()

    def disable(self):
        for module in self._data:
            module.disable()


def ui_settings():
    #bpy.ops.wm.window_fullscreen_toggle()
    bpy.ops.screen.area_headers_consistent()
    bpy.ops.screen.mode_zen()


def createConfig():
    bpy.context.user_preferences.view.show_splash = False
    ui_settings()
    AppAddonModules().disable()
    bpy.ops.wm.save_homefile()


def boot():
    print("Booting app")


@bpy.app.handlers.persistent
def render_settings(incoming):
    bpy.context.scene.render.engine = 'CYCLES'
    #print(bpy.context.screen.name)


@bpy.app.handlers.persistent
def load_modules(incoming):
    AppAddonModules().enable()


def VIEW3D_HT_header_operator(self, context):
    layout = self.layout
    row = layout.row()
    row.alert = True
    row.operator('wm.search_menu')


def register():
    Debug()("Registering application specific types")
    bpy.types.VIEW3D_HT_header.append(VIEW3D_HT_header_operator)
    bpy.app.handlers.load_post.insert(0, load_modules)
    bpy.app.handlers.load_post.append(render_settings)


def unregister():
    Debug()("Unegistering application specific types")
    bpy.types.VIEW3D_HT_header.remove(VIEW3D_HT_header_operator)
    bpy.app.handlers.load_post.remove(load_modules)
    bpy.app.handlers.load_post.remove(render_settings)


if __name__ == '__main__':
    register()
