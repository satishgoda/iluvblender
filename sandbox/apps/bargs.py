
class ProgramDetails:
    def __init__(self):
        import sys
        from os import readlink, getcwd
        from os.path import isabs, abspath, exists, islink, basename
        import shutil

        self.launcher = arg0 = sys.argv[0]

        program_path =  arg0 if isabs(arg0) else abspath(arg0)

        self.cwd = getcwd()

        if exists(program_path):
            if islink(program_path):
                self.path = readlink(shutil.which(program_path))
            else:
                self.path = program_path
        else:
            basename = basename(program_path)
            self.path = readlink(shutil.which(basename))
