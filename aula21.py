inteiro = input("Digite um número inteiro para verificar se é par ou ímpar: ")

if inteiro.isdigit():
    num = int(inteiro)


    if num % 2 == 0:
        print("Seu número é par")
    else:
        print("Seu número é ímpar")
else:
    print("Você não digitou números inteiros")