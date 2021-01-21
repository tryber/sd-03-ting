import sys
from os import path


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        sys.stderr.write("Formato inválido\n")
    exists = path.exists(path_file)
    if not exists:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return
    with open(path_file) as file:
        txt_imported = []
        for text in file.readlines():
            txt_imported.append(text.replace('\n', ''))
        return txt_imported


if __name__ == "__main__":
    print(txt_importer('./statics/arquivo_test.txt'))
