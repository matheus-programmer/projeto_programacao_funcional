# Gerenciador de Tarefas com Programação Funcional

Este projeto é um sistema simples de gerenciamento de tarefas (To-Do List) via linha de comando, desenvolvido como atividade para a disciplina de Paradigmas de Programação. O objetivo principal foi aplicar conceitos de **programação funcional** em Python para criar um código declarativo, modular e com funções puras (evitando efeitos colaterais).

## ✨ Funcionalidades

O sistema permite ao usuário realizar as seguintes operações:

-   ✅ **Adicionar** novas tarefas.
-   📋 **Listar** todas as tarefas existentes.
-   ✔️ **Marcar** uma tarefa como concluída.
-   ❌ **Excluir** uma tarefa da lista.
-   🔍 **Filtrar** tarefas por status (pendentes ou concluídas).

## 🚀 Conceitos de Programação Funcional Aplicados

A implementação deste projeto focou no uso dos seguintes conceitos funcionais:

-   **Função de Alta Ordem (High-Order Function)**: As funções `atualizar_tarefa` e `filtrar_tarefas` recebem outras funções como argumentos (`atualizador` e `criterio`, respectivamente), permitindo um comportamento dinâmico e reutilizável.
-   **Closure**: A função `gerador_de_id` utiliza uma closure para manter o estado do último ID gerado, garantindo que cada nova tarefa tenha um identificador único sem o uso de variáveis globais.
-   **Função Lambda**: Funções anônimas (lambdas) são usadas em conjunto com `filtrar_tarefas` para criar critérios de filtro de forma concisa e imediata (ex: `lambda t: t['concluida']`).
-   **List Comprehension**: Este recurso é amplamente utilizado para transformações de listas de forma declarativa, como em `formatar_tarefas_para_exibicao` e na lógica de exclusão de tarefas, alinhando-se ao princípio da imutabilidade ao criar novas listas em vez de modificar as existentes.

## 🛠️ Tecnologias Utilizadas

-   **Python 3.8+**
-   **unittest**: Módulo nativo do Python para a suíte de testes automatizados.

## ⚙️ Instalação e Configuração

Para executar este projeto, você precisa ter o Python 3.8 ou superior instalado.

1.  Clone o repositório:
    ```sh
    git clone <url-do-seu-repositorio>
    ```

2.  Navegue até a pasta do projeto:
    ```sh
    cd projeto_programacao_funcional
    ```

3.  (Opcional, mas recomendado) Crie e ative um ambiente virtual
