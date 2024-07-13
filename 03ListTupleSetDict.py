
### Lists ###

# Definición
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Brais"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación
print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación
my_other_list.append("MoureDev")
print(my_other_list)
my_other_list.insert(1, "Rojo")
print(my_other_list)
my_other_list[1] = "Azul"
print(my_other_list)
my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

# Operaciones con listas
my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas
print(my_new_list[1:3])

items = [31,32,30,29,28,30,31]
sliced = items[4:]
print(sliced) # 28,30,31

# Cambio de tipo
my_list = "Hola Python"
print(my_list)
print(type(my_list))

### List Comprehension ###
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))
my_list = [i + 1 for i in range(8)]
print(my_list)

my_list = [i * 2 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)

usdPrices = [120,100,30,55]
euroPrices = []
for price in usdPrices:
    exchanged = price * 0.98
    euroPrices.append(exchanged)
print(euroPrices)
# 117.6,98.0,29.4,53.9
# Lo mismo de otra forma:
usdPrices = [120,100,30,55]
euroPrices = [price * 0.98 for price in usdPrices]
print(euroPrices)
# aun de otra forma
def exchange(price):
    return price * 0.98
euroPrices = [exchange(price) for price in usdPrices]
print(euroPrices)

ages = [22,35,17,16,49]
eligible = [age for age in ages if age > 18]
print(eligible)

# ----------------------------
### Tuples ###

# Definición
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

# Acceso a elementos y búsqueda
print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Brais"))
print(my_tuple.index("Moure"))
print(my_tuple.index("Brais"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# Concatenación
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas
print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación
# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined

# ---------------------
### Sets ###

# Definición
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))
print(len(my_other_set))

# Inserción
my_other_set.add("MoureDev")
print(my_other_set)  # Un set no es una estructura ordenada
my_other_set.add("MoureDev")  # Un set no admite repetidos
print(my_other_set)

# Búsqueda
print("Moure" in my_other_set)
print("Mouri" in my_other_set)

# Eliminación
my_other_set.remove("Moure")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación
my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))

# ----------------------
### Dictionaries ###

# Definición
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Brais",
                 "Apellido": "Moure", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda
print(my_dict[1])
print(my_dict["Nombre"])

print("Moure" in my_dict)
print("Apellido" in my_dict)

# Inserción
my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

# Actualización
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminación
del my_dict["Calle"]
print(my_dict)

# Otras operaciones
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))

# -------------------------
