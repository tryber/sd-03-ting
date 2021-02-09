from .file_management import txt_importer
from .queue import Queue
import sys
from operator import itemgetter


def process(path_file, instance):
    processed_file = txt_importer(path_file)

    for i in range(len(instance)):
        if instance.search(i):
            item = instance.search(i)
            item = item["nome_do_arquivo"]
            if item and item == path_file:
                return None

    instance.enqueue({
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(processed_file),
        "linhas_do_arquivo": processed_file
    })

    stdout_return = "{"
    stdout_return += f"""
        'nome_do_arquivo': '{path_file}',
        'qtd_linhas': {len(processed_file)},
        'linhas_do_arquivo': {processed_file}
    """
    stdout_return += "}"

    sys.stdout.write(stdout_return)


def remove(instance):
    try:
        path_file = instance.dequeue()
        path_file = path_file["nome_do_arquivo"]
        for i in range(len(instance)):
            item = instance.search(i)
            item = item["nome_do_arquivo"]
            if item == path_file:
                del item
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")
    except IndexError:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        metadata = instance.search(position)
        file_path, lines_qty, data = itemgetter(
            "nome_do_arquivo",
            "qtd_linhas",
            "linhas_do_arquivo"
        )(metadata)

        stdout_return = "{"
        stdout_return += f"""
            'nome_do_arquivo': '{file_path}',
            'qtd_linhas': {lines_qty},
            'linhas_do_arquivo': {data}
        """
        stdout_return += "}"

    except IndexError:
        sys.stderr.write("Posição inválida")

    else:
        print("Saida file metadata:\n")
        sys.stdout.write(stdout_return)


if __name__ == "__main__":
    instance = Queue()
    process("../statics/arquivo_teste.txt", instance)
    print(instance.data)
    remove(instance)
    print(instance.data)
    process("../statics/arquivo_teste.txt", instance)
    file_metadata(instance, 0)
