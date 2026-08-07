import pandas as pd

uri = "https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv"
bebidas = pd.read_csv(uri, on_bad_lines='skip', encoding='latin-1')

bebidas.columns = ("País" , "Cervejas" , "Destilados", "Vinhos", "Total")

print(bebidas.head())