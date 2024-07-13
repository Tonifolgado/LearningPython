

from functools import reduce

numbers = [2, 5, 10, 21, 3, 30]

# Map
def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce
def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))