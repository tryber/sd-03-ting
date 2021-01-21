import sys


def process_file(file):
    length = file.readlines()
    qtd_rows = []
    for row in length:
        print(row)
        qtd_rows.append(row.strip())

    return qtd_rows


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, "r") as file:
            return process_file(file)
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
