from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def exists_word(word, instance):
    array_of_string_indexed = list()
    for node in instance:
        lines = node.value["linhas_do_arquivo"]
        word_dict = {
            "palavra": word,
            "arquivo": node.value["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for index, line in enumerate(lines):
            line_replaced = line.replace('.', '')
            lines_split = line_replaced.split()
            if word in lines_split:
                word_dict["ocorrencias"].append({"linha": index + 1})

        if len(word_dict["ocorrencias"]) > 0:
            array_of_string_indexed.append(word_dict)

    return array_of_string_indexed


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


if __name__ == "__main__":
    queue = Queue()
    process("statics/nome_pedro.txt", queue)
    word = exists_word("Pedro", queue)
    print(word)
    # process("./statics/arquivo_teste.txt", queue)
    # print(exists_word("kkk", queue))
