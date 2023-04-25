n = int(input("Digite o valor de n: "))

fatorial = 1

# Calcula o fatorial de n
for i in range(2, n+1):
    fatorial *= i

# Imprime o resultado
print(fatorial)
