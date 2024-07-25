# %%

import pandas as pd

data = {
   "Nome": ["Téo", "Nah", "Maria", "Nah", "Lara", "Téo"],
   "Idade": [32, 33, 2, 33, 31, 32],
   "updated_at": [1, 2, 3, 1, 2, 3]
}

# %%

df = pd.DataFrame(data)
df

# %%

df = (df.sort_values(by="updated_at", ascending=False).drop_duplicates(subset=["Nome", "Idade"], keep="first")) # o drop duplicates vai eliminar apenas os items que coiencidem em todas as colunas, se caso eu quiser eliminar de acordo com apenas em colunas especificas, tenho que usar o subset. já o keep é utilizado para eu setar qual item priorizar para remanescer na tabela, por default é o 'first', mas posso setar para ser o último usando o 'last'.
df

# %%
