import bpy

from rna_info import get_direct_properties

from itertools import groupby
from pprint import pprint


property_type = lambda prop: prop.type

theTypeRna = bpy.types.Object.bl_rna


properties = sorted(theTypeRna.properties, key=property_type)

properties_direct = sorted(get_direct_properties(theTypeRna), key=property_type)


pprint(set.difference(*(map(set, (properties, properties_direct)))))


propmap = { key: tuple(group) for key, group in groupby(properties_direct, property_type) }


pprint(propmap)
