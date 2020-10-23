totpreco = 0
precomais1000 = 0
produtomaisbarato = 0
precomaisbarato = ' '
print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)
while True:
    produto = str(input('Nome do Produto: ')).lower().strip()
    preco = float(input('Preço: R$ '))
    if preco >= 1000:
        precomais1000 += 1
    if totpreco == 0:
        produtomaisbarato = preco
        precomaisbarato = produto
    elif preco < produtomaisbarato:
        produtomaisbarato = preco
        precomaisbarato = produto
    totpreco += preco
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S / N] ')).lower().strip()[0]
    if continuar == 'n':
        break
print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
print(f'O total de compra foi R$ {totpreco:.2f}')
print(f'Temos {precomais1000} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi {precomaisbarato} que custa R${produtomaisbarato:.2f}')
