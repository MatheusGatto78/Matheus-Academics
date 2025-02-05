from flask import Flask, request

app = Flask(__name__) 

livro = {
    "1": "1984",
    "2": "Dom Casmurro",
    "3": "O Senhor dos Anéis",
    "4": "Harry Potter e a Pedra Filosofal",
    "5": "A Revolução dos Bichos"
}

autor = {
    "1": "George Orwell",  
    "2": "Machado de Assis", 
    "3": "J.R.R. Tolkien",  
    "4": "J.K. Rowling" 
}

cliente = {
    "1": "Carlos",
    "2": "Ana",
    "3": "Pedro",
    "4": "Mariana",
    "5": "Lucas"
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

@app.route("/livros", methods=["get"])  
def livros():
    return livro

@app.route("/autores", methods=["get"])  
def autores():
    return autor

@app.route("/clientes", methods=["get"])  
def clientes():
    return cliente

@app.route("/delete_livro/<string:id>", methods=["delete"])
def delete_livro(id):
    print(livro[id])
    print(f"\n\n-->{id}\n\n")
    del livro[id]
    return livro

@app.route("/add_livro", methods=["post"])
def add_livro():
    data = request.get_json()
    print(data)
    livro[f"{len(livro) + 1}"] = data["Titulo"]
    return livro

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")