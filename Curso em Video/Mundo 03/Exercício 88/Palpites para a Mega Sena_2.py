from random import sample
from time import sleep
jogo = list()
n = int(input('Quantos Jogos? '))
for c in range(n):
    a = sorted(sample(range(1, 61), 6))
    jogo.append(a[:])
    print(f'Jogo {c + 1}: {a}')
    sleep(0.8)


