from random import randint
from time import sleep
lista = ['pedra', 'papel', 'tesoura']
computador = randint(0, 2)
jogador = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
if jogador >= 3:
    print('Opção Invalida! Tente Novamente!')
    exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=' * 35)
print('O computador escolheu: {}'.format(lista[computador]))
print('O jogador escolheu: {}'.format(lista[jogador]))
print('=' * 35)
if computador == 0:
    if jogador == 0:
        print('Empatou!')
    elif jogador == 1:
        print('Jogador Venceu!')
    elif jogador == 2:
        print('Computador Venceu!')
elif computador == 1:
    if jogador == 0:
        print('Computador Venceu!')
    elif jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('Jogador Venceu!')
elif computador == 2:
    if jogador == 0:
        print('Jogador Venceu!')
    elif jogador == 1:
        print('Computador Venceu!')
    elif jogador == 2:
        print('Empatou!')
