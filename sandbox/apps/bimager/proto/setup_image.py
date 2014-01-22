import bpy
import sys

import argparse

args_to_parse = sys.argv[(sys.argv.index('--')+1):] if sys.argv.count('--') else []

kwargs = {
    'prog' : 'bimager',
    'description' : 'b3d Image Viewer'
}

parser = argparse.ArgumentParser(**kwargs)

parser.add_argument('imagefile', nargs='?', default='default.png')

args = parser.parse_args(args_to_parse)

bpy.data.images['Image'].filepath = args.imagefile

bpy.ops.image.reload({'context':bpy.context,'area': bpy.context.screen.areas[1]})
