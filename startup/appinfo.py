# -*- coding: utf-8 -*-

import bpy
import inspect


mros = inspect.getmro(type(bpy.app))


attrs = tuple(set(dir(mros[0])) - set(dir(mros[1])))


for attr in sorted(attrs):
    print()
    value = getattr(bpy.app, attr)
    
    if type(value) in (int, float, str, bool, tuple, bytes):
        print("{0} - {1}".format(attr, value))
    elif type(value) in (dict,):
        print(attr)
        for key, value in value.items():
            print("\t{0} - {1}".format(key, type(value)))
    elif isinstance(value, tuple):
        print("{0} - ".format(attr))
        mros = inspect.getmro(type(value))
        tattrs = tuple(set(dir(mros[0])) - set(dir(mros[1])))
        for tattr in tattrs:
            print("\t{0} - {1}".format(tattr, getattr(value, tattr))) 
    else:
        print("{0} - {1}".format(attr, 'WOT EEZ DIS'))
