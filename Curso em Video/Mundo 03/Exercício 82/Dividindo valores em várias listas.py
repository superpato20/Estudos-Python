lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/ N] ')).lower().strip()
    if continuar == 'n':
        break
print('-=' * 25)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de impares é {listaimpar}')
