from datetime import date
hoje = date.today().year
m = 0
n = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idatual = hoje - nasc
    if idatual >= 18:
        m += 1
    elif idatual < 18:
        n += 1
print('Ao todo tivemos {} pessoas maiores de idade.\nE também tivemos {} pessoas menores de idade.'.format(m, n))
