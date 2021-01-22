class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = []

    def __len__(self):
        return self.FIRST_ELEMENT

    def enqueue(self, value):
        self._data.insert(self.FIRST_ELEMENT, value)

    def dequeue(self):
        if self._data:
            return self._data.pop()

    def search(self, index):
        """codigo"""
