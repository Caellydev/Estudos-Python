#Exercício 1
print('AlÔ, Mundo!')
#Exercício 2
num = int(input("Digite um número: "))
print('O número informado foi:', num)
#Exercício 3
print('=====Soma=====')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('Seu resultado é:', num1 + num2)
#Exercício 4
print('====Média====')
nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))
nota3 = int(input('Digite sua terceira nota: '))
nota4 = int(input('Digite sua quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

if nota1 <= 10 and nota2 <= 10 and nota3 <= 10 and nota4 <= 10:
    print(f'Sua média é de: {media}')
else:
    print('Um ou mais valores estão incorretos')
#Exercício 5
print('====Conversão de Metros para Centímetros====')
metros = float(input('Digite o valor em metros: '))
cm = metros * 100
print(f'O valor convertido para centímetros é: {cm} cm')
#Exercício 6
print('====Descubra a área do círculo====')
raio = int(input('Digite o valor do raio: '))
area = (raio **2) * 3.14
print(f'Está é a área do seu círculo: {area}')
#Exercício 7
print('====Área Quadrado====')
lado = int(input('Digite um lado do quadrado para calcular a área: '))
areaquad = lado **2
quad2 = areaquad * 2
print(f'A área de seu quadrdado é: {areaquad} e o dobro é: {quad2}')
#Exercício 8
print("==== Salário ====")
salario = float(input("Quantas reais você ganha por hora? "))
salario2 = float(input("Qual o seu número de horas trabalhadas no mês? "))
calculo = salario * salario2

print("Seu total de salário no referido mês.", calculo)

#Exercício 9
print("====Fahrenheit====")
fahrenheit = float(input("Digite os graus em Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)
print("Graus em Celsius é:", celsius)

#Exercício 10
print("====Celsius====")
celsius2 = float(input("Digite os graus em Celsius: "))
fahrenheit2 = (celsius2 * 9/5) + 32
print("Graus em fahrenheit é:", fahrenheit2)

#Exercício 11
print("====Números Inteiros e Real====")
nums = int(input("Digite um Número Inteiro: "))
nums2 = int(input("Digite outro Número Inteiro: "))
nums3 = float(input("Digite um Número Real: "))
produto = (nums * 2) * (nums2 / 2)    
soma = (nums * 3) + nums3
cubo = nums3 ** 3   

print("Seu primeiro resultado: ", produto)
print("Seu segundo resultado: ", soma)
print("Seu terceiro resultado: ", cubo)

#Exercício 12
gigabyte = float(input("Digite a quantidade de dados em Gigabytes: "))
megabyte = gigabyte * 1024
print("Seus dados em Megabytes: ", megabyte)

#Exercício 14
print("====Pesca====")
peso = float(input("Digite a quantidade de peixes em kg: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print("Passou do peso máximo. Seu valor de multa é: ", multa)
    print("Quantidade de quilos excedentes: ", excesso)
else:
    print("Você não execedeu a quantidade de quilos")