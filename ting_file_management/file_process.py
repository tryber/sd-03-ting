import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    txt_file = txt_importer(path_file)
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_file),
        "linhas_do_arquivo": txt_file
    }
    instance.enqueue(data)
    print(data)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
