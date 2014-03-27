bpy.types.Area.basic_info = (lambda area, flag=False: "You get nothing" if flag else (area.type, len(area.regions)))
bpy.types.Area.basic_info.__doc__ = "Get the basic information of an area"
bpy.types.Area.basic_info.__annotations__['flag'] = 'Flag to flag an issue'
    
