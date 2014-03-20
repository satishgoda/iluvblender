import sys
import os


for path in sys.path:
    print(path)


sys.stdout.flush()


os._exit(0)

