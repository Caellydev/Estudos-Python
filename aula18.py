"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61
local_carro = 99 #km percorrido

RADAR_1 = 60 #constantes
LOCAL_1 = 100
RADAR_RANGE = 1 #a distância onde o radar pega


if velocidade > RADAR_1:
    print("Você está muito rápido.")

#Se 99 for igual ou maior do que local carro, imprima sifudeo
#Se 101 for igual ou menor do que local carro, imprima sifudeo
# é um encadeamento

    if (LOCAL_1 - RADAR_RANGE) <= local_carro <= (LOCAL_1 + RADAR_RANGE):
        print(f"O radar te pegou otaro {local_carro}, o radar estava em {LOCAL_1}")
    else:
        print("O radar não te pegou")
else:
    print("Está okay")

print("=" * 10)

#========================
velocidade = 50
local_carro = 80 #km percorrido

RADAR_1 = 60 #constantes
LOCAL_1 = 100
RADAR_RANGE = 1 #a distância onde o radar pega

rangemenos = LOCAL_1 - RADAR_RANGE
rangemais = LOCAL_1 + RADAR_RANGE
vel = velocidade > RADAR_1

if vel:
    print("Você está muito rápido.")
else:
    print("Velocidade okay")

    if rangemenos <= local_carro <= rangemais:
        print(f"O radar te pegou otaro {local_carro}, o radar estava em {LOCAL_1}")
    elif vel:
        print("Velocidade okay")
    else:
        print("O radar não te pegou")