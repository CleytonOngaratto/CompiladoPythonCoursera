def remove_repetidos(lista):
    lista_sem_repeticao = list(set(lista)) # cria uma lista sem elementos repetidos
    lista_sem_repeticao.sort() # ordena a lista
    return lista_sem_repeticao


lista = [2, 4, 2, 2, 3, 3, 1]
lista_sem_repeticao = remove_repetidos(lista)
print(lista_sem_repeticao) # saída: [1, 2, 3, 4]
