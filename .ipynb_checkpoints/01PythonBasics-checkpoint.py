
### Hola Mundo ###

"""
Este es un
comentario
en varias líneas
"""

'''
Este también es un
comentario
en varias líneas
'''

# Cómo consultar el tipo de dato
print(type("Soy un dato str"))  # Tipo 'str'
print(type(5))  # Tipo 'int'
print(type(1.5))  # Tipo 'float'
print(type(3 + 1j))  # Tipo 'complex'
print(type(True))  # Tipo 'bool'
print(type(print("Mi cadena de texto")))  # Tipo 'NoneType'

print('Hello, World!')
''' print() functions as newline character by default and you can override this default behavior as follows:
    any string passed as the value of the end parameter will be used as the terminating character of the printed line'''
print('Hello, World!', end=' | ')
print(100, end=' | ')
print(5 + 5)
# VARIABLES
name = 'Farhan'
age = 27
print('My name is ' + name)
# print('I am ' + age + 'years old') -->  this code produces an ERROR
# strings can be concatenated with strings only
# age is an integer, so a better way is embedding variables within string statements.
print(f'My name is {name}')
print(f'I am {age} years old')
# f turns the strings into f-strings. These strings are evaluated at runtime
# In a string, each character will have an index. And like arrays, string indexes are zero-based
name = 'Farhan'
print(name[0])
print(name[1])
# the output is F and a, in two lines
print(name[0:3])
# the output is Far, because is not included the character at the ending index
print(len(name)) # output: 6
# STRING METHODS
print('python is awesome'.capitalize()) # Python is awesome
print('python is awesome'.upper()) # PYTHON IS AWESOME
print('PYTHON IS AWESOME'.lower()) # python is awesome
print('PYTHON IS AWESOME'.islower()) # false
print('PYTHON IS AWESOME'.isupper()) # true
print('python is awesome'.replace('python', 'freeCodeCamp')) # freeCodeCamp is awesome
print('python is awesome'.split(' '))
'''The method takes a delimiter to split the string on. Here, I've used space as the delimiter. 
Output of this code will be ['python', 'is', 'awesome']. This is a list. '''
print(' '.join(['python', 'is', 'awesome'])) # python is awesome

# NUMBERS
a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
'''even if you perform a division operation between two integers, the result will always be a floating point. 
If you want the result to be an integer, you can do so as follows:'''
print(a//b)

# Converting strings into float
num1 = "10.1"
num2 = "5.3"
result = float(num1) + float(num2)
print(result)
print("{:.1f}".format(result)) # rounding the number specifying the decimal places


# USER INPUT
name = input('What is your name? ')
print(f'Your name is {name}')

# CONDITIONALS
a = float(input('First: '))
b = float(input('Second: '))
op = input('Operation (sum/sub/mul/div): ')

if op == 'sum':
    print(f'a + b = {a+b}')
elif op == 'sub':
    print(f'a - b = {a-b}')
elif op == 'mul':
    print(f'a * b = {a*b}')
elif op == 'div':
    print(f'a / b = {a/b}')
else:
    print('Invalid Operation!')

# a match-case is equivalent to a switch-case statement in other programming languages
a = float(input('First: '))
b = float(input('Second: '))
op = input('Operation (sum/sub/mul/div): ')

if op == 'sum':
    print(f'a + b = {a+b}')
elif op == 'sub':
    print(f'a - b = {a-b}')
elif op == 'mul':
    print(f'a * b = {a*b}')
elif op == 'div':
    print(f'a / b = {a/b}')
else:
    print('Invalid Operation!')

# Lists and Tuples
# Like strings, each element in a Python list has an index and these indexes start from zero
vowels = ['a', 'e', 'i', 'o', 'u']
print(vowels[0])
print(vowels[1])
# append() method appends a new item to the list and the extend() method adds multiple items
vowels = ['a', 'e']
vowels.append('i')
vowels.extend(['o', 'u'])
# insert() method inserts an item at a given index in the list:
vowels = ['a', 'i', 'o', 'u']
vowels.insert(1, 'e')
# pop() method pops the last element off the list:
vowels = ['a', 'e', 'i', 'o', 'u']
popped_item = vowels.pop()
print(popped_item) # u
print(vowels) # ['a', 'e', 'i', 'o']
# remove() method can remove a given element from the list
vowels.remove('e')
# clear() method removes all the elements from the list.
vowels = ['u', 'e', 'a', 'o', 'i']
vowels.sort()
print(vowels)
# If you want to reverse the list instead, there is the reverse() method:
vowels.reverse()

# Tuples are pretty similar to lists but you can not modify a tuple
vowels = ('a', 'e', 'i', 'o', 'u')
print(vowels)

# LOOPS
vowels = ['a', 'e', 'i', 'o', 'u']
for letter in vowels:
    print(letter.upper())

# DICTIONARIES
'''A hashmap is a collection of key-value pairs
{
    key_1: value_1,
    key_2: value_2,
    key_3: value_3,
    key_4: value_4,
    key_5: value_5,
}'''

sentence = 'the quick brown fox jumped over the lazy dog'
record = {}
for letter in sentence:
    if letter in record:
        record[letter] += 1
    else:
        record[letter] = 1
print(record)
''' Output for this code will be as follows:
{'t': 2, 'h': 2, 'e': 4, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r'}
This is a dictionary. Each letter is a key and their occurrence number is the value. 
On the code snippet, you declare a dictionary in the second line.'''

# FUNCTIONS
def sum(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

a = float(input('First: '))
b = float(input('Second: '))
op = input('Operation (sum/sub/mul/div): ')

if op == 'sum':
    print(f'a + b = {sum(a, b)}')
elif op == 'sub':
    print(f'a - b = {sub(a, b)}')
elif op == 'mul':
    print(f'a * b = {mul(a, b)}')
elif op == 'div':
    print(f'a / b = {div(a, b)}')
else:
    print('Invalid Operation!')


