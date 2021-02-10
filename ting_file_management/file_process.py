from ting_file_management.file_management import txt_importer
import sys


def file_already_exist(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return True
    return False


def process(path_file, instance):
    txt_file = txt_importer(path_file)
    if file_already_exist(path_file, instance):
        return

    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_file),
        "linhas_do_arquivo": txt_file
    }
    instance.enqueue(file_data)
    print(file_data, file=sys.stdout)


def remove(instance):
    if len(instance) <= 0:
        return print("Não há elementos")

    queue = instance.dequeue()
    print(f"Arquivo {queue['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        sys.stderr.write("Posição inválida")
