import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = txt_importer(path_file)

    for i in range(len(instance)):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return print('File already processed')

    enq_data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(data),
        'linhas_do_arquivo': data
    }

    instance.enqueue(enq_data)

    print(enq_data, file=sys.stdout)


def remove(instance):
    if instance.is_empty():
        return print('Não há elementos')

    removed = instance.dequeue()['nome_do_arquivo']

    print(f'Arquivo {removed} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    try:
        metadata = instance.search(position)
        print(metadata, file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
