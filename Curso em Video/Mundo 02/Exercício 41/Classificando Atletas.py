from datetime import date
ano = int(input('Ano de Nascimento: '))
hoje = date.today().year
idatual = hoje - ano
print('O atleta tem {} anos.'.format(idatual))
if idatual <= 9:
    print('Classificação: MIRIM')
elif idatual <= 14:
    print('Classificação: INFANTIL')
elif idatual <= 19:
    print('Classificação: JÚNIOR')
elif idatual <= 25:
    print('Classificação: SÊNIOR')
elif idatual > 25:
    print('Classificação: MASTER')
