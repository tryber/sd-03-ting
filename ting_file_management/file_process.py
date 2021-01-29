import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }
    instance.enqueue(dict)
    print(dict)


def remove(instance):
    if not instance:
        return print("Não há elementos", file=sys.stdout)
        path_file = instance.search(0)["nome_do_arquivo"]
        instance.dequeue()
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        print(data, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
