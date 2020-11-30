'''pessoas = maiorpeso = menorpeso = 0
listamaior = list()
listamenor = list()
while True:
    nome = str(input('Nome: '))
    pessoas += 1
    peso = float(input('Peso: '))

    if peso >= maiorpeso:
        listamaior.append(nome)
        listamaior.append(peso)
        maiorpeso = peso
        menorpeso = peso
    else:

        listamenor.append(nome)
        listamenor.append(peso)
        menorpeso = peso
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S / N] '))
    if continuar == 'n':
        break
print(f'Ao todo, você cadastrou {pessoas} pessoas.')
print(listamaior)
print(listamenor)'''


dados = []
povo = []
peso = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    povo.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? [S / N] ')).lower().strip()
    if continuar in 'n':
        break
print(f'Ao todo, você cadastrou {len(povo)} pessoas.')
print(f'O maior peso foi de {max(peso):.2f}2Kg.Peso de ',end=' ')
for p in povo:
    if p[1] == max(peso):
        print(f'{p[0]}', end=' ')
print(f'O menor peso foi de {min(peso):.2f}', end=' ')
for p in povo:
    if p[1] == min(peso):
        print(f'{p[0]}', end=' ')

