from os import makedirs,getenv
from typing import Literal
from dotenv import load_dotenv
from logging import info, error

def create_data_system_file():
    '''
    '''
    data_paths = [
        'data/raw',
        'data/processed'
        ]
    for path in data_paths:
        try:
            info(f"Criando o diretório {path}.")
            makedirs(path)
            info(f"Diretório {path} criado com sucesso!!")
        except FileExistsError as err:
            error(f"O diretório {path} já existe, nada será feito.")
        except Exception as err:
            error(f"Erro inesperado -> {err}.")
            raise err
        
def env_vars(group:Literal['email']):
    '''
    '''
    load_dotenv()
    data_dict ={
        'email':{
            'source_email':getenv('source_email'),
            'source_password':getenv('source_password'),
            'destiny_email':getenv('destiny_email')
        }
    }