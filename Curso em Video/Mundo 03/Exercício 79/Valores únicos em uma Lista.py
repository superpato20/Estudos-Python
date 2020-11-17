listanum = []
while True:
    n = (int(input('Digite um valor: ')))
    if n in listanum:
        print('a')
    listanum.append(n)
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar: [S / N] ')).lower().strip()
    if continuar == 'n':
        break
print(listanum)
