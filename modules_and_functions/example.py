# prints out all of the built in functions within
# the dir module (?)
for m in dir(__builtins__):
    print(m)

# TRICK: print dir(name_of_module) to see what is included in it

import numpy
print(dir(numpy))
