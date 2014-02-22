import bpy

import inspect
import pprint


mros = inspect.getmro(type(bpy.app))


attrs = set(dir(mros[0])) - set(dir(mros[1]))


attrs_partitioned = tuple(attr.partition('_') for attr in sorted(attrs))


prefixes_unique = { partition[0] for partition in attrs_partitioned }


attr_map = { prefix: [] for prefix in prefixes_unique }


for attr in attrs_partitioned:
    first, others = attr[0], attr[1:]
    if all(others):
        attr_map[first].append(others[-1])


kwargs = {
    'key': lambda key: len(attr_map[key]), 
    'reverse': True
}


keys_sorted = sorted(attr_map.keys(), **kwargs)


print(''.join(('\n', 'S'*79, '\n')))


for key in keys_sorted:
    items = attr_map[key]
    if len(items) > 1:
        print(key)
        pair = lambda item: (item, getattr(bpy.app, key+'_'+item))
        item_string_repr = lambda item: '   {0}\n      {1}'.format(*pair(item))
        item_strings = map(item_string_repr, items)
        print('\n'.join(item_strings))
    else:
        if len(items) == 1:
            attr = key + '_' + items[0]
        else:
            attr = key
        print('{0}\n   {1}'.format(attr, getattr(bpy.app, attr)))
    print()


print(''.join(('\n', 'E'*79, '\n')))
