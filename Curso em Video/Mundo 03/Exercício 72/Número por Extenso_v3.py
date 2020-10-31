cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'teze', 'catorze', 'quinze',
        'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente Novamente. ', end='')
print(f'Você digitou o numero {cont[num]}.')
conti = ' '
while conti not in 'n':
    conti = str(input('Quer continuar: [S / N] ')).lower()
    if conti in 'n':
        break
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente Novamente. ', end='')
print(f'Você digitou o numero {cont[num]}.')
