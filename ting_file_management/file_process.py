import sys
from functools import cache
from ting_file_management.file_management import txt_importer


# Implementa arquivo no fila
@cache
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


def remove(instance):
    if not len(instance):
        sys.stdout.write('Não há elementos\n')
    name_file = instance.dequeue()['nome_do_arquivo']
    print(f'Arquivo {name_file} removido com sucesso')


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        sys.stdout.write(str(result))
    except IndexError:
        sys.stderr.write('Posição inválida')
