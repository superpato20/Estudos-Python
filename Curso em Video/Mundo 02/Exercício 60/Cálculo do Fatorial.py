cont = 1
num = int(input('Digite um número para\n'
                'calcular o seu factorial: '))
print('Calculando {}! = '.format(num), end='')
while num != 1:
    cont *= num
    num -= 1
    print('{} x '.format(num + 1), end='')
print('1 = {}'.format(cont))
