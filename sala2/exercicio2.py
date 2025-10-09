a = float(input('Qual foi sua primeira nota?'))
b = float(input('Qual foi sua segunda nota?'))
m = (a + b) / 2
if m>= 6:
    print('Arovado com média', m)
else:
    e = float(input('Qual foi a nota do seu exame?'))
    mm = (m + e) / 2
    if mm >=5:
        print('o aluno foi aprovado em exame com a média', mm)
    else:
            print('Rerovado com média', mm)