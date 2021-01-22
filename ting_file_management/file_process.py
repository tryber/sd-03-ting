import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance):
    array_of_string = txt_importer(path_file)

    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return

    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(array_of_string),
        "linhas_do_arquivo": array_of_string,
    }

    instance.enqueue(file_dict)

    print(file_dict)


def remove(instance):
    if instance.is_empty():
        return print("Não há elementos")

    path_file = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()

    return print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        infos = instance.search(position)
        print(infos)
    except IndexError:
        print("Posição inválida", file=sys.stderr)


if __name__ == "__main__":
    queue = Queue()
    # process("./statics/arquivo_teste.txt", queue)
    remove(queue)
    # file_metadata(queue, 0)
