```markdown
# Django API Web

Esse é a atividade 2 do professor André, da disciplina de Banco de Dados, cujo objetivo é fazer uma API Web utilizando a tecnologia escolhida pelo grupo.
O meu grupo escolheu Django.

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados em seu sistema:

- Python 3.x
- pip (Python package installer)
- virtualenv (opcional, mas recomendado)

## Instalação

Siga os passos abaixo para configurar e rodar o projeto localmente.

### 1. Clonar o repositório

```bash
git clone https://github.com/felipequentino/bdAtividade-Joao-Felipe-Quentino.git
cd seu-repositorio
```

### 2. Criar um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o banco de dados

Crie e aplique as migrações do banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Rodar o servidor de desenvolvimento

Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```
A API estará disponível em `http://127.0.0.1:8000/api/usuarios/`.

## Estrutura do Projeto

- `bdAtividade/`: Diretório principal do projeto Django.
- `bdApp/`: Aplicativo Django com o modelo `Usuario`.
- `manage.py`: Script para executar comandos administrativos do Django.
