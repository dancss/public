# API de Gerenciamento de Tarefas
# Construção
- Arquivo database.py configurada conexão com Postgres
- Arquivo models.py cria tabela no postgres com id, título e descrição
- Arquivo schemas.py define classes do esquema
- Arquivo crud.py implementa operações de crud
- Arquivo routes.py implenta rotas get, post, get delete tasks
- Arquivo Main conecta chamadas api FastAPI
- 
## Instruções de Instalação
1. Clone o repositório.
2. Instale as dependências.
3. Configure o banco de dados PostgreSQL.

## Executando a Aplicação
```bash
uvicorn app.main:app --reload
```

## Endpoints
- `POST /tasks/`: Cria uma nova tarefa.
- `GET /tasks/`: Retorna todas as tarefas.
- `GET /tasks/{task_id}`: Retorna uma tarefa específica.
- `DELETE /tasks/{task_id}`: Exclui uma tarefa específica.

## Exemplo de Requisição
### Criar Tarefa
```bash
curl -X POST "http://127.0.0.1:8000/tasks/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"title":"Task 1","description":"Description 1"}'
