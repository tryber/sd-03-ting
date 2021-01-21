import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
    response = list()
    try:
        with open(path_file, "r", newline="") as txt_file:
            for news in txt_file.readlines():
                response.append(news.rstrip('\n'))
        return response
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
