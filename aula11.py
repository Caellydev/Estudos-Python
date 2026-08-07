#operador lógico NOT
#True = False
#False = True

senha = input("Digite a senha: ")

if not senha:
    print("Você não digitou a senha")
elif senha == "123456":
    print("Você entrou no sistema")
else:
    print("Senha incorreta")

print(not True) #false
print(not False) #true