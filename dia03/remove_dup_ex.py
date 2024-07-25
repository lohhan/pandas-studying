# %%

import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")

# %%

df_last = (df.sort_values(by="DtTransaction", ascending=False)).drop_duplicates(subset="IdCustomer", keep="first")

df_last


# %%

condicao = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"

df[condicao]

# %%
