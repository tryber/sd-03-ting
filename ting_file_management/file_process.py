import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    # verifica se o item já foi gravado na fila
    for item in range(len(instance)):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return

    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }
    instance.enqueue(file_info)
    print(file_info)


def remove(instance):
    """Aqui irá sua implementação"""
    if not instance or instance.is_empty():
        return print("Não há elementos", file=sys.stdout)
    file_name = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    print(f"Arquivo {file_name} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        meta_data = instance.search(position)
        print(meta_data, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
