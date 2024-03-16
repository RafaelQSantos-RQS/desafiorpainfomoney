# Desafio RPA infomoney
## Descrição
Extrair dados do site infomoney, consultar no google finance, gravar em uma planilha os resultados e enviar por e-mail.

Fiz esse com o framework da BotCity, tenho o mesmo fluxo feito com AutomationEdge, o qual vou postar noutra ocasião.

O desafio é o seguinte:
Construa o seu fluxo com a ferramenta que você domina (Uipath, automation anywhere, Python, o que você sabe usar), poste com a hashtag #desafiorpainfomoney e coloque o link nos comentários deste post para todos conhecerem seu trabalho.

A execução será:
1. Navegue para o site www.infomoney.com.br;
2. Extraia os dados da tabela de maiores altas;
3. Navegue para o site www.google.com/finance;
4. Pesquise o valor de cada ação coletada;
5. Guarde o valor e o índice de cada ação pesquisada;
6. Grave uma planilha com o resultado (modelo na última imagem deste post);
7. Envie um e-mail com o anexo (para onde você quiser, só é preciso funcionar);

## Ferramentas utilizadas
[![Python](https://skillicons.dev/icons?i=py)](https://www.python.org/) [![](https://skillicons.dev/icons?i=vscode)](https://code.visualstudio.com/)

Claro, aqui está uma versão aprimorada com os comandos que o usuário deve executar:

## Preparação
1. **Crie um ambiente virtual:**
   ```bash
   python3 -m venv myenv
   ```

2. **Instale as dependências do projeto:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Instale os webdrivers necessários do Playwright:**
   ```bash
   playwright install
   ```

4. **Abra o gerenciador de conta Google:**
   - Acesse [Gerenciador de Conta Google](https://myaccount.google.com/).

5. **Ative a verificação de duas etapas:**
   - No Gerenciador de Conta Google, vá para a seção "Segurança".
   - Encontre a opção "Verificação em duas etapas" e ative-a.

6. **Crie uma senha para o aplicativo do Google:**
   - Na mesma seção de "Segurança", vá para "Senhas de aplicativos".
   - Selecione "Gerar nova senha" e siga as instruções para criar uma senha específica do aplicativo para o seu projeto.

7. **Ative o acesso IMAP no Gmail:**
   - Acesse as "Configurações" no seu Gmail.
   - Vá para a guia "Encaminhamento e POP/IMAP".
   - Em "Acesso IMAP", marque a opção "Ativar IMAP".

8. **Crie um arquivo .env na raiz do projeto com as informações do e-mail:**
   - Na raiz do seu projeto, crie um arquivo chamado `.env`.
   - Adicione as seguintes linhas ao arquivo `.env`, substituindo os valores de exemplo pelos seus próprios:
     ```
     # Informações sobre o email
     source_email = "seu_email@gmail.com"
     source_password = "sua_senha_de_app_do_google"
     destiny_email = "destinatario@gmail.com"
     ```
   Certifique-se de nunca compartilhar ou publicar seu arquivo `.env` contendo informações confidenciais, como senhas, em repositórios públicos.

Com esses passos, você estará pronto para executar o código. Certifique-se de substituir quaisquer valores específicos (como endereços de e-mail, senhas, etc.) pelos seus próprios.

Claro, vamos detalhar um pouco mais, incorporando as funcionalidades específicas que estão presentes nas suas funções:

## Visão Geral do Main

O `main` é o componente central do nosso sistema, responsável por orquestrar todas as operações, desde a extração de dados até o envio de relatórios por e-mail. Aqui está uma descrição mais detalhada das principais funcionalidades:

1. **Configurações Iniciais**: O `main` inicia configurando o sistema, definindo o nível de registro de log para INFO e formatando as mensagens de log para facilitar a leitura. Em seguida, utiliza a função `create_data_system_file` do módulo `Utilities` para criar os diretórios necessários para armazenar os dados.

2. **Extração de Dados**:
   - Utiliza a função `extract_maiores_altas` do módulo `Extract` para extrair informações sobre as maiores altas do dia do site Infomoney. Essas informações são armazenadas em um dicionário.
   - Em seguida, utiliza a função `extract_google_finance` do mesmo módulo para obter informações sobre as ações pesquisadas no Google Finance. Os resultados são combinados com os dados extraídos do Infomoney e adicionados ao dicionário.

3. **Transformação de Dados**:
   - Os dados extraídos são transformados em um DataFrame do Pandas, facilitando a manipulação e análise futura dos dados. Durante essa etapa, os valores extraídos do Google Finance são adicionados ao DataFrame.

4. **Exportação de Dados**:
   - O DataFrame resultante é exportado para um arquivo Excel utilizando o método `to_excel` do Pandas. O arquivo é salvo no diretório `data/raw`, permitindo fácil acesso e posterior análise dos dados.

5. **Envio de Relatório por E-mail**:
   - Utiliza a função `env_vars` do módulo `Utilities` para obter as informações de e-mail armazenadas no arquivo `.env`.
   - Cria um e-mail com um assunto específico e um corpo HTML personalizado, informando sobre o comparativo entre as informações do Infomoney e do Google Finance.
   - Anexa o arquivo Excel com os dados das maiores altas ao e-mail.
   - Utiliza a função `send_email_gmail` do módulo `email` para enviar o e-mail ao destinatário especificado.

Essas etapas garantem que os dados sejam extraídos, processados e entregues de forma eficiente e conveniente, permitindo uma análise fácil e rápida das tendências do mercado financeiro.