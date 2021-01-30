import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            print("Formato inválido", file=sys.stderr)
        with open(path_file, 'r') as file:
            lines = file.readlines()
            lines_array = []
            for line in lines:
                lines_array.append(line.strip())
            return lines_array

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
