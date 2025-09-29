import unittest
from gerenciador_tarefas import (
    adicionar_tarefa,
    excluir_tarefa,
    atualizar_tarefa,
    marcar_como_concluida,
    filtrar_tarefas,
    formatar_tarefas_para_exibicao,
    gerador_de_id
)

class TestGerenciadorTarefasFuncional(unittest.TestCase):

    def setUp(self):
        """Configura um estado inicial para cada teste."""
        self.gerador_id = gerador_de_id()
        self.tarefas_iniciais = []
        self.tarefas_iniciais = adicionar_tarefa(self.tarefas_iniciais, "Tarefa Teste 1", self.gerador_id)
        self.tarefas_iniciais = adicionar_tarefa(self.tarefas_iniciais, "Tarefa Teste 2", self.gerador_id)

    def test_adicionar_tarefa(self):
        """Testa se uma nova tarefa é adicionada corretamente (RF01)."""
        novas_tarefas = adicionar_tarefa(self.tarefas_iniciais, "Nova Tarefa", self.gerador_id)
        self.assertEqual(len(novas_tarefas), 3)
        self.assertEqual(novas_tarefas[-1]['descricao'], "Nova Tarefa")
        self.assertFalse(novas_tarefas[-1]['concluida'])
        self.assertEqual(novas_tarefas[-1]['id'], 3)

    def test_adicionar_tarefa_com_descricao_vazia(self):
        """Testa se um erro é lançado ao tentar adicionar tarefa com descrição vazia."""
        with self.assertRaises(ValueError):
            adicionar_tarefa(self.tarefas_iniciais, "  ", self.gerador_id)

    def test_excluir_tarefa(self):
        """Testa a exclusão de uma tarefa (RF04)."""
        tarefas_apos_exclusao = excluir_tarefa(self.tarefas_iniciais, 1)
        self.assertEqual(len(tarefas_apos_exclusao), 1)
        # Verifica se a tarefa com ID 1 não existe mais
        ids_restantes = [t['id'] for t in tarefas_apos_exclusao]
        self.assertNotIn(1, ids_restantes)

    def test_excluir_tarefa_inexistente(self):
        """Testa se um erro é lançado ao tentar excluir uma tarefa que não existe."""
        with self.assertRaises(ValueError):
            excluir_tarefa(self.tarefas_iniciais, 99)

    def test_marcar_tarefa_como_concluida(self):
        """Testa a função de marcar uma tarefa como concluída (RF03)."""
        tarefas_atualizadas = atualizar_tarefa(self.tarefas_iniciais, 2, marcar_como_concluida)
        tarefa_modificada = None
        for tarefa in tarefas_atualizadas:
            if tarefa['id'] == 2:
                tarefa_modificada = tarefa
                break
        self.assertIsNotNone(tarefa_modificada)
        self.assertTrue(tarefa_modificada['concluida'])
        # Garante que a outra tarefa não foi modificada
        self.assertFalse(tarefas_atualizadas[0]['concluida'])

    def test_filtrar_tarefas_pendentes(self):
        """Testa o filtro de tarefas pendentes usando lambda (RF05)."""
        # Primeiro, marca uma como concluída
        tarefas_com_uma_concluida = atualizar_tarefa(self.tarefas_iniciais, 1, marcar_como_concluida)
        # Filtra as pendentes
        tarefas_pendentes = filtrar_tarefas(tarefas_com_uma_concluida, lambda t: not t['concluida'])
        self.assertEqual(len(tarefas_pendentes), 1)
        self.assertEqual(tarefas_pendentes[0]['id'], 2)

    def test_filtrar_tarefas_concluidas(self):
        """Testa o filtro de tarefas concluídas usando lambda (RF05)."""
        tarefas_com_uma_concluida = atualizar_tarefa(self.tarefas_iniciais, 1, marcar_como_concluida)
        tarefas_concluidas = filtrar_tarefas(tarefas_com_uma_concluida, lambda t: t['concluida'])
        self.assertEqual(len(tarefas_concluidas), 1)
        self.assertEqual(tarefas_concluidas[0]['id'], 1)

    def test_formatar_tarefas_para_exibicao(self):
        """Testa a formatação da lista de tarefas (RF02)."""
        tarefas_formatadas = formatar_tarefas_para_exibicao(self.tarefas_iniciais)
        self.assertEqual(len(tarefas_formatadas), 2)
        self.assertEqual(tarefas_formatadas[0], "[ ] ID: 1 - Tarefa Teste 1")
        self.assertEqual(tarefas_formatadas[1], "[ ] ID: 2 - Tarefa Teste 2")

        # Testa com uma tarefa concluída
        tarefas_atualizadas = atualizar_tarefa(self.tarefas_iniciais, 1, marcar_como_concluida)
        tarefas_formatadas_2 = formatar_tarefas_para_exibicao(tarefas_atualizadas)
        self.assertEqual(tarefas_formatadas_2[0], "[X] ID: 1 - Tarefa Teste 1")

    def test_gerador_de_id_closure(self):
        """Testa se o gerador de ID (closure) mantém o estado e gera IDs únicos."""
        gen = gerador_de_id()
        self.assertEqual(gen(), 1)
        self.assertEqual(gen(), 2)
        self.assertEqual(gen(), 3)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)