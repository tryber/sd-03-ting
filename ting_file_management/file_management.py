import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            print("Formato inválido", file=sys.stderr)

        with open(path_file, "r") as file:
            text_data = []
            text_lines = file.readlines()

            for line in text_lines:
                text_data.append(line.strip())
            return text_data

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
