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
galera1 = list()
galera1.append('Nara')

galera1.append(28)
galera1.append(teste), galera1.append(galera)
print(galera1)
