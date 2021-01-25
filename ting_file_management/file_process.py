import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    datas = txt_importer(path_file)

    data_structure = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(datas),
        "linhas_do_arquivo": datas,
    }

    print(data_structure, file=sys.stdout)
    instance.enqueue(data_structure)


def remove(instance):
    if len(instance) > 0:
        remove_news = instance.dequeue()
        name = remove_news["nome_do_arquivo"]
        return print(f"Arquivo {name} removido com sucesso", file=sys.stdout)

    return print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        datas = instance.search(position)
        print(datas)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
