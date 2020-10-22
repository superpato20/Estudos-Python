vc = int(input('Valor da casa: R$'))
sc = int(input('Salário comprador: '))
ano = int(input('Quantos anos de financiamento? '))
vp = vc / (ano * 12)
print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(vc, ano, vp))
if vp >= 30 * sc / 100:
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo pode ser CONCEDIDO!')
