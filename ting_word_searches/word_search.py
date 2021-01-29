import re


def exists_word(word, instance):
    lines = 0
    result = []
    ocorrences = []
    for words in range(len(instance)):
        lines += 1
        temp = instance.search(words)
        for line in temp["linhas_do_arquivo"]:
            if re.findall(word, line, re.IGNORECASE):
                line_number = lines
                ocorrences.append({"linha": line_number})
                result.append({
                    "palavra": f"{word}",
                    "arquivo": temp["nome_do_arquivo"],
                    "ocorrencias": ocorrences
                })
    return result


def search_by_word(word, instance):
    result = []
    ocorrences = []
    lines = 0
    for worlds in range(len(instance)):
        lines += 1
        temp = instance.search(worlds)
        for line in temp["linhas_do_arquivo"]:
            if re.findall(word, line, re.IGNORECASE):
                line_number = lines
                ocorrences.append({
                            "linha": line_number,
                            "conteudo": f"{line}"
                        })
                result.append(
                    {
                        "palavra": f"{word}",
                        "arquivo": temp["nome_do_arquivo"],
                        "ocorrencias": ocorrences,
                    }
                )
        return result
