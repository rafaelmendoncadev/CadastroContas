import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os

# Função para criar o banco de dados e as tabelas, caso não existam
def criar_banco():
    if not os.path.exists("banco.db"):
        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()

        # Criar a tabela Usuario
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuario (
            ID INTEGER PRIMARY KEY,
            Nome TEXT NOT NULL,
            Senha TEXT NOT NULL
        )
        """)

        # Criar a tabela Tipo
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Tipo (
            ID INTEGER PRIMARY KEY,
            Descricao TEXT NOT NULL
        )
        """)

        # Criar a tabela Contas
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Contas (
            ID INTEGER PRIMARY KEY,
            Descricao TEXT NOT NULL,
            Tipo INTEGER NOT NULL,
            Valor REAL NOT NULL,
            DataVencimento DATE NOT NULL,
            UsuarioID INTEGER NOT NULL,
            FOREIGN KEY (Tipo) REFERENCES Tipo(ID),
            FOREIGN KEY (UsuarioID) REFERENCES Usuario(ID)
        )
        """)

        # Inserir o usuário padrão "Admin"
        cursor.execute("""
        INSERT INTO Usuario (Nome, Senha)
        VALUES (?, ?)
        """, ("admin", "admin"))

        conn.commit()
        conn.close()
        print("Banco de dados criado com sucesso!")
    else:
        print("Banco de dados já existe.")

# Função para verificar login
def verificar_login():
    nome = entrada_nome.get()
    senha = entrada_senha.get()

    # Conectar ao banco de dados banco.db
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    # Verificar se o usuário existe no banco
    cursor.execute("SELECT * FROM Usuario WHERE Nome = ? AND Senha = ?", (nome, senha))
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        messagebox.showinfo("Login", "Login bem-sucedido!")
        # Aqui você pode chamar a próxima tela
    else:
        messagebox.showerror("Erro", "Nome ou senha inválidos!")

# Criar o banco de dados, se necessário
criar_banco()

# Configurar a janela principal
janela = tk.Tk()
janela.title("Sistema Financeiro - Login")
janela.geometry("400x300")  # Define o tamanho fixo da janela
janela.resizable(False, False)

# Centralizar a janela na tela
largura_janela = 400
altura_janela = 300

# Obter dimensões da tela do usuário
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calcular posição para centralizar a janela
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)

# Aplicar a posição
janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# Frame principal com centralização
frame = ttk.Frame(janela, padding="20")
frame.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o conteúdo dentro da janela

# Título
titulo = ttk.Label(frame, text="Login", font=("Arial", 18, "bold"))
titulo.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Nome de usuário
ttk.Label(frame, text="Nome:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entrada_nome = ttk.Entry(frame, width=30)
entrada_nome.grid(row=1, column=1, pady=5)

# Senha
ttk.Label(frame, text="Senha:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entrada_senha = ttk.Entry(frame, show="*", width=30)
entrada_senha.grid(row=2, column=1, pady=5)

# Botão de login
botao_login = ttk.Button(frame, text="Entrar", command=verificar_login)
botao_login.grid(row=3, column=0, columnspan=2, pady=15)

# Rodapé
rodape = ttk.Label(janela, text="© 2025 Sistema Financeiro", font=("Arial", 9), anchor="center")
rodape.place(relx=0.5, rely=0.95, anchor="center")  # Centraliza o rodapé

janela.mainloop()