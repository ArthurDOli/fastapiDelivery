# FastAPI Delivery API

A FastAPI Delivery API é uma API REST desenvolvida em Python com FastAPI, projetada para gerir um sistema de pedidos. A aplicação serve como um backend completo para uma plataforma de delivery ou e-commerce, incluindo autenticação de utilizadores, gestão de permissões e um fluxo completo de criação e manipulação de pedidos.

## Funcionalidades

- **Autenticação Segura com JWT:** Sistema completo de criação de contas, login e logout utilizando JWT para proteger as rotas. Inclui tokens de acesso e de atualização.
- **Controlo de Acesso por Função:** Distinção clara entre utilizadores comuns e administradores. Rotas críticas, como a listagem de todos os pedidos, são restritas a administradores.
- **Gestão Completa de Pedidos:** Operações CRUD (Create, Read, Update, Delete) para pedidos, permitindo criar, cancelar, finalizar e visualizar pedidos.
- **Manipulação de Itens:** Adicione e remova itens de um pedido existente, com o cálculo automático do preço total.
- **Validação de Dados:** Utilização de Pydantic para definir schemas de dados, garantindo que todas as requisições e respostas da API sejam consistentes e válidas.

## Tecnologias Utilizadas

- **Backend:** Python, FastAPI
- **Banco de Dados:** SQLite, SQLAlchemy

## Instalação e Configuração

Siga os passos abaixo para configurar e executar o projeto localmente:

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/ArthurDOli/fastapiDelivery.git](https://github.com/ArthurDOli/fastapiDelivery.git)
    cd fastapiDelivery
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv .venv
    # No Windows
    .venv\Scripts\activate
    # No macOS/Linux
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**

    Instale as dependências com:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Crie um ficheiro `.env` na raiz do projeto e adicione as seguintes variáveis. Pode gerar uma chave secreta forte para `SECRET_KEY`.

    ```
    SECRET_KEY=sua_chave_secreta_
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

5.  **Crie e atualize a base de dados com o Alembic:**
    Este comando irá ler os ficheiros de migração e criar o ficheiro `banco.db` com todas as tabelas necessárias.

    ```bash
    alembic upgrade head
    ```

6.  **Execute a aplicação:**
    ```bash
    uvicorn main:app --reload
    ```
    A API estará disponível em `http://127.0.0.1:8000`, e a documentação interativa em `http://127.0.0.1:8000/docs`.

## Estrutura do Projeto

```bash
fastapiDelivery/
├── alembic/
│   └── ...
├── .gitignore
├── alembic.ini
├── auth_routes.py
├── dependencies.py
├── main.py
├── models.py
├── order_routes.py
├── schemas.py
├── security.py
└── README.md
```
