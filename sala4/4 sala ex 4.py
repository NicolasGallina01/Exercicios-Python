a = []
for i in range(5):
    a.append(int(input('escolha os valores da sua lista A:')))
b = []
for i in range(5):
    b.append(int(input('escolha os valores da sua lista B:')))
c = []
for i in range(5):
    c.append(a[i])
for i in range(5):
    c.append(b[i])
for i in range(10):
    print(c[i])