lista = ['pão', 'biscoito', 'café', 'rosca']
print(lista)
lista.append('leite')      # adiciona elemento a lista frente no final
print(lista)
lista.insert(2, 'bolo')    # adiciona elemento a lista na posição requerida
print(lista)
del lista[3]               # apaga o elemento requerido da lista
lista.pop(4)               # apaga o elemento requerido da lista
print(lista)
lista.remove('bolo')       # apaga o elemento especifico da lista
print(lista)
print(len(lista))
