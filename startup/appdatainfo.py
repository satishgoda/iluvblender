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

attrs = set.difference(*map(setdir, mros[:2]))

attr_map = {}
attrs_grouped = set()
attrs_plain = set()

for key, group in itertools.groupby(sorted(attrs), prefix):
    grouped = list(group)
    k, v = None, None
    if len(grouped) > 1:
        k, v = (key, grouped)
        attrs_grouped.add(key)     
    else: 
        k, v = (grouped[0], None)
        attrs_plain.add(k)
    
    attr_map[k] = v


# Print

buffer = []

for prefix in sorted(attrs_grouped):
    items = attr_map[prefix]
    buffer.append(prefix.upper()+'\n')
    buffer.extend(list(map(attr_repr_indent, items)))

for attr in sorted(attrs_plain):
   buffer.append(attr_repr_normal(attr))


print(''.join(('\n', 'S'*79, '\n')))

print('\n\n'.join(buffer))

print(''.join(('\n', 'E'*79, '\n')))
