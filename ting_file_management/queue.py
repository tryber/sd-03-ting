class Queue:
    f_elem = 0

    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = ()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.insert(self.f_elem.value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self._data.pop()

    def search(self, index):
        """Aqui irá sua implementação"""
        if index >= len(self._data) or index < 0:
            raise IndexError
