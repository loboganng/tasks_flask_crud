

from flask import Flask, request, jsonify
from Models.task import Task    # Precisamos importar a classe e método, da outra pasta
app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete
# Tabela: Tarefa


# Para iniciar a gestão desses dados, vamos utilizar uma lista.
# Vamos organizar as tarefas através de classes (Dentro do arquivo tasks.py)
tasks = []    # Vamos armazenar as tarefas aqui dentro (Enquanto não temos um banco de dados)
task_id_control = 1   # Precisa ser criada fora da função para manter o controle do ID


@app.route('/tasks', methods=['POST'])
# Criaremos uma função que será responsável pela criação de atividades
def create_task():
  global task_id_control    # Faz com que a função consiga acessar uma variável fora do seu escopo.
  data = request.get_json()   # Esse método vai recuperar o que o cliente enviou, e atribuir a variável "Data"
  new_task = Task(id=task_id_control ,title=data['title'], description=data.get("description", ""))
  task_id_control += 1
  tasks.append(new_task)
  print(tasks)
  return jsonify({"message": "Nova tarefa criada com sucesso. ", "id": new_task.id}), 200   # Vai transformar o retorno e JSON (padrão de retorno para API/CRUD)

@app.route('/tasks', methods=['GET'])
def get_tasks():
  # Maneira 1: Mais trabalhosa
  # task_list = []
  # for task in tasks:
  #   task_list.append(task.to_dict())
  
  #Maneira 2: Mais prático e rápido
  task_list = [task.to_dict() for task in tasks]
  
  output = {
    "tasks": task_list,
    "total_tasks": len(task_list)
  }
  return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
  task = None
  for t in tasks:   # T é CADA atividade dentro do tasks. 
    if t.id == id:
      return jsonify(t.to_dict())
  return jsonify ({"message": "Não foi possível encontrar a atividade. "}), 404  # Como estamos retornando um erro, usamos o 404.
  # Precisamos retornar a mensagem de erro como um {dicionário}. 
  
@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):
  task = None
  for t in tasks:
    if t.id == id:
      task = t
  print(task)
  if task == None:
    return jsonify({"message": "Não foi possível encontrar a atividade. "}), 404
  
  data = request.get_json()
  task.title = data['title']
  task.description = data['description']
  task.completed = data['completed']
  print(task)
  return jsonify({"message": "Tarefa atualizada com sucesso. "})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
  task = None
  for t in tasks:
    print(t)
    if t.id == id:
      task = t
      break
      
  if not task:
    return jsonify({"message": "Não foi possível encontrar a atividade. "}), 404
  
  tasks.remove(task)
  return jsonify({"message": "Tarefa deletada com sucesso. "})


if __name__ == '__main__':
  app.run(debug=True)
