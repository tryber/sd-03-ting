import sys
from os import path


def txt_importer(path_file):
    path_valide = path.exists(path_file)

    if not path_valide:
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    if not path_file.endswith(".txt"):
        raise ValueError("Formato inválido", file=sys.stderr)
    with open(path_file, "r") as file_news:
        news = file_news.readlines()
        return [new.strip() for new in news]
