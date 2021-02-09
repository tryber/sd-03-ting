import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file) as value:
            lines = value.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)


if __name__ == '__main__':
    txt_importer('statics/arquivo_teste.txt')