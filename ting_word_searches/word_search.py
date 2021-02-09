# from .content_deque import Deque
from operator import itemgetter
# sys.path.insert(1, '../ting_file_management')
# from file_process import process
# from file_management import txt_importer
# from queue import Queue


def phrase_to_words(phrase):
    special_chars = "*/-+.;/,:~^][{}()´`-_=+!@#$%¨&|\\"
    phrase = "".join(x for x in phrase)
    for letter in phrase:
        if letter in special_chars:
            phrase = phrase.replace(letter, "")
    phrase = phrase.split(" ")
    return phrase


def exists_word(word, instance):
    result = list()
    for i in range(len(instance)):
        process_metada = instance.search(i)
        file_path, lines_qty, data = itemgetter(
            "nome_do_arquivo",
            "qtd_linhas",
            "linhas_do_arquivo"
        )(process_metada)

        words = [
            {"linha": index + 1}
            for index, phrase in enumerate(data)
            if word in phrase_to_words(phrase)
        ]

        if len(words) == 0:
            break

        result.append({
            "palavra": word,
            "arquivo": file_path,
            "ocorrencias": [*words]
        })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""

# if __name__ == "__main__":
#     instance = Queue()
#     process("../statics/arquivo_teste.txt", instance)
#     exists_word("é", instance)
