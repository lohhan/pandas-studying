# %%

import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df

# %%

new_column_list = ["UUID", "Points", "IdCustomer", "DtTransaction"]
new_column_list

# %%

df = df[new_column_list]
df

# %%

df.info(memory_usage='deep')
# %%
