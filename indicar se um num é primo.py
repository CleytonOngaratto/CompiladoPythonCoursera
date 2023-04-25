#aqui identificamos se um n um é primo
def primo(num):
    i = 2
    while i < num:
        if num % i == 0:
            #exemplo de fun break
            break
        i += 1
    return i == num


#aqui eu identifico quais os primos de uma sequência range
for n in range(eval(input("Digite um número: "))):
    if not primo(n):
        # exemplo de func continue
          continue
    print(n)
 
