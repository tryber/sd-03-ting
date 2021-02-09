def procura_palavra(palavra, sentences):
    value1 = []
    for line_index, sentence in enumerate(sentences):
        for word in sentence.split(" "):
            if word.lower().replace(".", "") == palavra.lower():
                value1.append(
                    {
                        "linha": line_index + 1,
                        "conteudo": sentence,
                    }
                )

    return value1


def search_new_word(palavra, sentences):
    value1 = []
    for line_index, sentence in enumerate(sentences):
        for word in sentence.split(" "):
            if word.lower().replace(".", "") == palavra.lower():
                value1.append({"linha": line_index + 1})

    return value1


def search_by_word(palavra, instance):
    value2 = []
    for i_news in range(len(instance)):
        lines_arquivo = instance.dequeue()
        matched_lines = procura_palavra(
            palavra, lines_arquivo["linhas_do_arquivo"]
        )
        if matched_lines:
            value2.append(
                {
                    "palavra": palavra,
                    "arquivo": lines_arquivo["nome_do_arquivo"],
                    "ocorrencias": matched_lines,
                }
            )
        instance.enqueue(lines_arquivo)

    return value2


def exists_word(palavra, instance):
    value2 = []
    for i_news in range(len(instance)):
        lines_arquivo = instance.dequeue()
        verify = search_new_word(palavra, lines_arquivo["linhas_do_arquivo"])
        if verify:
            value2.append(
                {
                    "palavra": palavra,
                    "arquivo": lines_arquivo["nome_do_arquivo"],
                    "ocorrencias": verify,
                }
            )
        instance.enqueue(lines_arquivo)

    return value2


if __name__ == "__main__":
    from ting_file_management.queue import Queue
    from ting_file_management.file_process import process

    project = Queue()
    process("statics/nome_pedro.txt", project)
    palavra = search_by_word("pedro", project)
    print(palavra)
