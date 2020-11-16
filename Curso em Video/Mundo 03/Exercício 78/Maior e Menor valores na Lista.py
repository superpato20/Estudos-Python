lista = []
lista2 = []
for c in range(0, 5):
    n = int(input(f'Digite um valor para a Posição {c}: '))
    lista.append(n)
print(f'Você digitou os valores {lista}.'.replace(',', '').replace('[', '').replace(']', ''))
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for n in lista:
    print(f'{lista.index(max(lista)) + 1}...')
print(f'O menor valor digitado foi {min(lista)}')

