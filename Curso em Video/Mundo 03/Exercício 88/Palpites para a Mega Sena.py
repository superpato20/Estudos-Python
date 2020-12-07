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
        jogos.append(randint(0, 60))
    print(jogos)
    sleep(1)
    jogos.clear()

