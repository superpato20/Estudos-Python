n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o ultimo numero: '))
numeros = (n1, n2, n3, n4)
contador = 0
if n1 % 2 == 0:
    contador += 1
if n2 % 2 == 0:
    contador += 1
elif n3 % 2 == 0:
    contador += 1
elif n4 % 2 == 0:
    contador += 1
print(f'Você digitou os valores: {numeros}.'.replace(',', '').replace('(', '').replace(')', ''))
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição.')
print(f'Os valores pares digitados foram {contador}')
