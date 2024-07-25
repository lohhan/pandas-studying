# %%

import pandas as pd

# %%

dados = {"nome":["Téo", "Nah", "Napoleão"], "idade": [31, 32, 14]}

df = pd.DataFrame(dados)
df

# %%

sumario = df.describe()
sumario

# %%

df["nome"].describe()

# %%

round(sumario["idade"]["mean"])

# %%

df["nome"].iloc[-1]

# %%

df.iloc[-1]

# %%

df.iloc[-1, 0]

# %%

df.info(memory_usage='deep')

# %%

df.head(2)

# %%

df["nome"].tail(1)

# %%
