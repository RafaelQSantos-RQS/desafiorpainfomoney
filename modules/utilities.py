from os import makedirs,getenv
from typing import Literal
from dotenv import load_dotenv
from logging import info, error

def create_data_system_file():
    '''
    Cria os diretórios necessários para o sistema de dados.

    Esta função cria os diretórios necessários para o sistema de dados, incluindo diretórios para dados brutos (raw) e processados (processed).

    Raises:
    - FileExistsError: Se um dos diretórios já existir.
    - Exception: Se ocorrer um erro inesperado durante a criação dos diretórios.
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
    Retorna as variáveis de ambiente relacionadas a um grupo específico.

    Esta função carrega as variáveis de ambiente de um arquivo .env usando a biblioteca dotenv e retorna um dicionário com as variáveis relacionadas ao grupo especificado.

    Parâmetros:
    - group (Literal['email']): O grupo de variáveis de ambiente a serem recuperadas. Atualmente, apenas 'email' é suportado.

    Retorna:
    - dict: Um dicionário contendo as variáveis de ambiente relacionadas ao grupo especificado.

    Raises:
    - ValueError: Se o grupo especificado não pertencer a nenhum grupo de variáveis de ambiente pré-definido.
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