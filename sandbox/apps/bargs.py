class ProgramLauncher(object):
    import os
    cwd = os.getcwd()

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __str__(self):
        l = self._print()
        l += '\n    located at {0}'.format(self.path)
        l += '\n    CWD: {0}'.format(self.cwd)
        l += '\n'
        return l


class ProgramLauncherBinary(ProgramLauncher):
    def _print(self):
        return "Launched as binary {0}".format(self.name)


class ProgramLauncherSymlink(ProgramLauncher):
    def __init__(self, name, path):
        import os
        super(ProgramLauncherSymlink, self).__init__(name, os.readlink(path))

    def _print(self):
        return "Launched via a symlink {0}".format(self.name)


class ProgramDetails:
    def __init__(self):
        import sys
        from os.path import isabs, abspath, exists, islink, basename

        arg0 = sys.argv[0]

        program_path =  arg0 if isabs(arg0) else abspath(arg0)

        if exists(program_path):
            if islink(program_path):
                self.launcher = ProgramLauncherSymlink(arg0, program_path)
            else:
                self.launcher = ProgramLauncherBinary(arg0, program_path)
        else:
            basename = basename(program_path)
            import shutil
            self.launcher = ProgramLauncherSymlink(arg0, shutil.which(basename))
