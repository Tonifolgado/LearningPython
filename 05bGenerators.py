'''
Generators are a simpler way to create iterators.
They use the YIELD keyword to return values one at
a time, making them more memory-efficiency
'''

def my_generator(start,end):
    current = start
    while current <= end:
        yield current
        current += 1

# Calling the generator
for num in my_generator(1,4):
    print(num)
#output: 1 2 3 4 (in one line for each)

'''
Generator expressions provide a concise way to
create generators. They are similar to list
comprehensions but use () instead of [].
'''
gen_expr = (x**3 for x in range(4))
# Using the generator expression
for num in gen_expr:
    print(num)
# output: 0 1 8 27

'''
Generators are useful for reading large files line
by line without loading the entire file into memory
'''
def read_file(file_path):
    with open(file_path) as file:
        for line in file:
            yield line

for line in read_file('temperature.txt'):
    print(line.strip())

