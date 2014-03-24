>>> bpy.types.Header.__subclasses__
<built-in method __subclasses__ of RNAMeta object at 0x2aaab10fa920>

>>> bpy.types.Header.__subclasses__()
[<class 'bl_ui.space_clip.CLIP_HT_header'>, <class 'bl_ui.space_console.CONSOLE_HT_header'>, <class 'bl_ui.space_dopesheet.DOPESHEET_HT_header'>, <class 'bl_ui.space_filebrowser.FILEBROWSER_HT_header'>, <class 'bl_ui.space_graph.GRAPH_HT_header'>, <class 'bl_ui.space_image.IMAGE_HT_header'>, <class 'bl_ui.space_info.INFO_HT_header'>, <class 'bl_ui.space_logic.LOGIC_HT_header'>, <class 'bl_ui.space_nla.NLA_HT_header'>, <class 'bl_ui.space_node.NODE_HT_header'>, <class 'bl_ui.space_outliner.OUTLINER_HT_header'>, <class 'bl_ui.space_properties.PROPERTIES_HT_header'>, <class 'bl_ui.space_sequencer.SEQUENCER_HT_header'>, <class 'bl_ui.space_text.TEXT_HT_header'>, <class 'bl_ui.space_time.TIME_HT_header'>, <class 'bl_ui.space_userpref.USERPREF_HT_header'>, <class 'bl_ui.space_view3d.VIEW3D_HT_header'>, <class 'development_icon_get.CONSOLE_HT_icons'>]

>>> for header in bpy.types.Header.__subclasses__():
...     print(header)
...     
<class 'bl_ui.space_clip.CLIP_HT_header'>
<class 'bl_ui.space_console.CONSOLE_HT_header'>
<class 'bl_ui.space_dopesheet.DOPESHEET_HT_header'>
<class 'bl_ui.space_filebrowser.FILEBROWSER_HT_header'>
<class 'bl_ui.space_graph.GRAPH_HT_header'>
<class 'bl_ui.space_image.IMAGE_HT_header'>
<class 'bl_ui.space_info.INFO_HT_header'>
<class 'bl_ui.space_logic.LOGIC_HT_header'>
<class 'bl_ui.space_nla.NLA_HT_header'>
<class 'bl_ui.space_node.NODE_HT_header'>
<class 'bl_ui.space_outliner.OUTLINER_HT_header'>
<class 'bl_ui.space_properties.PROPERTIES_HT_header'>
<class 'bl_ui.space_sequencer.SEQUENCER_HT_header'>
<class 'bl_ui.space_text.TEXT_HT_header'>
<class 'bl_ui.space_time.TIME_HT_header'>
<class 'bl_ui.space_userpref.USERPREF_HT_header'>
<class 'bl_ui.space_view3d.VIEW3D_HT_header'>
<class 'development_icon_get.CONSOLE_HT_icons'>

>>> header
<class 'development_icon_get.CONSOLE_HT_icons'>

>>> header.__module__
'development_icon_get'

>>> for header in filter(lambda header: header.__module__ == 'bl_ui', bpy.types.Header.__subclasses__()):
...     print(header)
...     
>>> 

>>> bpy.types.VIEW3D_HT_header
<class 'bl_ui.space_view3d.VIEW3D_HT_header'>

>>> bpy.types.VIEW3D_HT_header.__module__
'bl_ui.space_view3d'

>>> for header in filter(lambda header: header.__module__.startswith('bl_ui'), bpy.types.Header.__subclasses__()):
...     print(header)
...     
<class 'bl_ui.space_clip.CLIP_HT_header'>
<class 'bl_ui.space_console.CONSOLE_HT_header'>
<class 'bl_ui.space_dopesheet.DOPESHEET_HT_header'>
<class 'bl_ui.space_filebrowser.FILEBROWSER_HT_header'>
<class 'bl_ui.space_graph.GRAPH_HT_header'>
<class 'bl_ui.space_image.IMAGE_HT_header'>
<class 'bl_ui.space_info.INFO_HT_header'>
<class 'bl_ui.space_logic.LOGIC_HT_header'>
<class 'bl_ui.space_nla.NLA_HT_header'>
<class 'bl_ui.space_node.NODE_HT_header'>
<class 'bl_ui.space_outliner.OUTLINER_HT_header'>
<class 'bl_ui.space_properties.PROPERTIES_HT_header'>
<class 'bl_ui.space_sequencer.SEQUENCER_HT_header'>
<class 'bl_ui.space_text.TEXT_HT_header'>
<class 'bl_ui.space_time.TIME_HT_header'>
<class 'bl_ui.space_userpref.USERPREF_HT_header'>
<class 'bl_ui.space_view3d.VIEW3D_HT_header'>

>>> header.__name__
'VIEW3D_HT_header'

>>> header.bl_space_type
'VIEW_3D'
