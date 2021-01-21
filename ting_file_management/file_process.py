import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }
    print(dict)


def remove(instance):
    if not instance:
        return print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
