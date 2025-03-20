import json
import os

#Carregar tarefas do arquivo JSON
def carregar_tarefas():
    if os.path.exists("tarefas.json"):
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)

    return[]

#Salvar tarefas no arquivo JSON
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

#Adicionar uma tarefa
def adicionar_tarefa(tarefas, descricao):
    tarefa = {
        'descricao': descricao,
        'concluida': False
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print(f'Tarefa "{descricao}" adicionada.')

#Adicionar para listar tarefas
def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print('Nenhuma tarefa encontrada.')
        return
    print('\nLista de Tarefas:')
    for i, tarefa in enumerate(tarefas, 1):
        status = "Concluída" if tarefa['concluida'] else "Pendente"
        print(f"{i}. {tarefa['descricao']} - {status}")

#Marcar uma tarefa com concluída
def concluir_tarefa(tarefas, indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]['concluída'] = True
        salvar_tarefas(tarefas)
        print(f'Tarefa {indice+1} marcada como concluída.')
    else:
        print('Indice inválido.')

#Excluir uma tarefa
def excluir_tarefa(tarefas, indice):
    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        salvar_tarefas(tarefas)
        print(f"Tarefa '{tarefa_removida['descricao']}' excluída.")
    else:
        print('Indice inválido.')

#Exibir menu
def menu():
    tarefas = carregar_tarefas()

    while True:
        print('\n1. Adicionar Tarefa')
        print('2. Listar Tarefas')
        print('3. Concluir Tarefa')
        print('4. Excluir Tarefa')
        print('5. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            descricao = input('Digite a descrição da tarefa: ')
            adicionar_tarefa(tarefas, descricao)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            listar_tarefas(tarefas)
            try:
                indice = int(input('Digite o número da tarefa a ser concluída: ')) -1
                concluir_tarefa(tarefas, indice)
            except ValueError:
                print('Por favor, insira um número válido.')
        elif opcao == '4':
            listar_tarefas(tarefas)
            try:
                indice = int(input('Digite o número da tarefa a ser exclúida: ')) -1
                excluir_tarefa(tarefas, indice)
            except ValueError:
                print('Por favor, insira um número válido.')
        elif opcao == '5':
            print('Saindo...')
            break
        else:
            print('Opção inválida, tente novamente.')

if __name__ == '__main__':
    menu()
