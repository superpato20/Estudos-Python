p = 0
count = -1
soma = 0
while p != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    p = n
    count += 1
    soma += n
print('Você digitou {} números e a soma entre eles foi de {}.'.format(count, soma - 999))
print('FIM')

