# -*- coding: utf-8 -*-

import bpy
import inspect

mros = inspect.getmro(bpy.app.__class__)

app_attrs = sorted(tuple(set(dir(mros[0])) - set(dir(mros[1]))))

for attr in app_attrs:
    print(attr, getattr(bpy.app, attr))
