import sys
from queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    try:
        info = {}
        array = txt_importer(path_file)

        for i in range(len(instance)):
            if instance.search(i)['nome_do_arquivo'].find(path_file) >= 0:
                return False

        info['nome_do_arquivo'] = path_file
        info['qtd_linhas'] = len(array)
        info['linhas_do_arquivo'] = array

        instance.enqueue(info)
        sys.stdout.write(str(info))
        return info

    except FileNotFoundError:
        return print(f'Arquivo {path_file} não encontrado', file=sys.stderr)


def remove(instance):
    if not len(instance):
        sys.stdout.write('Não há elementos\n')
    else:
        rem_name = instance.dequeue()['nome_do_arquivo']
        sys.stdout.write(f'Arquivo {rem_name} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        sys.stdout.write(str(result))
    except IndexError:
        sys.stderr.write('Posição inválida')


if __name__ == '__main__':
    queue = Queue()
    process('../statics/arquivo_teste.txt', queue)
    process('../statics/arquivo_teste.txt', queue)
    process('../statics/nome_pedro.txt', queue)
    process('../statics/nome_pedro.txt', queue)
    process('../statics/test1.txt', queue)
    process('../statics/test2.txt', queue)
    # process('../statics/test.txt', queue)
    # process('statics/novo_paradigma_globalizado.txt', queue)
    print(queue)
    print(len(queue))
    # print(queue.search(1)['nome_do_arquivo'].find('../statics/nome_pedro.txt'))
    # print(queue.search(1)['nome_do_arquivo'].find('algo'))
    # print('object' in str(queue))
    # remove(queue)
    # print(file_metadata(queue, 1))
