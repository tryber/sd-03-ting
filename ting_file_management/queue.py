class Queue:
    def __init__(self):
        self._data = list()
        self._len = 0

    def __len__(self):
        return self._len

    def is_empty(self):
        return not self._len

    def enqueue(self, value):
        if value not in self._data:
            self._data.append(value)
            self._len += 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self._data[0]
        self._data = self._data[1:]
        self._len -= 1
        return value

    def search(self, index):
        if self._len >= index >= 0:
            return self._data[index]
        raise IndexError()
