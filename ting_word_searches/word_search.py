import re


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    line_number = 0
    result = []
    word_ocorrences = []
    for words in range(instance.__len__()):
        line_number += 1
        temp = instance.search(words)
        for line in temp["linhas_do_arquivo"]:
            if re.findall(word, line, re.IGNORECASE):
                word_ocorrences.append({"linha": line_number})
                result.append(
                    {
                        "palavra": f"{word}",
                        "arquivo": temp["nome_do_arquivo"],
                        "ocorrencias": word_ocorrences,
                    }
                )
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    line_number = 0
    result = []
    word_ocorrences = []
    for words in range(instance.__len__()):
        line_number += 1
        temp = instance.search(words)
        for line in temp["linhas_do_arquivo"]:
            if re.findall(word, line, re.IGNORECASE):
                word_ocorrences.append(
                    {"linha": line_number, "conteudo": f"{line}"},
                )
                result.append(
                    {
                        "palavra": f"{word}",
                        "arquivo": temp["nome_do_arquivo"],
                        "ocorrencias": word_ocorrences,
                    }
                )
    return result
