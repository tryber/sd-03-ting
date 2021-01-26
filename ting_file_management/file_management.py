import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return print('Formato inválido', file=sys.stderr)
    try:
        output = []
        textstream = open(path_file, 'r', encoding='UTF-8')
        for line in textstream:
            output.append(line.replace('\n', ''))
        textstream.close()
        return output
    except FileNotFoundError:
        return print(f'Arquivo {path_file} não encontrado', file=sys.stderr)


if __name__ == '__main__':
    txt_importer('../statics/arquivo_teste.txt')
