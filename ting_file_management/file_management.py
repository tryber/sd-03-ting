from os import path
import sys


def txt_importer(path_file):
    if path.splitext(path_file)[1] != '.txt':
        return print("Formato inválido", file=sys.stderr)
    if path.exists(path_file) is False:
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    with open(path_file) as file:
        return [line.strip() for line in file]
