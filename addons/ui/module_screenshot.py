import bpy
import os


class Screenshot(object):
    filename_ext = 'png'
    filename_suffix = None
    filename_suffix_char = '_'
    filename = 'untitled'
    dirname = os.getcwd()
    
    def __init__(self):
        _filepath = bpy.data.filepath
        if _filepath:
            self.filename = bpy.path.display_name_from_filepath(_filepath)  
            self.dirname = os.path.dirname(_filepath)
    
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
