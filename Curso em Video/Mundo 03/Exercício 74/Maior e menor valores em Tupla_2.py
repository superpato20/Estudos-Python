from random import randint
sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in sorteio:
    print(f'{n}', end=' ')
print(f'.\nO maior valor sorteado foi o de {max(sorteio)}.')
print(f'O menor valor sorteado foi o de {min(sorteio)}.')
