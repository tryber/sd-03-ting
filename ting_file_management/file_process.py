import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file not in instance._files:
        file = txt_importer(path_file)

        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }

        instance.enqueue(data)
        instance.add_file(path_file)
        print(data, file=sys.stdout)


def remove(instance):
    if len(instance._data):
        path_file = instance._data[0]["nome_do_arquivo"]
        instance.dequeue()
        instance.remove_file(path_file)
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)
    print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    if instance.__len__() <= position:
        print("Posição inválida", file=sys.stderr)
    else:
        return instance.search(position)
