from flask import Flask 

app = Flask(__name__) 

produto = {
    "prego":"14",
    "martelo":"35",
    "furadeira":"12"
}

@app.route("/")  
def homepage():
    return '''
    <h1>Bem vindo ao TechFix</h1>
    <a href="/produtos">Ir para a página de Produtos</a>
    '''

@app.route("/produtos")  
def produtos():
    return produto

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")