from flask import Flask 

app = Flask(__name__) 

livro = {
    "1984": 5,
    "Dom Casmurro": 18,
    "O Senhor dos Anéis": 34,
    "Harry Potter e a Pedra Filosofal": 3,
    "A Revolução dos Bichos": 8
}

autor = {
    "George Orwell": 46,  
    "Machado de Assis": 61, 
    "J.R.R. Tolkien": 81,  
    "J.K. Rowling": 58  
}

cliente = {
    "Carlos": 3,
    "Ana": 5,
    "Pedro": 2,
    "Mariana": 4,
    "Lucas": 1
}

@app.route("/")
def homepage():
    return '''
    <h1>Bem vindo a nossa livraria</h1>
    <a href="/livros">Ir para a página de Livros</a>
    <h1>   </h1>
    <a href="/autores">Ir para a página de Autores</a>
    <h1>   </h1>
    <a href="/clientes">Ir para a página de Clientes</a>
    '''

@app.route("/livros")  
def livros():
    return livro

@app.route("/autores")  
def autores():
    return autor

@app.route("/clientes")  
def cliente():
    return autor

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")