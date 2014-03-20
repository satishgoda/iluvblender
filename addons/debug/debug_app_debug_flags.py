bl_info = {
    'name': 'Application Debugging Flags',
    'description': 'User interface to the application debug flags (bpy.app.debug[_*])',
    'category': 'Debugging',
}


import bpy


class BAppRuntime(object):
    __slots__ = ()
    bclass = bpy.app
    _filter = lambda attr: attr
        
    @classmethod
    def getattrs(cls):
        setdir = lambda bclass: set(dir(bclass))
        attrs = set.difference(*map(setdir, type(cls.bclass).mro()[:2]))
        return sorted(filter(cls._filter, attrs))

    @classmethod
    def getattrdoc(cls, attr):
        import inspect
        return inspect.getdoc(vars(cls.bclass.__class__)[attr]) 


class BAppRuntimeDebug(BAppRuntime):
    _filter = lambda attr: attr.startswith('debug')

    @classmethod
    def getflag(cls, flag_enum):
        return cls.flag_map[flag_enum]

    @classmethod
    def getenumeration(cls, self, context):
        enum_items = []
        index = 10000
        for attr in cls.getattrs():
            attr_value = getattr(cls.bclass, attr)
            if isinstance(attr_value, bool):
                enum = attr.split('_')[1] if attr.count('_') else attr
                enum = enum.upper()
                name = enum.capitalize()
                description = cls.getattrdoc(attr)
                icon = 'CHECKBOX_HLT' if attr_value else 'CHECKBOX_DEHLT'
                index += 1
                enum_items.append((enum, name, description, icon, index))
                if not hasattr(cls, 'flag_map'):
                    cls.flag_map = {}
                cls.flag_map[enum] = attr
        return enum_items


def getAppDebugEnumeration(self, context):
    return BAppRuntimeDebug.getenumeration(self, context)


class BAppRuntimeDebugOperator(bpy.types.Operator):
    bl_idname = 'debug.app_debug'
    bl_label = 'bpy.app.debug[_*]'
    bl_description = bpy.app.__doc__
    bl_options = {'REGISTER'}
    
    flag = bpy.props.EnumProperty(items=getAppDebugEnumeration, 
                                    name='App Debug Toggles')

    def draw(self, context):
        layout = self.layout
        layout.operator_enum(self, 'flag')

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)

    def execute(self, context):
        flag = BAppRuntimeDebug.getflag(self.flag)
        value = getattr(bpy.app, flag)
        setattr(bpy.app, flag, not value)
        self.report({'INFO'}, "{} bpy.app.{}".format("Disabled" if value else "Enabled", flag))
        return {'FINISHED'}


def bpy_app_debug_items_draw(self, context):
    layout = self.layout
    layout.operator_enum('debug.app_debug', 'flag')


def register():
    bpy.utils.register_class(BAppRuntimeDebugOperator)


def unregister():
    bpy.utils.unregister_class(BAppRuntimeDebugOperator)


if __name__ == '__main__':
    register()
    bpy.context.window_manager.popup_menu(bpy_app_debug_items_draw, 
                                          title=BAppRuntimeDebugOperator.bl_label,
                                          icon='BLENDER')

