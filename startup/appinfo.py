# -*- coding: utf-8 -*-

import bpy

for attr in filter(lambda s: s != 'driver_namespace', filter(lambda s: not s.startswith('__'),  dir(bpy.app))):
    print("{0}\n\t{1}\n".format(attr, getattr(bpy.app, attr)))

