# ControlVet Backend

## Descrição
ControlVet Backend é uma API RESTful que fornece endpoints para gerenciar dados de uma clínica veterinária, como informações dos pacientes.

## Recursos
- Criar, ler, atualizar e excluir informações de pacientes
- Agendar e gerenciar consultas
- Registrar e recuperar prontuários médicos

## Tecnologias Utilizadas
- Python
- Flask (Framework web em Python)
- MySQL (Sistema de gerenciamento de banco de dados relacional)
- Swagger (Documentação da API)

## Instalação
1. Clone o repositório:
git clone https://github.com/seu-usuário/controlvet-backend.git


2. Crie um ambiente virtual:
cd controlvet-backend
python3 -m venv venv


3. Ative o ambiente virtual:
- No Windows:
  ```
  venv\Scripts\activate
  ```
- No macOS e Linux:
  ```
  source venv/bin/activate
  ```

4. Instale as dependências:
pip install -r requirements.txt


5. Configure o banco de dados MySQL:
Certifique-se de ter o MySQL instalado e em execução.
Crie um novo banco de dados para o aplicativo.
Atualize a configuração do banco de dados no arquivo app.py com os detalhes da sua conexão MySQL (host, usuário, senha, banco de dados).
Os scripts para criação do banco de dados se encontram no codigo, nas pasta database.


7. Execute a aplicação:
flask run


8. Acesse a documentação da API:
Abra o navegador da web e acesse http://localhost:5000/apidocs


## Utilização
- Use os endpoints da API para interagir com o backend e realizar operações de CRUD nas informações do pacientes.
- Consulte a documentação da API para obter informações detalhadas sobre cada endpoint e seus formatos de requisição/resposta.


