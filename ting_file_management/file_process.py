from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_content = txt_importer(path_file)
    dict_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }
    print(dict_data)
    instance.enqueue(dict_data)
    return dict_data
    

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
