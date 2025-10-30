a = []
for i in range(5):
    a.append(int(input('escolha os valores da sua lista A:'))) 
b = []
for i in range(5):
    b.append(a[i] * 3)
print('A sua lista B ficou', b)