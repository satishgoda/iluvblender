import bpy

import itertools

order = lambda prop: prop.type

iterable = bpy.types.Object.bl_rna.properties

propmap = {}

for key, group in itertools.groupby(sorted(iterable, key=order), order):
    propmap[key] = tuple(group)

import pprint

pprint.pprint(propmap)
