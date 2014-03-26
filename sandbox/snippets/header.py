bpy.types.Header.__subclasses__
#~ <built-in method __subclasses__ of RNAMeta object at 0x2aaab10fa920>
#~ 

bpy.types.Header.__subclasses__()
#~ [<class 'bl_ui.space_clip.CLIP_HT_header'>, <class 'bl_ui.space_console.CONSOLE_HT_header'>, <class 'bl_ui.space_dopesheet.DOPESHEET_HT_header'>, <class 'bl_ui.space_filebrowser.FILEBROWSER_HT_header'>, <class 'bl_ui.space_graph.GRAPH_HT_header'>, <class 'bl_ui.space_image.IMAGE_HT_header'>, <class 'bl_ui.space_info.INFO_HT_header'>, <class 'bl_ui.space_logic.LOGIC_HT_header'>, <class 'bl_ui.space_nla.NLA_HT_header'>, <class 'bl_ui.space_node.NODE_HT_header'>, <class 'bl_ui.space_outliner.OUTLINER_HT_header'>, <class 'bl_ui.space_properties.PROPERTIES_HT_header'>, <class 'bl_ui.space_sequencer.SEQUENCER_HT_header'>, <class 'bl_ui.space_text.TEXT_HT_header'>, <class 'bl_ui.space_time.TIME_HT_header'>, <class 'bl_ui.space_userpref.USERPREF_HT_header'>, <class 'bl_ui.space_view3d.VIEW3D_HT_header'>, <class 'development_icon_get.CONSOLE_HT_icons'>]
#~ 

for header in bpy.types.Header.__subclasses__():
    print(header)
    
#~ <class 'bl_ui.space_clip.CLIP_HT_header'>
#~ <class 'bl_ui.space_console.CONSOLE_HT_header'>
#~ <class 'bl_ui.space_dopesheet.DOPESHEET_HT_header'>
#~ <class 'bl_ui.space_filebrowser.FILEBROWSER_HT_header'>
#~ <class 'bl_ui.space_graph.GRAPH_HT_header'>
#~ <class 'bl_ui.space_image.IMAGE_HT_header'>
#~ <class 'bl_ui.space_info.INFO_HT_header'>
#~ <class 'bl_ui.space_logic.LOGIC_HT_header'>
#~ <class 'bl_ui.space_nla.NLA_HT_header'>
#~ <class 'bl_ui.space_node.NODE_HT_header'>
#~ <class 'bl_ui.space_outliner.OUTLINER_HT_header'>
#~ <class 'bl_ui.space_properties.PROPERTIES_HT_header'>
#~ <class 'bl_ui.space_sequencer.SEQUENCER_HT_header'>
#~ <class 'bl_ui.space_text.TEXT_HT_header'>
#~ <class 'bl_ui.space_time.TIME_HT_header'>
#~ <class 'bl_ui.space_userpref.USERPREF_HT_header'>
#~ <class 'bl_ui.space_view3d.VIEW3D_HT_header'>
#~ <class 'development_icon_get.CONSOLE_HT_icons'>
#~ 

header
#~ <class 'development_icon_get.CONSOLE_HT_icons'>
#~ 

header.__module__
#~ 'development_icon_get'
#~ 

for header in filter(lambda header: header.__module__ == 'bl_ui', bpy.types.Header.__subclasses__()):
    print(header)
    
bpy.types.VIEW3D_HT_header
#~ <class 'bl_ui.space_view3d.VIEW3D_HT_header'>
#~ 

bpy.types.VIEW3D_HT_header.__module__
#~ 'bl_ui.space_view3d'
#~ 

for header in filter(lambda header: header.__module__.startswith('bl_ui'), bpy.types.Header.__subclasses__()):
    print(header)
    
#~ <class 'bl_ui.space_clip.CLIP_HT_header'>
#~ <class 'bl_ui.space_console.CONSOLE_HT_header'>
#~ <class 'bl_ui.space_dopesheet.DOPESHEET_HT_header'>
#~ <class 'bl_ui.space_filebrowser.FILEBROWSER_HT_header'>
#~ <class 'bl_ui.space_graph.GRAPH_HT_header'>
#~ <class 'bl_ui.space_image.IMAGE_HT_header'>
#~ <class 'bl_ui.space_info.INFO_HT_header'>
#~ <class 'bl_ui.space_logic.LOGIC_HT_header'>
#~ <class 'bl_ui.space_nla.NLA_HT_header'>
#~ <class 'bl_ui.space_node.NODE_HT_header'>
#~ <class 'bl_ui.space_outliner.OUTLINER_HT_header'>
#~ <class 'bl_ui.space_properties.PROPERTIES_HT_header'>
#~ <class 'bl_ui.space_sequencer.SEQUENCER_HT_header'>
#~ <class 'bl_ui.space_text.TEXT_HT_header'>
#~ <class 'bl_ui.space_time.TIME_HT_header'>
#~ <class 'bl_ui.space_userpref.USERPREF_HT_header'>
#~ <class 'bl_ui.space_view3d.VIEW3D_HT_header'>
#~ 

header.__name__
#~ 'VIEW3D_HT_header'
#~ 

header.bl_space_type
#~ 'VIEW_3D'
#~ 

>>> header.__name__
'VIEW3D_HT_header'


>>> bpy.types.INFO_HT_header._dyn_ui_initialize()
[<function ALL_HT_header_draw_override at 0x2aaab6e4d5f0

>>> inspect.getfile(bpy.types.INFO_HT_header._dyn_ui_initialize()[0])
'scripts/startup/overrides.py'

>>> bpy.types.INFO_HT_header.draw
<function _GenericUI._dyn_ui_initialize.<locals>.draw_ls at 0x2aaab6ffa170>

>>> inspect.getfile(bpy.types.INFO_HT_header.draw)
'/home/satishg/bin/blenderinstalldir/blender-2.70-linux-glibc211-x86_64/2.70/scripts/modules/bpy_types.py'

>>> bpy.types.INFO_HT_header.draw._draw_funcs
[<function ALL_HT_header_draw_override at 0x2aaab6e4d5f0>]

>>> bpy.types.INFO_HT_header.draw.__dict__
{'_draw_funcs': [<function ALL_HT_header_draw_override at 0x2aaab6e4d5f0>]}

>>> vars(bpy.types.INFO_HT_header.draw)
{'_draw_funcs': [<function ALL_HT_header_draw_override at 0x2aaab6e4d5f0>]}


>>> bpy.types.CONSOLE_HT_header._dyn_ui_initialize()
[<function CONSOLE_HT_header.draw at 0x2aaab1ac1440>, <function CONSOLE_HT_header_debug_paths_menu at 0x2aaab1bdfb00>]


>>> bpy.types.VIEW3D_HT_header._dyn_ui_initialize()
[<function VIEW3D_HT_header.draw at 0x2aaab1b8af80>, <function draw_pause at 0x2aaab1c7e200>]


##############################################################

>>> bpy.types.CONSOLE_HT_header
<class 'bl_ui.space_console.CONSOLE_HT_header'>

>>> bpy.types.CONSOLE_HT_header.draw
<function CONSOLE_HT_header.draw at 0x2aaab1ac1440>

>>> bpy.types.CONSOLE_HT_header._draw_funcs
Traceback (most recent call last):
  File "<blender_console>", line 1, in <module>
AttributeError: type object 'CONSOLE_HT_header' has no attribute '_draw_funcs'

>>> bpy.types.CONSOLE_HT_header._dyn_ui_initialize()
[<function CONSOLE_HT_header.draw at 0x2aaab1ac1440>]

>>> bpy.types.CONSOLE_HT_header.draw
<function _GenericUI._dyn_ui_initialize.<locals>.draw_ls at 0x2aaab1e09e60>

#################################################################

>>> for header in bpy.types.Header.__subclasses__():
...     if header.__module__.startswith('bl_ui') and header.bl_space_type in enum_space_types:
...         print("{}\n   {}\n   {}".format(header, header.__module__, header.draw))
...         
<class 'bl_ui.space_clip.CLIP_HT_header'>
   bl_ui.space_clip
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_console.CONSOLE_HT_header'>
   bl_ui.space_console
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_dopesheet.DOPESHEET_HT_header'>
   bl_ui.space_dopesheet
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_filebrowser.FILEBROWSER_HT_header'>
   bl_ui.space_filebrowser
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_graph.GRAPH_HT_header'>
   bl_ui.space_graph
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_image.IMAGE_HT_header'>
   bl_ui.space_image
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_info.INFO_HT_header'>
   bl_ui.space_info
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_logic.LOGIC_HT_header'>
   bl_ui.space_logic
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_nla.NLA_HT_header'>
   bl_ui.space_nla
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_node.NODE_HT_header'>
   bl_ui.space_node
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_outliner.OUTLINER_HT_header'>
   bl_ui.space_outliner
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_properties.PROPERTIES_HT_header'>
   bl_ui.space_properties
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_sequencer.SEQUENCER_HT_header'>
   bl_ui.space_sequencer
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_text.TEXT_HT_header'>
   bl_ui.space_text
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_time.TIME_HT_header'>
   bl_ui.space_time
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_userpref.USERPREF_HT_header'>
   bl_ui.space_userpref
   <function ALL_HT_header_draw_override at 0x2aaab1c047a0>
<class 'bl_ui.space_view3d.VIEW3D_HT_header'>
   bl_ui.space_view3d
   <function _GenericUI._dyn_ui_initialize.<locals>.draw_ls at 0x2aaab1c67200>


def debug_headers():
    enum_space_types = bpy.types.Space.bl_rna.properties['type'].enum_items
    import inspect
    for header in bpy.types.Header.__subclasses__():
        if header.__module__.startswith('bl_ui') and header.bl_space_type in enum_space_types:
            print("{}\n   {}\n   {}".format(header, header.draw, inspect.getfile(header.draw)))
