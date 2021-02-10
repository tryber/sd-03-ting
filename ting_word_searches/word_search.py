import re


def exists_word(word, instance):
    ocorrences = []
    return_list = []
    for i in range(len(instance)):
        current_file = instance.search(i)
        for line in current_file["linhas_do_arquivo"]:
            if re.search(word, line, re.IGNORECASE):
                ocorrences.append({"linha": i + 1})
                return_list.append(
                    {
                        "palavra": f"{word}",
                        "arquivo": current_file["nome_do_arquivo"],
                        "ocorrencias": ocorrences,
                    }
                )
    return return_list


def search_by_word(word, instance):
    ocorrences = []
    return_list = []
    for i in range(len(instance)):
        current_file = instance.search(i)
        for line in current_file["linhas_do_arquivo"]:
            if re.search(word, line, re.IGNORECASE):
                ocorrences.append(
                    {"linha": i + 1, "conteudo": f"{line}"},
                )
                return_list.append(
                    {
                        "palavra": f"{word}",
                        "arquivo": current_file["nome_do_arquivo"],
                        "ocorrencias": ocorrences,
                    }
                )
    return return_list
