# -*- coding: utf-8 -*-

import bpy

def factory(value):
    if value:
        if isinstance(value, dict):
            return value.keys()
        else:
            return value
    elif isinstance(value, bool):
        return False
    elif isinstance(value, str):
        return '""'
    else:
        return value

names_in_scope = dir(bpy.app)

non_specials = list(filter(lambda s: not s.startswith('__'), names_in_scope))

attr_value_pairs = dict(map(lambda attr: (attr, getattr(bpy.app, attr)), non_specials))

for key, value in sorted(attr_value_pairs.items(), key=lambda t: t[0]):
    print("{0}\n\t{1}".format(key, factory(value)))


