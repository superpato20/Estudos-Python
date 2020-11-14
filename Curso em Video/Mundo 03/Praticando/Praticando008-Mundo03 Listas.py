a = [2, 3, 4, 7]
#b = a                # faz as duas variaves ficarem ligadas
b = a[:]              # faz uma copia da variavel
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
