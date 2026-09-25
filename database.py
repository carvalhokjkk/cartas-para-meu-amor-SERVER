import sqlite3

DATABASE = "cartas.db"


def conectar():
    conexao = sqlite3.connect(DATABASE)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS cartas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL,
            emissario TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def inserir_carta(texto, emissario):
    conexao = conectar()

    conexao.execute(
        "INSERT INTO cartas (texto, emissario) VALUES (?, ?)",
        (texto, emissario)
    )

    conexao.commit()
    conexao.close()


def listar_cartas():
    conexao = conectar()

    cartas = conexao.execute(
        "SELECT * FROM cartas"
    ).fetchall()

    conexao.close()

    return [dict(carta) for carta in cartas]


def deletar_carta(id):
    conexao = conectar()

    conexao.execute(
        "DELETE FROM cartas WHERE id = ?",
        (id,)
    )

    conexao.commit()
    conexao.close()


