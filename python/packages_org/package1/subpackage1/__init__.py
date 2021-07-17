from pkgutil import iter_modules

# Let to export all modules in the pkg including subpackages
__all__ = [name for _, name, _ in iter_modules(__path__)]

print('package all: ', __all__)