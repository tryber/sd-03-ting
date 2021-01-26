from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def exists_word(word, instance):
    results = []
    occurrences = []
    foundFilePath = ''

    for i in range(len(instance)):
        for j in instance.search(i)['linhas_do_arquivo']:
            if j.lower().find(word.lower()) >= 0:
                occurrences.append({
                    'linha': i,
                })
                foundFilePath = instance.search(i)['nome_do_arquivo']
        if occurrences != []:
            results.append({
                "palavra": word,
                "arquivo": foundFilePath,
                "ocorrencias": occurrences
            })
            occurrences = []
            foundFilePath = ''
    return results


def search_by_word(word, instance):
    results = []
    occurrences = []
    foundFilePath = ''

    for i in range(len(instance)):
        for j in instance.search(i)['linhas_do_arquivo']:
            if j.lower().find(word.lower()) >= 0:
                occurrences.append({
                    'linha': i,
                    'conteudo': j
                })
                foundFilePath = instance.search(i)['nome_do_arquivo']
        if occurrences != []:
            results.append({
                "palavra": word,
                "arquivo": foundFilePath,
                "ocorrencias": occurrences
            })
            occurrences = []
            foundFilePath = ''
    return results


if __name__ == '__main__':
    filinha = Queue()
    process('../statics/arquivo_teste.txt', filinha)
    process('../statics/nome_pedro.txt', filinha)
    process('../statics/test1.txt', filinha)
    process('../statics/test2.txt', filinha)
    print('\n\n\n')
    print(exists_word('de', filinha))
    print(search_by_word('pedro', filinha))
