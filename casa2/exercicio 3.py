a = float(input('Qual foi a sua nota'))
b = a % 1
if b<=0.5:
    c = a - b
    print('Sua nota foi arredondada para', c)
else:
    c = (a - b) + 1.0
    print('Sua nota foi arredondada para', c)