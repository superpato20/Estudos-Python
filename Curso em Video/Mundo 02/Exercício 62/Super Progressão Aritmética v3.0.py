print('Gerador de PA')
print('-=' * 10)
pt = int(input('Primeiro Termo: '))
rp = int(input('Razão da PA: '))
cont = 1
termo = pt
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(' {} '.format(termo), end='')
        termo += rp
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

