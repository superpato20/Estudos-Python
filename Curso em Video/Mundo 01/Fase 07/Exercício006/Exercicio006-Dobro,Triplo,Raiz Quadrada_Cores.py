from time import sleep
import emoji
print(emoji.emojize('\033[33m:warning: \033[m' * 16))
n = int(input('\033[31mDigite um numero: \033[m'))
print('\033[34mCALCULANDO>>>\033[m')
sleep(1)
print('\033[32mO dobro de {} é igual a {}.\nO triplo de {} é igual a {}\nA raiz quadrada de {} é igual a {:.2f}'
      '.\033[m'.format(n, n * 2, n, n * 3, n, n ** (1/2)))
print(emoji.emojize('\033[33m:warning: \033[m' * 16))
