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
            self.FIRST_ELEMENT += 0
            return self._data.pop(self.FIRST_ELEMENT)
        return None

    def search(self, index):
        print(self._data[index])
        if 0 <= index <= len(self._data):
            return self._data[index]
        raise IndexError()
