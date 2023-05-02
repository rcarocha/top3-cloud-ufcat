import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    html = "<html><body><h2>Programa de Teste de Aplicação na Nuvem</h2>Computação em Nuvem: <img src=\"https://i.redd.it/ue5crvrqes001.jpg\"></body></html>"
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
