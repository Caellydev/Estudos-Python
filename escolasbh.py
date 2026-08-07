import pandas as pd
import matplotlib.pyplot as plt # -> Gráficos

escolas = pd.read_csv("dados/b-dataset_escolas_20181130.csv", on_bad_lines='skip', encoding='utf-8-sig')


print(escolas.shape)

print(escolas["NOM_BAIR"].value_counts())

top10 = escolas["NOM_BAIR"].value_counts().head(10)
top10.plot(kind='bar')
plt.title("Top 10 bairros com mais escolas municipais - BH")
plt.xlabel("Bairros")
plt.ylabel("Quantidade de escolas")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

'''
 ===== value_counts() - anotações =====

 O QUE FAZ: Conta quantas vezes cada valor único aparece em uma coluna (Series).

 SINTAXE:
 df["nome_da_coluna"].value_counts()

 Repara: primeiro seleciona a coluna com [], DEPOIS chama o método.
 Não existe df.value_counts("coluna") direto no DataFrame inteiro.

 COMPORTAMENTO PADRÃO:
 - Ordena do valor mais frequente pro menos frequente (decrescente)
 - Ignora valores NaN (não conta ausências) por padrão.
'''

#git add .
#git commit -m "sua mensagem aqui"
#git push
