from extractor.api_extractor import extract_covid_countries
from transformer.df_transformer import transform_covid_df
from database.sqlite_handler import save_df_to_sqlite
import pandas as pd

# Configuração de pandas para melhor visualização no terminal
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
pd.set_option('display.width', 200)

def main():
    # Extrai dados da API
    df = extract_covid_countries()
    
    # Aplica transformações
    df = transform_covid_df(df)

    # Exibe os primeiros registros
    if not df.empty:
        print("DataFrame transformado (5 primeiros registros):")
        print(df.head())

        # Salva no SQLite com logging e tratamento de erros
        save_df_to_sqlite(df)
    else:
        print("Falha na extração ou transformação dos dados.")

if __name__ == "__main__":
    main()