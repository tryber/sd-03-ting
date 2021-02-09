from functools import cache
from ting_file_management.file_management import txt_importer
import sys


# Implementa arquivo no fila
@cache
def process(path_file, instance):
    txt = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt),
        "linhas_do_arquivo": txt,
    }
    print(data, file=sys.stdout)
    instance.enqueue(data)
    return data


def remove(instance):
    if instance.__len__() > 0:
        file = instance.dequeue()
        print(
            f"Arquivo {file['nome_do_arquivo']} removido com sucesso"
        )
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        retorno = instance.search(position)
        sys.stdout.write(str(retorno))
    except IndexError:
        sys.stderr.write('Posição inválida')
