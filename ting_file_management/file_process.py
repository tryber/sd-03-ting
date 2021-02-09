import sys
from ting_file_management.file_management import txt_importer


def format_data(name, lines):
    return {
        "nome_do_arquivo": name,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }


def process(path_file, instance):
    text_data = txt_importer(path_file)
    for i in range(instance.__len__()):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return

    return_dict = format_data(path_file, text_data)
    instance.enqueue(return_dict)
    print(return_dict, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
