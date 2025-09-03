import sqlite3
import pandas as pd
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def save_df_to_sqlite(df: pd.DataFrame, db_name: str = "covid.db", table_name: str = "covid_paises"):
    try:
        conn = sqlite3.connect(db_name)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        logging.info(f"Tabela '{table_name}' carregada no SQLite com sucesso!")

        # Query de exemplo para verificar os dados
        query = f"SELECT pais, populacao, categorizacao_populacao FROM {table_name};"
        resultado = pd.read_sql(query, conn)
        logging.info(f"Visualizando os primeiros registros da tabela '{table_name}':\n{resultado.head()}")
    except Exception as e:
        logging.error(f"Erro ao salvar ou consultar SQLite: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            logging.info("Conexão com SQLite encerrada.")
