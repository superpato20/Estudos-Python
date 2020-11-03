num = ' '
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'teze', 'catorze', 'quinze',
        'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while num not in range(0, 21):
    num = int(input('Digite um numero entre 0 e 20: '))
    if num not in range(0, 21):
        print('Tente Novamente. ', end='')
    elif num in range(0, 21):
        print(f'Você digitou o numero {cont[num]}.')
        conti = ' '
        while conti not in 'n':
            conti = str(input('Quer continuar: [S / N] ')).lower().strip()
            if conti == 'n':
                break
            num = int(input('Digite um numero entre 0 e 20: '))
            if num not in range(0, 21):
                print('Tente Novamente. ', end='')
                break
            if num in range(0, 21):
                print(f'Você digitou o numero {cont[num]}.')
print('Programa encerrado!')
