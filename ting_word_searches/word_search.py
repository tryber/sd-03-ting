import re


def exists_word(word, instance):
    queue_list = instance._queue
    matches = []
    occurrences = []
    line_count = 0

    for file in queue_list:
        for phrase in file["linhas_do_arquivo"]:
            if re.findall(word, phrase, re.IGNORECASE):
                line_count += 1
                occurrences.append({"linha": line_count})

        if len(occurrences):
            matches.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences})

    return matches


def search_by_word(word, instance):
    queue_list = instance._queue
    matches = []
    occurrences = []
    line_count = 0

    for file in queue_list:
        for phrase in file["linhas_do_arquivo"]:
            if re.findall(word, phrase, re.IGNORECASE):
                line_count += 1
                occurrences.append({"linha": line_count, "conteudo": phrase})

        if len(occurrences):
            matches.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences})

    return matches
