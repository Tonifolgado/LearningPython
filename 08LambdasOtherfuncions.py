### Lambdas ###

def sum_two_values(first_value, second_value): return first_value + second_value
print(sum_two_values(2, 4))

def multiply_values(first_value, second_value): return first_value * second_value - 3
print(multiply_values(2, 4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value
print(sum_three_values(5)(2, 4))

# ------------------
### Higher Order Functions ###

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

### Closures ###
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))

### Built-in Higher Order Functions ###
numbers = [2, 5, 10, 21, 3, 30]

# Map
def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

'''
[4, 10, 20, 42, 6, 60]
[4, 10, 20, 42, 6, 60]
'''

# Filter
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

'''
[21, 30]
[21, 30]
'''

# Reduce
def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers)) # 71

# The self parameter
# The first parameter of any method of a class is always self
# It is a reference to the current instance of the class and is used to access variables and methods
# self keyword to access the data members and call member functions of the object
# ejemplo con self
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
        print(f"Mi nombre es {self.nombre} y mi edad es {self.edad}")


              