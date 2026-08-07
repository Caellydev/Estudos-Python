"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f -> .2f (casas decimais)
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 12345
print(variavel)
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{1238.299999999999:.2f}')
print(f'{1238.2999:0>10.1f}')
#No caso de {1238.2999:0>10.1f} o 0>10 ele está adicionando os zero na esquerda, porém ele adiciona a quantidade
#que falta para 10 caracteres, então, ele coloca apenas 4 0, porquê já imprimi 6 caracteres. (Apenas 6 por conta do .1f)
print(f'O hexadecimal de 1500 é {1500:07x}')
print(f'O hexadecimal de 1500 é {1500:x}')
print(f'O hexadecimal de 1500 é {1500:X}')