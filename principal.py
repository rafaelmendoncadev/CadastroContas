import tkinter as tk
from tkinter import Menu

def cadastrar_usuarios():
    print("Abrir tela de Cadastro de Usuários")

def cadastrar_contas():
    print("Abrir tela de Cadastro de Contas")

def consultar_contas():
    print("Abrir tela de Consulta de Contas")

def realizar_backup():
    print("Realizar Backup")

def sair_sistema():
    janela.destroy()

# Criando a janela principal
janela = tk.Tk()
janela.title("Sistema de Controle de Contas")
janela.geometry("600x400")

# Centralizando a janela na tela
largura_janela = 600
altura_janela = 400
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)
janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# Desabilitando o botão de maximizar
janela.resizable(False, False)

# Criando o menu
menu_principal = Menu(janela)

# Menu Cadastro
menu_cadastro = Menu(menu_principal, tearoff=0)
menu_cadastro.add_command(label="Cadastro de Usuários", command=cadastrar_usuarios)
menu_cadastro.add_command(label="Cadastro de Contas", command=cadastrar_contas)
menu_principal.add_cascade(label="Cadastro", menu=menu_cadastro)

# Menu Consulta
menu_consulta = Menu(menu_principal, tearoff=0)
menu_consulta.add_command(label="Consulta de Contas", command=consultar_contas)
menu_principal.add_cascade(label="Consulta", menu=menu_consulta)

# Menu Backup
menu_backup = Menu(menu_principal, tearoff=0)
menu_backup.add_command(label="Realizar Backup", command=realizar_backup)
menu_principal.add_cascade(label="Backup", menu=menu_backup)

# Adicionando o menu à janela
janela.config(menu=menu_principal)

# Criando botões de atalho
frame_botoes = tk.Frame(janela)
frame_botoes.pack(expand=True)  # Centraliza os botões verticalmente

btn_cadastrar_contas = tk.Button(
    frame_botoes, 
    text="Cadastro de Contas", 
    command=cadastrar_contas, 
    width=25, 
    height=2, 
    bg="#4CAF50",  # Cor de fundo (verde)
    fg="white",    # Cor do texto (branco)
    font=("Arial", 14)  # Tamanho da fonte aumentado
)
btn_cadastrar_contas.pack(pady=10)

btn_consultar_contas = tk.Button(
    frame_botoes, 
    text="Consulta de Contas", 
    command=consultar_contas, 
    width=25, 
    height=2, 
    bg="#2196F3",  # Cor de fundo (azul)
    fg="white",    # Cor do texto (branco)
    font=("Arial", 14)  # Tamanho da fonte aumentado
)
btn_consultar_contas.pack(pady=10)

btn_sair = tk.Button(
    frame_botoes, 
    text="Sair", 
    command=sair_sistema, 
    width=25, 
    height=2, 
    bg="#F44336",  # Cor de fundo (vermelho)
    fg="white",    # Cor do texto (branco)
    font=("Arial", 14)  # Tamanho da fonte aumentado
)
btn_sair.pack(pady=10)

# Loop da aplicação
janela.mainloop()