a = float(input('Informe o primeiro lado do triangulo'))
b = float(input('Informe o segundo lado do triangulo'))
c = float(input('Informe o terceiro lado do triangulo'))
if a<b+c or b<a+c or c<a+b:
    if a==b==c:
        print('triangulo equilatero')
    elif a!=b and b!=c and a!=c:
        print('triangulo escaleno')
    else:
        print('triangulo isoceles')
else:
    print('Não é um triangulo')