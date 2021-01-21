import sys
from os import path


def txt_importer(path_file):
    exists = path.exists(path_file)
    if not exists:
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    if not path_file.endswith(".txt"):
        return print("Formato inválido", file=sys.stderr)

    with open(path_file) as file:
        array_of_string = list()

        for line in file:
            array_of_string.append(line.replace("\n", ""))

        return array_of_string


if __name__ == "__main__":
    print(txt_importer("./statics/arquivo_teste.txt"))
