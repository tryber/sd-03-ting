class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self._data:
            return self._data.pop(self.FIRST_ELEMENT)
        return None

    def search(self, index):
        if(index > len(self._data) or index < 0):
            raise IndexError
        return self._data[index]
