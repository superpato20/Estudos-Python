print('=' * 30)
print('BANCO CEV'.center(25))
print('=' * 30)
cedulas50 = cedulas20 = cedulas10 = cedulas01 = 0
valor = int(input('Que valor você quer sacar? R$ '))
while valor != 0:
    while valor >= 50:
        valor -= 50
        cedulas50 += 1
    while valor >= 20:
        valor -= 20
        cedulas20 += 1
    while valor >= 10:
        valor -= 10
        cedulas10 += 1
    while valor >= 1:
        valor -= 1
        cedulas01 += 1
while cedulas50 >= 1:
    print(f'Total de {cedulas50} cédulas de R$50')
    break
while cedulas20 >= 1:
    print(f'Total de {cedulas20} cédulas de R$20')
    break
while cedulas10 >= 1:
    print(f'Total de {cedulas10} cédulas de R$10')
    break
while cedulas01 >= 1:
    print(f'Total de {cedulas01} céduças de R$1')
    break
print('=' * 30)
print('Volte Sempre ao BANCO PATO! Tenha um Bom Dia!')
