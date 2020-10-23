lista = []
for c in range(1, 6):
    peso = float(input('Pesso da {}ª pessoa: '.format(c)))
    lista.append(peso)
print('O maior peso lido foi de {}Kg.\nO menor peso lido foi de {}Kg.'.format(max(lista), min(lista)))
