>>> for x, y in inspect.getmembers(bpy.app.__class__, inspect.ismemberdescriptor):
...     print(x)
...     
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


>>> for x, y in inspect.getmembers(bpy.app.__class__, inspect.isdatadescriptor):
...     print(x)
...     
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

