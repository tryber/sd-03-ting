from ting_file_management.queue import Queue


def append_if(local_list, line, content, search):
    if search:
        local_list.append({"linha": line, "conteudo": content})
    else:
        local_list.append({"linha": line})


def word_searcher(word, instance, isSearching):
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
                append_if(
                    local_word["ocorrencias"], current_line, line, isSearching
                )
            current_line += 1
        if word_appears:
            words.append(local_word)
    return words


def exists_word(word, instance):
    return word_searcher(word, instance, False)


def search_by_word(word, instance):
    return word_searcher(word, instance, True)


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
