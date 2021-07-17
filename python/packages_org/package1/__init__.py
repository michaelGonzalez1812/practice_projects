from pkgutil import iter_modules

# Must import subpkg modules if you want you use as subpkg.module
# If you do not do it you only only have acces to the modules in directory of current file
from .subpackage1 import *

# Let to export all modules in the pkg including subpackages
__all__ = [name for _, name, _ in iter_modules(__path__)]

print('package all: ', __all__)