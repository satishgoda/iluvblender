import bpy

class Debug(object):
    def __call__(self, message):
        if bpy.app.debug:
            print("{0}: {1}".format(__name__, message))


def boot():
    bpy.context.user_preferences.view.show_splash = False
    bpy.ops.wm.window_fullscreen_toggle()


def render_settings(incoming):
    bpy.context.scene.render.engine = 'CYCLES'


@bpy.app.handlers.persistent
def load_modules(incoming):
    addons_module_location = bpy.utils.user_resource('SCRIPTS', path='addons')

    app_addon_modules = bpy.path.module_names(addons_module_location)

    for addon_module in app_addon_modules:
        Debug()("Enabling {0} located @ {1}".format(*addon_module))
        bpy.ops.wm.addon_enable(module=addon_module[0])


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
