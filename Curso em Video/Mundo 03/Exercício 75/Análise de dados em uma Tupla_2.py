n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o ultimo numero: '))
numeros = (n1, n2, n3, n4)
contador = 0
for c in numeros:
    if c % 2 == 0:
        contador += 1
print(f'Você digitou os valores: {numeros}.'.replace(',', '').replace('(', '').replace(')', ''))
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição.')
else:
    print('O valor 3 não apareceu em nenhuma posição.')
print(f'Os valores pares digitados foram {contador}')
