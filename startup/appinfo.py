# -*- coding: utf-8 -*-

import bpy
import inspect

def factory(value):
    if value:
        if isinstance(value, dict):
            return value.keys()
        elif isinstance(value, tuple):
            fields = set(dir(value)) - set(dir(tuple))
            return tuple(fields)
        else:
            return value
    elif isinstance(value, bool):
        return False
    elif isinstance(value, str):
        return '""'
    else:
        return value

mros = inspect.getmro(bpy.app.__class__)

app_attrs = set(dir(mros[0])) - set(dir(mros[1]))

app_attr_value_pairs = map(lambda attr: (attr, getattr(bpy.app, attr)), app_attrs)

app_attr_value_pairs = sorted(app_attr_value_pairs, key=lambda t: t[0])

for key, value in app_attr_value_pairs:
    print("{0}\n\t{1}".format(key, factory(value)))
