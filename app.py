from flask import Flask, jsonify, request
from database import criar_tabela, inserir_carta, listar_cartas, deletar_carta

app = Flask(__name__)

criar_tabela()

@app.post("/cartas")
def criar_carta():
    dados = request.json
    inserir_carta(
        dados["texto"],
        dados["emissario"]
    )

    return jsonify({
        "mensagem": "Carta criada"
    }), 201


@app.get("/cartas")
def pegar_cartas():
    cartas = listar_cartas()

    return jsonify(cartas)


@app.delete("/cartas/<int:id>")
def apagar_carta(id):
    deletar_carta(id)

    return jsonify({
        "mensagem": "Carta deletada"
    })


if __name__ == "__main__":
    app.run(debug=True)

