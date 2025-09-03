import pandas as pd
import logging

# Configuração básica do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def transform_column_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converte colunas específicas para tipo string.
    """
    try:
        df[['country', 'countryInfo', 'continent']] = df[['country', 'countryInfo', 'continent']].astype('string')
        logging.info("Transformação de tipos concluída.")
    except KeyError as e:
        logging.error(f"Coluna não encontrada para transformar tipo: {e}")
    except Exception as e:
        logging.error(f"Erro inesperado em transform_column_types: {e}")
    return df

def transform_fields_rename(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renomeia as colunas para nomes mais amigáveis em português.
    """
    try:
        df = df.rename(columns={
            'updated':'atualizado', 'country':'pais', 'countryInfo':'info_pais',
            'cases':'casos', 'todayCases':'casos_hoje', 'deaths':'mortes', 'todayDeaths':'mortes_hoje',
            'recovered':'recuperados', 'todayRecovered':'recuperados_hoje', 'active':'ativos', 'critical':'criticos',
            'casesPerOneMillion':'casos_por_milhao', 'deathsPerOneMillion':'mortes_por_milhao',
            'tests':'testes', 'testsPerOneMillion':'testes_por_pessoa', 'population':'populacao', 'continent':'continente',
            'oneCasePerPeople':'casos_por_pessoa', 'oneDeathPerPeople':'mortes_por_pessoa', 'oneTestPerPeople':'testes_por_pessoa',
            'activePerOneMillion':'ativos_por_milhao', 'recoveredPerOneMillion':'recuperados_por_milhao',
            'criticalPerOneMillion':'criticos_por_milhao',
        })
        logging.info("Renomeação das colunas concluída.")
    except Exception as e:
        logging.error(f"Erro ao renomear colunas: {e}")
    return df

def transform_new_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria novas colunas derivadas, como categorização da população.
    """
    try:
        if 'populacao' in df.columns:
            bins = [0, 1_000_000, 10_000_000, 100_000_000, df['populacao'].max()+1]
            labels = ['pequena', 'média', 'grande', 'muito grande']
            df['categorizacao_populacao'] = pd.cut(df['populacao'], bins=bins, labels=labels)
            logging.info("Coluna categorizacao_populacao criada com sucesso.")
        else:
            logging.warning("Coluna 'populacao' não encontrada, categorizacao_populacao não foi criada.")
    except Exception as e:
        logging.error(f"Erro ao criar novas colunas: {e}")
    return df

def transform_covid_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica todas as transformações de forma sequencial:
    1. Ajusta tipos de colunas
    2. Renomeia colunas
    3. Cria novas colunas derivadas
    """
    df = transform_column_types(df)
    df = transform_fields_rename(df)
    df = transform_new_columns(df)
    logging.info("Todas as transformações aplicadas com sucesso.")
    return df
