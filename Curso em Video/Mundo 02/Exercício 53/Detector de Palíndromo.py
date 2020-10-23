frase = input('Digite uma frase: ').lower().replace(' ', '').strip()
inverso = frase[:: -1]
print('A frase é {}, a frase invertida é {}.'.format(frase, inverso))
if frase == inverso:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')
