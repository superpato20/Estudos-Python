brasil = []
estado1 = {'urf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'urf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['urf'])
print(brasil[1]['sigla'])
print(brasil[0]['urf'], '-', brasil[0]['sigla'])
