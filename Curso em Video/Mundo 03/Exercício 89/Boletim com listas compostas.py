listanome = list()
listanome2 = list()
while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    listanome.append(nome)
    listanome.append(nota1)
    listanome.append(nota2)
    listanome2.append(listanome[:])
    listanome.clear()
    continuar = ' '
    if continuar not in 'sn':
        continuar = str(input('Quer continuar? [S / N] ')).lower().strip()
    if continuar == 'n':
        break
print(listanome2)
