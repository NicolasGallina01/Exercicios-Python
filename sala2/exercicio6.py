import math
a = int(input('Informe um valor:'))
b = int(input('Informe um segundo valor:'))
c = int(input('Informe um terceiro valor'))
d = (b**2 - 4 * a * c)
if d<0:
    print('Não tem raizes reais')
else:
    d = d ** (1/2)
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    print('As razei são', x1, x2)