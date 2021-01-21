def process_file(file):
    qtd_rows = 0
    for row in file:
        print(row)
        qtd_rows = len(row)

    return qtd_rows


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return print("Formato inválido\n")
    try:
        with open(path_file, "r") as file:
            process_file(file)
    except IOError:
        print(f"Arquivo {path_file} não encontrado\n")
