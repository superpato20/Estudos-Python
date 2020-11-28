pessoas = maiorpeso = menorpeso = 0
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
print(listamenor)
