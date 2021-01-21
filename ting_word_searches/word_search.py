from ting_file_management.queue import Queue


def exists_word(word, instance):
    words = []
    current_line = 1
    for item in instance:
        current_line = 1
        word_appears = False
        local_word = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for line in item["linhas_do_arquivo"]:
            if word.lower() in line.lower():
                word_appears = True
                local_word["ocorrencias"].append({"linha": current_line})
            current_line += 1
        if word_appears:
            words.append(local_word)
    return words


def search_by_word(word, instance):
    words = []
    current_line = 1
    for item in instance:
        current_line = 1
        word_appears = False
        local_word = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for line in item["linhas_do_arquivo"]:
            if word.lower() in line.lower():
                word_appears = True
                local_word["ocorrencias"].append(
                    {"linha": current_line, "conteudo": line}
                )
            current_line += 1
        if word_appears:
            words.append(local_word)
    return words


if __name__ == "__main__":
    test = [
        {
            "nome_do_arquivo": "arquivo_teste.txt",
            "qtd_linhas": "3",
            "linhas_do_arquivo": [
                "Acima de tudo,",
                "é fundamental ressaltar que a adoção de políticas nos obriga",
                "à análise do levantamento das variáveis envolvidas.",
            ],
        },
        {
            "nome_do_arquivo": "nome_pedro.txt",
            "qtd_linhas": "1",
            "linhas_do_arquivo": [
                "Aqui contem que fala sobre um menino pobre chamado Pedro.",
            ],
        },
    ]
    queue = Queue()
    for elem in test:
        queue.enqueue(elem)
    print(exists_word("pedro", queue))
