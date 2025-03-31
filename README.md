Aplicação Web - CRUD com Flask
Este projeto é uma aplicação web simples que utiliza Flask, Python e CSV para armazenar e gerenciar dados de uma lista de pessoas. A aplicação permite realizar operações básicas de CRUD (Criar, Ler, Atualizar, Excluir) e expõe uma API RESTful para manipulação desses dados.

Funcionalidades
A aplicação oferece as seguintes funcionalidades:

Criar - Adicionar novos dados (nome e idade).

Ler - Obter todos os dados cadastrados.

Atualizar - Modificar a idade de uma pessoa através do nome.

Deletar - Remover uma pessoa com base no nome.

Tecnologias Utilizadas
Flask: Framework para criar a API RESTful.

Pandas: Para manipulação e leitura do arquivo CSV.

CORS: Habilita requisições entre diferentes origens (permitindo o front-end se comunicar com o back-end sem bloqueios de CORS).

CSV: Armazenamento dos dados em um arquivo CSV.

Estrutura do Projeto
bash
Copy
/Aplicação_Web
    ├── /venv                 # Ambiente virtual do Python
    ├── /app.py               # Código backend (Flask API)
    ├── /Dados.csv            # Arquivo CSV para armazenar os dados
    ├── /requirements.txt     # Dependências do projeto
    ├── /frontend             # Código do front-end (se houver)
Instalação e Execução
Pré-requisitos
Python 3.x instalado.

Endpoints da API
A API possui os seguintes endpoints:

1. GET /dados
Retorna todos os dados armazenados no CSV.
2. POST /dados
Adiciona um novo dado (nome e idade) ao CSV.
3. PUT /dados/<nome>
Atualiza a idade de uma pessoa com o nome fornecido.
4. DELETE /dados/<nome>
Exclui a pessoa com o nome fornecido.

Dependências
Flask==2.0.1

Flask-Cors==3.1.1

pandas==1.3.1
