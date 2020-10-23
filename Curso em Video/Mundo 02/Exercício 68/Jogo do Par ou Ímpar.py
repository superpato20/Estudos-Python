import random
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
count = 0
while True:
    n = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P / Í] ')).lower().strip()
    computador = random.randint(0, 10)
    total = computador + n
    resto = total % 2
    if escolha == 'p':
        print('-' * 30)
        print(f'Você jogou {n} e o computador {computador}.', end='')
        if resto == 0:
            print(f'Total de {total} DEU PAR.')
            print('-' * 30)
            print('Você VENCEU!')
            print('Vamos jogar novamente ...')
            print('=-' * 20)
            count += 1
        else:
            print(f'Total de {total} DEU ÍMPAR.')
            print('-' * 30)
            print('Você PERDEU!')
            break
    elif escolha == 'i':
        print('-' * 30)
        print(f'Você jogou {n} e o computador {computador}.', end='')
        if resto == 0:
            print(f'Total de {total} DEU PAR.')
            print('-' * 30)
            print('Você PERDEU!')
            break
        else:
            print(f'Total de {total} DEU ÍMPAR.')
            print('-' * 30)
            print('Você VENCEU!')
            print('Vamos jogar novamente ...')
            print('=-' * 20)
            count += 1
print('=-' * 20)
print(f'GAME OVER! Você venceu {count} vez(es).')
