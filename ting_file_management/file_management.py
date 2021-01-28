import os
import sys


def txt_importer(path_file):
    file_extension = os.path.basename(path_file)
    if (not file_extension.endswith('.txt')):
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, 'r') as file:
            file_list = list()
            file_lines = file.readlines()
            for line in file_lines:
                line = line.strip()
                file_list.append(line)
            return file_list
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
