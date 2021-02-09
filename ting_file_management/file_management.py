import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return print("Formato inválido\n", file=sys.stderr)
    try:
        with open(path_file, 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]

    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)


if __name__ == "__main__":
    txt_importer("statics/arquivo_teste.txt")
