class ProgramDetails:
    def __init__(self):
        import sys
        import os
        from os import path

        arg0 = sys.argv[0]

        launched_program_name =  arg0 if path.isabs(arg0) else path.abspath(arg0)

        self.arg0 = arg0

        if path.isfile(launched_program_name) and not path.islink(launched_program_name):
            self.actual_program_name = launched_program_name
        else:
            import shutil
            basename = path.basename(launched_program_name)
            self.actual_program_name = os.readlink(shutil.which(basename))
