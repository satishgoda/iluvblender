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
            name, module = cls.__name__, cls.__module__
            return Class.Info(name, module, file)

def main():
    for subclass in type.__subclasses__(type):
        print(Class.info(subclass))


if __name__ == '__main__':
    main()
