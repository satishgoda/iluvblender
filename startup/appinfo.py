# -*- coding: utf-8 -*-

import bpy

names_in_scope = dir(bpy.app)

non_specials = list(filter(lambda s: not s.startswith('__'), names_in_scope))

attr_value_pairs = dict(map(lambda attr: (attr, getattr(bpy.app, attr)), non_specials))

for key, value in sorted(attr_value_pairs.items()):
    print("{0}\n\t{1}".format(key, value))
