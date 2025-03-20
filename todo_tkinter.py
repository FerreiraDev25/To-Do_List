import json
import os
import tkinter as tk
from tkinter import messagebox

# Nome do arquivo JSON para armazenar as tarefas
ARQUIVO_TAREFAS = "tarefas.json"

# Função para carregar tarefas do arquivo JSON
def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, 'r') as arquivo:
            return json.load(arquivo)
    return []

# Função para salvar tarefas no arquivo JSON
def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

# Função para atualizar a lista exibida na interface gráfica
def atualizar_lista():
    listbox_tarefas.delete(0, tk.END)  # Limpa a lista
    for i, tarefa in enumerate(tarefas):
        status = "✔" if tarefa["concluida"] else "❌"
        listbox_tarefas.insert(tk.END, f"{i+1}. {status} {tarefa['descricao']}")

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    descricao = entrada_tarefa.get().strip()
    if descricao:
        tarefas.append({"descricao": descricao, "concluida": False})
        salvar_tarefas(tarefas)
        atualizar_lista()
        entrada_tarefa.delete(0, tk.END)  # Limpa o campo de entrada
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa válida!")

# Função para marcar uma tarefa como concluída
def concluir_tarefa():
    try:
        indice = listbox_tarefas.curselection()[0]  # Obtém o índice selecionado
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
        atualizar_lista()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para concluir.")

# Função para excluir uma tarefa
def excluir_tarefa():
    try:
        indice = listbox_tarefas.curselection()[0]  # Obtém o índice selecionado
        del tarefas[indice]
        salvar_tarefas(tarefas)
        atualizar_lista()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para excluir.")

# Carregar as tarefas do arquivo JSON ao iniciar
tarefas = carregar_tarefas()

# Criando a Janela Principal
root = tk.Tk()
root.title("To-Do List com Tkinter")
root.geometry("400x500")
root.configure(bg="#f4f4f4")

# Widget de Entrada para Nova Tarefa
entrada_tarefa = tk.Entry(root, width=40)
entrada_tarefa.pack(pady=10)

# Botão de Adicionar Tarefa
btn_adicionar = tk.Button(root, text="Adicionar", command=adicionar_tarefa, bg="#4CAF50", fg="white")
btn_adicionar.pack(pady=5)

# Lista de Tarefas (Listbox)
listbox_tarefas = tk.Listbox(root, width=50, height=15)
listbox_tarefas.pack(pady=10)

# Botões para Concluir e Excluir Tarefas
btn_concluir = tk.Button(root, text="Concluir", command=concluir_tarefa, bg="#2196F3", fg="white")
btn_concluir.pack(pady=5)

btn_excluir = tk.Button(root, text="Excluir", command=excluir_tarefa, bg="#F44336", fg="white")
btn_excluir.pack(pady=5)

# Carregar as tarefas ao iniciar o programa
atualizar_lista()

# Rodar a interface gráfica
root.mainloop()
