from flask import Flask #importando o flask

app = Flask(__name__) #define o nome do app

@app.route("/")  #usando um decorator para definir a rota do APP
def hello_world():
    return "<h1>TESTE DA AULINHA</h1>"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")