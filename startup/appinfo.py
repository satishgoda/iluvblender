# -*- coding: utf-8 -*-

import bpy
import inspect

mros = inspect.getmro(type(bpy.app))

app_attrs = tuple(set(dir(mros[0])) - set(dir(mros[1])))

base_attrs = tuple(filter(lambda attr: attr.find('_') == -1, app_attrs))

prefix_attrs = tuple(set(app_attrs) - set(base_attrs))

base_prefix_attrs = tuple(map(lambda attr: tuple(filter(lambda pattr: pattr.startswith(attr), prefix_attrs)), base_attrs))

print(sorted(base_attrs))
print()
print(sorted(prefix_attrs))
print()
print(base_prefix_attrs)


#for attr in app_attrs:
#    print(attr, getattr(bpy.app, attr))
