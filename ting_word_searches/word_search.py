import re


def exists_word(word, instance):
    list_of_occurrences = []
    occurrences = []
    for i in range(instance.__len__()):
        for j in range(len(instance.search(i)['linhas_do_arquivo'])):
            if (
                re.search(word, instance.search(i)['linhas_do_arquivo'][j],
                          re.IGNORECASE)):
                occurrences.append({
                    "linha": j + 1,
                    "conteudo": instance.search(i)['linhas_do_arquivo'][j]
                    .strip(),
                })

        if len(occurrences) > 0:
            list_of_occurrences.append({
                "palavra": word,
                "arquivo": instance.search(i)['nome_do_arquivo'],
                "ocorrencias": occurrences
            })
            occurrences = []

    return list_of_occurrences


def search_by_word(word, instance):
    pass
