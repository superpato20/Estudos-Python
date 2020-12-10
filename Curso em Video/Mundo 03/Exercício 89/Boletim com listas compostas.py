from time import sleep
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
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S / N] ')).lower().strip()
    if continuar == 'n':
        break
print('-=' * 15)

print('{}  {}       {}'.format('Nº', 'NOME', 'MÉDIA'))
print('-' * 30)
for index, item in enumerate(listanome2):
    print(f'{index} {item[0]:>6} {(item[1] + item[2]) / 2:>9}')
print('-' * 30)
while True:
    notas = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if notas == 999:
        break
    listanome3 = list()
    listanome3.append(listanome2[notas])
    for index, item in enumerate(listanome3):
        print(f'Notas de {item[0]} são [{item[1]}, {item[2]}]')
    print('-' * 30)
print('FINALIZANDO ...')
sleep(1.2)
print('VOLTE SEMPRE!!!')
