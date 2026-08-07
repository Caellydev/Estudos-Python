print("====Calculadora de IMC====")
#cálculo de IMC
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso // (altura ** 2 )
print("========")
print("Olá", nome, "Seu peso é:", peso, "kg")
print("Sua altura é:", altura, "metros")
print("E o seu IMC é:", imc)
#cálculo de IMC2
print("====Calculadora de IMC====")
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2 )
linha_1 = f'Olá {nome} seu peso é {peso} kg'
linha_2 = f'sua altura é {altura} metros'
linha_3 = f'E o seu IMC é: {imc:.2f}'
print("========")
print(linha_1)
print(linha_2)
print(linha_3)