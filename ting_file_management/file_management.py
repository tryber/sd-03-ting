import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    try:
        if not path_file.endswith(".txt"):
            raise ValueError("Formato inválido", file=sys.stderr)
        with open(path_file, "r") as file_news:
            news = file_news.readlines()
            return [new.strip() for new in news]

    except FileNotFoundError:
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
