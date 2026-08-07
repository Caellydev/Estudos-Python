#caractere de escape
#Serve para Strings e é bem útil caso eu precise imprimir um texto com aspas, por exemplo.
#print("Carolina da Sila \"Nagibe\"")
#porém existe uma opção bem mais interessante e mais válida também: (obs-> é possível inverter tbm)
#print('Carolina da Silva "Nagibe"')
#Type é uma classe onde podemos verificar qual o tipo de dado está seno atribuído.
x = 23
y = 15

if x == y:
    print("Iguais")
else:
    print("Falso")

# =================================================

print(int('1'), type((int('1'))))
print((float('1') + 1))
print(str(11) + 'b') 
print(int('11') + 1)

# =================================================

nome_completo = input('Digite o seu Nome Completo: ')
soma = 2 + 5
print(nome_completo,', Obrigado!', 'O resultado da sua soma é:', soma)

# =================================================

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você não é maior de idade")

# =================================================

nome = "Carolina"
idade = 24
maiorIdade = idade >= 18
print('Nome:', nome, 'Idade:', idade, 'é maior de idade?', maiorIdade)