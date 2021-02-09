import sys
from ting_file_management.file_management import txt_importer


# Implementa arquivo no fila
def process(path_file, instance):
    for element in range(len(instance)):
        if instance.search(element)["nome_do_arquivo"] == path_file:
            return

    linhas_do_arquivo = txt_importer(path_file)
    new_entry = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(linhas_do_arquivo),
        "linhas_do_arquivo": linhas_do_arquivo,
    }

    instance.enqueue(new_entry)
    instance.last_element()


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
        print(instance.search(position))
    except IndexError:
        sys.stderr.write("Posição inválida")
