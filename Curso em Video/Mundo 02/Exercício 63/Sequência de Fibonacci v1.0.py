print('-' * 25)
print('Sequencia de Fibonacci')
print('-' * 25)
n = int(input('Quantos termos você quer mostrar? '))
numeroanterior = 1
sequencia = 0
while n > 0:
    print('{}'.format(sequencia), end=' → ')
    sequencia = sequencia + numeroanterior
    numeroanterior = sequencia - numeroanterior
    n -= 1
print('FIM')
