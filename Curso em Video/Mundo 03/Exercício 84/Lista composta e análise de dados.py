pessoas = maiorpeso = menorpeso = 0
listamaior = list()
listamenor = list()
c = 0
while True:
    nome = str(input('Nome: '))
    pessoas += 1
    peso = float(input('Peso: '))
    listamaior.append(nome)
    listamaior.append(peso)
    listamenor.append(nome)
    listamenor.append(peso)
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S / N] '))
    if continuar == 'n':
        break
print(f'Ao todo, você cadastrou {pessoas} pessoas.')
print()
print(listamenor)
