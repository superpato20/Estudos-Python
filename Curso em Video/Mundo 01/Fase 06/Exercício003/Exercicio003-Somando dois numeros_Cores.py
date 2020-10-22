import time
print('\033[44m                                       \033[m')
print('\033[36m%\033[m\033[32m%\033[m\033[35m%\033[m' * 13)
num1 = int(input('\033[34mDigite um valor: \033[m'))
num2 = int(input('\033[34mDigite outro valor: \033[m'))
print('\033[31mC\033[m\033[32mA\033[m\033[33mL\033[m\033[34mC\033[m\033[35mU\033[m\033[36mL\033[m\033[92mANDO...\033[m')
time.sleep(2)
print('\033[35mA soma entre {} e {} é igual a {}.\033[m'.format(num1, num2, num1 + num2))
print('\033[44m                                       \033[m')
print('\033[36m%\033[m\033[32m%\033[m\033[35m%\033[m' * 13)

