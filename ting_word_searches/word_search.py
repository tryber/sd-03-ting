def search_new_word(searched_word, sentences):
    lines = []
    for line_index, sentence in enumerate(sentences):
        for word in sentence.split(" "):
            if word.lower().replace(".", "") == searched_word.lower():
                lines.append({"linha": line_index + 1})

    return lines


def search_word_sentence(searched_word, sentences):
    lines = []
    for line_index, sentence in enumerate(sentences):
        for word in sentence.split(" "):
            if word.lower().replace(".", "") == searched_word.lower():
                lines.append(
                    {
                        "linha": line_index + 1,
                        "conteudo": sentence,
                    }
                )

    return lines


def exists_word(word, instance):
    news = []
    for i_news in range(len(instance)):
        current = instance.dequeue()
        matched_lines = search_new_word(word, current["linhas_do_arquivo"])
        if matched_lines:
            news.append(
                {
                    "palavra": word,
                    "arquivo": current["nome_do_arquivo"],
                    "ocorrencias": matched_lines,
                }
            )
        instance.enqueue(current)

    return news


def search_by_word(word, instance):
    news = []
    for i_news in range(len(instance)):
        current = instance.dequeue()
        matched_lines = search_word_sentence(
            word, current["linhas_do_arquivo"]
        )
        if matched_lines:
            news.append(
                {
                    "palavra": word,
                    "arquivo": current["nome_do_arquivo"],
                    "ocorrencias": matched_lines,
                }
            )
        instance.enqueue(current)

    return news


if __name__ == "__main__":
    from ting_file_management.queue import Queue
    from ting_file_management.file_process import process

    project = Queue()
    process("statics/nome_pedro.txt", project)
    word = search_by_word("pedro", project)
    print(word)
