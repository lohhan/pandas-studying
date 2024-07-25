# %%

import pandas as pd

# %%

lista_numeros = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
dados = pd.Series(lista_numeros)
dados

# %%

round(dados.mean()) # Média dos valores da lista

# %%

round(dados.std()) # Desvio padrão dos valores da lista

# %%

dados.max() # Valor maior da lista

# %%

