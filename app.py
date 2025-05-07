# Importa o Flask e a função para renderizar arquivos HTML
from flask import Flask, render_template, request, redirect, url_for

# Cria a aplicação Flask
app = Flask(__name__)

# Rota principal: quando você acessa "/", mostra a index.html
@app.route("/")
def index():
    return render_template("index.html")  # Renderiza a página inicial

# Rota para a página de cuidados: acessível por "/cuidados"
@app.route("/cuidados")
def cuidados():
    return render_template("cuidados.html")  # Renderiza a página de cuidados

@app.route("/primeiros_cuidados")
def primeiros_cuidados():
    return render_template("primeiros_cuidados.html") # Renderiza a página de primeiros cuidados

@app.route("/alimentacao")
def alimentacao():
    return render_template("alimentacao.html") # Renderiza a página de primeiros cuidados

@app.route("/higiene")
def higiene():
    return render_template("higiene.html") # Renderiza a página de primeiros cuidados

@app.route("/saude")
def saude():
    return render_template("saude.html")

@app.route("/entretenimento")
def entretenimento():
    return render_template("entretenimento.html")

# Executa o servidor Flask em modo de desenvolvimento
if __name__ == "__main__":
    app.run(debug=True)