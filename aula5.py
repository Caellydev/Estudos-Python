#O método .format() serve para inserir valores dentro de uma string de forma organizada, 
# sem precisar concatenar tudo com +. É bastante comum em Python.
#Tudo que o .format() faz, o f-string também faz — inclusive a formatação de números

a = "A"
b = "B"
c = 1.1
formato = "{}, {}, {}".format(a,b,c)
print(formato)

#=====

a = "A"
b = "B"
c = 1.1345324643
string = "a={0}, b={1}, c={2:.2f}"
formato = string.format(a,b,c)
print(formato)
#mesmo resultado, caminhos diferentes

#=====

nome = "Carolina"
idade = 19
resultado = "Nome= {}, Idade= {}".format(nome, idade)
print(resultado)

#=====

nome = "Carolina"
idade = 19
resultado = "Nome= {}, Idade= {}"
formato = resultado.format(nome,idade)
print(formato)
#mesmo resultado, caminhos diferentes