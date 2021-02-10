import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for item in range(instance.__len__()):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file)
    }

    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""
    if not instance or instance.__len__() == 0:
        print('Não há elementos', file=sys.stdout)
    file_data = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    print(f"Arquivo {file_data} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        metadata = instance.search(position)
        print(metadata, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
