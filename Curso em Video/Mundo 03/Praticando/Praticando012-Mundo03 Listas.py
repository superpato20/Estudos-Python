dados = {'nome': 'Luiz', 'sexo': 'Masculino', 'idade': '36'}
print(dados['nome'], dados['sexo'], dados['idade'])
print(f"O {dados['nome']} tem {dados['idade']} anos.")
print(dados.keys())
print(dados.values())
print(dados.items())
print('-' * 30)
for k in dados:
    print(k)
print('-' * 30)
for k in dados.values():
    print(k)
print('-' * 30)
for k, v in dados.items():
    print(f'{k} = {v}')
print('-' * 30)
del dados['sexo']
for k, v in dados.items():
    print(f'{k} = {v}')
