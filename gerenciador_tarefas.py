"""
Módulo principal do Sistema Gerenciador de Tarefas (To-Do List).

Este módulo contém toda a lógica para adicionar, listar, atualizar e
excluir tarefas, utilizando conceitos de programação funcional.
"""
from typing import List, Dict, Any, Callable

# Tipagem para melhor legibilidade
Tarefa = Dict[str, Any]
ListaDeTarefas = List[Tarefa]

def gerador_de_id() -> Callable[[], int]:
    """
    Cria um gerador de IDs sequenciais para as tarefas.

    Conceito: Closure.
    A função interna 'proximo_id' "lembra" do estado da variável
    'ultimo_id' da função externa, mesmo após a execução de
    gerador_de_id ter terminado.
    """
    ultimo_id = 0
    def proximo_id() -> int:
        nonlocal ultimo_id
        ultimo_id += 1
        return ultimo_id
    return proximo_id

def adicionar_tarefa(tarefas: ListaDeTarefas, descricao: str, gerador_id: Callable[[], int]) -> ListaDeTarefas:
    """
    Adiciona uma nova tarefa à lista. Retorna uma nova lista com a tarefa adicionada.
    Mapeamento: RF01
    """
    if not isinstance(descricao, str) or not descricao.strip():
        raise ValueError("A descrição da tarefa não pode ser vazia.")

    nova_tarefa = {
        "id": gerador_id(),
        "descricao": descricao,
        "concluida": False
    }
    # Retorna uma nova lista, mantendo a imutabilidade da original
    return tarefas + [nova_tarefa]

def excluir_tarefa(tarefas: ListaDeTarefas, id_tarefa: int) -> ListaDeTarefas:
    """
    Exclui uma tarefa da lista com base no seu ID.
    Retorna uma nova lista sem a tarefa especificada.
    Mapeamento: RF04
    """
    tarefa_encontrada = any(t['id'] == id_tarefa for t in tarefas)
    if not tarefa_encontrada:
        raise ValueError(f"Tarefa com ID {id_tarefa} não encontrada.")

    return [tarefa for tarefa in tarefas if tarefa['id'] != id_tarefa]

def atualizar_tarefa(tarefas: ListaDeTarefas, id_tarefa: int, atualizador: Callable[[Tarefa], Tarefa]) -> ListaDeTarefas:
    """
    Atualiza uma tarefa específica usando uma função de atualização.
    Retorna uma nova lista com a tarefa modificada.

    Conceito: Função de Alta Ordem (High-Order Function).
    Esta função recebe outra função, 'atualizador', como argumento.
    Mapeamento: RF03
    """
    tarefa_encontrada = any(t['id'] == id_tarefa for t in tarefas)
    if not tarefa_encontrada:
        raise ValueError(f"Tarefa com ID {id_tarefa} não encontrada.")

    return [atualizador(t) if t['id'] == id_tarefa else t for t in tarefas]

def marcar_como_concluida(tarefa: Tarefa) -> Tarefa:
    """Função auxiliar para ser usada com 'atualizar_tarefa'."""
    return {**tarefa, 'concluida': True}

def filtrar_tarefas(tarefas: ListaDeTarefas, criterio: Callable[[Tarefa], bool]) -> ListaDeTarefas:
    """
    Filtra a lista de tarefas com base em um critério (função).

    Conceito: Função de Alta Ordem (High-Order Function).
    Recebe 'criterio' como uma função que retorna True ou False.
    Mapeamento: RF05
    """
    return [tarefa for tarefa in tarefas if criterio(tarefa)]

def formatar_tarefas_para_exibicao(tarefas: ListaDeTarefas) -> List[str]:
    """
    Formata a lista de tarefas para uma exibição amigável.

    Conceito: List Comprehension.
    Usada para transformar a lista de dicionários em uma lista de strings
    de forma declarativa e concisa.
    Mapeamento: RF02
    """
    return [
        f"[{'X' if t['concluida'] else ' '}] ID: {t['id']} - {t['descricao']}"
        for t in tarefas
    ]

def main():
    """Função principal para interação com o usuário."""
    minhas_tarefas = []
    gerador_id = gerador_de_id()

    # Exemplo de uso
    print("Bem-vindo ao Gerenciador de Tarefas Funcional!")

    # Adicionando tarefas (RF01)
    minhas_tarefas = adicionar_tarefa(minhas_tarefas, "Estudar Programação Funcional", gerador_id)
    minhas_tarefas = adicionar_tarefa(minhas_tarefas, "Fazer o trabalho da faculdade", gerador_id)
    minhas_tarefas = adicionar_tarefa(minhas_tarefas, "Comprar pão", gerador_id)

    # Listando todas as tarefas (RF02)
    print("\n--- Todas as Tarefas ---")
    for tarefa_formatada in formatar_tarefas_para_exibicao(minhas_tarefas):
        print(tarefa_formatada)

    # Marcando uma tarefa como concluída (RF03)
    print("\nMarcando tarefa ID 1 como concluída...")
    minhas_tarefas = atualizar_tarefa(minhas_tarefas, 1, marcar_como_concluida)
    
    print("\n--- Todas as Tarefas (Atualizado) ---")
    for tarefa_formatada in formatar_tarefas_para_exibicao(minhas_tarefas):
        print(tarefa_formatada)

    # Filtrando tarefas concluídas (RF05 com Lambda)
    print("\n--- Apenas Tarefas Concluídas ---")
    tarefas_concluidas = filtrar_tarefas(minhas_tarefas, lambda t: t['concluida'] is True)
    for tarefa_formatada in formatar_tarefas_para_exibicao(tarefas_concluidas):
        print(tarefa_formatada)

    # Filtrando tarefas pendentes (RF05 com Lambda)
    print("\n--- Apenas Tarefas Pendentes ---")
    tarefas_pendentes = filtrar_tarefas(minhas_tarefas, lambda t: t['concluida'] is False)
    for tarefa_formatada in formatar_tarefas_para_exibicao(tarefas_pendentes):
        print(tarefa_formatada)

    # Excluindo uma tarefa (RF04)
    print("\nExcluindo tarefa ID 3...")
    minhas_tarefas = excluir_tarefa(minhas_tarefas, 3)

    print("\n--- Lista Final de Tarefas ---")
    for tarefa_formatada in formatar_tarefas_para_exibicao(minhas_tarefas):
        print(tarefa_formatada)

if __name__ == "__main__":
    main()