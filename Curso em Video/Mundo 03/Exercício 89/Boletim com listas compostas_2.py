ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S / N]')).lower().strip()
    if resp in 'Nn':
        break
print('-=' * 15)
print(f'{"Nº":<4}{"Nome":<10}{"MÉDIA":>8}')


