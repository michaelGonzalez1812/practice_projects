
if __name__ == '__main__':
    from package1 import *

    # Use a function from module1 in package1
    subpackage1.module1.function1()

    from package1.subpackage1 import *
    # Use a function from module 1 class in package1
    module = module1.Module1()
    module.function()

    module11.function1()