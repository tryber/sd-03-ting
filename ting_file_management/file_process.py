import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    lines = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    instance.enqueue(data)
    sys.stdout.write(f"{data}\n")
    return data


def remove(instance):
    removed = instance.dequeue()
    if removed is None:
        sys.stdout.write("Não há elementos\n")
    else:
        sys.stdout.write(
            "Arquivo {nome_do_arquivo} removido com sucesso\n".format_map(
                removed
            )
        )
    return


def file_metadata(instance, position):
    try:
        found_file = instance.search(position)
        sys.stdout.write(f"{found_file}\n")
        return
    except IndexError:
        sys.stderr.write("Posição inválida")


if __name__ == "__main__":
    queue = Queue()
    process("statics/arquivo_teste.txt", queue)
    file_metadata(queue, 0)
    remove(queue)
