n = int(input('Digite um numero: '))
m = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        m += 1
    else:
        print('\033[31m', end='')

    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(n, m))
if m <= 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
