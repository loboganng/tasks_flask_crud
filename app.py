

# Inicialmente precisamos importar a biblioteca do Flask
from flask import Flask

# Agora para a criação do aplicativo, devemos criar uma variável e utilizamos a Classe Flask() 
app = Flask(__name__) # Dentro dessa classe passamos uma variável que geralmente é NAME, e é o nome do arquivo.
# Se executarmos de forma manual a inserção do nome do arquivo, ele vai ter o nome de MAIN
# __name__ = "main"   -   Assim sabemos que isso está sendo implantado manualmente, e não por algum outro arquivo, através de importação

# Agora criaremos uma ROTA, onde vamos poder nos comunicar com outros clientes e usuários.
# A Primeira rota que vamos criar vai ser um 'Hello, World!', que vai retornar no formato HTML.

# Como vai ser a rota padão, usamos só a /
@app.route('/')
# Agora criaremos o que vai ser executado quando alguém acessar essa rota, então vamos criar uma função pra isso.
def hello_world():
  return 'Hello, world!'

# Da mesma maniera podemos criar outras rotas.
@app.route('/about')
def about():
  return 'Página sobre'

# Lembrando que quando executamos o __name__ de forma manual, recebemos ele como main
# Agora se comparar-mos os dois
# utilizamos o método a seguir SOMENTE para desenvolvimento LOCAL.
if __name__ == '__main__':
  app.run(debug=True)   # O método debug vai nos permitir ver informações úteis pra entender o que está acontecendo nesse servidor web.
  
  
  # Pra acessar o servidor criado basta digitar o endereço gerado no Terminal no nosso navegador. (http://127.0.0.1:5000), esse é o servidor padrão.
  # Pra acessar a nova rota que criamos (about), basta acessar o servidor + o endereço da rota nova (http://127.0.0.1:5000/about)
  
  # Sempre que receber-mos alguma requisição nesse servidor, se tiver-mos o modo debug ligado, isso vai gerar m registro. 