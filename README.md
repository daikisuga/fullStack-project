# COMO CONFIGURAR O SERVIDOR LOCAL

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
        python run.py

# 5 Desativando o ambiente virtual(venv)
    No terminal digite:
        deactivate

# INSTALANDO BIBLIOTECAS
    - pip install -r requirements.txt
    
# COMO USAR O CÓDIGO

# 1 - Instalção
    * Python 
# 2 - Executar backend
    2.1 ativar o ambiente virtual
    2.2 executar run.py

# 3 - Abrir página
    3.1 - No terminal irá mostrar uma mensagem (Running on http:192.xxx.xxx-xx:8000)
    Copie o link e abra no navegador


Estrutura salva no csv
| id | titulo | arquivo-video | arquivo-pdf | desc | status |
