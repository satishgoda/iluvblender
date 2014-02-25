import bpy
import os


class Screenshot(object):
    if bpy.data.filepath:
        filename = bpy.path.display_name_from_filepath(bpy.data.filepath)  
        dirname = os.path.dirname(bpy.data.filepath)
    else:
        filename = 'untitled'
        dirname = os.getcwd()
    filename_ext = 'png'
    filename_suffix = None
    filename_suffix_char = '_'
    
    @property
    def filepath(self):
        filename = self.filename
        if self.filename_suffix:
            filename += self.filename_suffix_char 
            filename += self.filename_suffix
        filename += '.' + self.filename_ext
        return os.path.join(self.dirname, filename)
        
if __name__ == '__main__':
    pass
