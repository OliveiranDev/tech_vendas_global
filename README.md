tech_vendas_global
Visão Geral

O projeto tech_vendas_global tem como objetivo a geração de dados sintéticos de vendas para fins de estudo e prática em Excel, Power BI e SQL, simulando cenários reais encontrados em projetos de dados no mercado.

Este repositório contém apenas a etapa de geração dos arquivos CSV, que serão utilizados posteriormente para:

Limpeza e tratamento de dados

Análise exploratória

Criação de dashboards

Consultas SQL

Simulação de problemas comuns em pipelines de dados

As próximas etapas do projeto envolverão o uso desses dados em ferramentas analíticas e bancos de dados.

Objetivo do Projeto

Criar um conjunto de dados realista que permita praticar:

Modelagem dimensional (fato e dimensões)

Limpeza de dados “sujos” (datas inconsistentes, espaços em branco, formatos inválidos)

Análises no Excel

Dashboards no Power BI

Consultas e transformações em SQL

Estrutura dos Dados

O script gera três arquivos principais:

Dimensões

dim_clientes.csv

ID do cliente

Segmento (Gold, Silver, Bronze)

Região

dim_produtos.csv

ID do produto

Categoria

Preço unitário

Fato

vendas_big.csv

ID da venda

Data da venda (com inconsistências propositalmente inseridas)

ID do produto

ID do cliente

Quantidade vendida

Os arquivos são gerados com dados propositalmente sujos, simulando problemas comuns encontrados em bases reais.

Estrutura do Projeto
tech_vendas_global/
├── gera_arquivos/
│   ├── main.py              # Script de geração dos dados
│   ├── requirements.txt     # Dependências do projeto
│   ├── README.md            # Documentação do projeto
│   ├── .gitignore
│   └── data/
│       ├── dim_clientes.csv
│       ├── dim_produtos.csv
│       └── vendas_big.csv

Tecnologias Utilizadas

Python 3.12+

Pandas

NumPy

Como Executar o Projeto

Clone o repositório:

git clone https://github.com/OliveiranDev/tech_vendas_global.git


Acesse a pasta do projeto:

cd tech_vendas_global/gera_arquivos


Crie e ative o ambiente virtual:

python -m venv .venv
source .venv/Scripts/activate


Instale as dependências:

pip install -r requirements.txt


Execute o script:

python main.py


Os arquivos CSV serão gerados dentro da pasta data/.

Próximas Etapas do Projeto

Limpeza e tratamento dos dados no Excel

Criação de dashboards no Power BI

Modelagem e consultas em SQL

Simulação de um mini Data Warehouse

Observações

Este projeto tem finalidade educacional e prática, focado no desenvolvimento de habilidades em análise e engenharia de dados.

Autor

Rodrigo Neves
Projeto desenvolvido para estudo e portfólio em Dados.