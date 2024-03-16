from bs4 import BeautifulSoup
from logging import info, error
from playwright.sync_api import sync_playwright, expect

INFOMONEY_URL = "https://www.infomoney.com.br/"
GOOGLE_FINANCE_URL = "https://www.google.com/finance"

def extract_maiores_altas(headless:bool=False) -> dict:
    '''
    '''
    try:
        with sync_playwright() as p:
            info("Configurando o navegador")
            browser = p.chromium.launch(channel='msedge',headless=headless)

            info("Criando um novo contexto")
            context = browser.new_context()

            info("Criando uma nova página")
            page = context.new_page()

            info("Navegando até url")
            page.goto(INFOMONEY_URL)

            info("Extraindo o html do maiores altas")
            maiores_altas = page.locator("#high")
            maiores_altas_html = maiores_altas.inner_html()

            info("Usando beautifulsoup para raspar os dados do html extraído")
            soup = BeautifulSoup(maiores_altas_html,features="html.parser")
            info_dict = {"AÇÃO":[],"INDICE INFOMONEY":[],"VALOR INFOMONEY":[]}
            for tr in soup.find_all('tr'):
                td = tr.find_all('td')
                info_dict['AÇÃO'].append(td[0].get_text())
                info_dict['INDICE INFOMONEY'].append(td[1].get_text())
                info_dict['VALOR INFOMONEY'].append(float(td[2].get_text().replace("R$ ","").replace(",",".")))

            return info_dict

    except Exception as ex:
        error(f"Error na extração infomoney -> {ex}")
        raise ex
    
def extract_google_finance(acao:list,headless:bool=False) -> tuple:
    '''
    '''
    try:
        with sync_playwright() as p:
            info("Configurando o navegador")
            browser = p.chromium.launch(channel='msedge',headless=headless)

            info("Criando um novo contexto")
            context = browser.new_context()

            info("Criando uma nova página")
            page = context.new_page()

            result = []
            for i in acao:
                info(f"Navegando até url {GOOGLE_FINANCE_URL}")
                page.goto(GOOGLE_FINANCE_URL)

                info(f"Pesquisando a ação {i}")
                first_title = page.title()
                page.get_by_role("combobox").fill(i)
                page.keyboard.press("Enter")

                while (page.title() == first_title):
                    pass

                actual_title = page.title()
                preco = actual_title.split("R$")[1].split(" ")[0].strip()
                variacao = actual_title.split("(")[1].split(")")[0].strip().replace("▲","+").replace("▼","-")
                result.append((variacao,float(preco)))

            return result
    except Exception as ex:
        error(f"Error na extração infomoney -> {ex}")
        raise ex