def find_word(word, instance, function):
    word_list = []
    for i in range(len(instance)):
        search = instance.search(i)
        word_occurence = []
        for index, line in enumerate(search['linhas_do_arquivo']):
            if word.lower() in line.lower():
                if function == 'exists':
                    word_occurence.append({"linha": index + 1})
                else:
                    word_occurence.append(
                        {"linha": index + 1, "conteudo": line}
                    )
        if word_occurence == []:
            return word_occurence
        word_list.append({
            "arquivo": search['nome_do_arquivo'],
            "ocorrencias": word_occurence,
            "palavra": word
        })
        return word_list


def exists_word(word, instance):
    return find_word(word, instance, 'exists')


def search_by_word(word, instance):
    return find_word(word, instance, 'search')
