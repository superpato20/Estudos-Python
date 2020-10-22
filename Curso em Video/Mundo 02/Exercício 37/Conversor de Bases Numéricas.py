n = int(input('Digite um numero inteiro: '))
es = int(input('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL  
[ 3 ] converter para HEXADECIMAL
Sua opção: '''))
if es == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif es == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif es == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção Invalida!Tente Novamente!')
