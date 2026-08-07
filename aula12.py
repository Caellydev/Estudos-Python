#operadores IN
#operadores NOT IN 

nome = 'Carolina'
print(nome[0])
print(nome[-8])
print("l" in nome)
print("h" in nome)
print("========")
print("Caro" not in nome)
print("nina" not in nome)

print(10 * "-")

nome = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar em seu nome: ")

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print("Não foi possível encontrar")