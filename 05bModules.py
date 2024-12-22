# Modules are files containing Python definitions and statements
# They help organize and reuse code
# They allow to use functions, classes, and variables defined in other files
# Modules can be imported into other modules or directly into the main script

# to import a module, use the import statement
import math
print(math.pi)

# to import the entire module, and access all the functions and variables
import math
print(math.pow(2,3))
# output 8

import random
print('I will', random.choice(['watch a movie','read a book','play tennis','study coding']))
print('The winning lottery number is', random.randint(1,1000))
'''
I will read a book
The winning lottery number is 233
(but every time the output is different)
'''

# to import specific functions or variables
from datetime import datetime
print(datetime.today())

from math import pi, sin, sqrt

print('The sinus of 30º is', round(sin(0), 0))

# import all names from a module
from math import *
print('The value of pi is', pi)
# Using from module import * imports everything 
# but is discouraged due to namespace pollution and readability issues.

'''
# We can shorten module names with as
import pandas as pd
df = pd.DataFrame(.....)
print(df)

Importing modules inside a function limits scope
We can import a submodule from a package (a directory containing multiple modules)
'''
def calculate_square_root(x):
    import math
    return math.sqrt(x)
print(calculate_square_root(100))

# Importing a module from a subpackage
from calculator import functions
functions.calculate_square_root()
# functions is a subdirectory of calculator

# use importlib for dynamic module imports at runtime
import importlib
module_name = 'numpy'
np_module = importlib.import_module(module_name)
arr = np_module.arange(0, 10, 2)
print(arr)
# [0 2 4 6 8]

# import a module conditionally
balance = float(input('Input your bank balance: '))
if balance >= 0:
    import math
    print('Interest rate:', math.sqrt(balance) * 0.01)
else:
    import cmath
    print('Interest rate:', abs(cmath.sqrt(balance)) * 0.01)


