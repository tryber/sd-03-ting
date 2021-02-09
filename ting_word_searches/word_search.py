def search_word_sentence(searched_word, sentences):
    value1 = []
    for line_index, sentence in enumerate(sentences):
        for word in sentence.split(" "):
            if word.lower().replace(".", "") == searched_word.lower():
                value1.append(
                    {
                        "linha": line_index + 1,
                        "conteudo": sentence,
                    }
                )

    return value1


def search_new_word(searched_word, sentences):
    value1 = []
    for line_index, sentence in enumerate(sentences):
        for word in sentence.split(" "):
            if word.lower().replace(".", "") == searched_word.lower():
                value1.append({"linha": line_index + 1})

    return value1


def search_by_word(word, instance):
    value2 = []
    for i_news in range(len(instance)):
        lines_arquivo = instance.dequeue()
        matched_lines = search_word_sentence(
            word, lines_arquivo["linhas_do_arquivo"]
        )
        if matched_lines:
            value2.append(
                {
                    "palavra": word,
                    "arquivo": lines_arquivo["nome_do_arquivo"],
                    "ocorrencias": matched_lines,
                }
            )
        instance.enqueue(lines_arquivo)

    return value2


def exists_word(word, instance):
    value2 = []
    for i_news in range(len(instance)):
        lines_arquivo = instance.dequeue()
        verify = search_new_word(word, lines_arquivo["linhas_do_arquivo"])
        if verify:
            value2.append(
                {
                    "palavra": word,
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
    word = search_by_word("pedro", project)
    print(word)
