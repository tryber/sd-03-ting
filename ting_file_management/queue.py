class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = []
        self._len = 0

    def __len__(self):
        return self._len

    def enqueue(self, value):
        self._data.append(value)
        self._len += 1

    def dequeue(self):
        if not self._len:
            return None

        remove = self._data.pop()
        self._len -= 1
        return remove

    def search(self, index):
        if self._len >= index >= 0:
            return self._data[index]
        raise IndexError
