def validar_lista_tarefas(response):
    data = response.json()

    assert isinstance(data, list), "A resposta não é uma lista"

    assert any("completed" in tarefa for tarefa in data), \
        "Nenhuma tarefa contém a chave 'completed'"