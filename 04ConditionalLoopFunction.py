
### Conditionals ###
''' Index:
- IF
- IF, ELIF, ELSE
- LOOPS: While, For
- FUNCTIONS
'''


# if
my_condition = False
if my_condition:  # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")

my_condition = 5 * 5
if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

# if, elif, else
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")
print("La ejecución continúa")


age = 20
isEligible = age > 18
if isEligible:
    print('You can vote!')


# Condicional con ispección de valor
my_string = ""
if not my_string:
    print("Mi cadena de texto es vacía")
if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")

# ------------------
### Loops ###

# While
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")
print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)
print("La ejecución continúa")

# For
my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
for element in my_tuple:
    print(element)

my_set = {"Brais", "Moure", 35}
for element in my_set:
    print(element)

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bluce for para diccionario ha finalizado")
print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")

# Iterators
'''
An iterator is an object that allows to iterate through
all the elements of a collection, such as a list or tuple.
Iterators implement 2 methods:
1. __iter__(): returns the iterator object itself.
2. __next__(): returns the next value and raises a
To create an iterator you need to implement the two methods
StopIteration exception: when no more values are available
'''
working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
iterator = iter(working_days)
print(next(iterator)) # Monday
print(next(iterator)) # Tuesday

class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

#using the iterator
itearator = MyIterator(1,4)
for num in iterator:
    print(num)
# output: 1 2 3 4 (one line for each)



# -------------------
### Functions ###

# Definición
def my_function():
    print("Esto es una función")

my_function()
my_function()

# Función con parámetros de entrada/argumentos

def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

def country_to_capital():
    country = input('Please enter a country name: ')
    capital = ''
    if country == 'France':
        capital = 'Paris'
    elif country == 'Germany':
        capital = 'Berlin'
    elif country == 'Italy':
        capital = 'Rome'
    print('The capital of {} is {}'.format(country,capital))

# we can split the function into two
def get_country():
    country = input('Please enter a country name: ')
    return country

def country_to_capital():
    country = get_country()
    capital = ''
    if country == 'France':
        capital = 'Paris'
    elif country == 'Germany':
        capital = 'Berlin'
    elif country == 'Italy':
        capital = 'Rome'
    print('The capital of {} is {}'.format(country,capital))

country_to_capital()

# we can add a function to print
def print_in_console(country,capital):
    print('The capital of {} is {}'.format(country,capital))

def country_to_capital():
    country = get_country()
    capital = ''
    if country == 'France':
        capital = 'Paris'
    elif country == 'Germany':
        capital = 'Berlin'
    elif country == 'Italy':
        capital = 'Rome'
    print_in_console(country,capital)

country_to_capital()

# Función con parámetros de entrada/argumentos y retorno
def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Función con parámetros de entrada/argumentos por clave
def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Moure", name="Brais")

# Función con parámetros de entrada/argumentos por defecto
def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "MoureDev")

# Función con parámetros de entrada/argumentos arbitrarios
def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")

'''
'''