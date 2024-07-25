# %%
import pandas as pd
# %%

df = pd.read_csv("../data/customers.csv", sep=";")

df
# %%

# %%

df = (df.sort_values(by=["Points", "Name"], ascending=[False, True]).rename(columns={"Name":"Nome", "Points":"Pontos"})) # Ordenando pela pontuação (ordem descendente), em caso de empate ordernar em ordem alfabética pelo nome, e por fim  renomeando as colunas
df

# %%

