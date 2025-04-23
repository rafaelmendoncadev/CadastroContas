import sqlite3

def listar_transacoes():
    conn = sqlite3.connect("financeiro.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transacoes")
    transacoes = cursor.fetchall()

    conn.close()

    return transacoes