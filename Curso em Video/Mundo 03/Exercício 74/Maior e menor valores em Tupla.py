from random import randint
sorteio = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: {sorteio}.'.replace(',', '').replace('(', '').replace(')', ''))
print(f'O maior valor sorteado foi {max(sorteio)}.')
print(f'O menor valor sorteado foi {min(sorteio)}.')
