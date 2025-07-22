# COMO CONFIGURAR O SERVIDOR LOCAL

### 1 Tenha o python instalado na máquina 
     1.1 Baixe o instalador: 
    Windows: https://www.python.org/downloads/windows/
        selecione a versão mais recente
     1.2 Siga os passos instalação
        * Não esqueça de marcar a flag "Add to PATH"

### 2 Abrir o código no VsCode
    O código está salvo no caminho
    S:\Projeto Documentacao html\Doc_Interativo
    Copie e cole na sua área de trabalho

### 3 Criar ambiente virtual
    - Este passo é opcional mas altamente recomendado
    - Mantém o ambiente limpo de outras bibliotecas que poderiam causar conflito na execução do código
    3.1 Abra o terminal do VsCode (Ctrl + J)
        rode o comando: python -m venv nome_do_seu_ambiente
        
        Este comando irá gerar uma pasta com o nome do seu ambiente

    3.2 Ativar o ambiente
        no terminal, rode:
            '.\nome_do_seu_ambiente\Scripts\activate'
            exemplo: 
                '.\.venv\Scripts\activate'
    
    3.3 instalar as bibliotecas necessárias:
        Com o ambiente ativado, rode no terminal:
            pip install -r requirements.txt

### 4 Desativando o ambiente virtual(venv)
    No terminal digite:
        deactivate
    
# COMO USAR O CÓDIGO

### 1 - Instalação
    * Python 
### 2 - Intalação e configuração do Xampp
    2.1 - Acesse o link https://www.apachefriends.org/pt_br/download.html e baixe a versão mais recente;
    2.2 - Ao abrir o xampp, clique em start no Apache e MySQL;

    * Caso não possua o banco de dados do projeto criado:
     1 - Clique em admin do MySQL;
     2 - Na tela do phpMyAdmin clique em novo;
     3 - Insira o nome dataset_tcc_db e escolha a opção utf8mb4_general_tc;
     4 - Ao terminar de criar o banco e selecioná-lo, será possível clicar na opção importar;
     5 - Basta importar o arquivo "dataset_tcc_db.db" disponível na tela inicial do github com os demais arquivos. Clique no botão importar no final da página.
    
    
### 3 - Executar backend
    3.1 ativar o ambiente virtual
    3.2 executar run.py

### 4 - Abrir página
    4.1 - No terminal irá mostrar uma mensagem (Running on http:192.xxx.xxx-xx:8000)
    Copie o link e abra no navegador

# COMO USAR AS BIBLIOTECAS

### OpenCV
    No terminal digite: pip install opencv-python

Estrutura salva no csv
| id | titulo | arquivo-video | arquivo-pdf | desc | status |
