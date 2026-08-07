# Crie as variáveis de acordo com os prints()

nome = "Carolina"
sobrenome = "Nagibe"
idade = 19
nascimento = 3,9,2006
tamanho = 1.52

print("Digite seu nome:", nome)
print("Digite seu sobrenome:", sobrenome )
print("Digite sua idade:", idade )
print("Digite seu ano de nascimento: ", *nascimento, sep="/")
print("Digite seu tamanho em metros: ", tamanho, "metros")

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você não é maior de idade :(")

# o asterístco, separa os valores