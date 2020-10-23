c = str(input('Informe seu sexo: [M/F] ')).upper().strip()
while c not in 'MmFf':
    c = str(input('Dados inválidos.Por favor, informe o seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(c))

