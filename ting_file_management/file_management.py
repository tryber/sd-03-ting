import re
import sys

def txt_importer(path_file):
    try:
        if not re.search('.txt$', path_file):
            return sys.stderr.write("Formato inválido\n")
        with open(path_file, "r", encoding="utf-8") as file:
            text = ""
            for line in file:
                text += line
            text = text.split("\n")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    else:
        return text



if __name__ == "__main__":
    txt_importer("../statics/arquivo_teste.txt")
