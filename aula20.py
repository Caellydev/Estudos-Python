try:
    inteiro = int(input("Digite um número inteiro para verificar se é par ou ímpar: "))
    num = int(inteiro) 


    if num % 2 == 0:
        print("Seu número é par")

    else:
        print("Seu número é ímpar")

except ValueError:
    print("Digite números inteiros")

'''
inteiro = input("Digite um número inteiro para verificar se é par ou ímpar: ")

if inteiro.isdigit():
    num = int(inteiro)


    if num % 2 == 0:
        print("Seu número é par")
    else:
        print("Seu número é ímpar")
else:
    print("Você não digitou números inteiros")
'''

#Neste exercício, utilizei o try/except, porquê quando o usuário digitar um valor diferente do inteiro
#ele já cai no except (ValueError). 

print("=" * 10)

hora = int(input("Digite que horas são: "))


if 0 <= hora <= 11:
    print(f"Bom dia: {hora} hrs")
#"Se 0 for menor ou igual a hora, E hora for menor ou igual a 11, imprima bom dia"

elif 12 <= hora <= 17:
    print(f"Boa tarde {hora} hrs")

elif 18 <= hora <= 23:
    print(f"Boa noite {hora} hrs")

else:
    print("Digite novamente, essa hora não existe")

print("=" * 10)

nome = input("Digite o seu nome: ")

if len(nome) <= 4:
    print("Seu nome é curto")

elif len(nome) >= 5 and len(nome) <= 6:
    print("Seu nome é normal")

#elif len(nome) == 5 or len(nome) == 6: 
#    print("Seu nome é normal")

else:
    print("Seu nome é grande")