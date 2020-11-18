elementos = 0
lista = []
while True:
    n = int(input('Digite um valor: '))
    elementos += 1
    lista.append(n)
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S / N] ')).lower().strip()
    if continuar in 'n':
        break
lista.sort(reverse=True)
print('-=' * 25)
print(f'Você digitou {elementos} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
