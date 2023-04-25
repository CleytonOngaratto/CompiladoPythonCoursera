def soma_elementos(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma


lista = [1, 2, 3, 4, 5]
resultado = soma_elementos(lista)
print(resultado) # saída: 15
