homem = 0
acima18 = 0
mulherabai18 = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M / F] ')).lower().strip()[0]
    print('-' * 30)
    if idade > 18:
        acima18 += 1
        if sexo == 'm':
            homem += 1
    elif sexo == 'm':
        homem += 1
    elif sexo == 'f' and idade < 20:
        mulherabai18 += 1
    es = ' '
    while es not in 'sn':
        es = str(input('Quer continuar? [S/ N] '))
    if es == 'n':
        break
print(f'Total de pessoas com mais de 18 anos: {acima18}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulherabai18} mulheres com menos de 20 anos.')
