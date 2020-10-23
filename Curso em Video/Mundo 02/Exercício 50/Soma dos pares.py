a = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        a += n
        cont += 1
print('Foram informados {} numeros PARES, e a soma somente dos numeros pares digitado é {}'.format(cont, a))

