import pytest, requests

# CRUD
# Aqui inserimos a rota do teste, como nosso arquivo está rodando no servidor local, vamos colocar esse endereço abaixo
BASE_URL = 'http://127.0.0.1:5000'
# Agora toda tarefa que vamos criar, vamos adicionar nessa lista para podermos testa-las (UPDATE, DELETE, GET...)
tasks = []

# CREATE
# Criação da função para testar se o CREATE funciona
def test_create_task():
  # Aqui criamos o variável que vai receber os dados da task nova
  new_task_data = {
    "title": "Nova tarefa",
    "description": "Descrição da nova tarefa"
    }
  # Aqui criamos uma variável, que vai armazenar o resultado do request de post que fizemos, validando ele ou não
  # Request.post é a função que vamos utilizar
  # BASE_URL é o local pra onde isso vai ser enviado (Essa é a rota do postman)
  # Json=new_task_data é o valor que vai ser enviado no post
  response = requests.post(f'{BASE_URL}/tasks', json=new_task_data)
  # Assert é o método que o pytest usa para verificar se os valores batem
  # Response.status_code == 200, verifica se o test é sucedido (200 é o valor de confirmação)
  assert response.status_code == 200
  # Agora com o response_json vamos recuperar a resposta do servidor, incluindo o ID. (Vai ser o corpo do retorno).
  response_json = response.json()
  # Agora verificamos se o programa retorna a mensagem de sucesso
  assert "message" in response_json
  # E também verificamos se o programa retorna o ID.
  assert "id" in response_json
  # Agora vamos adicionar esse ID da task nova dentro da list da tasks.
  tasks.append(response_json['id'])
  
# READ
  
# Agora criaremos um teste para criar todas as funções
def test_get_tasks():
  response = requests.get(f'{BASE_URL}/tasks')
  # Não precisamos passar nenhum json, pois a requisição não têm nenhum corpo
  assert response.status_code == 200
  response_json = response.json()
  assert 'tasks'in response_json
  assert 'total_tasks' in response_json
  
# Agora para validar a tarefa específica, precisamos garantir que a tarefa exista
def test_get_task():
  if tasks:
    task_id = tasks[0]
    response = requests.get(f'{BASE_URL}/tasks/{task_id}')
    assert response.status_code == 200
    response_json = response.json()
    assert task_id == response_json['id']
    

#UPDATE

# Criaremos uma função para testar a atualização
# Criaremos uma requisição para nosso endpoint de atualização
# Pra isso precisamos já ter uma atividade cadastrada
def test_update_task():
  # Como já criamos a atividade anteriormente, só vamos usar ela
  if tasks: # Checa se existe algo dentro da lista tasks
    task_id = tasks[0] # Pegamos a primeira atividade existente na lista e enviamos uma requisição PUT
    # Pra isso utilizamos uma PAYLOAD
    payload = {
      "completed": True,
      "description": "Nova descrição",
      "id": 1, # NÃO PODEMOS ATUALIZAR ID
      "title": "Título atualizado",
    }
    response = requests.put(f'{BASE_URL}/tasks/{task_id}', json=payload)
    response.status_code == 200
    response_json = response.json()
    assert "message"in response_json
    
    # Automatizando o test
    # Nova requisição a tarefa específica
    task_id = tasks[0]
    response = requests.get(f'{BASE_URL}/tasks/{task_id}')
    assert response.status_code == 200
    response_json = response.json()
    # Agora verificamos se as infos da resposta, são as mesmas que enviamos para a API
    # Provando que a atualização funcionou
    assert response_json['title'] == payload['title']
    assert response_json['description'] == payload['description']
    assert response_json['completed'] == payload['completed']
    
    
# DELETE

def test_delete_task():
  if tasks:
    task_id = tasks[0]
    response = requests.delete(f'{BASE_URL}/tasks/{task_id}')
    response.status_code == 200
    
    # Agora para verificar que o DELETE foi executado
    response = requests.get(f'{BASE_URL}/tasks/{task_id}')
    # Para verificar se o DELETE funcionou, basta ver se o response retorna um erro quando fazemos um get da tarefa
    assert response.status_code == 404