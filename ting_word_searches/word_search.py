import re


def exists_word(word, instance):
    new_list = []
    count = 0

    for i in range(len(instance)):
        count += 1
        occurrence = []

        new_search = instance.search(i)
        for line in new_search["linhas_do_arquivo"]:
            if re.search(word, line, re.IGNORECASE):
                occurrence.append({
                    "linha": count,
                })
                print(count)
                new_list.append({
                    "palavra": f"{word}",
                    "arquivo": new_search["nome_do_arquivo"],
                    "ocorrencias": occurrence,
                })

    return new_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
