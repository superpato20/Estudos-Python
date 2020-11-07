listagem = ('APRENDER', 'PROGRAMAR')
for c in listagem:
    for letra in enumerate(c):
        if letra in 'aeiou':
            print(f'Na palavra {c} temos {letra}')

'''nome = input("Digite o nome: ")
for index, letra in enumerate(nome):
    if letra in "aeiou":
        print("Encontrado a letra '%c' na posição %d" % (letra, index))'''

