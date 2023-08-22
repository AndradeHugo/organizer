from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homePage():
    return render_template("home.html")


@app.route("/categorias")
def categorias():
    return render_template("categorias.html")


@app.route("/usuarios/<nomeUsuario>")
def usuarios(nomeUsuario):
    return render_template("usuarios.html", nomeUsuario=nomeUsuario)


if __name__ == "__main__":
    app.run(debug=True)
