import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            return print("Formato inválido", file=sys.stderr)
        with open(path_file) as file:
            lines = "".join(list(file)).split("\n")
            print(lines, file=sys.stderr)
            return lines
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        