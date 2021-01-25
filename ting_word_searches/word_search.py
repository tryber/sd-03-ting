import re


def exists_word(word, instance):
    result = list()
    counter = 0
    for n in range(len(instance)):
        counter += 1
        occours = list()
        temp = instance.search(n)
        for line in temp["linhas_do_arquivo"]:
            if re.search(word, line, re.IGNORECASE):
                line_number = counter
                occours.append({
                            "linha": line_number,
                        })
                print(line_number)
                result.append(
                    {
                        "palavra": f"{word}",
                        "arquivo": temp["nome_do_arquivo"],
                        "ocorrencias": occours,
                    }
                )
        return result


def search_by_word(word, instance):
    result = list()
    counter = 0
    for n in range(len(instance)):
        counter += 1
        occours = list()
        temp = instance.search(n)
        for line in temp["linhas_do_arquivo"]:
            if re.search(word, line, re.IGNORECASE):
                line_number = counter
                occours.append({
                            "linha": line_number,
                            "conteudo": f"{line}"
                        })
                print(line_number)
                result.append(
                    {
                        "palavra": f"{word}",
                        "arquivo": temp["nome_do_arquivo"],
                        "ocorrencias": occours,
                    }
                )
        return result
