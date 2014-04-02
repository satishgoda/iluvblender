import bpy

from inspect import getfile


class Class:
    class Info:
        def __init__(self, name, module, file):
            self.name = name
            self.module = module
            self.file = file
        
        def __repr__(self):
            kwargs = {key: getattr(self, key) for key in self.__dict__}
            return "{name}\n\t{module}\n\t{file}\n".format(**kwargs)
    
    @staticmethod
    def info(cls):
        try:
            file = getfile(cls)
        except TypeError as e:
            file = e
        else:
            pass
        finally:
            name, module = cls.__qualname__, cls.__module__
            return Class.Info(name, module, file)


def info(cls='type'):
    try:
        for subclass in type.__subclasses__(eval(cls)):
            print(Class.info(subclass))
    except NameError as ne:
        header = "Invalid Input:"
        help = 'Try entering a valid class like "type" or "object"'
        print('{} {}\n\t{}'.format(header, ne, help))


if __name__ == '__main__':
    info('object')
