
import bpy

def explain(self):
    """Explain in detail about this object"""
    print(self.bl_rna.identifier, "belonging to", self.id_data.bl_rna.description)
    print('\t', self.bl_rna.name)
    print('\t', self.bl_rna.description)
    print()
    for prop in self.bl_rna.properties:
        if prop.identifier in ('rna_type',):
            continue
        print("{} ({})\n\t{}\n".format(prop.identifier, prop.name, prop.description))


bpy.types.Area.basic_info = (lambda area, flag=False: "You get nothing" if flag else (area.type, len(area.regions)))
bpy.types.Area.basic_info.__doc__ = "Get the basic information of an area"
bpy.types.Area.basic_info.__annotations__['flag'] = 'Flag to flag an issue'
    
bpy.types.Area.explain = explain

    
