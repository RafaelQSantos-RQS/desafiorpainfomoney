import pandas as pd
import modules.extract as Extract
import modules.utilities as Utilities
from logging import basicConfig,INFO, info, error

def main():
    print("\n\t\t## CONFIGURAÇÕES ##")
    basicConfig(level=INFO, format=f'%(asctime)s: %(message)s',datefmt='%d/%m/%Y %H:%M:%S') # Configurações do log
    Utilities.create_data_system_file()

    print("\n\t\t## EXTRAÇÃO ##")
    dict_extracted = Extract.extract_maiores_altas(headless=True)
    list_of_values_google = Extract.extract_google_finance(dict_extracted.get("AÇÃO"),headless=True)

    print("\n\t\t## TRANSFORMAÇÃO ##")
    info("Inserindo os valores extraído do google finance no dicionário extraído do infomoney")
    dict_extracted['INDICE GOOGLE FINANCE'] = []
    dict_extracted['VALOR GOOGLE FINANCE'] = []
    for value in list_of_values_google:
        dict_extracted['INDICE GOOGLE FINANCE'].append(value[0])
        dict_extracted['VALOR GOOGLE FINANCE'].append(value[1])
    
    info("Convertendo em um dataframe")
    df = pd.DataFrame(dict_extracted)
    
    print("\n\t\t## EXPORTAÇÃO ##")
    info("Exportando para excel no diretório data/raw")
    path = 'data/raw/'
    df.to_excel(f'{path}Maiores Altas.xlsx',index=False)

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        raise err