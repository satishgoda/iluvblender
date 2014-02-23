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


pair = lambda attr: (attr, getattr(bpy.app, attr))
_attr_repr = lambda attr, indent='': '{0}{1}\n      {2}'.format(indent, *pair(attr))
attr_repr_normal = lambda attr: _attr_repr(attr)
attr_repr_indent = lambda attr: _attr_repr(attr, indent='   ')

for key in keys_sorted:
    items = attr_map[key]
    if len(items) > 1:
        print(key.upper()+'\n')
        print('\n'.join(map(attr_repr_indent, items)))
    else:
        attr = items[0] if items else key
        print(attr_repr_normal(attr))
    print()


print(''.join(('\n', 'E'*79, '\n')))
