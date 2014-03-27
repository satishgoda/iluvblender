
import bpy

def explain(cls):
    """Explain in detail about this object"""
    print(cls.bl_rna.identifier)
    print('\t', cls.bl_rna.name)
    print('\t', cls.bl_rna.description)
    print()
    for prop in cls.bl_rna.properties:
        if prop.identifier in ('rna_type',):
            continue
        print("{} ({})\n\t{}\n".format(prop.identifier, prop.name, prop.description))

def register():
    # http://blender.stackexchange.com/questions/1153/is-it-possible-to-add-a-custom-property-on-bpy-types-sequence
    bpy.types.Area.basic_info = (lambda area, flag=False: "You get nothing" if flag else (area.type, len(area.regions)))
    bpy.types.Area.basic_info.__doc__ = "Get the basic information of an area"
    bpy.types.Area.basic_info.__annotations__['flag'] = 'Flag to flag an issue'
    
    bpy.types.Area.explain = classmethod(explain)
    
def unregister():
    pass
