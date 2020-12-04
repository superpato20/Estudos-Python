matriz = [[], [], []]
for c in range(0, 3):
    for d in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c},{d}]: ')))
print('-=' * 30)
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matriz[c][d]:^5}]', end='')
    print()
