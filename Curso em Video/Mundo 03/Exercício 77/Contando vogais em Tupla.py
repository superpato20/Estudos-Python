listagem = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in listagem:
    print(f'Na palavra {c} temos ', end='')
    for d in c:
        if d in 'AEIOU':
            print(d.lower(), end=' ')
    print('.')
