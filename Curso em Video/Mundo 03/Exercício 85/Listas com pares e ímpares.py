imp = []
par = []
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)
print('-=' * 30), par.sort(), imp.sort()
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores impares digitados foram: {imp}')
