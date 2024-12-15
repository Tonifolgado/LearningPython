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

from math import sin,cos
print('The sinus of 30º is',round(math.sin(0),0))

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

from calculator import functions
functions.calculate_square_root()
# functions is a subdirectory of calculator

# use importlib for dynamic module imports at runtime
import importlib
module_name = 'numpy'
np_module = importlib.import_module(module_name)
arr = np_module.arange(0,10,2)
print(arr)
# [0 2 4 6 8]

# import a module conditionaly
if input(balance:= 'Input your bank balance') >= 0:
    import math
    print('Interest rate:',math.sqrt(balance)*0.01)
else:
    import cmath
    print('Interest rate:',abs(cmath.sqrt(balance))*0.01)

# dir() function
import math
print(dir(math)) # list all the functions and variables in the math module
'''
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
'''


