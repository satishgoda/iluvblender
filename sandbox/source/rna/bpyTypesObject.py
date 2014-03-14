import bpy

from itertools import groupby
from pprint import pprint


order = lambda prop: prop.type

iterable = sorted(bpy.types.Object.bl_rna.properties, key=order)

propmap = { key: tuple(group) for key, group in groupby(iterable, order) }


pprint(propmap)

