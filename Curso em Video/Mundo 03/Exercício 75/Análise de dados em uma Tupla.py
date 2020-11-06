num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o ultimo numero: ')))
contador = 0
print(f'Você digitou os valores: {num}.'.replace(',', '').replace('(', '').replace(')', ''))
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição.')
for c in num:
    if c % 2 == 0:
        contador += 1
print(f'Os valor pares digitados foram {contador}.')
