a = []
for i in range(6):
    a.append(int(input('escolha os valores da sua lista A:')))
b = []
for i in range(6):
    b.append(int(input('escolha os valores da sua lista B:')))
c = []
for i in range(6):
    c.append(a[i]-b[i])
    print(c[i])