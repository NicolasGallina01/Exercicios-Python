a = int('Fale um número correspondente ao seu curso')
match a:
    case 1:
        print('Engenharia')
    case 2:
        print('Edificações')
    case 3:
        print('Sistemas elétricos')
    case 4:
        print('Turismo')
    case 5:
        print('Análise de desenvolvimento de sistemas')
    case _:
        print('Curso inválido')