# %%
import pandas as pd

# %%

data_users = {
   "id": [1,2,3,4],
   "nome": ["Lohhan", "Joao", "Viviane", "Laete Jr"],
   "idade": [19,10,42,46],
}

df_user = pd.DataFrame(data_users)
df_user

# %%

data_transacoes = {
   "id_user": [1,1,1,2,3,3],
   "vl": [432,532,123,6,4,87],
   "qtProdutos": [2,1,3,6,10,2],
}

df_transacao = pd.DataFrame(data_transacoes)
df_transacao

# %%

df_transacao.merge(df_user,
                  how="left",
                  left_on="id_user",
                  right_on="id"
                  )

# to adicionando os dados da tabela df_user para a tabela df_transacao, sendo ela a tabela da esquerda.

# o how serve para dizer ao pandas que quero manter os dados da tabela da esquerda

# o left_on e o right_on serve para eu setar quais são colunas das respectivas tabelas da esquerda e da direita se conectam

# %%
