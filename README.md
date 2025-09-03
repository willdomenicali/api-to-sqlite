# api-to-sqlite

# Pipeline de Dados COVID-19 (API → Pandas → SQLite)

## Descrição
Este projeto implementa um **pipeline de dados** que:
1. Extrai informações de COVID-19 a partir de uma API pública (`disease.sh`).
2. Transforma os dados utilizando **pandas** (tipos de colunas, renomeações, novas features).
3. Persiste os dados em um banco de dados **SQLite** para consultas posteriores.

O projeto foi desenvolvido com foco em **boas práticas de versionamento (Git)**, **organização de código** e **tratamento de erros**.

## Estrutura do Projeto

src/extractor/api_extractor.py (Responsável pela extração da API)

src/transformer/df_transformer.py  (Responsável pelas transformações no DataFrame)

src/database/sqlite_handler.py (Responsável pela persistência no SQLite)

src/main.py (Script principal que orquestra o pipeline)
## 🚀 Como executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/willdomenicali/api-to-sqlite.git
   cd api-to-sqlite

2. Crie um ambiente virtual (opcional):
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Instale as dependências:
pip install -r requirements.txt

4. Execute o pipeline:
python src/main.py

## Exemplo de Query no SQLite
SELECT pais, populacao, categorizacao_populacao
FROM covid_paises
LIMIT 10;

## Futuras Melhorias

- Criação de visualizações (dashboards)
- Automação de atualização diária

## Este projeto foi desenvolvido em diferentes branches para demonstrar controle de versão profissional:

- main → versão estável

- dev → desenvolvimento ativo

- feature/transformar-df → transformação do DataFrame

- feature/banco-dados → persistência em SQLite

#### As branches foram mantidas para demonstrar o fluxo de construção do projeto.