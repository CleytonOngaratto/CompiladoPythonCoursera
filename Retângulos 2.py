largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

for i in range(altura):
    linha = ""
    for j in range(largura):
        if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:
            linha += "#"
        else:
            linha += " "
    print(linha)
