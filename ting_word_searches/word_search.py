def search_word_sentence(palavra_procurada, value):
    lines = []
    for line_index, sentence in enumerate(value):
        for word in sentence.split(" "):
            if word.lower().replace(".", "") == palavra_procurada.lower():
                lines.append(
                    {
                        "linha": line_index + 1,
                        "conteudo": sentence,
                    }
                )

    return lines


def search_word_new(palavra_procurada, value):
    lines = []
    for i, sentence in enumerate(value):
        for word in sentence.split(" "):
            if word.lower().replace(".", "") == palavra_procurada.lower():
                lines.append({"linha": i + 1})

    return lines


def exists_word(word, instance):
    news = []

    for i_news in range(len(instance)):
        foundFile = instance.dequeue()
        matched_lines = search_word_new(word, foundFile["linhas_do_arquivo"])
        if matched_lines:
            news.append(
                {
                    "palavra": word,
                    "arquivo": foundFile["nome_do_arquivo"],
                    "ocorrencias": matched_lines,
                }
            )
        instance.enqueue(foundFile)

    return news


def search_by_word(word, instance):
    news = []
    for i_news in range(len(instance)):
        foundFile = instance.dequeue()
        matched_lines = search_word_sentence(
            word, foundFile["linhas_do_arquivo"]
        )
        if matched_lines:
            news.append(
                {
                    "palavra": word,
                    "arquivo": foundFile["nome_do_arquivo"],
                    "ocorrencias": matched_lines,
                }
            )
        instance.enqueue(foundFile)

    return news


if __name__ == "__main__":
    from ting_file_management.queue import Queue
    from ting_file_management.file_process import process

    filona = Queue()
    process("statics/nome_pedro.txt", filona)
    word = search_by_word("pedro", filona)