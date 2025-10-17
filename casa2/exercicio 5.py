func = 0
sal_t = 0
fds = 1
while fds:
    sb = float(input('Qual o seu salário mensal?'))
    if sb <= 0:
        break
    h = int(input('Quantas horas você trabalhou neste mês?'))
    desc_t = 0
    match sb:
        case _ if sb > 1600:
            desc_t = 0.22
        case _ if 1000 <= sb <= 1600:
            desc_t = 0.13
        case _:
            desc_t = 0
            sl = sb - (sb * desc_t)
    adic = 0
    if h > 160:
        horaex = h - 160
        adic = horaex * (sb / 160)
    sl = sb - desc_t + adic
    sal_t += sl
    func += 1
print('Número de funcionários:', func)
print('Salário liquido total:', sal_t)