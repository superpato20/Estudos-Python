c = str(input('Informe seu sexo: [M/F] ')).upper().strip()
while c != 'M' and c != 'F':
    c = str(input('Dados inválidos.Por favor, irfome seu sexo: ')).upper().strip()
print('Sexo {} registrado com sucesso!'.format(c))
