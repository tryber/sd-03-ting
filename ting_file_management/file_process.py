import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = txt_importer(path_file)
    """ print(data) """
    info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }
    print(info)
    for i in instance:
        if i.value == info:
            info = {}

    info and instance.enqueue(info)

    return info


def remove(instance):
    if not len(instance):
        print("Não há elementos")
    else:
        info = instance.dequeue()
        print(f"Arquivo {info['nome_do_arquivo']} removido com sucesso\n")


def file_metadata(instance, position):
    if len(instance) <= position:
        print("Posição inválida", file=sys.stderr)
    else:
        return instance.search(position)
