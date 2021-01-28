def exists_word(word, instance):
    found_list = []
    for i in range(len(instance)):
        entry = instance.search(i)
        occurrences = []
        for index, line in enumerate(entry['linhas_do_arquivo']):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1})
        if occurrences == []:
            return occurrences
        found_list.append({
            "arquivo": entry['nome_do_arquivo'],
            "ocorrencias": occurrences,
            "palavra": word
        })
    return found_list


def search_by_word(word, instance):
    found_list = []
    for i in range(len(instance)):
        entry = instance.search(i)
        occurrences = []
        for index, line in enumerate(entry['linhas_do_arquivo']):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1, "conteudo": line})
        if occurrences == []:
            return occurrences
        found_list.append({
            "arquivo": entry['nome_do_arquivo'],
            "ocorrencias": occurrences,
            "palavra": word
        })
    return found_list
