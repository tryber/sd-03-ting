import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    lines = list()
    result = dict()

    # verifica se o arquivo já existe na fila
    for n in range(len(instance)):
        check_list = instance.search(n)
        if check_list["nome_do_arquivo"] == f"{path_file}":
            return None

    # se o arquivo nao existe, carregue-o
    lines = txt_importer(path_file)
    if lines is not None:
        result = {
            "nome_do_arquivo": f"{path_file}",
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines
        }
    else:
        return None

    # coloque o arquivo na fila e imprima as informacoes
    instance.enqueue(result)
    sys.stdout.write(f"'nome_do_arquivo': '{path_file}'")
    sys.stdout.write(f"'qtd_linhas': {len(lines)}")
    sys.stdout.write(f"'linhas_do_arquivo': {lines}")


def remove(instance):
    if instance.is_empty():
        sys.stdout.write("Não há elementos\n")
    else:
        result = instance.dequeue()
        sys.stdout.write(
            f"Arquivo {result['nome_do_arquivo']} removido com sucesso\n"
        )


def file_metadata(instance, position):
    if position < 0 or position > len(instance):
        sys.stderr.write("Posição inválida")
        return None
    result = instance.search(position)
    sys.stdout.write(f"{result}")
