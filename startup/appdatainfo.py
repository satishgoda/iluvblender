import bpy
import pprint


mros = bpy.app.__class__.mro()


attrs = tuple(set(dir(mros[0])) - set(dir(mros[1])))


attrs_partiotioned = tuple(map(lambda attr: attr.partition('_'), sorted(attrs)))


attr_map = {}


for attr in attrs_partiotioned:
    first = attr[0]
    others = attr[1:]
    if not all(others) or first not in attr_map:
        attr_map[first] = []
    else:
        attr_map[first].extend(others[1:])


pprint.pprint(attr_map)
