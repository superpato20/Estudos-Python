lista = []
maior = []
menor = []
for c in range(0, 5):
    n = int(input(f'Digite um valor para a Posição {c}: '))
    lista.append(n)
for posicao, valor in enumerate(lista):
    if valor == max(lista):
        maior.append(posicao)
    if valor == min(lista):
        menor.append(posicao)
print(f'Você digitou os valores {lista}.'.replace(',', '').replace('[', '').replace(']', ''))
print(f'O maior valor digitado foi {max(lista)} nas posições {maior}.'.replace('[', '')
      .replace(']', ''))
print(f'O menor valor digitado foi {min(lista)} nas posições {menor}.'.replace('[', '')
      .replace(']', ''))
