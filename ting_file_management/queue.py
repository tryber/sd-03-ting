class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.insert(self.FIRST_ELEMENT, value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if self._data:
            return self._data.pop()

    def search(self, index):
        """Aqui irá sua implementação"""
        if index >= len(self._data) or index > 0:
            return self._data[index]
        else:
            raise IndexError
