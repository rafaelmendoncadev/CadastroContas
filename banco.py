import sqlite3

# Conectar ao banco (cria o arquivo se não existir)
conn = sqlite3.connect("financeiro.db")
cursor = conn.cursor()

# Criar tabela de usuários
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL
    )
''')

# Criar tabela de transações
cursor.execute('''
    CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL,  -- "pagar" ou "receber"
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        data TEXT NOT NULL
    )
''')

# Salvar e fechar conexão
conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")