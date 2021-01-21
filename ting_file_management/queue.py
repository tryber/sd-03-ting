class Queue:

    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = ()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.insert(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self._data.pop()

    def search(self, index):
        """Aqui irá sua implementação"""
        try:
            if index <= 0 or len(self._data) <= -1:
                return None
        except IndexError:
            return "indice invalido"
        else:
            for i in index:
                return index[i]
