class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.insert(self.FIRST_ELEMENT, value)

    def dequeue(self):
        # remove o elemento da fila
        if self._data:
            return self._data.pop()

    def search(self, index):
        if index < 0 or index > len(self) - 1:
            raise IndexError
