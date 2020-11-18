lista = list()
for c in range(5):
    n = int(input('Dgite um valor: '))
    if c == 0 or c == 3:
        lista.append(n)
        print('Adicionado ao final da lista...')
    elif c == 1 or c == 4:
        lista.insert(0, n)
        print('Adicionado na posição 0 da lista...')
    else:
        lista.insert(1, n)
        print('Adicionado na posição 1 da lista...')
print('-=' * 25)
print(f'Os valores digitados em ordem foram {lista}')
