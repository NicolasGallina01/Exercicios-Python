a = 50
b = int(input('Determine um valor entre 0 e 100'))
if b>0 and b<100:
    if a<b:
        c = b - a
        print('A diferença entre o valor e a chave é de', c)
    else:
        c = a - b
        print('A diferença entre o valor e a chave é de', c)
else:
    print('Seu número está fora dos limites')