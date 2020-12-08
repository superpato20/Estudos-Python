print('-' * 30)
print('{:>22}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
njogos = int(input('Quantos jogos você quer que eu sorteie? '))
from random import randint
from time import sleep
jogos = []
a = 0
print('-=' * 2, end=' ')
print(f'Sorteando {njogos} Jogos', end=' ')
print('-=' * 2)
while a != njogos:
    a += 1
    for c in range(0, 6):
        n = (randint(1, 60))
        if n not in jogos:
            jogos.append(n)
            if len(jogos) == 5:
                n = jogos.append(randint(1, 60))
    print(f'Jogo {a}: {sorted(jogos)}')
    jogos.clear()
    sleep(1)
