listanum = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in listanum:
        print('Valor adicionado com sucesso...')
        listanum.append(n)
    else:
        print('Valor duplicado!Não vou adicionar...')
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar: [S / N] ')).lower().strip()
    if continuar == 'n':
        break
print(listanum)
