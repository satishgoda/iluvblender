class ProgramDetails:
    def __init__(self):
        import sys
        import os

        arg0 = sys.argv[0]

        launched_program_name =  arg0 if os.path.isabs(arg0) else os.path.abspath(arg0)

        self.arg0 = arg0

        if os.path.isfile(launched_program_name):
            self.actual_program_name = launched_program_name
        else:
            import subprocess
            basename = os.path.basename(launched_program_name)
            output = subprocess.check_output("where {0}".format(basename).split(), shell=True)
            self.actual_program_name = os.readlink(output.strip())
