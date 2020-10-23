print('=' * 8, 'LOJAS DO PATO', '=' * 8)
c = float(input('Preço das Compras: R$'))
p = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinehiro / cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? '''))
if p == 1:
    print('Sua compra de R${} vai custar R${} no final.'.format(c, c - (10 * c / 100)))
elif p == 2:
    print('Sua compra de R${} vai custar R${} no final.'.format(c, c - (5 * c / 100)))
elif p == 3:
    print('Sua compra de R${} será parcelada em 2x de R${} SEM JUROS!'.format(c, c / 2))
elif p == 4:
    np = int(input('Quantas parcelas? '))
    a = (c + (20 * c / 100)) / np
    ct = c + (20 * c /100)
    print('''Sua compra será parcelada em {}x de R${} COM JUROS
Sua compra de R${} vai custar R${} no final.'''.format(np, a, c, ct))
elif p != 1 or p != 2 or p != 3 or p != 4:
    print('Opção Invalida. Tente Novamente!')
