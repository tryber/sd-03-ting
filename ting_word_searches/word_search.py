def exists_word(word, instance):
    matches = list()
    for i in range(len(instance)):
        deq = instance.dequeue()
        matched_lines = list()

        for line, string in enumerate(deq['linhas_do_arquivo']):
            if word in string.replace('.', '').split():
                matched_lines.append({'linha': line + 1})

        if matched_lines:
            matches.append({
                'palavra': word,
                'arquivo': deq['nome_do_arquivo'],
                'ocorrencias': matched_lines
            })
    return matches


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
