from datetime import date
sexo = int(input('''Qual o seu sexo:
[ 1 ] MASCULINO
[ 2 ] FEMININO '''))
if sexo == 1:
    nasc = int(input('Ano de nascimento: '))
    hoje = date.today().year
    idatual = hoje - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idatual, hoje))
    if idatual < 18:
        print('Ainda faltam {} anos para o alistamento'.format(18 - idatual))
        print('Seu alistamento será em {}.'.format(nasc + 18))
    elif idatual > 18:
        print('Você já deveria ter se alistado há {} anos.'.format(idatual - 18))
        print('Seu alistamento foi em {}.'.format(nasc + 18))
    elif idatual == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Opção Invalida! Tente Novamente!')
