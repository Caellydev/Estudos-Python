#operador lógico AND
#operador lógico OR
entrada = input("[E]ntrar [S]air: ")
senha_user = input("Senha: ")

senha_system = "123456"

if (entrada == "E" or "e") and senha_user == senha_system:
    print("Você entrou no sistema")
    print("Senha correta!")

elif entrada == "S":
    print("Você saiu do sistema.")

elif entrada != "E" and "S":
    print("Tente novamente.")

elif senha_user != senha_system:
    print("Você digitou a senha incorretamente!")

else:
    print("Travou")
#------------------------
senha = input('Digite sua senha: ') or "Sem senha"
print(senha) # Resultado igual a de um if
