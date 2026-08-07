"""
Existem três flags:

!s — str()
Força o Python a usar str() no valor. É o padrão, então na prática quase nunca você precisa escrever isso explicitamente 
— mas existe por completude.

f"{nome!s}"  # equivale a str(nome)


!r — repr()
Essa é a mais usada na prática. Usa repr() em vez de str(). A diferença aparece principalmente com strings:

nome = "Ana"
print(f"{nome}")    # Ana
print(f"{nome!r}")  # 'Ana'   <- com aspas!

Isso é super útil pra debug, porque repr() mostra a representação "oficial" do objeto, deixando claro, por exemplo, 
que tem espaços extras ou que é realmente uma string:

valor = "  oi  "
print(f"{valor}")    #   oi   (difícil ver os espaços)
print(f"{valor!r}")  # '  oi  '  (agora dá pra ver claramente)


!a — ascii()
Usa ascii(), que é como o repr(), mas escapa caracteres não-ASCII (acentos, emojis, etc.)

palavra = "café"
print(f"{palavra!r}")  # 'café'
print(f"{palavra!a}")  
"""

nome = "Júlia"
print(f"{nome!s}") # equivale a str(nome)

#======

nome = "Ana"
print(f"{nome}")
print(f"{nome!r}")

#======

palavra = "café"
print(f"{palavra!r}")  # 'café'
print(f"{palavra!a}")  # 'caf\xe9'
