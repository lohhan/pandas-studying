# %%
import pandas as pd

# %%
data_01 = {
   "id": [1,2,3,4],
   "nome": ["Lohhan", "Joao", "Viviane", "Laete Jr"],
   "idade": [19,10,42,46],
}

df_01 = pd.DataFrame(data_01)

data_02 = {
   "id": [5,6,7,8],
   "nome": ["Teo", "Mat", "Nah", "Mah"],
   "idade": [31,31,32,32],
}

df_02 = pd.DataFrame(data_02)

# %%
pd.concat([df_01, df_02]).reset_index(drop=True)

# %%
data_03 = {
   "sobrenome": ["Calvo", "Silva", "Costa", "Ferreira"],
   "renda": [3100, 3100, 3200, 3200],
}

df_03 = pd.DataFrame(data_03).sort_values(["renda", "sobrenome"], ascending=[False, True])
df_03    

# %%
pd.concat([df_01, df_03], axis=1)

# %%
