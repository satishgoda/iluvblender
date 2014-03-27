
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
        ptype = prop.fixed_type.identifier if hasattr(prop, 'fixed_type') else prop.type
        print("{}\n\t{} {}\n\t{}\n".format(prop.name, prop.identifier, ptype, prop.description))

def register():
    bpy.types.Area.basic_info = (lambda area, flag=False: "You get nothing" if flag else (area.type, len(area.regions)))
    bpy.types.Area.basic_info.__doc__ = "Get the basic information of an area"
    bpy.types.Area.basic_info.__annotations__['flag'] = 'Flag to flag an issue'
    
    bpy.types.Area.explain = classmethod(explain)
    
def unregister():
    pass
