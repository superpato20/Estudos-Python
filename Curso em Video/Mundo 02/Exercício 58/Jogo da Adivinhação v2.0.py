import random
pc = random.randint(1, 10)
tentativas = 1
print('''Sou seu computador ...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
jogador = int(input('Qual é o seu palpite? '))
while pc != jogador:
    if pc > jogador:
        jogador = int(input('Mais ...Tente mais uma vez. '))
        tentativas += 1
    elif pc < jogador:
        jogador = int(input('Menos ...Tente mais uma vez. '))
        tentativas += 1
print('Acertou com {} tentativas. Parabens!'.format(tentativas))

