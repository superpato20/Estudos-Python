continuar = False
cont = 0
soma = 0
lista = []
n = int(input('Digite um número: '))
while not continuar:
    cont += 1
    soma += n
    lista.append(n)
    es = str(input('Quer continuar? [S / N]')).lower().strip()
    if es == 's':
        n = int(input('Digite um número: '))
    elif es != 's' and es != 'n':
        print('Opção Invalida!')
    else:
        continuar = True
print('Você digitou {} números e a média foi {:.2f}.'.format(cont, soma / cont))
print('O maior valor foi {} e o menor valor foi {}.'.format(max(lista), min(lista)))
