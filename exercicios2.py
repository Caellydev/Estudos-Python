'''
Exercício 15
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.


'''

quantoganha1 = input("Quanto você ganha por hora ? ")
quantotrabalha1 = input("Quantas horas você trabalha no mês ? ")

quantoganha = float(quantoganha1)
quantotrabalha = float(quantotrabalha1)

bruto = quantoganha * quantotrabalha
ir = 11 / 100
inss = 8 / 100
sindicato = 5 / 100 

descontoir = bruto * ir
descontoinss =  descontoir * inss
descontosindi = descontoinss * sindicato

liquido = bruto - (descontoir + descontoinss + descontosindi)

print(f"Seu salário bruto é de: {bruto:.2f}")
print(f"Seu desconto de ir: {descontoir:.2f} R$")
print(f"Seu desconto de inss: {descontoinss:.2f} R$")
print(f"Seu desconto de sindicato: {descontosindi:.2f} R$")
print(f"Seu salário líquido {liquido:.2f} R$")

'''
Exercício 16
Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''


