# Gerenciador de Tarefas com Programação Funcional

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Concluído-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

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

3.  (Opcional, mas recomendado) Crie e ative um ambiente virtual:
    ```sh
    # Criar ambiente virtual
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

## ▶️ Como Executar

### Executando a Aplicação Principal

Para ver uma demonstração do sistema em funcionamento, execute o arquivo principal:

```sh
python gerenciador_tarefas.py
```

Isso executará a função `main()`, que simula a adição, listagem, atualização e exclusão de tarefas, imprimindo os resultados no console.

### Executando os Testes

Para garantir que todas as funções operem corretamente, execute a suíte de testes automatizados:

```sh
python -m unittest test_gerenciador_tarefas.py
```

A saída esperada é a confirmação de que todos os testes passaram:

```
.........
----------------------------------------------------------------------
Ran 9 tests in X.XXXs

OK
```

## 📂 Estrutura do Projeto

```
projeto_programacao_funcional/
├── .gitignore               # Arquivo para ignorar arquivos e pastas no Git
├── gerenciador_tarefas.py   # Código-fonte principal da aplicação
├── test_gerenciador_tarefas.py # Casos de teste automatizados
└── README.md                # Este arquivo
```

## 👥 Autores

Este projeto foi desenvolvido pela seguinte equipe:

Matheus Alves Medeiros – 2323804 
Carlos Henrique Alves, 2323853
Wiulis de Araujo Monteiro – 2326322
Nicole Stefhany Monteiro Amed – 2326323

---

*Este projeto foi criado para fins acadêmicos. A estrutura inicial e os exemplos foram gerados com o auxílio de IA (Gemini) e posteriormente revisados e adaptados pela equipe.*