# -*- coding: utf-8 -*-

import bpy
import inspect

mros = inspect.getmro(type(bpy.app))

attrs = tuple(set(dir(mros[0])) - set(dir(mros[1])))

attrs_no_underscore = tuple(filter(lambda attr: attr.find('_') == -1, attrs))

attrs_underscore = tuple(set(attrs) - set(attrs_no_underscore))

base_prefix_attrs = tuple(filter(lambda base: set(filter(lambda pattr: pattr.startswith(base), attrs_underscore)), attrs_no_underscore))

print(sorted(attrs_no_underscore))
print()

print(sorted(attrs_underscore))
print()

print(sorted(base_prefix_attrs))
print()
