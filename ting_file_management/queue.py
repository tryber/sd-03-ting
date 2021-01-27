class Queue:
    def __init__(self):
        self._list = list()

    def __len__(self):
        return len(self._list)

    def enqueue(self, value):
        return self._list.append(value)
    
    def dequeue(self):
        return self._list.pop(0)

    def search(self, index):
        if 0 > index <= len(self._list):
            raise IndexError()
        else:
            return self._list[index]