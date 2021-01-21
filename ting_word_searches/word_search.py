from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def exists_word(word, instance):
    words = []
    for item in instance:
        local_word = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for line in item["linhas_do_arquivo"]:
            if word in line:
                local_word["ocorrencias"]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


if __name__ == "__main__":
    test = [
        {
            "nome_do_arquivo": "arquivo_teste.txt",
            "qtd_linhas": "3",
            "linhas_do_arquivo": [
                "Acima de tudo,",
                "é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga",
                "à análise do levantamento das variáveis envolvidas.",
            ],
        },
        {
            "nome_do_arquivo": "nome_pedro.txt",
            "qtd_linhas": "1",
            "linhas_do_arquivo": [
                "Aqui contem um texto que fala sobre um menino pobre chamado Pedro.",
            ],
        },
    ]
    queue = Queue()
    for elem in test:
        queue.enqueue(elem)
    exists_word("a", queue)
