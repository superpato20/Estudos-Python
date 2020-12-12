dados = dict()
dados1 = list()
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f"Média de {dados['nome']}: "))
dados['situação'] = 'Aprovado' if dados['media'] >= 7 else 'Reprovado' if dados['media'] < 6 else 'Recuperação'
dados1.append(dados.copy())
for e in dados1:
    for k, v in e.items():
        print(f'- {k} é igual a '
              f'{v} ')
