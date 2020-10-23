tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M / F] ')).lower().strip()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'm':
        totH += 1
    if sexo == 'f' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [S / N] ')).lower().strip()[0]
    if resp == 'n':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')
