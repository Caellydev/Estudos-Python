#Operadores de Comparação (Relacionais)
# >           Maior       2 > 1
# <           Menor       1 < 2
# >=      Maior ou igual  x >= 8
# <=      Menor ou igual  x <= 8
# ==          Igual      10 == 10
# !=       Diferente     10 != 9
num1 = input("Digite o primeiro valor: ")
num2 = input("Digite o segundo valor valor: ")

numero1 = int(num1)
numero2 = int(num2)

if numero1 > numero2:
    print(f'O primeiro valor {numero1} é maior do que o segundo {numero2}')
elif numero2 > numero1:
    print(f'O segundo valor {numero2} é maior do que o primeiro {numero1}')
else:
    print("São valores iguais")