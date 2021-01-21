def process_file(file):
    """sua funcao aqui"""


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return ValueError("Formato inválido\n")
    try:
        with open(path_file, "r") as file:
            process_file(file)
    except IOError:
        print(f"Arquivo {path_file} não encontrado\n")
