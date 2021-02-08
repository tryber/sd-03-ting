  
def extract_word_occurrence_from_file(word, file, content=None):
    holder = {
        "palavra": word,
        "arquivo": file["nome_do_arquivo"],
        "ocorrencias": [],
    }
    file_lines = file["linhas_do_arquivo"]
    for line in range(len(file_lines)):
        print(line)
        print(file_lines[line])
        if word.lower() in file_lines[line].lower():
            occur = {
                "linha": line + 1,
            }
            if content:
                occur["conteudo"] = file_lines[line]
            holder["ocorrencias"].append(occur)
    return holder


def exists_word(word, instance):
    result = []
    for item in instance:
        search = extract_word_occurrence_from_file(word, item.value)
        if search["ocorrencias"]:
            result.append(search)
    return result


def search_by_word(word, instance):
    result = []
    for item in instance:
        search = extract_word_occurrence_from_file(
            word, item.value, content=True
        )
        if search["ocorrencias"]:
            result.append(search)
    return result
