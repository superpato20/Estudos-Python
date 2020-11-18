lista = []
expre = str(input('Digite uma expressão matematica: ')).strip()
for c in expre:
    if '(' in c:
        lista.append(c)
    elif ')' in c:
        if '(' in lista:
            lista.pop()
        else:
            lista.append(c)
if len(lista) == 0:
    print(f'A expressão {expre} é valida.')
else:
    print(f'A expressão {expre} não é valida.')
