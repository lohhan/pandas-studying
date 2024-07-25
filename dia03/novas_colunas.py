# %%

import pandas as pd
import numpy as np

# %%

df = pd.read_csv("../data/customers.csv", sep=";")
df

# %%

df["Points_Double"] = df["Points"] * 2

# %%

df

# %%

df["log"] = np.log(df["Points"])

# %%

df["Name"].str.upper()

# %%

def get_first(nome:str):
   nome = nome.upper()
   return nome.split("_")[0]

df["Name_First"] = df["Name"].apply(get_first)

# %%

# usando lambda

df["Name_First"] = df["Name"].apply( lambda x: x.upper().split("_")[0] )
df

# %%

def intervalo_pontos(pontos):
   if pontos < 2500:
      return "baixo"
   elif pontos < 3500:
      return "medio"
   else:
      return "alto"
   
df["Faixa_Pontos"] = df["Points"].apply(intervalo_pontos)
df

# %%

data = {
   "nome": ["Teo", "Nah", "Maria", "Lara"],
   "recencia": [1, 30, 10, 45],
   "valor": [100, 2000, 15, 500],
   "frequencia": [2, 5, 1, 15],
}

df_crm = pd.DataFrame(data)

def rfv(row):
   nota = 0

   if row["recencia"] <= 10:
      nota += 10
   elif 10 < row["recencia"] <= 30:
      nota += 5
   elif row["recencia"] > 30:
      nota += 0

   if row["valor"] > 1000:
      nota += 10
   elif 100 <= row["valor"] < 1000:
      nota += 5
   elif row["valor"] < 100:
      nota += 0
   
   if row["frequencia"] > 10:
      nota += 10
   elif 5 <= row["frequencia"] < 10:
      nota += 5
   elif row["frequencia"] < 5:
      nota += 0

   return nota

# %%

df_crm["RFV"] = df_crm.apply(rfv, axis=1)

# %%

df_crm
# %%
