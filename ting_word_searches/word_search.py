from operator import itemgetter


def phrase_to_words(phrase):
    special_chars = "*/-+.;/,:~^][{}()´`-_=+!@#$%¨&|\\"
    phrase = "".join(str(x).lower() for x in phrase)
    for letter in phrase:
        if letter in special_chars:
            phrase = phrase.replace(letter, "")
    phrase = phrase.split(" ")
    return phrase


def exists_word(word, instance):
    result = list()
    for i in range(len(instance)):
        process_metada = instance.search(i)
        file_path, lines_qty, phrases = itemgetter(
            "nome_do_arquivo",
            "qtd_linhas",
            "linhas_do_arquivo"
        )(process_metada)

        match_ocurrences = [
            {"linha": index + 1}
            for index, phrase in enumerate(phrases)
            if str(word).lower() in phrase_to_words(phrase)
        ]

        if len(match_ocurrences) == 0:
            break

        result.append({
            "palavra": word,
            "arquivo": file_path,
            "ocorrencias": [*match_ocurrences]
        })

    return result


def search_by_word(word, instance):
    result = list()
    for i in range(len(instance)):
        process_metada = instance.search(i)
        file_path, lines_qty, phrases = itemgetter(
            "nome_do_arquivo",
            "qtd_linhas",
            "linhas_do_arquivo"
        )(process_metada)

        match_ocurrences = [
            {"linha": index + 1, "conteudo": phrase}
            for index, phrase in enumerate(phrases)
            if word in phrase_to_words(phrase)
        ]

        if len(match_ocurrences) == 0:
            break

        result.append({
            "palavra": word,
            "arquivo": file_path,
            "ocorrencias": [*match_ocurrences]
        })

    return result
