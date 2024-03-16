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
            'email':getenv('source_email'),
            'password':getenv('source_password'),
            'destiny':getenv('destiny_email')
        }
    }
    
    if group not in data_dict.keys():
        msg = "O grupo de variáveis inserido não pertence a nenhum grupo de variáveis de ambiente pré definido"
        error(msg=msg)
        raise ValueError(msg)
    
    return data_dict.get(group)