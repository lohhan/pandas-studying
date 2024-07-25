# %% 

import pandas as pd

df = pd.read_csv("../data/products.csv", sep=";", names=["ID", "Names", "Description"])

# %%

df.rename(columns={"Names": "Nomes", "Description": "Descrição"}, inplace=True)
df

# %%