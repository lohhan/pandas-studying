# %%

import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df

# %%

df_user = df[df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"]
df_user["Points"].sum()

# %%

pontos = {}
for i in df["IdCustomer"].unique():
   pontos[i] = df[df["IdCustomer"] == i]["Points"].sum()

pontos

# %%

df_summary = df.groupby(["IdCustomer"])["Points"].sum()

# %%

df_summary

# %%

df_summary.reset_index() # reseta o index da tabela

# %%

# %%

import datetime

def recencia(x):
   diff = datetime.datetime.now() - x.max()
   return diff.days

df.groupby("IdCustomer").agg(
   {
      "Points": "sum", 
      "UUID": "count",
      "DtTransaction": recencia
   }
).rename(columns=
      {
         "Points": "Valor",
         "UUID": "Frequencia",
         "DtTransaction": "Ultima_Data"
      }
).reset_index() # agg permite fazer mais de uma operação nas colunas 


# %%
