
class Task:
  def __init__(self, id, title, description, completed=False) -> None:
    self.id = id
    self.title = title
    self.description = description
    self.completed = completed
    
  # Criaremos uma método de retorno (Vai retornar as informações armazenadas, em forma de dicionário)
  def to_dict(self):
    return{
      "id": self.id,
      "title": self.title,
      "description": self.description,
      "completed": self.completed
    }