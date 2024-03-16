import pandas as pd
import modules.extract as Extract
import modules.utilities as Utilities
import modules.email as email
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

    print("\n\t\t## ENVIO DE RELATÓRIO ##")
    email_info = Utilities.env_vars(group='email')
    subject = "Relatório infomoney vs google finance"
    msg = "\
        <html> \
            <head> \
            </head> \
            <body> \
                <h1>Relatório infomoney vs google finance</h1> \
                <h2>Segue anexo a Planilha com informações das Ações.</h2> \
                <h3>Comparativo entre infomoney e google finance</h3> \
            </body> \
        </html>"
    path_file = f'{path}Maiores Altas.xlsx'
    email.send_email_gmail(credential=email_info,destiny=email_info.get('destiny'),subject=subject,msg=msg,file_path=path_file)

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        raise err