import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

#Configuração
np.random.seed(42)
n_rows = 10000

#Tabela de Produtos(Dimensão)
produtos = pd.DataFrame({
    'ID_Produto': [f'P-{i:03d}' for i in range(1, 21)],
    'Categoria': ['Eletrônicos', 'Móveis', 'Roupas', 'Acessórios'] * 5,
    'Preco_unitario': np.random.randint(50, 2000, 20)
}

)

# Tabela de Clientes(Dimensão)
clientes = pd.DataFrame({
    'ID_Cliente': range(1, 101),
    'Segmento': np.random.choice(['Gold', 'Silver', 'Bronze'], 100, p=[0.1, 0.3, 0.6]),
    'Regiao': np.random.choice(['Norte', 'Sul','Leste','Oeste'], 100)
})

# Tabela de Vendas (Fato) - Propositalmente sujo
data_inicial = datetime(2023, 1, 1)
datas = [data_inicial + timedelta(days=np.random.randint(0, 365)) for _ in range(n_rows)]

df_vendas = pd.DataFrame({
    'ID_Venda': range(10001, 10001 + n_rows),
    'Data': datas,
    'ID_Produto': np.random.choice(produtos['ID_Produto'], n_rows),
    'ID_Cliente': np.random.choice(clientes['ID_Cliente'], n_rows),
    'Qtd': np.random.randint(1, 5, n_rows)
})

# Inserindo sujeira
# Espaços em branco nos IDs
df_vendas['ID_Produto'] = df_vendas['ID_Produto'].apply(lambda x: f" {x} " if random.random() < 0.2 else x )

#Datas como texto (formato brasileiro errado para sistemas americanos)
df_vendas['Data'] = df_vendas['Data'].apply(lambda x: x.strftime('%d/%m/%Y') if random.random() < 0.3 else x)

# Salvar
df_vendas.to_csv('vendas_big.csv', index=False, sep=';') #CSV com ponto e vírgula
produtos.to_csv('dim_produtos.csv', index=False, sep=';')
clientes.to_csv('dim_clientes.csv', index=False, sep=';')

print("Arquivos gerados: vendas_big.csv, dim_produtos.csv, dim_clientes.csv")

