import sys

try:
    print("====Calculadora Simples====")

    numero1 = input("Digite o primeiro número: ")
    numero2 = input("Digite o segundo número: ")
    num1 = int(numero1)
    num2 = int(numero2)

except ValueError:
    print("Digite apenas números inteiros.")
    sys.exit("Programa encerrado!")

operadores = input("Escolha a operação matemática: +, -, *, / \n")

if operadores == "+":
    soma = num1+num2
    print(f"O resultado da soma é: {soma}")

elif operadores == "-":
    sub = num1-num2
    print(f"O resultado da subtração é: {sub}")

elif operadores == "*":
    mult = num1*num2
    print(f"O resultado da multiplicação é: {mult}")

elif operadores == "/":
    div = num1/num2
    print(f"O resultado da divisão é: {div}")

else:
    print("Digite novamente.")

#exit() ou sys.exit() — encerra o programa na hora