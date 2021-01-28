class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = list()
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        self.__length += 1
        self._data.append(value)

    def dequeue(self):
        if self._data:
            self.__length -= 1
            return self._data.pop(self.FIRST_ELEMENT)
        return

    def search(self, index):
        if index <= self.__length and index > -1:
            return self._data[index]
        raise IndexError
        return

    def all_data(self):
        return self._data

    def last_element(self):
        return print(self._data[-1])

    def search_word(self, word):
        found_list = []
        for entry in self._data:
            index = 1
            occurrence = []
            for line in entry['linhas_do_arquivo']:
                if word.lower() in line.lower():
                    occurrence.append({"linha": 1})
                index += 1
            if occurrence == []:
                return occurrence
            found_list.append({
                "arquivo": entry['nome_do_arquivo'],
                "ocorrencias": occurrence,
                "palavra": word,
            })

        return found_list

    def search_frase(self, word):
        found_list = []
        for entry in self._data:
            index = 1
            occurrence = []
            for line in entry['linhas_do_arquivo']:
                if word.lower() in line.lower():
                    occurrence.append({"linha": 1, "conteudo": line})
                index += 1
            if occurrence == []:
                return occurrence
            found_list.append({
                "arquivo": entry['nome_do_arquivo'],
                "ocorrencias": occurrence,
                "palavra": word,
            })

        return found_list
