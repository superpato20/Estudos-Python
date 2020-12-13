from random import randint
from time import sleep

jogadores1 = dict()
print('Valores sorteados:')
for c in range(0, 4):
    jogadores1['sorteio'] = randint(1, 10)
    print(f"jogador{c} tirou {jogadores1['sorteio']} no dado.")
    sleep(0.9)

print('-=' * 15)
print(jogadores1)

