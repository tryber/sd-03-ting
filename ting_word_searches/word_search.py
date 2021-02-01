import re


def exists_word(word, instance):
    data = instance._data
    result = []
    occurrences = []
    line = 0
    for file in data:
        for phrase in file["linhas_do_arquivo"]:
            if re.findall(word, phrase, re.IGNORECASE):
                line += 1
                occurrences.append({"linha": line})
        if len(occurrences):
            result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )
    return result


def search_by_word(word, instance):
    data = instance._data
    result = []
    occurrences = []
    line = 0
    for file in data:
        for phrase in file["linhas_do_arquivo"]:
            if re.findall(word, phrase, re.IGNORECASE):
                line += 1
                occurrences.append({"linha": line, "conteudo": phrase})
        if len(occurrences):
            result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )
    return result
