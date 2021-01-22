import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    lines = list()
    result = dict()

    lines = txt_importer(path_file)
    if lines is not None:
        result = {
            "nome_do_arquivo": f"{path_file}",
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines
        }
    else:
        return None
    sys.stdout.write(f"'nome_do_arquivo': '{path_file}'")
    sys.stdout.write(f"'qtd_linhas': {len(lines)}")
    sys.stdout.write(f"'linhas_do_arquivo': {lines}")
    return instance.enqueue(result)


def remove(instance):
    if instance.is_empty():
        sys.stdout.write("Não há elementos\n")
    else:
        result = instance.dequeue()
        # print(result["nome_do_arquivo"])
        sys.stdout.write(
            f"Arquivo {result['nome_do_arquivo']} removido com sucesso\n"
        )


def file_metadata(instance, position):
    if position < 0 or position > len(instance):
        sys.stderr.write("Posição inválida")
        return None
    result = instance.search(position)
    sys.stdout.write(f"{result}")
