import sqlite3

def cadastrar_transacao(tipo, descricao, valor, data):
    conn = sqlite3.connect("financeiro.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO transacoes (tipo, descricao, valor, data) VALUES (?, ?, ?, ?)", 
                   (tipo, descricao, valor, data))

    conn.commit()
    conn.close()

    print("Transação registrada com sucesso!")