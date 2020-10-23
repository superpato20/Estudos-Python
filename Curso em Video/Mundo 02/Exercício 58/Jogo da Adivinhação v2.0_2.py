import random
pc = random.randint(1, 10)
palpites = 0
acertou = False
print('''Sou seu computador ...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi? ''')
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais ...Tente mais uma vez.')
        elif jogador > pc:
            print('Menos ...Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))

