"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero = input("Digite um número para ver o valor em dobro: ")

try:
    num = int(numero) * 2
    print(num)
except:
    print("Isso não é um número")