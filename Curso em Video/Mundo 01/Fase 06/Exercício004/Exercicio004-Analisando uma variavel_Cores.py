from time import sleep
print('\033[103m                \033[m\033[104m                \033[m\033[105m                \033[m')
cores = {'limpa': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}
print('\033[31m#\033[m\033[32m@\033[m\033[33m#\033[m\033[34m@\033[m' * 12)
print('\033[35mPESQUISANDO\033[m\033[36m...\033[m')
sleep(2)
n = input('\033[31mDigite algo: \033[m')
print('\033[31mO tipo primitivo desse valor é \033[m{}{}{}.'.format(cores['yellow'], type(n), cores['limpa']))
print('\033[31mSó tem espaços? \033[m{}{}{}'.format(cores['blue'], n.isspace(), cores['limpa']))
print('\033[31mÉ um numero? \033[m{}{}{}'.format(cores['green'], n.isnumeric(), cores['limpa']))
print('\033[31mÉ alfabético? \033[m{}{}{}'.format(cores['yellow'], n.isalpha(), cores['limpa']))
print('\033[31mÉ alfanumérico? \033[m{}{}{}'.format(cores['blue'], n.isalnum(), cores['limpa']))
print('\033[31mEsta em maiúscula? \033[m{}{}{}'.format(cores['green'], n.isupper(), cores['limpa']))
print('\033[31mEsta em minúscula? \033[m{}{}{}'.format(cores['yellow'], n.islower(), cores['limpa']))
print('\033[31mEsta capitalizada? \033[m{}{}{}'.format(cores['blue'], n.istitle(), cores['limpa']))
print('\033[31m#\033[m\033[32m@\033[m\033[33m#\033[m\033[34m@\033[m' * 12)
sleep(1)
print('\033[30:96mFIM!!!\033[m')
print('\033[103m                \033[m\033[104m                \033[m\033[105m                \033[m')
