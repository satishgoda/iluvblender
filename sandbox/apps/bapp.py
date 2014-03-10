import bpy

from apps import Debug, AppAddonModules

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
