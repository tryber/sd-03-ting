import sys
from functools import cache
from ting_file_management.file_management import txt_importer


# Implementa arquivo no fila
@cache
def remove(instance):
    if instance.__len__() > 0:
        file = instance.dequeue()
        print(
            f"Arquivo {file['nome_do_arquivo']} removido com sucesso"
        )
    else:
        print("Não há elementos")


def process(path_file, instance):
    values = txt_importer(path_file)
    processed_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(values),
        "linhas_do_arquivo": values,
    }
    instance.enqueue(processed_data)
    print(processed_data, file=sys.stdout)
    return processed_data


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        sys.stderr.write("Posição inválida")
