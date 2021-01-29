import re


def exists_word(word, instance):
    word_list = []
    lines = 0

    for i in range(len(instance)):
        seach_intance = instance.search(i)
        list_of_ocorrence = []
        lines += 1
        for line in seach_intance["linhas_do_arquivo"]:
            if re.search(word, line, re.IGNORECASE):
                list_of_ocorrence.append({
                    "linha": lines,
                })
                word_list.append({
                    "palavra": f"{word}",
                    "arquivo": seach_intance["nome_do_arquivo"],
                    "ocorrencias": list_of_ocorrence,
                })

    return word_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
