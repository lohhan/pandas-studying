# %%

import pandas as pd

df_costumers = pd.read_csv("../data/customers.csv", sep=";")
df_costumers

# %%

type(df_costumers)

# %%

df_costumers.shape

# %%

df_costumers.describe()

# %%

df_costumers["Points"].astype(int) # tranformando a coluna points para inteiro

# %%

df_costumers["Points"].describe()

# %%

max_points = df_costumers["Points"].max()
condicao = df_costumers["Points"] == max_points

df_costumers["Name"][condicao].iloc[0]

# %%

df_costumers["Points"][df_costumers["Points"] > 3000]

# %%

df_costumers[(df_costumers["Points"] > 1000) & (df_costumers["Points"] < 2000)]

# %%

condicao = (df_costumers["Points"] >= 1000) & (df_costumers["Points"] <= 2000)
df_1000_2000 = df_costumers[condicao].copy()

df_1000_2000["Points"] = df_1000_2000["Points"] * 10

# %%

df_1000_2000

# %%

df_costumers[["Name", "Points"]] # buscar 2 colunas

# %%

# ordenando as colunas em ordem alfabética
colunas = df_costumers.columns.tolist()
colunas.sort()

df_costumers = df_costumers[colunas] 
df_costumers

# %%  

# renomeando colunas

df_costumers = df_costumers.rename(columns={"Name": "Nome", "Points": "Pontos"})
df_costumers
# %%

# renomeia as colunas e ja reatribui o valor ao dataframe

df_costumers.rename(columns={"UUID": "ID"}, inplace=True)
df_costumers

# %%
