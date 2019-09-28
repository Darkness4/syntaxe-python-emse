# -*- coding: utf-8 -*-
"""Language Tour: Basics"""

from functools import reduce

# Variables et Built-in types

entier = 1_000_000  # int()
entier += 1  # etc.
calc = entier**2  # power
calc = entier // 2  # div eucli ou floor division
print(calc)
# Bitwise operators également supportés

float_var = 1.0  # float()
float_var = 5e6

complex_var = complex(1, 2)  # 1 + 2j
complex_var = 1 + 2j

bool_var = True  # and False

string = "hey\nman"  # str()
print("Culcule {} est fait !".format(
    0.1))  # printf, voir doc python pour plus de précision
print("First letter: {first}. Last letter: {last}.".format(
    last='Z', first='A'))
# ... et plein d'autre truc
raw_string = r"hey\nman"  # => hey\nman

# Multi-line code
long_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
Aenean eget aliquam risus. Sed ac quam vitae enim aliquet auctor. Aliquam\
hendrerit dictum eros nec sagittis. Quisque eleifend vitae arcu congue\
commodo. Suspendisse convallis ex non euismod hendrerit. Phasellus sit amet\
nulla sodales, scelerisque dolor eget, scelerisque urna. Class aptent taciti\
sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\
Morbi posuere ac neque a tincidunt. Phasellus maximus quam nec urna sagittis\
lobortis. Nullam non pharetra augue. Donec sagittis orci eu massa finibus\
semper. Donec nisi lorem, laoreet in arcu a, scelerisque euismod dui."

# => print 1 line

multi_line_string = """Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Aenean eget aliquam risus. Sed ac quam vitae enim aliquet auctor.
Aliquam hendrerit dictum eros nec sagittis. Quisque eleifend vitae arcu
congue commodo. Suspendisse convallis ex non euismod hendrerit. Phasellus
sit amet nulla sodales, scelerisque dolor eget, scelerisque urna. Class
aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos
himenaeos. Morbi posuere ac neque a tincidunt. Phasellus maximus quam nec
urna sagittis lobortis. Nullam non pharetra augue. Donec sagittis orci eu
massa finibus semper. Donec nisi lorem, laoreet in arcu a, scelerisque
euismod dui."""
# => print multi-line

# Multi-line code (math)
nombre = (
    1 + 2 + 3 + 4 +  # Espace entre opérateurs PEP8
    5 + 6)

# Espace après la virgule, norme PEP8
list_var = [1, 2, 3, 4, 5]  # list(), mutable (contenu modifiable)
list_dynamic_var = [1, 'two', 3.14, [0, 3, 5]]
last = list_var[-1]  # 5
between = list_var[0:1]  # [1], end excluded
from_start = list_var[:1]  # [1]
from_last = list_var[1:]  # [2, 3, 4, 5]
every_x_step = list_var[::2]  # [1, 3, 5]
reverse_magic = list_var[::-1]  # [5, 4, 3, 2, 1]

tuple_var = (1, 2)  # tuple(), immutable (ex: coordonnées fixe)

dict_var = {
    'foo': 'bar',
    'd3ad': 'c0de',
}  # dict(), mutable
dict_var['new_key'] = 'new_value'

set_var = {1, 2, 3}  # Sans ordre, de toute façon personne l'utilise, mutable

# Loops
# indentation 4 espaces (norme PEP8)
for i in range(10):
    if i < 1:
        "do if"
    if 1 < 2:
        "do if 2"
    else:
        "else"
        break  # Go to else
else:
    "i is not in range ?!"

for value in range(len(list_var)):  # Shitty code
    print(value)

for value in list_var:
    print(value)

for idx, value in enumerate(list_var):
    value == list_var[idx]  # => true

L = [2, 4, 6, 8, 10]
R = [3, 6, 9, 12, 15]
for lval, rval in zip(L, R):  # Parcourir 2 listes en même temps
    print(lval, rval)

for value in tuple_var:
    print(value)

for key in dict_var:
    print(key)

for value in dict_var.values():
    print(value)

for key, value in dict_var.items():
    print(key, value)

# while, break, continue
while True is False:
    if 2 is not 2:
        "get out of this hell"
        break
    if 1 is 1:
        continue
    "i guess i'm skipped if 1 is 1"

# Compare
a = 16
if 15 < a < 30:  # in between
    "true"

# or, and, is
if (a > 15 and a < 30) or (a == "16" and a is not str):
    "do some sh*t"

# in
if (a in [15, 16, 17]):
    "do"

# False condition
# 0 == False
# None == False
# "" == False
# [] == False


# Functions
def function(
        dynamic,
        type_hint_decimal: float,
        *args,  # Surplus d'argument
        optionnel="moi",
        **kwargs) -> int:  # Surplus d'argument key=word
    """
    documentation: description rapide


    Description longue.
    Cette function fait que dalle.
    De toute façon personne l'aime.

    Exemple markdown:
    ```
    print(function('bull', 1, optionnel))  # => None
    ```
    """  # Ceci est stocké dans une variable __doc__ (privé)
    print(dynamic)
    print(type_hint_decimal)
    print(optionnel)
    for value in args:
        print(value)
    for key, value in kwargs.items():
        print(key, value)
    return int(dynamic)  # Parce que dynamic est dynamic, faut parser en int


my_kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
my_args = ('args var 1', 'args var 2')  # ou list()
print(function('1042', 1, "not moi", *my_args, **my_kwargs))

# -- Pause --

# Lambdas
add_lambda = lambda x, y: x + y  # A ne pas faire : var prend lambda
print(add_lambda(1, 2))  # Fonction sans nom (x, y) => x + y


# Deux lignes entre les fonctions (norme PEP8)
def add(x, y):
    """Littéralement, ajouter"""
    return x + y  # Même fonction avec un nom


# Usage
list_seconde = [60, 267, 472859]
# => [1, 4, 7880]
list_minutes = list(map(lambda val: val // 60, list_seconde))

for val in map(lambda val: val**2, list_seconde):  # ❤️
    print(val, end=' ')  # => 3600 71289 223595633881

for val in filter(lambda val: (val % 2) == 0, list_seconde):  # ❤️
    print(val, end=' ')  # => 60

sum_var = reduce(lambda a, b: a + b, [1, 2, 3, 4])

# Unpack
print(32, *list_seconde)
print(32, 60, 267, 472859)  # Même chose

# Error handling
try:
    # Code avec erreurs
    pass
except:  # Super illegal => catch n'importe quoi
    print("any error")

try:
    raise Exception("my error message")
except Exception as error:  # Pas conseillé => trop générique
    print(error)
else:  # S'execute si sans problème
    pass
finally:  # S'execute après le try/catch/else
    pass


class MyException(Exception):
    """This is my exception error."""


try:
    type_of_error = 1
    if type_of_error == 1:
        raise MyException("My Exception")
    else:
        raise Exception("Unknow case")
except MyException as error:  # Pas conseillé => trop générique
    print(error)
else:
    pass
finally:
    pass

# -- Pause --
