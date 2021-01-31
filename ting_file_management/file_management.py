import sys
from os import path


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path.exists(path_file):
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
    with open(path_file, "r", encoding="UTF-8") as file:
        content = []
        for line in file:
            content.append(line.replace("\n", ""))
        return content
