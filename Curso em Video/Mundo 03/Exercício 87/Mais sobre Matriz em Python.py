matriz = [[], [], []]
pares = 0
for c in range(0, 3):
    for d in range(0, 3):
        n = (int(input(f'Digite um valor para [{c},{d}]: ')))
        matriz[c].append(n)
        if n % 2 == 0:
            pares += n
print('-=' * 25)
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matriz[c][d]:^5}]', end='')
    print()
terceiracoluna = 0
for coluna in range(len(matriz[0])):
    soma = 0
    for linha in range(len(matriz)):
        if matriz[linha][coluna] >= 0:
            soma += matriz[linha][coluna]
    terceiracoluna = soma
print('-=' * 25)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terceiracoluna}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
