from os import path

def txt_importer(path_file):
    """Aqui irá sua implementação"""
    try:
        if not path.exists(path_file):
            print("Formato inválido")

        with open(path_file, "r") as file:
            text_data = []
            text_lines = file.readlines()

            for line in text_lines:
                text_data.append(line.strip())
            return text_data

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado")