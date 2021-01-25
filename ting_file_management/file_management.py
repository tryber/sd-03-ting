import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    try:
        if not path_file.endswith(".txt"):
            print("Formato inválido", file=sys.stderr)
        with open(path_file) as file:
            lines = file.readlines()
            return [line.strip() for line in lines]

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
