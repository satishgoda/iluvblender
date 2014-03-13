import sys
import os
from os import path
import shutil


class ProgramLauncher(object):

    cwd = os.getcwd()

    def __init__(self, name, path):
        self.name = name
        self.path = path

    @property
    def args(self):
        return (self.name,)

    def __str__(self):
        l = self.format_string.format(*self.args)
        l += '\n    located at {0}'.format(self.path)
        l += '\n    CWD: {0}'.format(self.cwd)
        l += '\n'
        return l

    @staticmethod
    def create(arg0):
        launcher = None

        program_path =  arg0 if path.isabs(arg0) else path.abspath(arg0)

        if path.exists(program_path):
            if path.islink(program_path):
                launcher = _ProgramLauncherSymlink(arg0, program_path)
            else:
                launcher = _ProgramLauncherBinary(arg0, program_path)
        else:
            prog_name = path.basename(program_path)
            launcher = _ProgramLauncherSymlink(arg0, shutil.which(prog_name))

        return launcher


class _ProgramLauncherBinary(ProgramLauncher):
    format_string = "Launched as binary {0}"


class _ProgramLauncherSymlink(ProgramLauncher):
    format_string = "Launched via a symlink {0}"
    def __init__(self, name, path):
        super(_ProgramLauncherSymlink, self).__init__(name, os.readlink(path))


class ProgramDetails:
    def __init__(self):
        self.launcher = ProgramLauncher.create(sys.argv[0])

