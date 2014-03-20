for x, y in inspect.getmembers(bpy.app.__class__, inspect.ismemberdescriptor):
    print(x)

background
binary_path
build_branch
build_cflags
build_commit_date
build_commit_time
build_commit_timestamp
build_cxxflags
build_date
build_hash
build_linkflags
build_options
build_platform
build_system
build_time
build_type
ffmpeg
handlers
ocio
oiio
translations
version
version_char
version_cycle
version_string


for x, y in inspect.getmembers(bpy.app.__class__, inspect.isdatadescriptor):
    print(x)

__class__
autoexec_fail
autoexec_fail_message
autoexec_fail_quiet
background
binary_path
build_branch
build_cflags
build_commit_date
build_commit_time
build_commit_timestamp
build_cxxflags
build_date
build_hash
build_linkflags
build_options
build_platform
build_system
build_time
build_type
debug
debug_events
debug_ffmpeg
debug_freestyle
debug_handlers
debug_python
debug_value
debug_wm
driver_namespace
ffmpeg
handlers
ocio
oiio
tempdir
translations
version
version_char
version_cycle
version_string


setdir = lambda bclass: set(dir(bclass))


sorted(filter(lambda attr: attr.startswith('debug'), set.difference(*map(setdir, type(bpy.app).mro()[:2]))))
['debug', 'debug_events', 'debug_ffmpeg', 'debug_freestyle', 'debug_handlers', 'debug_python', 'debug_value', 'debug_wm']


>>> sorted(filter(lambda attr: attr.startswith('debug'), set.difference(*map(setdir, inspect.getmro(bpy.app.__class__)[:2]))))
['debug', 'debug_events', 'debug_ffmpeg', 'debug_freestyle', 'debug_handlers', 'debug_python', 'debug_value', 'debug_wm']


>>> print(inspect.getdoc(bpy.app.__class__.__dict__['debug']))
Boolean, for debug info (started with --debug / --debug_* matching this attribute name)


>>> print(inspect.getdoc(bpy.app.__class__.__dict__['binary_path']))
The location of blenders executable, useful for utilities that spawn new instances
