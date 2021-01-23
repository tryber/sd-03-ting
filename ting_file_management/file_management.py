import csv
import itertools
import sys
import os


def txt_importer(path_file):
    merged = ""
    file_content = []
    if not os.path.exists(path_file):
        return sys.stderr.write("Arquivo statics/arquivo_nao_existe.txt não encontrado\n")   
    elif not path_file.endswith("txt"):
        return sys.stderr.write("Formato inválido\n")
    else:
        with open(path_file) as txt_file:
            txt_content = csv.reader(txt_file, delimiter="\n")
            for row in txt_content:
                file_content.append(row)
        # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
        merged = list(itertools.chain(*file_content))
        return merged
