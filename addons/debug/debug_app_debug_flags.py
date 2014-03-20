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
    def getenumeration(cls):
        enum_items = []
        for attr in cls.getattrs():
            enum = attr.split('_')[1] if attr.count('_') else attr
            enum = enum.upper()
            name = enum.capitalize()
            description = cls.getattrdoc(attr)
            attr_value = getattr(bpy.app, attr)
            icon = 'CHECKBOX_HLT' if attr_value else 'CHECKBOX_DEHLT'
            enum_items.append((enum, name, description, icon))
        return enum_items


def register():
    import pprint
    pprint.pprint(BAppRuntimeDebug.getenumeration())


def unregister():
    pass


if __name__ == '__main__':
    register()
