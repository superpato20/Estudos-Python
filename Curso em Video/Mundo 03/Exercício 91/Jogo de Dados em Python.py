from random import randint
from time import sleep
resultados = dict()
jogadores = list()
print('Valores sorteados:')
for c in range(0, 4):
    n = randint(1, 6)
    resultados['Jogador' + str(c + 1)] = n
    jogadores.append(n)
    sleep(0.5)
    print(f'O {"jogador" + str(c + 1)} tirou {n}')
jogadores.sort(reverse=True)
jogar = 't'
print('Ranking dos Jogadores: ')
for p in range(0, 4):
    print(f'{p + 1}º Lugar: ', end='')
    for k, v in resultados.items():
        if v == jogadores[p] and jogar != k:
            sleep(0.5)
            print(k, 'com', v)
            jogar = k
            break
