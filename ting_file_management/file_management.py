import sys


def txt_importer(path_file):
    txt_list = []
    try:
        if not path_file.endswith(".txt"):
            print("Formato inválido", file=sys.stderr)
        with open(path_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                txt_list.append(line.strip())
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        return txt_list
