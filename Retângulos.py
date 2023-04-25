
largura = int(input("Digite a largura do retângulo:"))
altura = int(input("Digite a altura do retângulo:"))

for i in range(altura):
    linha = ""
    for j in range(largura):
        linha += "#"
    print(linha)
