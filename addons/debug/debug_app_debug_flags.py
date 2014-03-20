bl_info = {
    'name': 'Application Debugging Flags',
    'description': 'User interface to the application debug flags (bpy.app.debug[_*])',
    'category': 'Debugging',
}

import bpy

class BAppRuntime(object):
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
        return enum_items


def getAppDebugEnumeration(self, context):
    return BAppRuntimeDebug.getenumeration(self, context)


class BAppRuntimeDebugOperator(bpy.types.Operator):
    bl_idname = 'debug.app_debug'
    bl_label = 'bpy.app.debug[_*]'
    bl_description = bpy.app.__doc__
    bl_options = {'INTERNAL'}
    
    items = bpy.props.EnumProperty(items=getAppDebugEnumeration, 
                                    name='App Debug Toggles')

    def execute(self, context):
        print(self.items)
        self.report({'WARNING'}, self.items)
        return {'FINISHED'}


def bpy_app_debug_items_draw(self, context):
    layout = self.layout
    layout.operator_enum('debug.app_debug', 'items')


def register():
    bpy.utils.register_class(BAppRuntimeDebugOperator)
    bpy.context.window_manager.popup_menu(bpy_app_debug_items_draw, 
                                            title=BAppRuntimeDebugOperator.bl_label,
                                            icon='BLENDER')


def unregister():
    bpy.utils.unregister_class(BAppRuntimeDebugOperator)


if __name__ == '__main__':
    register()
