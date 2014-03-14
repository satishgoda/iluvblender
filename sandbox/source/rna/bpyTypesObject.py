import bpy

from rna_info import get_direct_properties

from itertools import groupby
from pprint import pprint


property_type = lambda prop: prop.type

theType = bpy.types.Object

iterable = sorted(get_direct_properties(theType.bl_rna), key=property_type)

propmap = { key: tuple(group) for key, group in groupby(iterable, property_type) }

pprint(propmap)
