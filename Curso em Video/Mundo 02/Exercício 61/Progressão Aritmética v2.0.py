print('Gerador de PA')
print('-=' * 10)
pt = int(input('Primeiro Termo: '))
rp = int(input('Razão da PA: '))
cont = 0
termo = pt
while cont < 10:
    print(' {} >'.format(termo), end='')
    termo += rp
    cont += 1
print(' FIM')
