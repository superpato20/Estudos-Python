import emoji
from time import sleep
print('\033[41m                                          \033[m')
print(emoji.emojize('\033[31m:helicopter: \033[m' * 15))
n = int(input('\033[34mDigite um numero: \033[m'))
print('\033[31:102mPROCESSANDO...\033[m')
sleep(1)
print('\033[34mAnalisando o valor {}, o seu antecessor é {}, e o seu sucessor é {}.\033[m'.format(n, n - 1, n + 1))
print(emoji.emojize('\033[31m:helicopter: \033[m' * 15))
print('\033[41m                                          \033[m')
