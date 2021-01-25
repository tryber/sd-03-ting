import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    file_lines = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines,
    }
    Queue.enqueue(data)
    sys.stdout.write(f"{data}\n")
    return data


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) > 0:
        remove_news = Queue.dequeue()
        name = remove_news["nome_do_arquivo"]
        return print(f"Arquivo {name} removido com sucesso", file=sys.stdout)

    return print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        file_meta = Queue.search(position)
        sys.stdout.write(f"{file_meta}\n")
        return
    except IndexError:
        sys.stderr.write("Posição inválida")
