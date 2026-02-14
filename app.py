import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/projetos")
def projetos():
    with open("projects.json", "r", encoding="utf-8") as f:
        projects = json.load(f)
    return render_template("projetos.html", projects=projects)


@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        mensagem = request.form["mensagem"]
        print(f"Mensagem recebida de {nome} ({email}): {mensagem}")
        return "Obrigado pelo contato!"
    return render_template("contato.html")


if __name__ == "__main__":
    app.run(debug=True)
