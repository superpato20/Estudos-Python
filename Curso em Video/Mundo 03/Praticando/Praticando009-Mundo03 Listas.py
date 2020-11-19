teste = list()
teste.append('Luiz')
teste.append(25)
print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'Mark'
teste[1] = '30'
galera.append(teste[:])
print(galera)
