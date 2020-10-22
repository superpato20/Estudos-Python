from time import sleep
cores = {'limpa': '\033[m', 'red': '\033[31m', 'blue': '\033[34m', 'green': '\033[32m'}
print('\033[44m                                        \033[m')
print('\033[31m()\033[m\033[34m()\033[m' * 10)
n1 = float(input('{}Digite a primeira nota do aluno: '.format(cores['blue'], cores['limpa'])))
n2 = float(input('{}Digite a segunda nota do aluno: '.format(cores['blue'], cores['limpa'])))
print('{}CALCULANDO...'.format(cores['green'], cores['limpa']))
sleep(2)
print('{}A media entre as notas {:.1f} e {:.1f} será {:.1f}.'.format(cores['red'], n1, n2, (n1 + n2) / 2))
sleep(1)
print('{}FIM!!'.format(cores['green']))
print('\033[31m()\033[m\033[34m()\033[m' * 10)
print('\033[44m                                        \033[m')

