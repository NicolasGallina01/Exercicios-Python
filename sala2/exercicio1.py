a = float(input('Qual foi sua primeira nota?'))
b = float(input('Qual foi sua segunda nota?'))
c = float(input('Qual foi sua terceira nota?'))
m = (a + b + c) / 3
if m >= 6:
    print('Aprovado')
else:
    print('Reprovado')