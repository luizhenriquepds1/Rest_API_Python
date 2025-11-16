# Rest_API_Python: API de Estudo com Python e FastAPI

## 📚 Sobre o Projeto

Este repositório contém uma **API RESTful** desenvolvida em **Python** utilizando o *framework* **FastAPI**. O projeto foi criado com o objetivo principal de servir como um ambiente de **estudo e aprendizado** sobre o desenvolvimento de APIs modernas, cobrindo tópicos essenciais como:

*   Estrutura de projeto com FastAPI.
*   Definição de rotas e *endpoints*.
*   Modelagem de dados e persistência com **SQLAlchemy**.
*   Gerenciamento de migrações de banco de dados com **Alembic**.
*   Separação de lógica em módulos (`auth_routes.py`, `order_routes.py`, `models.py`).

## 🛠️ Tecnologias Utilizadas

O projeto utiliza as seguintes tecnologias principais:

| Tecnologia | Descrição |
| :--- | :--- |
| **Python** | Linguagem de programação principal. |
| **FastAPI** | *Framework* web de alta performance para construção de APIs. |
| **SQLAlchemy** | Kit de ferramentas SQL e Mapeador Objeto-Relacional (ORM) para interagir com o banco de dados. |
| **Alembic** | Ferramenta de migração de banco de dados para SQLAlchemy. |
| **SQLite** | Banco de dados leve utilizado para desenvolvimento (`banco.db`). |

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar a API localmente.

### Pré-requisitos

Certifique-se de ter o **Python 3.8+** instalado em sua máquina.

### 1. Clonar o Repositório

```bash
git clone https://github.com/luizhenriquepds1/Rest_API_Python.git
cd Rest_API_Python
```

### 2. Criar e Ativar o Ambiente Virtual

É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto.

```bash
# Cria o ambiente virtual
python3 -m venv venv

# Ativa o ambiente virtual (Linux/macOS)
source venv/bin/activate

# Ativa o ambiente virtual (Windows)
venv\Scripts\activate
```

### 3. Instalar as Dependências

As dependências necessárias estão listadas no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Executar as Migrações do Banco de Dados

O projeto utiliza o Alembic para gerenciar o esquema do banco de dados.

```bash
# Inicializa o banco de dados e aplica as migrações
alembic upgrade head
```

### 5. Iniciar a API

Utilize o `uvicorn` para rodar o servidor da FastAPI.

```bash
uvicorn main:app --reload
```

A API estará acessível em `http://127.0.0.1:8000`.

## 📄 Documentação da API

O FastAPI gera automaticamente a documentação interativa da API. Após iniciar o servidor, você pode acessá-la nos seguintes *endpoints*:

*   **Swagger UI:** `http://127.0.0.1:8000/docs`
*   **ReDoc:** `http://127.0.0.1:8000/redoc`

## 🗺️ Estrutura do Projeto

A estrutura de arquivos do projeto é organizada da seguinte forma:

```
Rest_API_Python/
├── alembic/                 # Diretório de migrações do Alembic
├── alembic.ini              # Arquivo de configuração do Alembic
├── auth_routes.py           # Rotas relacionadas à autenticação
├── banco.db                 # Banco de dados SQLite (gerado após a primeira execução)
├── main.py                  # Ponto de entrada principal da aplicação FastAPI
├── models.py                # Definições dos modelos de dados (SQLAlchemy)
├── order_routes.py          # Rotas relacionadas a pedidos/ordens
└── requirements.txt         # Lista de dependências do Python
```

## 📝 Rotas Principais (Endpoints)

Com base nos arquivos de rotas, a API provavelmente inclui *endpoints* para:

| Módulo | Funcionalidade Principal |
| :--- | :--- |
| `auth_routes.py` | Cadastro de usuários, login e geração de tokens (Autenticação). |
| `order_routes.py` | Criação, leitura, atualização e exclusão de pedidos (CRUD de Pedidos). |
