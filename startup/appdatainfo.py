import bpy

import inspect
import itertools
import pprint


# Callbacks

setdir = lambda iclass: set(dir(iclass))

prefix = lambda attr: attr.partition('_')[0]

pair = lambda attr: (attr, getattr(bpy.app, attr))

_attr_repr = lambda attr, indent='': '{0}{1}\n      {2}'.format(indent, *pair(attr))
attr_repr_normal = lambda attr: _attr_repr(attr)
attr_repr_indent = lambda attr: _attr_repr(attr, indent='   ')


# Process

mros = inspect.getmro(type(bpy.app))

attrs = sorted(set.difference(*map(setdir, mros[:2])))

attr_map = {}

for key, group in itertools.groupby(attrs, prefix):
    attr_map[key] = list(group)


# Organize

kwargs = {
    'key': lambda key: len(attr_map[key]), 
    'reverse': True
}

keys_sorted = sorted(attr_map.keys(), **kwargs)

buffer = []

for key in keys_sorted:
    items = attr_map[key]
    if len(items) > 1:
        buffer.append(key.upper()+'\n')
        buffer.extend(list(map(attr_repr_indent, items)))
    else:
        attr = items[0] if items else key
        buffer.append(attr_repr_normal(attr))


# Print

print(''.join(('\n', 'S'*79, '\n')))

print('\n\n'.join(buffer))

print(''.join(('\n', 'E'*79, '\n')))
