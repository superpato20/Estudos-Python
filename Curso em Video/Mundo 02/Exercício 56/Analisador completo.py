listaida = []
mulher = 0
homem = 0
idadhomem = 0
for c in range(1, 5):
    print('---- {}ª Pessoa ----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M / F]: ')).upper().strip()
    listaida.append(idade)
    if sexo == 'F':
        if idade < 20:
            mulher += 1
    elif sexo == 'M':
        homem = nome
        idadhomem = idade
    else:
        if idade > idadhomem:
            homem = nome
            idadhomem = idade
print('A média de idade do grupo é de {} anos.'.format(sum(listaida) / len(listaida)))
print('O homem mais velho tem {} anos e se chama {}.'.format(idadhomem, homem))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulher))
