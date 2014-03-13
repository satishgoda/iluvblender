class ProgramLauncher(object):

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

    @staticmethod
    def create(arg0):
        launcher = None

        program_path =  arg0 if isabs(arg0) else abspath(arg0)

        if exists(program_path):
            if islink(program_path):
                launcher = ProgramLauncherSymlink(arg0, program_path)
            else:
                launcher = ProgramLauncherBinary(arg0, program_path)
        else:
            prog_name = basename(program_path)
            launcher = ProgramLauncherSymlink(arg0, shutil.which(prog_name))

        return launcher


class ProgramLauncherBinary(ProgramLauncher):
    def _print(self):
        return "Launched as binary {0}".format(self.name)


class ProgramLauncherSymlink(ProgramLauncher):
    def __init__(self, name, path):
        super(ProgramLauncherSymlink, self).__init__(name, os.readlink(path))

    def _print(self):
        return "Launched via a symlink {0}".format(self.name)


class ProgramDetails:
    def __init__(self):
        self.launcher = ProgramLauncher.create(sys.argv[0])
