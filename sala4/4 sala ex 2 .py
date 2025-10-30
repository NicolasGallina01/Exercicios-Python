import math
a = []
for i in range(6):
    a.append(int(input('escolha os valores da sua lista A:')))
b = []
for i in range(6):
    b.append(math.factorial(a[i]))
    print(b[i])