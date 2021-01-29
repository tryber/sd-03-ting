class Queue:

    def __init__(self):
        self._data = []
        self._len = 0

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)
        self._len += 1

    def dequeue(self):
        if not self._len:
            return None

        dequeue_remove = self._data[0]
        self._data.pop()
        self._len -= 1
        return dequeue_remove

    def search(self, index):
        if index >= len(self._data) or index >= 0:
            return self._data[index]
        raise IndexError
