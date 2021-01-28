import sys
from ting_file_management.file_management import txt_importer


def pre_process(name, lines):
    return {
        "nome_do_arquivo": name,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }


def process(path_file, instance):
    linhas_do_arquivo = txt_importer(path_file)
    for i in range(instance.__len__()):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return None

    return_dict = pre_process(path_file, linhas_do_arquivo)

    instance.enqueue(return_dict)
    print(return_dict, file=sys.stdout)
    return return_dict


def remove(instance):
    if (instance.__len__() == 0):
        return print('Não há elementos', file=sys.stdout)
    file_name = instance.search(0)['nome_do_arquivo']
    instance.dequeue()
    return print(f'Arquivo {file_name} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        return print(
            pre_process(file['nome_do_arquivo'],
                        file['linhas_do_arquivo']), file=sys.stdout)
    except IndexError:
        return print('Posição inválida', file=sys.stdout)
