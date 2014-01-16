import os
import subprocess

filepath = bpy.data.filepath

args = [bpy.app.binary_path, '-b', filepath, '-P', os.path.join(os.path.split(filepath)[0], 'wedges.py')]

subprocess.call(args)


