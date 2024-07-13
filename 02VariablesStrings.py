### Variables ###

my_string_variable = "My String variable"
my_int_variable = 5
print(my_int_variable)
# conversion
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# ---------------------
### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo
name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")
# f is a shorter form of the format() function
# We can hold the result of the format() function in a variable and use it in the next lines
followers = 47
online_users = 7
all_users = 100
result = f'You have {followers} followers'
print(result)
print(f'{all_users - online_users} users are offline')


# Desempaqueado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a) # p
print(e) # o

# División
language_slice = language[1:3]
print(language_slice) # yt
language_slice = language[1:]
print(language_slice) # ython
language_slice = language[-2]
print(language_slice) # o
language_slice = language[0:6:2]
print(language_slice) # pto

# Reverse
reversed_language = language[::-1]
print(reversed_language) # nohtyp

# Métodos de los strings
print(language.capitalize()) # Python
print(language.upper()) # PYTHON
print(language.count("t")) # 1
print(language.isnumeric()) # False
print("1".isnumeric()) # True
print(language.lower()) # python
print(language.lower().isupper()) # False
print(language.startswith("Py")) # False
print("Py" == "py")  # False

# -------------------
