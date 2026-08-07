"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome} (okay)
        Seu nome invertido é {nome invertido} (okay)
        Seu nome contém (ou não) espaços (okay)
        Seu nome tem {n} letras (okay)
        A primeira letra do seu nome é {letra} (okay)
        A última letra do seu nome é {letra} (okay)
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios." (okay)
"""

nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")
quantidade = len(nome)
espaco = " " in nome

if nome and idade:
    print(f"Seu nome: {nome} e sua idade: {idade}")
    print(f"Seu nome invertido: {nome[::-1]}")
    print(f"{quantidade}, quantidade de caracteres")
    print(f"Primeira letra do seu nome: {nome[0]}")
    print(f"Última letra do seu nome: {nome[-1]}")

    if espaco:
        print(f"Possui espaço(s) no seu nome: {espaco!r}") 
    else:
        print(f"Seu nome não possui espaços.")

else:
    print("Desculpe, você deixou campos vazios.")


#no segundo If eu poderia apenas ter feito da seguinte maneira:
    #if " " in nome:
        #print("Tem espaços no seu nome")


