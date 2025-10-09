a = int(input('Informe um valor:'))
b = int(input('Informe um segundo valor:'))
c = int(input('Informe um terceiro valor'))
if a%6==0 and b%6==0 and c%6==0:
    print('Os valores multiplos de 6 são', a, b, c)
elif a%6==0 and b%6==0:
    print('Os valores multiplos de 6 são', a, b)
elif b%6==0 and c%6==0:
    print('Os valores multiplos de 6 são', b, c)
elif a%6==0 and c%6==0:
    print('Os valores multiplos de 6 são', a, c)
elif a%6==0:
    print('Os valores multiplos de 6 são', a)
elif b%6==0:
    print('Os valores multiplos de 6 são', b)
elif c%6==0:
    print('Os valores multiplos de 6 são', c)
else:
    print('Nenhum dos valores são divisiveis por 6')