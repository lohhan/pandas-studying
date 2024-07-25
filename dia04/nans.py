# %%
import pandas as pd
import numpy as np
# %%

data = {
   "nome": ["Téo", "Nah", "Lah", "Mah", "Jo"],
   "idade": [31, 32, 34, 12, np.nan],
   "renda": [np.nan, 3245, 357, 12432, np.nan],
}


# %%

df = pd.DataFrame(data)
df
# %%
df["idade"].isna()
# %%
df["idade"].isna().sum() # conta quantos true tem (true = 1, false = 0)
# %%
df.isna()
# %%
df.isna().sum()
# %%
df.isna().mean() # identificar a proporção de valores nulos nas colunas
# %%

df.fillna(
   {
      "idade": df["idade"].mean(),
      "renda": df["renda"].mean()
   }
)

# %%
df.dropna()
# %%
df.dropna(subset=["idade", "renda"], how='all') # removendo a linha que tanto a idade quanto a renda sao n.a.

# how all => remove a linha apenas se todas as colunas forem n.a., nesse caso usando subset ele irá considerar apenas os subset (e)

# how any => basta uma coluna ser n.a. para ser removido (ou)
# %%

df.dropna(axis=1, how='all') # remove colunas inves de linhas que conterem n.a.

# %%

df.dropna(axis=1, thresh=4) # o thresh serve para dar uma condição, de ah tem que ter tantos nao nulos para nao remover (tipo acima, se tiver 4 não nulos, blz, mas caso não tiver, remove a coluna)
# %%
