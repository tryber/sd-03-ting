import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = txt_importer(path_file)
    for i in range(instance.__len__()):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return

    retorno = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }
    instance.enqueue(retorno)
    print(retorno, file=sys.stdout)


def remove(instance):
    if (instance.__len__() == 0):
        return print('Não há elementos', file=sys.stdout)
    file_name = instance.search(0)['nome_do_arquivo']
    instance.dequeue()
    return print(f'Arquivo {file_name} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    try:
        text = instance.search(position)
        return print(
            text,
            file=sys.stdout)

    except IndexError:
        print("Posição inválida", file=sys.stderr)
