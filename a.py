import sys

try:
    print("====Calculadora Simples====")

    numero1 = input("Digite o primeiro número: ")
    numero2 = input("Digite o segundo número: ")
    num1 = int(numero1)
    num2 = int(numero2)
    
    soma = num1+num2
    sub = num1-num2
    mult = num1*num2
    div = num1/num2


except ValueError:
    print("Digite apenas números inteiros.")
    sys.exit("Programa encerrado!")

operadores = input("Escolha a operação matemática: +, -, *, / \n")

if operadores == "+":
    resultado = soma
    print(f"O resultado da soma é: {resultado}")

    if resultado == 67:
        print("Aí é muito fácil professora é SIX SEVENNN!")

elif operadores == "-":
    resultado = sub
    print(f"O resultado da subtração é: {resultado}")

    if resultado == 67:
        print("Aí é muito fácil professora é SIX SEVENNN!")

elif operadores == "*":
    resultado = mult
    print(f"O resultado da multiplicação é: {resultado}")

    if resultado == 67:
        print("Aí é muito fácil professora é SIX SEVENNN!")

elif operadores == "/":
    resultado = div
    print(f"O resultado da divisão é: {resultado:.2f}")

    if resultado == 67:
        print("Aí é muito fácil professora é SIX SEVENNN!")

else:
    print("Digite novamente.")

#exit() ou sys.exit() — encerra o programa na hora