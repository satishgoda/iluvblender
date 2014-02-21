# -*- coding: utf-8 -*-

import bpy
import inspect

mros = inspect.getmro(type(bpy.app))

app_attrs = sorted(set(dir(mros[0])) - set(dir(mros[1])))

for attr in app_attrs:
    print(attr, getattr(bpy.app, attr))
