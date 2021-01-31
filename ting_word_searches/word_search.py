import re


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    lines = 0
    result = []
    ocorrences = []
    for words in range(instance.__len__()):
        lines += 1
        temp = instance.search(words)
        for line in temp["linhas_do_arquivo"]:
            if re.findall(word, line, re.IGNORECASE):
                line_number = lines
                ocorrences.append({"linha": line_number})
                result.append(
                    {
                        "palavra": f"{word}",
                        "arquivo": temp["nome_do_arquivo"],
                        "ocorrencias": ocorrences,
                    }
                )
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
