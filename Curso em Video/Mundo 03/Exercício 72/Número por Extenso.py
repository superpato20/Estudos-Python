num = ' '
num1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while num not in range(0, 21):
    num = int(input('Digite um numero entre 0 e 20: '))
    if num not in range(0, 21):
        print('Tente Novamente.', end='')
    elif num in range(0, 21):
        print(f'Você digitou o numero {num1[num]}')
        conti = ' '
        while conti not in 'n':
            conti = str(input('Quer continuar: [S / N] ')).lower().strip()
            if conti == 'n':
                break
            num = int(input('Digite um numero entre 0 e 20: '))
            if num not in range(0, 21):
                print('Tente Novamente.', end='')
                break
            elif num in range(0, 21):
                print(f'Você digitou o numero {num1[num]}')
print('Programa encerrado!')
