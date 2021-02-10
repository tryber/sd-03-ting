import re


def exists_word(word, instance):
    ocurrences = []
    lister = []
    for i in range(len(instance)):
        for line in instance.search(i)["linhas_do_arquivo"]:
            if re.search(word, line, re.IGNORECASE):
                ocurrences.append({"linha": i + 1})
                lister.append(
                    {
                        "palavra": f"{word}",
                        "arquivo": instance.search(i)["nome_do_arquivo"],
                        "ocorrencias": ocurrences,
                    }
                )
    return lister


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
