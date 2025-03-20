Funções principais(todo.py):

carregar_tarefas(): Carrega as tarefas do arquivo JSON se ele existir. Caso contrário, retorna uma lista vazia.

salvar_tarefas(): Salva as tarefas no arquivo JSON, garantindo que elas persistam.

adicionar_tarefa(): Adiciona uma nova tarefa à lista.

listar_tarefas(): Exibe todas as tarefas e seu status (concluída ou pendente).

concluir_tarefa(): Marca uma tarefa como concluída, dado seu índice na lista.

excluir_tarefa(): Exclui uma tarefa da lista com base no índice.

menu(): Exibe o menu de opções para o usuário interagir com o programa.


Explicação do Código(todo_tkinter):
✅ O que cada parte faz?
Carrega e salva tarefas no arquivo JSON para manter os dados armazenados.

Interface gráfica com Tkinter, incluindo:

Um campo de entrada (Entry) para adicionar novas tarefas.

Uma lista (Listbox) para exibir as tarefas.

Botões para adicionar, concluir e excluir tarefas.

Funções para manipular tarefas:

adicionar_tarefa(): Adiciona uma nova tarefa.

concluir_tarefa(): Marca uma tarefa como concluída.

excluir_tarefa(): Remove uma tarefa.

atualizar_lista(): Atualiza a exibição das tarefas na lista.

✅ Dicas Extras
As tarefas concluídas são marcadas com um ✔ e as pendentes com um ❌.

As mensagens de erro aparecem com messagebox.showwarning(), para avisar o usuário caso tente realizar ações inválidas.
