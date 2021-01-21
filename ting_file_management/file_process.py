import sys
from ting_file_management.file_management import txt_importer
from functools import cache


@cache
def process(path_file, instance):
    lines = txt_importer(path_file)

    processed_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    print(processed_data, file=sys.stdout)
    instance.enqueue(processed_data)
    return processed_data


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos", file=sys.stdout)
    news = instance.dequeue()
    file_name = news["nome_do_arquivo"]
    print(f"Arquivo {file_name} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        news = instance.search(position)
        print(news, file=sys.stdout)
        return news
    except IndexError:
        print("Posição inválida", file=sys.stderr)


if __name__ == "__main__":
    from queue import Queue

    project = Queue()
    process("statics/novo_paradigma_globalizado-min.txt", project)
    print(project)
    file_metadata(project, 0)
