def exercicio():
    palavra = input("Digite a sua palvara: ")
    lista = list(palavra)
    segredo = ""

    for x in lista:
        if (x=="z"):
            segredo +="a" 
        elif (x=="Z"):
            segredo += "A"
        else:
            segredo += chr(ord(x) + 1)
    print(segredo)

exercicio()

"""
ord(x) pega o caractere x e devolve o número (código Unicode/ASCII) que representa ele. Ex: ord("a") → 97
+ 1 desloca esse número pro próximo da tabela
chr(...) faz o caminho inverso: pega o número e devolve o caractere correspondente. Ex: chr(98) → "b"
"""