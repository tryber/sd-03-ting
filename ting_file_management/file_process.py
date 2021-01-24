from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file_content = txt_importer(path_file)
    for each_queue in range(len(instance)):
        if instance.search(each_queue)["nome_do_arquivo"] == path_file:
            return
    dict_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }
    print(dict_data)
    instance.enqueue(dict_data)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    try:
        instance.search(position)
    except IndexError:
        sys.stderr.write("Posição inválida")
