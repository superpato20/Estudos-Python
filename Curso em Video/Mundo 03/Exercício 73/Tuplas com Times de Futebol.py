times = ('Internacional', 'Flamengo', 'Atletico-MG', 'Fluminense', 'São Paulo', 'Santos',
         'Palmeiras', 'Grêmio', 'Sport', 'Fortaleza', 'Corinthians', 'Ceará', 'Atletico-GO',
         'Botafogo', 'Bahia', 'Vasco', 'Coritiba', 'Bragantino', 'Atletico-PR', 'Goias')
print('-=' * 51)
print(f'Lista de times do Brasileirão 2020: {times}')
print('-=' * 51)
print(f'Os cincos primeiros são {times[0:5]}.')
print('-=' * 51)
print(f'Os quatros ultimos são {times[16:20]}')
print('-=' * 51)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 51)
print('A posição do Bragantino é a {}ª posição.'.format(times.index('Bragantino')))
