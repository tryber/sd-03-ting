import sys


def txt_importer(path_file):
    if path_file.endswith('txt'):
        try:
            with open(path_file, 'r') as file:
                return file.read().split("\n")
        except FileNotFoundError:
            return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    sys.stderr.write("Formato inválido\n")
