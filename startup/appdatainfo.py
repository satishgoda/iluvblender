import bpy

import inspect
import itertools
import pprint


mros = inspect.getmro(type(bpy.app))


attrs = sorted(set(dir(mros[0])) - set(dir(mros[1])))


prefix = lambda attr: attr.partition('_')[0]


attr_map = {}
for key, group in itertools.groupby(attrs, prefix):
    attr_map[key] = list(group)


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
        pair = lambda item: (item, getattr(bpy.app, item))
        item_string_repr = lambda item: '   {0}\n      {1}'.format(*pair(item))
        item_strings = map(item_string_repr, items)
        print('\n'.join(item_strings))
    else:
        if len(items) == 1:
            attr = items[0]
        else:
            attr = key
        print('{0}\n   {1}'.format(attr, getattr(bpy.app, attr)))
    print()


print(''.join(('\n', 'E'*79, '\n')))
