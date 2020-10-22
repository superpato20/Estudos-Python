m = int(input('Uma distancia em metros: '))
print('A medida de {:.1f}m corresponde a\n{}km\n{}hm\n{}dam\n{}dm\n{}cm'
      '\n{}mm'.format(m, m / 1000, m / 100, m / 10, m / 0.1, m / 0.01, m / 0.001))
