

class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._queue = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._queue)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        return self._queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self._queue.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index >= len(self._queue) or index < 0:
            raise IndexError
        return self._queue[index]
            
