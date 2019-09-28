# Fast swap
x, y = 10, 10
x, y = y, x

liste = ['usefull', 'usefull', 'useless', 'useless', 'useless']

for useless, usefull in enumerate(liste):
    "do"

for _, usefull in enumerate(liste):
    "do"

data = ('usefull', 'usefull', 'useless', 'useless', 'useless')

a, b, *_ = data
