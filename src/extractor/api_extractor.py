import requests
import pandas as pd

def extract_covid_countries():
    """
    Extrai dados COVID-19 por país da API disease.sh e retorna como DataFrame

    Returns:
        pd.DataFrame: Dados por país com métricas da COVID-19
    """
    url = "https://disease.sh/v3/covid-19/countries"
    
    try:
        response = requests.get(url, timeout=10)  # timeout evitando travamento
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        return df
    
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição da API: {e}")
        return pd.DataFrame()  # retorna DataFrame vazio para não quebrar o fluxo
    
    except (ValueError, TypeError) as e:
        print(f"Erro ao processar os dados: {e}")
        return pd.DataFrame()  # retorna DataFrame vazio

df = extract_covid_countries()