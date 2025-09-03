from extractor.api_extractor import extract_covid_countries

def main():
    df = extract_covid_countries()
    if not df.empty:
        print("Dados extraídos da API (2 primeiros registros):")
        print(df.head(2))
    else:
        print("Falha na extração dos dados.")

if __name__ == "__main__":
    main()