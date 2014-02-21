import bpy

import inspect
import pprint


mros = inspect.getmro(type(bpy.app))


attrs = tuple(set(dir(mros[0])) - set(dir(mros[1])))


attrs_partitioned = tuple(map(lambda attr: attr.partition('_'), sorted(attrs)))


attr_map = {}


for attr in attrs_partitioned:
    first, others = attr[0], attr[1:]
    if first not in attr_map:
        attr_map[first] = []
    if all(others):
        attr_map[first].extend(others[1:])


kwargs = {
    'key': lambda key: len(attr_map[key]), 
    'reverse': True
}


keys_sorted = sorted(attr_map.keys(), **kwargs)


print(''.join(('\n', 'S'*79, '\n')))


for key in keys_sorted:
    items = attr_map[key]
    if items:
        if len(items) > 1:
            print(key)
            pair = lambda item: (item, getattr(bpy.app, key+'_'+item))
            item_string_repr = lambda item: '   {0}\n      {1}'.format(*pair(item))
            item_strings = map(item_string_repr, items)
            print('\n'.join(item_strings))
        else:
            attr = key + '_' + items[0]
            print('{0}\n   {1}'.format(attr, getattr(bpy.app, attr)))
    else:
        attr = key
        print('{0}\n   {1}'.format(attr, getattr(bpy.app, attr)))
    
    print()


print(''.join(('\n', 'E'*79, '\n')))
