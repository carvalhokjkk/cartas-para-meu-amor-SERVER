from flask import Flask, jsonify, request
from database import criar_tabela, inserir_carta, listar_cartas, deletar_carta, USUARIOS

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



@app.get("/login")
def login():
    usuario_fornecido  = request.args.get('user')
    senha_fornecida  = request.args.get('senha')
    print(request.args)

    if usuario_fornecido in USUARIOS:
        if USUARIOS[usuario_fornecido] == senha_fornecida:
            return jsonify({'usuario': usuario_fornecido, 'erro': 'OK'})
        else:
            return jsonify({'usuario': usuario_fornecido, 'erro': 'SENHA INCORRETA'})
    else:
        return jsonify({'usuario': usuario_fornecido, 'erro': 'USUARIO NAO ENCONTRADO'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
