Como configurar o servidor local:

# 1 Tenha o python instalado na máquina
    ## 1.1 Baixe o instalador: 
    Windows: https://www.python.org/downloads/windows/
        selecione a versão mais recente
    ## 1.2 Siga os passos instalação
        * Não esqueça de marcar a flag "Add to PATH"

# 2 Abrir o código no VsCode
    O código está salvo no caminho
    S:\Projeto Documentacao html\Doc_Interativo
    Copie e cole na sua área de trabalho

# 3 Criar ambiente virtual
    - Este passo é opcional mas altamente recomendado
    - Mantém o ambiente limpo de outras bibliotecas que poderiam causar conflito na execução do código
    3.1 Abra o terminal do VsCode (Ctrl + J)
        rode o comando: python -m venv (nome_do_seu_ambiente)
            * o nome do ambiente não deve conter 
        
        Este comando irá gerar uma pasta com o nome do seu ambiente

    3.2 Ativar o ambiente
        no terminal, rode:
            '.\nome_do_seu_ambiente\Scripts\activate'
            exemplo: 
                '.\.venv\Scripts\activate'
    
    3.3 instalar as bibliotecas necessárias:
        Com o ambiente ativado, rode no terminal:
            pip install -r requirements.txt
    
# 4 Execute o código python
    - o código está na pasta backend
    - selecione-o e execute
    ou
    - no terminal rode
        python /backend/server.py

# 5 Desativando o ambiente virtual(venv)
    No terminal digite:
        deactivate

# 6 Possíveis problemas
    A primeira vez o código irá rodar novamente, mas quando fechar o terminal pode encerrar o ambiente virtual também
    Para evitar isso siga os passos:
    6.1 Pressione (Ctrl+Shift+P)
    6.2 Selecione ( Python: Create Enviroment... )
    6.3 Selecione ( Venv )
    6.4 Selecione ( Use Existing )

# COMO USAR O CÓDIGO

# 1 - Instalção
    * Python 
    * Extenção "Live Preview" by Microsoft no VSCode
# 2 - Executar backend
    2.1 ativar o ambiente virtual
    2.2 executar o server.py
# 3 - Abrir o index
    3.1 - Clique com botão direito no index.html
    3.2 - Selecione "Show Preview"
    3.3 (opcional) - Copie a URL da janela que o Show Preview mostra e cole no navegador para melhor visibilidade
    3.4 - Pode fechar a janela do 'Show Preview' no VsCode

Estrutura salva no csv
| id | titulo | arquivo-video | arquivo-pdf | desc | status |