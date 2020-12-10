listanome = list()
listanome2 = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
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
print('-=' * 15)
print('Nº', 'NOME', 'MÉDIA')
print('-' * 30)
for index, item in enumerate(listanome2):
    print(index, item[0], (item[1] + item[2]) / 2)
print('-' * 30)
