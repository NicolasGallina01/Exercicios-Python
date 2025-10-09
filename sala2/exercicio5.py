a = int(input('Informe um valor:'))
b = int(input('Informe um segundo valor:'))
c = int(input('Informe um terceiro valor'))
if a>b and a>c:
    if b>c:
        print('os valores são', a, b, c)
    else:
        print('os valores são', a, c, b)
elif b>a and b>c:
    if a>c:
        print('os valores são', b, a, c)
    else:
        print('os valores são', b, c, a)
else:
    if a>b:
        print('os valores são', c, a ,b)
    else:
        print('os valores são', c, b, a)