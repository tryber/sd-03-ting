import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        raise ValueError("Formato inválido", file=sys.stderr)
    if path_file.exists(path_file) is False:
        raise ValueError(
            f"Arquivo {path_file.basename(path_file)} não encontrado")
    with open(path_file, "r") as file_news:
        news = file_news.readlines()
        return [new.strip() for new in news]
