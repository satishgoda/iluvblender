import bpy


@bpy.app.handlers.persistent
def keymaps(incoming):
    keyconfig = bpy.context.window_manager.keyconfigs.user

    for source, destination in (('Console', 'TEXT_EDITOR'), ('Text', 'CONSOLE')):
        args = ('wm.context_set_enum', 'ESC', 'PRESS')
        kwargs = {'shift':True}

        keymap = keyconfig.keymaps.get(source)

        if not keymap:
            keymap = keyconfig.keymaps.new(source)
            
        properties = keymap.keymap_items.new(*args, **kwargs).properties
        
        properties.data_path = 'area.type'
        properties.value = destination


bpy.app.handlers.load_post.insert(0, keymaps)


bpy.ops.wm.read_homefile()
