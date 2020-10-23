import time
a = False
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
while not a:
    op = int(input('[ 1 ] Somar \n'
                   '[ 2 ] Multiplicação\n'
                   '[ 3 ] Maior valor\n'
                   '[ 4 ] Novos números\n'
                   '[ 5 ] Sair do Programa\n'
                   '>>>>> Qual é a sua opção? '))
    if op == 1:
        print('A soma entre {} e {} é {}.'.format(v1, v2, v1 + v2))
        print('=-=' * 10)
    elif op == 2:
        print('A multiplicação entre {} e {} é {}.'.format(v1, v2, v1 * v2))
        print('=-=' * 10)
    elif op == 3:
        if v1 > v2:
            print('Entre {}  e {} o maior valor é {}.'.format(v1, v2, v1))
        else:
            print('Entre {} e {} o maior valor é {}.'.format(v1, v2, v2))
        print('=-=' * 10)
    elif op == 4:
        print('Informe novos números novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
        print('=-=' * 10)
    elif op == 5:
        a = True
    else:
        print('Opção invalida!')
        print('=-=' * 10)
print('Finalizando ...')
time.sleep(2)
print('=-=' * 10)
print('Fim do Programa! Volte Sempre!')

