class Queue:

    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = []
        self._len = 0

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.append(value)
        self._len += 1

    def dequeue(self):
        """Aqui irá sua implementação"""
        if not self._len:
            return None

        dequeue_remove = self._data[0]
        self._data.pop()
        self._len -= 1
        return dequeue_remove

    def search(self, index):
        """Aqui irá sua implementação"""
        if index >= len(self._data) or index >= 0:
            return self._data[index]
        raise IndexError
