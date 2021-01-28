class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None
        value = self._data[0]
        del self._data[0]
        return value

    def search(self, index):
        if len(self._data) > 0 and index > -1:
            return self._data[index]
        raise IndexError
        return

    def last_file(self):
        return print(self._data[-1])
