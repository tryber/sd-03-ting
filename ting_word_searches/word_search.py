def exists_word(word, instance):
    """Aqui irá sua implementação"""
    word_news = []
    for i in instance:
        find_word = instance.search(word)
        if find_word[i]:
            return word_news.append(find_word)


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
