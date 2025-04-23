import sqlite3

# Função para criar um usuário padrão
def criar_usuario_inicial():
    conn = sqlite3.connect("financeiro.db")
    cursor = conn.cursor()

    # Adicionar usuário padrão
    cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", ("admin", "1234"))

    conn.commit()
    conn.close()

    print("Usuário inicial criado com sucesso!")

# Executar a função
criar_usuario_inicial()