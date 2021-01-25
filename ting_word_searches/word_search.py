def exists_word(word, instance):
    new_list = []

    for node in instance:
        lines = node.value["linhas_do_arquivo"]
        new_dict = {
            "palavra": word,
            "arquivo": node.value["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for i, line in enumerate(lines):
            line_change = line.replace(".", "")
            line_split = line_change.split()
            if word in line_split:
                new_dict["ocorrencias"].append({"linha": i + 1})

        if len(new_dict["ocorrencias"]) > 0:
            new_list.append(new_dict)

    return new_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
